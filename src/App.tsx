import { useEffect, useMemo, useState } from 'react';
import { HistoryView } from './components/History';
import { Home } from './components/Home';
import { Quiz } from './components/Quiz';
import { Results } from './components/Results';
import { Setup } from './components/Setup';
import { loadExams } from './data/loadExams';
import { examMinutes } from './lib/score';
import { drawQuestions } from './lib/sample';
import { createSession, gradeSession, questionMap } from './lib/session';
import { shuffle } from './lib/shuffle';
import {
  clearHistory,
  loadHistory,
  loadMissed,
  loadSession,
  loadTheme,
  saveAttempt,
  saveSession,
  saveTheme,
  type Theme,
} from './lib/storage';
import type { Attempt, Mode, Session } from './types';

type View = 'home' | 'setup' | 'quiz' | 'results' | 'history';

function Logo() {
  return (
    <svg width="28" height="28" viewBox="0 0 32 32" aria-hidden="true">
      <rect width="32" height="32" rx="8" fill="currentColor" />
      <path d="M8 16.5 13.2 22 24 10" fill="none" stroke="var(--bg)" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

export function App() {
  const exams = useMemo(() => loadExams(), []);
  const byId = useMemo(() => new Map(exams.map((exam) => [exam.id, exam])), [exams]);
  const [theme, setTheme] = useState<Theme>(() => loadTheme());
  const [history, setHistory] = useState<Attempt[]>(() => loadHistory());
  const [session, setSession] = useState<Session | null>(() => loadSession());
  const [view, setView] = useState<View>(() => (loadSession() ? 'quiz' : 'home'));
  const [setupExamId, setSetupExamId] = useState<string | null>(null);
  const [setupMode, setSetupMode] = useState<Mode>('practice');
  const [resultId, setResultId] = useState<string | null>(null);
  const [missTick, setMissTick] = useState(0);

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    saveTheme(theme);
  }, [theme]);

  useEffect(() => {
    saveSession(session);
  }, [session]);

  useEffect(() => {
    if (view !== 'quiz' || session?.mode !== 'exam') return;
    const onLeave = (event: BeforeUnloadEvent) => {
      event.preventDefault();
      event.returnValue = '';
    };
    window.addEventListener('beforeunload', onLeave);
    return () => window.removeEventListener('beforeunload', onLeave);
  }, [session?.mode, view]);

  useEffect(() => {
    const titles: Record<View, string> = {
      home: 'Certline — free CompTIA practice tests',
      setup: 'Set up a test · Certline',
      quiz: 'Question · Certline',
      results: 'Results · Certline',
      history: 'History · Certline',
    };
    document.title = titles[view];
  }, [view]);

  const missed = useMemo(() => {
    const counts: Record<string, number> = {};
    for (const exam of exams) counts[exam.id] = loadMissed(exam.id).length;
    return counts;
    // missTick refreshes counts after a graded attempt.
  }, [exams, history, missTick]);

  function openSetup(examId: string, mode: Mode) {
    setSetupExamId(examId);
    setSetupMode(mode);
    setView('setup');
  }

  function start(mode: Mode, count: number, domainIds: string[]) {
    const exam = setupExamId ? byId.get(setupExamId) : undefined;
    if (!exam) return;
    const drawn = drawQuestions(exam.questions, exam.domains, count, domainIds.length ? domainIds : null);
    const minutes = mode === 'exam' ? examMinutes(drawn.length, exam.examQuestions, exam.minutes) : null;
    setSession(createSession(exam, mode, drawn, minutes));
    setView('quiz');
  }

  function retry(examId: string, ids: string[]) {
    const exam = byId.get(examId);
    if (!exam) return;
    const wanted = new Set(ids);
    const questions = shuffle(exam.questions.filter((question) => wanted.has(question.id)));
    if (questions.length === 0) return;
    setSession(createSession(exam, 'practice', questions, null));
    setView('quiz');
  }

  function finish(endedBy: 'submit' | 'time') {
    if (!session) return;
    const exam = byId.get(session.examId);
    if (!exam) return;
    const attempt = gradeSession(exam, session, session.mode === 'practice' ? 'practice' : endedBy);
    const next = saveAttempt(attempt);
    setHistory(next);
    setResultId(attempt.id);
    setSession(null);
    setMissTick((value) => value + 1);
    setView('results');
  }

  const activeExam = session ? byId.get(session.examId) : undefined;
  const result = history.find((attempt) => attempt.id === resultId) ?? null;
  const resultExam = result ? byId.get(result.examId) : undefined;
  const setupExam = setupExamId ? byId.get(setupExamId) : undefined;

  return (
    <>
      <a className="skip" href="#main">
        Skip to content
      </a>
      <div className="shell">
        <header className="top">
          <button className="brand" onClick={() => setView('home')}>
            <Logo />
            <span>Certline</span>
          </button>
          <div className="top-actions">
            {session && view !== 'quiz' && (
              <button className="ghost" onClick={() => setView('quiz')}>
                Resume
              </button>
            )}
            <button onClick={() => setView('history')}>History</button>
            <button
              aria-pressed={theme === 'light'}
              aria-label={theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}
              onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            >
              {theme === 'dark' ? 'Light' : 'Dark'}
            </button>
          </div>
        </header>
        <main id="main">
          {view === 'home' && (
            <Home
              exams={exams}
              history={history}
              missed={missed}
              onPractice={(examId) => openSetup(examId, 'practice')}
              onExam={(examId) => openSetup(examId, 'exam')}
              onRetry={(examId) => retry(examId, loadMissed(examId))}
              onHistory={() => setView('history')}
            />
          )}
          {view === 'setup' && setupExam && (
            <Setup exam={setupExam} initialMode={setupMode} onBack={() => setView('home')} onStart={start} />
          )}
          {view === 'quiz' && activeExam && session && (
            <Quiz
              exam={activeExam}
              session={session}
              questions={questionMap(activeExam)}
              onChange={setSession}
              onSubmit={finish}
            />
          )}
          {view === 'results' && result && resultExam && (
            <Results
              exam={resultExam}
              attempt={result}
              questions={questionMap(resultExam)}
              onHome={() => setView('home')}
              onNew={() => openSetup(resultExam.id, result.mode)}
              onRetryMissed={() =>
                retry(
                  resultExam.id,
                  result.items.filter((item) => !item.correct).map((item) => item.qid),
                )
              }
            />
          )}
          {view === 'history' && (
            <HistoryView
              exams={exams}
              history={history}
              onHome={() => setView('home')}
              onReview={(id) => {
                setResultId(id);
                setView('results');
              }}
              onClear={() => {
                clearHistory();
                setHistory([]);
                setMissTick((value) => value + 1);
              }}
            />
          )}
          {view === 'quiz' && !activeExam && <p className="panel">That saved session does not match a current exam.</p>}
          {view === 'results' && !result && <p className="panel">That result is no longer saved on this device.</p>}
        </main>
        <footer className="footer">
          <p>
            Certline is an independent study tool. It is not affiliated with, endorsed by, or sponsored by CompTIA or
            Professor Messer. CompTIA, Network+, and A+ are trademarks of CompTIA. Study links open Professor Messer’s
            free course index for that exam so you can find the matching objective. Questions here are original and are
            not from his exams, notes, or videos.
          </p>
        </footer>
      </div>
    </>
  );
}
