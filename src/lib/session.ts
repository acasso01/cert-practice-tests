import type { Attempt, Exam, Question, Session, SessionItem } from '../types';
import { isPassing, percentScore, scaledScore } from './score';
import { setsEqual, shuffle } from './shuffle';

export function questionMap(exam: Exam): Map<string, Question> {
  return new Map(exam.questions.map((question) => [question.id, question]));
}

export function createSession(
  exam: Exam,
  mode: Session['mode'],
  questions: Question[],
  minutes: number | null,
): Session {
  const items: SessionItem[] = questions.map((question) => ({
    qid: question.id,
    choiceOrder: shuffle(question.choices.map((_, index) => index)),
    selected: [],
    flagged: false,
    revealed: false,
  }));
  const startedAt = Date.now();
  return {
    id: crypto.randomUUID(),
    examId: exam.id,
    mode,
    startedAt,
    endsAt: minutes == null ? null : startedAt + minutes * 60_000,
    index: 0,
    items,
  };
}

export function gradeSession(exam: Exam, session: Session, endedBy: Attempt['endedBy']): Attempt {
  const questions = questionMap(exam);
  const items = session.items.map((item) => {
    const question = questions.get(item.qid);
    const correct = question ? setsEqual(item.selected, question.answer) : false;
    return {
      qid: item.qid,
      choiceOrder: item.choiceOrder,
      selected: item.selected,
      flagged: item.flagged,
      correct,
    };
  });
  const correct = items.filter((item) => item.correct).length;
  const total = items.length;
  const scaled = scaledScore(correct, total);
  const domainStats = exam.domains.map((domain) => {
    const inDomain = items.filter((item) => questions.get(item.qid)?.domain === domain.id);
    return {
      id: domain.id,
      correct: inDomain.filter((item) => item.correct).length,
      total: inDomain.length,
    };
  });
  return {
    id: crypto.randomUUID(),
    examId: exam.id,
    mode: session.mode,
    startedAt: session.startedAt,
    completedAt: Date.now(),
    endedBy,
    correct,
    total,
    percent: percentScore(correct, total),
    scaled,
    passed: isPassing(scaled, exam.passScaled),
    domains: domainStats,
    items,
  };
}
