export type Difficulty = 'easy' | 'medium' | 'hard';
export type Mode = 'practice' | 'exam';

export type Question = {
  id: string;
  domain: string;
  objective: string;
  difficulty: Difficulty;
  /** 1 for a single answer, 2 for a choose-two item. */
  select: 1 | 2;
  stem: string;
  choices: string[];
  /** Indexes into `choices`. */
  answer: number[];
  /** Why the correct choice is right, in plain language. */
  explanation: string;
  /** One note per choice, in choice order, including the correct ones. */
  choiceNotes: string[];
};

export type Objective = {
  id: string;
  name: string;
};

export type Domain = {
  id: string;
  name: string;
  /** Official percentage of the exam. */
  weight: number;
  objectives: Objective[];
};

export type ExamMeta = {
  id: string;
  code: string;
  name: string;
  title: string;
  summary: string;
  versionNote?: string;
  minutes: number;
  /** Maximum questions on the real exam. */
  examQuestions: number;
  passScaled: number;
  studyUrl: string;
  studyLabel: string;
  accent: string;
  domains: Domain[];
};

export type Exam = ExamMeta & {
  questions: Question[];
};

export type SessionItem = {
  qid: string;
  /** Original choice indexes, in the shuffled display order. */
  choiceOrder: number[];
  /** Original choice indexes the candidate picked. */
  selected: number[];
  flagged: boolean;
  revealed: boolean;
};

export type Session = {
  id: string;
  examId: string;
  mode: Mode;
  startedAt: number;
  /** Epoch ms when an exam auto-submits. Null in practice. */
  endsAt: number | null;
  index: number;
  items: SessionItem[];
};

export type AttemptItem = {
  qid: string;
  choiceOrder: number[];
  selected: number[];
  flagged: boolean;
  correct: boolean;
};

export type DomainStat = {
  id: string;
  correct: number;
  total: number;
};

export type Attempt = {
  id: string;
  examId: string;
  mode: Mode;
  startedAt: number;
  completedAt: number;
  endedBy: 'submit' | 'time' | 'practice';
  correct: number;
  total: number;
  percent: number;
  scaled: number;
  passed: boolean;
  domains: DomainStat[];
  items: AttemptItem[];
};
