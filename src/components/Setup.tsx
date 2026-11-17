import { useMemo, useState } from 'react';
import type { Exam, Mode } from '../types';
import { examMinutes } from '../lib/score';

type Props = {
  exam: Exam;
  initialMode: Mode;
  onBack: () => void;
  onStart: (mode: Mode, count: number, domainIds: string[]) => void;
};

const PRESETS = [10, 25, 50, 90];

export function Setup({ exam, initialMode, onBack, onStart }: Props) {
  const [mode, setMode] = useState<Mode>(initialMode);
  const [preset, setPreset] = useState<number | 'custom'>(mode === 'exam' ? 90 : 10);
  const [custom, setCustom] = useState(15);
  const [domains, setDomains] = useState<string[]>([]);

  const pool = useMemo(() => {
    if (domains.length === 0) return exam.questions.length;
    return exam.questions.filter((question) => domains.includes(question.domain)).length;
  }, [domains, exam.questions]);

  const requested = preset === 'custom' ? custom : preset;
  const count = Math.max(0, Math.min(requested || 0, pool, mode === 'exam' ? exam.examQuestions : pool));
  const minutes = mode === 'exam' ? examMinutes(count, exam.examQuestions, exam.minutes) : null;

  function toggleDomain(id: string) {
    setDomains((current) => (current.includes(id) ? current.filter((item) => item !== id) : [...current, id]));
  }

  return (
    <section className="setup">
      <button className="text-btn" onClick={onBack}>
        Back
      </button>
      <h1>{exam.name}</h1>
      <p className="lede">{exam.summary}</p>
      <div className="panel">
        <div className="mode-switch" role="tablist" aria-label="Mode">
          <button className="chip" aria-pressed={mode === 'practice'} onClick={() => setMode('practice')}>
            Practice
          </button>
          <button className="chip" aria-pressed={mode === 'exam'} onClick={() => { setMode('exam'); setPreset(90); }}>
            Timed exam
          </button>
        </div>
        {mode === 'practice' ? (
          <p>
            You get the explanation as soon as you answer. Wrong choices are marked too, including why they do not fit.
            Questions and answer order are shuffled.
          </p>
        ) : (
          <p>
            This simulates the multiple-choice portion: up to {exam.examQuestions} questions and a countdown. A full set
            uses {exam.minutes} minutes. Shorter sets get one minute per question. Nothing is graded until you submit or
            time runs out. You can flag items and jump around. Unanswered questions count as wrong. The real exam also
            includes performance-based questions, which this drill does not.
          </p>
        )}
        <div className="field">
          <span id="count-label">Number of questions</span>
          <div className="chips" role="group" aria-labelledby="count-label">
            {PRESETS.filter((value) => value <= Math.max(pool, 1)).map((value) => (
              <button key={value} className="chip" aria-pressed={preset === value} onClick={() => setPreset(value)}>
                {value}
              </button>
            ))}
            <button className="chip" aria-pressed={preset === 'custom'} onClick={() => setPreset('custom')}>
              Custom
            </button>
          </div>
          {preset === 'custom' && (
            <label>
              Custom count
              <input
                type="number"
                min={1}
                max={mode === 'exam' ? Math.min(pool, exam.examQuestions) : pool}
                value={custom}
                onChange={(event) => setCustom(Number(event.target.value))}
              />
            </label>
          )}
        </div>
        <div className="field">
          <span id="domain-label">Domains</span>
          <div className="chips" role="group" aria-labelledby="domain-label">
            <button className="chip" aria-pressed={domains.length === 0} onClick={() => setDomains([])}>
              All domains
            </button>
            {exam.domains.map((domain) => (
              <button
                key={domain.id}
                className="chip"
                aria-pressed={domains.includes(domain.id)}
                onClick={() => toggleDomain(domain.id)}
              >
                {domain.id}.0 {domain.name}
              </button>
            ))}
          </div>
          <p className="fine">
            Leave this on all domains for a mix that follows the official weights. Filtering builds a focused set.
          </p>
        </div>
        <p className="meta">
          {count} question{count === 1 ? '' : 's'} ready
          {pool < (preset === 'custom' ? custom : preset) ? ` (only ${pool} match the filter)` : ''}
          {minutes != null ? ` · ${minutes} minute timer` : ''} · pass mark {exam.passScaled} on a 100–900 scale
        </p>
        <div className="row">
          <button
            className="primary"
            disabled={count < 1}
            data-testid="start-session"
            onClick={() => onStart(mode, count, domains)}
          >
            Start {mode === 'exam' ? 'exam' : 'practice'}
          </button>
        </div>
      </div>
    </section>
  );
}
