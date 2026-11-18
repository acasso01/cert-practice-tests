import { useMemo, useState } from 'react';
import type { Exam, Mode } from '../types';
import { examMinutes } from '../lib/score';

type Props = {
  exam: Exam;
  initialMode: Mode;
  seenAt: Record<string, number>;
  onBack: () => void;
  onStart: (mode: Mode, count: number, domainIds: string[], freshOnly: boolean) => void;
  onResetSeen: () => void;
};

const PRESETS = [10, 25, 50, 90];

export function Setup({ exam, initialMode, seenAt, onBack, onStart, onResetSeen }: Props) {
  const [mode, setMode] = useState<Mode>(initialMode);
  const [preset, setPreset] = useState<number | 'custom'>(mode === 'exam' ? 90 : 10);
  const [custom, setCustom] = useState(15);
  const [domains, setDomains] = useState<string[]>([]);
  const [freshOnly, setFreshOnly] = useState(false);

  const poolQuestions = useMemo(() => {
    const inDomains =
      domains.length === 0
        ? exam.questions
        : exam.questions.filter((question) => domains.includes(question.domain));
    return freshOnly ? inDomains.filter((question) => seenAt[question.id] == null) : inDomains;
  }, [domains, exam.questions, freshOnly, seenAt]);

  const pool = poolQuestions.length;
  const unseenInFilter = useMemo(() => {
    const inDomains =
      domains.length === 0
        ? exam.questions
        : exam.questions.filter((question) => domains.includes(question.domain));
    return inDomains.filter((question) => seenAt[question.id] == null).length;
  }, [domains, exam.questions, seenAt]);

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
            Questions you have not seen come first, and both the question order and the answer order are shuffled.
          </p>
        ) : (
          <p>
            This simulates the multiple-choice portion: up to {exam.examQuestions} questions and a countdown. A full set
            uses {exam.minutes} minutes. Shorter sets get one minute per question. Nothing is graded until you submit or
            time runs out. You can flag items and jump around. Unanswered questions count as wrong. The draw is weighted
            like the real exam and avoids questions you have already seen until it has to reuse the oldest ones. The
            real exam also includes performance-based questions, which this drill does not.
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
        <div className="field">
          <span id="seen-label">Questions you have already seen</span>
          <p className="meta">
            {unseenInFilter} unseen of {domains.length === 0 ? exam.questions.length : exam.questions.filter((question) => domains.includes(question.domain)).length} in this filter.
            New sets use unseen questions first, then the ones you saw longest ago.
          </p>
          <label className="meta">
            <input
              type="checkbox"
              checked={freshOnly}
              data-testid="fresh-only"
              onChange={(event) => setFreshOnly(event.target.checked)}
            />{' '}
            Fresh questions only
          </label>
          <button type="button" className="ghost" data-testid="reset-seen" onClick={onResetSeen}>
            Reset seen history
          </button>
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
            onClick={() => onStart(mode, count, domains, freshOnly)}
          >
            Start {mode === 'exam' ? 'exam' : 'practice'}
          </button>
        </div>
      </div>
    </section>
  );
}
