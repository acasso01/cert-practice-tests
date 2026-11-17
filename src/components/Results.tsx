import { useMemo, useState } from 'react';
import type { Attempt, Exam, Question } from '../types';
import { domainName, objectiveName } from '../data/loadExams';
import { downloadAttemptPdf } from '../lib/pdf';
import { SCALE_MAX, SCALE_MIN } from '../lib/score';

type Filter = 'all' | 'missed' | 'flagged';

type Props = {
  exam: Exam;
  attempt: Attempt;
  questions: Map<string, Question>;
  onHome: () => void;
  onRetryMissed: () => void;
  onNew: () => void;
};

export function Results({ exam, attempt, questions, onHome, onRetryMissed, onNew }: Props) {
  const [filter, setFilter] = useState<Filter>('all');
  const missed = attempt.items.filter((item) => !item.correct).length;
  const visible = attempt.items
    .map((item, index) => ({ item, index }))
    .filter(({ item }) => {
      if (filter === 'missed') return !item.correct;
      if (filter === 'flagged') return item.flagged;
      return true;
    });

  const weak = attempt.domains.filter((stat) => stat.total > 0 && stat.correct / stat.total < 0.7);
  const radius = 52;
  const circ = 2 * Math.PI * radius;
  const offset = circ * (1 - Math.min(100, Math.max(0, attempt.percent)) / 100);
  const title = useMemo(() => (attempt.passed ? 'Pass' : 'Fail'), [attempt.passed]);

  return (
    <section className="results">
      <div className="panel score-hero">
        <svg className="ring" viewBox="0 0 120 120" role="img" aria-label={`${Math.round(attempt.percent)} percent correct`}>
          <circle className="ring-track" cx="60" cy="60" r={radius} />
          <circle
            className={`ring-value ${attempt.passed ? 'pass' : 'fail'}`}
            cx="60"
            cy="60"
            r={radius}
            strokeDasharray={circ}
            strokeDashoffset={offset}
          />
        </svg>
        <div className="score-copy">
          <p className="kicker">{exam.code} · {attempt.mode === 'exam' ? 'Exam mode' : 'Practice'}</p>
          <h1 data-testid="results-score">
            {title} · {attempt.scaled}
          </h1>
          <p className="score-number" style={{ fontSize: '1.4rem' }}>
            {attempt.correct}/{attempt.total} · {Math.round(attempt.percent)}%
          </p>
          <p>
            Pass mark is {exam.passScaled} on a {SCALE_MIN}–{SCALE_MAX} scale. This scaled score is an approximation:
            100 plus the percent correct times 8. CompTIA scales statistically, so your exam-day number will not match
            this line exactly.
          </p>
          {attempt.endedBy === 'time' && <p className="note">Time expired, so the exam was submitted automatically.</p>}
        </div>
      </div>
      <div className="panel">
        <h2>Domains</h2>
        {attempt.domains.filter((stat) => stat.total > 0).map((stat) => {
          const pct = Math.round((stat.correct / stat.total) * 100);
          const isWeak = pct < 70;
          return (
            <div key={stat.id} className={`domain-row${isWeak ? ' weak' : ''}`}>
              <div className="exam-top">
                <span>
                  {stat.id}.0 {domainName(exam, stat.id)}
                </span>
                <span>
                  {stat.correct}/{stat.total} · {pct}%{isWeak ? ' · review' : ''}
                </span>
              </div>
              <div className="track" aria-hidden="true">
                <span style={{ width: `${pct}%` }} />
              </div>
            </div>
          );
        })}
        <p className="fine">
          {weak.length
            ? 'Anything under 70% is marked for another pass. Open the missed questions, then use the study link on each one.'
            : 'No domain landed under 70% on this set.'}
        </p>
      </div>
      <div className="row">
        <button className="primary" data-testid="download-pdf" onClick={() => downloadAttemptPdf(exam, attempt, questions)}>
          Download PDF
        </button>
        {missed > 0 && (
          <button className="ghost" onClick={onRetryMissed}>
            Retry missed ({missed})
          </button>
        )}
        <button className="ghost" onClick={onNew}>
          New set
        </button>
        <button className="text-btn" onClick={onHome}>
          Home
        </button>
      </div>
      <div className="review-tools" role="group" aria-label="Review filter">
        <button className="chip" aria-pressed={filter === 'all'} onClick={() => setFilter('all')}>
          All
        </button>
        <button className="chip" aria-pressed={filter === 'missed'} onClick={() => setFilter('missed')}>
          Missed
        </button>
        <button className="chip" aria-pressed={filter === 'flagged'} onClick={() => setFilter('flagged')}>
          Flagged
        </button>
      </div>
      <div className="review">
        {visible.map(({ item, index }) => {
          const question = questions.get(item.qid);
          return (
            <details key={item.qid} open={!item.correct && filter !== 'flagged'}>
              <summary>
                Question {index + 1} · {item.correct ? 'Correct' : 'Incorrect'}
                {question ? ` · ${question.objective}` : ''}
                {item.flagged ? ' · Flagged' : ''}
              </summary>
              {question ? (
                <div>
                  <p>{question.stem}</p>
                  <ul className="choices">
                    {item.choiceOrder.map((original, display) => {
                      const picked = item.selected.includes(original);
                      const right = question.answer.includes(original);
                      return (
                        <li key={original} className={`choice ${right ? 'correct' : ''} ${picked && !right ? 'wrong' : ''}`}>
                          <span className="letter">{String.fromCharCode(65 + display)}</span>
                          <span className="choice-body">
                            <span>{question.choices[original]}</span>
                            {right && <span className="tag">Correct</span>}
                            {picked && !right && <span className="tag">Your answer</span>}
                            {picked && right && <span className="tag">Your answer · correct</span>}
                            <span className="choice-note">{question.choiceNotes[original]}</span>
                          </span>
                        </li>
                      );
                    })}
                  </ul>
                  {item.selected.length === 0 && <p className="note">You did not answer this one.</p>}
                  <div className="explain">
                    <h3>Why</h3>
                    <p>{question.explanation}</p>
                    <a href={exam.studyUrl} target="_blank" rel="noreferrer">
                      Study objective {question.objective} ({objectiveName(exam, question.objective)}) on {exam.studyLabel}
                    </a>
                  </div>
                </div>
              ) : (
                <p>This question is no longer in the bank.</p>
              )}
            </details>
          );
        })}
        {visible.length === 0 && <p className="meta">Nothing in this filter.</p>}
      </div>
    </section>
  );
}
