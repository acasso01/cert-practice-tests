import { useState } from 'react';
import type { Attempt, Exam } from '../types';
import { Modal } from './Modal';

type Props = {
  exams: Exam[];
  history: Attempt[];
  onReview: (attemptId: string) => void;
  onClear: () => void;
  onResetSeen: () => void;
  onHome: () => void;
};

function Spark({ attempts }: { attempts: Attempt[] }) {
  const ordered = [...attempts].reverse();
  if (ordered.length < 2) return <p className="fine">Take at least two sets to see a trend.</p>;
  const points = ordered
    .map((attempt, index) => {
      const x = (index / (ordered.length - 1)) * 100;
      const y = 36 - ((attempt.scaled - 100) / 800) * 32;
      return `${x},${y}`;
    })
    .join(' ');
  return (
    <svg className="spark" viewBox="0 0 100 40" role="img" aria-label="Scaled scores from oldest to newest">
      <polyline points={points} />
    </svg>
  );
}

export function HistoryView({ exams, history, onReview, onClear, onResetSeen, onHome }: Props) {
  const [confirm, setConfirm] = useState(false);
  const byExam = exams
    .map((exam) => ({ exam, attempts: history.filter((attempt) => attempt.examId === exam.id) }))
    .filter((group) => group.attempts.length > 0);

  return (
    <section className="history">
      <button className="text-btn" onClick={onHome}>
        Back
      </button>
      <h1>History</h1>
      <p className="lede">Scores stay in this browser only. Clearing history also clears the missed-question deck.</p>
      {history.length === 0 && <p className="panel">No attempts yet. Finish a practice set or an exam and it will land here.</p>}
      {byExam.map(({ exam, attempts }) => (
        <div key={exam.id} className="panel">
          <div className="exam-top">
            <h2>{exam.name}</h2>
            <span className="pill">Pass {exam.passScaled}</span>
          </div>
          <Spark attempts={attempts} />
          {attempts.map((attempt) => (
            <article key={attempt.id} className="history-item">
              <div className="history-top">
                <strong>
                  {attempt.scaled} · {attempt.passed ? 'Pass' : 'Fail'}
                </strong>
                <span className="meta">{new Date(attempt.completedAt).toLocaleString()}</span>
              </div>
              <p className="meta">
                {attempt.mode === 'exam' ? 'Exam' : 'Practice'} · {attempt.correct}/{attempt.total} ·{' '}
                {Math.round(attempt.percent)}%
              </p>
              <button className="ghost" onClick={() => onReview(attempt.id)}>
                Review
              </button>
            </article>
          ))}
        </div>
      ))}
      <div className="row">
        {history.length > 0 && (
          <button className="ghost" onClick={() => setConfirm(true)}>
            Clear history
          </button>
        )}
        <button className="ghost" data-testid="reset-seen-all" onClick={onResetSeen}>
          Reset seen history
        </button>
      </div>
      {confirm && (
        <Modal title="Clear every saved attempt?" onClose={() => setConfirm(false)}>
          <p>This removes scores, reviews, and the missed-question list from this browser.</p>
          <div className="row">
            <button
              className="primary"
              onClick={() => {
                setConfirm(false);
                onClear();
              }}
            >
              Clear
            </button>
            <button className="ghost" onClick={() => setConfirm(false)}>
              Cancel
            </button>
          </div>
        </Modal>
      )}
    </section>
  );
}
