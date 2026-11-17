import { useEffect, useMemo, useRef, useState } from 'react';
import type { Exam, Question, Session } from '../types';
import { objectiveName } from '../data/loadExams';
import { Modal } from './Modal';

type Props = {
  exam: Exam;
  session: Session;
  questions: Map<string, Question>;
  onChange: (session: Session) => void;
  onSubmit: (endedBy: 'submit' | 'time') => void;
};

function formatRemaining(ms: number): string {
  const total = Math.max(0, Math.ceil(ms / 1000));
  const minutes = Math.floor(total / 60);
  const seconds = total % 60;
  return `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

export function Quiz({ exam, session, questions, onChange, onSubmit }: Props) {
  const item = session.items[session.index];
  const question = item ? questions.get(item.qid) : undefined;
  const [now, setNow] = useState(() => Date.now());
  const [confirmSubmit, setConfirmSubmit] = useState(false);
  const [confirmExit, setConfirmExit] = useState(false);
  const [live, setLive] = useState('');
  const submitted = useRef(false);
  const headingRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    headingRef.current?.focus();
  }, [session.index, item?.revealed]);

  useEffect(() => {
    if (session.mode !== 'exam' || session.endsAt == null) return;
    const timer = window.setInterval(() => setNow(Date.now()), 250);
    return () => window.clearInterval(timer);
  }, [session.endsAt, session.mode]);

  const remaining = session.endsAt == null ? null : session.endsAt - now;

  useEffect(() => {
    if (remaining == null || submitted.current) return;
    if (remaining <= 0) {
      submitted.current = true;
      onSubmit('time');
    }
  }, [onSubmit, remaining]);

  const unanswered = session.items.filter((entry) => entry.selected.length === 0).length;
  const flagged = session.items.filter((entry) => entry.flagged).length;

  function updateItem(next: Session['items'][number]) {
    const items = session.items.map((entry, index) => (index === session.index ? next : entry));
    onChange({ ...session, items });
  }

  function pick(displayIndex: number) {
    if (!item || !question || item.revealed) return;
    const original = item.choiceOrder[displayIndex];
    if (original == null) return;
    let selected = item.selected;
    if (question.select === 1) {
      selected = item.selected[0] === original ? [] : [original];
    } else if (item.selected.includes(original)) {
      selected = item.selected.filter((value) => value !== original);
    } else {
      selected = [...item.selected, original].slice(-question.select);
    }
    const revealed = session.mode === 'practice' && question.select === 1 && selected.length === 1;
    updateItem({ ...item, selected, revealed });
    if (revealed) announce(question, selected);
  }

  function announce(current: Question, selected: number[]) {
    const correct = [...selected].sort().join() === [...current.answer].sort().join();
    const letters = current.answer
      .map((original) => {
        const display = item?.choiceOrder.indexOf(original) ?? -1;
        return display >= 0 ? String.fromCharCode(65 + display) : '';
      })
      .filter(Boolean)
      .join(' and ');
    setLive(correct ? 'Correct.' : `Incorrect. The correct answer is ${letters}.`);
  }

  function checkMulti() {
    if (!item || !question || question.select !== 2 || item.selected.length !== 2) return;
    updateItem({ ...item, revealed: true });
    announce(question, item.selected);
  }

  function go(nextIndex: number) {
    onChange({ ...session, index: Math.max(0, Math.min(session.items.length - 1, nextIndex)) });
  }

  useEffect(() => {
    function onKey(event: KeyboardEvent) {
      if (event.repeat) return;
      if (!question || !item) return;
      const target = event.target as HTMLElement | null;
      if (target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA')) return;
      if (confirmSubmit || confirmExit) return;
      const key = event.key.toLowerCase();
      const choiceIndex = '123456'.includes(key)
        ? Number(key) - 1
        : 'abcdef'.includes(key)
          ? key.charCodeAt(0) - 97
          : -1;
      if (choiceIndex >= 0 && choiceIndex < question.choices.length) {
        event.preventDefault();
        pick(choiceIndex);
        return;
      }
      if (key === 'f' && session.mode === 'exam') {
        event.preventDefault();
        updateItem({ ...item, flagged: !item.flagged });
        return;
      }
      if (event.key === 'Enter') {
        event.preventDefault();
        if (session.mode === 'practice' && question.select === 2 && !item.revealed) {
          checkMulti();
          return;
        }
        if (session.mode === 'practice' && !item.revealed) return;
        if (session.index === session.items.length - 1 && (session.mode === 'exam' || item.revealed)) {
          if (session.mode === 'exam') setConfirmSubmit(true);
          else onSubmit('submit');
          return;
        }
        if (session.mode === 'exam' || item.revealed) go(session.index + 1);
      }
      if (session.mode === 'exam' && event.key === 'ArrowRight') go(session.index + 1);
      if (session.mode === 'exam' && event.key === 'ArrowLeft') go(session.index - 1);
    }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  });

  const timerClass = remaining == null ? 'timer' : remaining < 120_000 ? 'timer late' : remaining < 600_000 ? 'timer warn' : 'timer';
  const progress = useMemo(() => {
    const answered = session.items.filter((entry) => entry.revealed || entry.selected.length > 0).length;
    return Math.round((answered / session.items.length) * 100);
  }, [session.items]);

  if (!item || !question) return null;

  return (
    <section className="quiz-layout">
      <div className="sr-only" aria-live="polite">{live}</div>
      <article className="q-card" key={`${item.qid}-${item.revealed ? 'open' : 'shut'}`}>
        <div className="q-top">
          <p className="objective">
            {exam.code} · {question.objective} {objectiveName(exam, question.objective)} · {question.difficulty}
            {question.select === 2 ? ' · Choose two' : ''}
          </p>
          {remaining != null && (
            <span className={timerClass} role="timer" aria-label={`${formatRemaining(remaining)} remaining`}>
              {formatRemaining(remaining)}
            </span>
          )}
        </div>
        <div
          className="progress"
          role="progressbar"
          aria-valuemin={1}
          aria-valuemax={session.items.length}
          aria-valuenow={session.index + 1}
          aria-label="Progress"
        >
          <span style={{ width: `${progress}%` }} />
        </div>
        <h2 className="stem" tabIndex={-1} ref={headingRef}>
          Question {session.index + 1} of {session.items.length}. {question.stem}
        </h2>
        <div className="choices" role={question.select === 1 ? 'radiogroup' : 'group'} aria-label="Answers">
          {item.choiceOrder.map((original, display) => {
            const picked = item.selected.includes(original);
            const right = question.answer.includes(original);
            const show = item.revealed;
            const className = ['choice', show && right ? 'correct' : '', show && picked && !right ? 'wrong' : '']
              .filter(Boolean)
              .join(' ');
            const letter = String.fromCharCode(65 + display);
            return (
              <button
                key={original}
                className={className}
                aria-pressed={picked}
                disabled={item.revealed}
                data-testid={`choice-${letter}`}
                onClick={() => pick(display)}
              >
                <span className="letter">{letter}</span>
                <span className="choice-body">
                  <span>{question.choices[original]}</span>
                  {show && right && <span className="tag">Correct</span>}
                  {show && picked && !right && <span className="tag">Your answer</span>}
                  {show && <span className="choice-note">{question.choiceNotes[original]}</span>}
                </span>
              </button>
            );
          })}
        </div>
        {session.mode === 'practice' && question.select === 2 && !item.revealed && (
          <div className="row" style={{ marginTop: 12 }}>
            <button className="primary" disabled={item.selected.length !== 2} onClick={checkMulti} data-testid="check-answer">
              Check answer
            </button>
          </div>
        )}
        {item.revealed && (
          <div className="explain">
            <h3>{[...item.selected].sort().join() === [...question.answer].sort().join() ? 'Correct' : 'Not quite'}</h3>
            <p>{question.explanation}</p>
            <a href={exam.studyUrl} target="_blank" rel="noreferrer">
              Study objective {question.objective} on {exam.studyLabel}
            </a>
          </div>
        )}
        <div className="row" style={{ marginTop: 14 }}>
          <button className="ghost" onClick={() => go(session.index - 1)} disabled={session.index === 0}>
            Previous
          </button>
          {session.mode === 'exam' && (
            <button className="ghost" aria-pressed={item.flagged} onClick={() => updateItem({ ...item, flagged: !item.flagged })}>
              {item.flagged ? 'Flagged' : 'Flag for review'}
            </button>
          )}
          {session.index < session.items.length - 1 ? (
            <button
              className="primary"
              data-testid="next-question"
              disabled={session.mode === 'practice' && !item.revealed}
              onClick={() => go(session.index + 1)}
            >
              Next
            </button>
          ) : (
            <button
              className="primary"
              data-testid="finish-session"
              disabled={session.mode === 'practice' && !item.revealed}
              onClick={() => (session.mode === 'exam' ? setConfirmSubmit(true) : onSubmit('submit'))}
            >
              {session.mode === 'exam' ? 'Submit exam' : 'See results'}
            </button>
          )}
          <button className="text-btn" onClick={() => (session.mode === 'exam' ? setConfirmExit(true) : setConfirmExit(true))}>
            End
          </button>
        </div>
        <p className="fine">
          <kbd>1</kbd>–<kbd>4</kbd> or <kbd>A</kbd>–<kbd>D</kbd> answer · <kbd>Enter</kbd> next
          {session.mode === 'exam' ? ' · F flag · arrows move' : ''}
        </p>
      </article>
      <aside className="side-card">
        <h2>{session.mode === 'exam' ? 'Navigator' : 'This set'}</h2>
        {session.mode === 'exam' ? (
          <>
            <p className="meta">
              {unanswered} unanswered · {flagged} flagged
            </p>
            <div className="nav-grid" aria-label="Question navigator">
              {session.items.map((entry, index) => (
                <button
                  key={entry.qid}
                  className={`nav-btn${entry.selected.length ? ' answered' : ''}${entry.flagged ? ' flagged' : ''}${
                    index === session.index ? ' active' : ''
                  }`}
                  aria-current={index === session.index ? 'true' : undefined}
                  aria-label={`Question ${index + 1}${entry.selected.length ? ', answered' : ', unanswered'}${
                    entry.flagged ? ', flagged' : ''
                  }`}
                  onClick={() => go(index)}
                >
                  {index + 1}
                </button>
              ))}
            </div>
            <button className="primary" onClick={() => setConfirmSubmit(true)}>
              Submit exam
            </button>
          </>
        ) : (
          <p className="meta">
            Feedback stays on the question after you answer. Finish the set for a domain breakdown and a downloadable
            record.
          </p>
        )}
      </aside>
      {confirmSubmit && (
        <Modal title="Submit this exam?" onClose={() => setConfirmSubmit(false)}>
          <p>
            {unanswered > 0
              ? `${unanswered} question${unanswered === 1 ? ' is' : 's are'} unanswered and will be marked wrong.`
              : 'Every question has an answer.'}{' '}
            You will not be able to change answers after this.
          </p>
          <div className="row">
            <button className="primary" data-testid="confirm-submit" onClick={() => onSubmit('submit')}>
              Submit
            </button>
            <button className="ghost" onClick={() => setConfirmSubmit(false)}>
              Keep working
            </button>
          </div>
        </Modal>
      )}
      {confirmExit && (
        <Modal title="End this set?" onClose={() => setConfirmExit(false)}>
          <p>
            {session.mode === 'exam'
              ? 'Ending now submits the exam with unanswered questions marked wrong.'
              : 'Ending now scores the questions you have answered. Unanswered ones count as wrong.'}
          </p>
          <div className="row">
            <button className="primary" onClick={() => onSubmit('submit')}>
              Score it
            </button>
            <button className="ghost" onClick={() => setConfirmExit(false)}>
              Keep going
            </button>
          </div>
        </Modal>
      )}
    </section>
  );
}
