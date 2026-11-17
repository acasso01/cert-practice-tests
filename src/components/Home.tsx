import type { Attempt, Exam } from '../types';

type Props = {
  exams: Exam[];
  history: Attempt[];
  missed: Record<string, number>;
  onPractice: (examId: string) => void;
  onExam: (examId: string) => void;
  onRetry: (examId: string) => void;
  onHistory: () => void;
};

export function Home({ exams, history, missed, onPractice, onExam, onRetry, onHistory }: Props) {
  const recent = history[0];
  return (
    <>
      <section className="hero">
        <p className="kicker">Free · no account · stays on this device</p>
        <h1>Practice that explains the miss.</h1>
        <p className="lede">
          Original Network+ and A+ questions, tagged to the objective, with a reason for every choice.
          Practice gives feedback immediately. Exam mode waits until you submit.
        </p>
      </section>
      {recent && (
        <p className="note">
          Latest {exams.find((exam) => exam.id === recent.examId)?.name ?? 'attempt'}: {recent.scaled} scaled
          {recent.passed ? ' · pass' : ' · below the pass mark'}.{' '}
          <button className="text-btn" onClick={onHistory}>
            Open history
          </button>
        </p>
      )}
      <section className="exam-grid" aria-label="Exams">
        {exams.map((exam) => {
          const missedCount = missed[exam.id] ?? 0;
          return (
            <article key={exam.id} className="exam-card" style={{ ['--stripe' as string]: exam.accent }}>
              <div className="exam-top">
                <span className="code">{exam.code}</span>
                <span className="pill">Pass {exam.passScaled}</span>
              </div>
              <h2>{exam.name}</h2>
              <p>{exam.summary}</p>
              {exam.versionNote && <p className="note">{exam.versionNote}</p>}
              <ol className="weights">
                {exam.domains.map((domain) => (
                  <li key={domain.id}>
                    <span>
                      {domain.id}.0 {domain.name}
                    </span>
                    <span>{domain.weight}%</span>
                    <div className="bar" aria-hidden="true">
                      <span style={{ width: `${domain.weight}%` }} />
                    </div>
                  </li>
                ))}
              </ol>
              <p className="meta">
                {exam.questions.length} original questions · up to {exam.examQuestions} on the timed exam ·{' '}
                {exam.minutes} minutes
              </p>
              <div className="row">
                <button className="primary" onClick={() => onPractice(exam.id)} data-testid={`practice-${exam.id}`}>
                  Practice
                </button>
                <button className="ghost" onClick={() => onExam(exam.id)} data-testid={`exam-${exam.id}`}>
                  Timed exam
                </button>
                {missedCount > 0 && (
                  <button className="ghost" onClick={() => onRetry(exam.id)}>
                    Retry missed ({missedCount})
                  </button>
                )}
              </div>
            </article>
          );
        })}
      </section>
    </>
  );
}
