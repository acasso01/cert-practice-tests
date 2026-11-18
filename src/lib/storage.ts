import type { Attempt, Session } from '../types';

const HISTORY_KEY = 'certline.history.v1';
const MISSED_KEY = 'certline.missed.v1';
const THEME_KEY = 'certline.theme.v1';
const SESSION_KEY = 'certline.session.v1';
const RESULT_KEY = 'certline.result.v1';
const SEEN_KEY = 'certline.seen.v1';

function readJson<T>(storage: Storage, key: string, fallback: T): T {
  try {
    const raw = storage.getItem(key);
    if (!raw) return fallback;
    return JSON.parse(raw) as T;
  } catch {
    return fallback;
  }
}

function writeJson(storage: Storage, key: string, value: unknown): void {
  try {
    storage.setItem(key, JSON.stringify(value));
  } catch {
    // Private mode and full disks should not crash a study session.
  }
}

export type Theme = 'dark' | 'light';

export function loadTheme(): Theme {
  const value = readJson<string>(localStorage, THEME_KEY, 'dark');
  return value === 'light' ? 'light' : 'dark';
}

export function saveTheme(theme: Theme): void {
  writeJson(localStorage, THEME_KEY, theme);
}

export function loadHistory(): Attempt[] {
  const history = readJson<Attempt[]>(localStorage, HISTORY_KEY, []);
  return Array.isArray(history) ? history : [];
}

export function saveAttempt(attempt: Attempt): Attempt[] {
  const history = [attempt, ...loadHistory()].slice(0, 40);
  writeJson(localStorage, HISTORY_KEY, history);
  const missed = loadMissedMap();
  const set = new Set(missed[attempt.examId] ?? []);
  for (const item of attempt.items) {
    if (item.correct) set.delete(item.qid);
    else set.add(item.qid);
  }
  missed[attempt.examId] = [...set];
  writeJson(localStorage, MISSED_KEY, missed);
  writeJson(sessionStorage, RESULT_KEY, attempt.id);
  return history;
}

export function clearHistory(): void {
  writeJson(localStorage, HISTORY_KEY, []);
  writeJson(localStorage, MISSED_KEY, {});
}

function loadMissedMap(): Record<string, string[]> {
  const value = readJson<Record<string, string[]>>(localStorage, MISSED_KEY, {});
  return value && typeof value === 'object' ? value : {};
}

export function loadMissed(examId: string): string[] {
  const list = loadMissedMap()[examId];
  return Array.isArray(list) ? list : [];
}

export function loadSession(): Session | null {
  const session = readJson<Session | null>(sessionStorage, SESSION_KEY, null);
  if (!session || !session.id || !Array.isArray(session.items)) return null;
  return session;
}

export function saveSession(session: Session | null): void {
  if (!session) {
    try {
      sessionStorage.removeItem(SESSION_KEY);
    } catch {
      // Ignore storage failures.
    }
    return;
  }
  writeJson(sessionStorage, SESSION_KEY, session);
}

export function loadResultId(): string | null {
  const id = readJson<string | null>(sessionStorage, RESULT_KEY, null);
  return typeof id === 'string' ? id : null;
}

type SeenBook = Record<string, Record<string, number>>;

function loadSeenBook(): SeenBook {
  const value = readJson<SeenBook>(localStorage, SEEN_KEY, {});
  return value && typeof value === 'object' ? value : {};
}

/** Question ids this browser has already been shown, with the last time each was shown. */
export function loadSeen(examId: string): Record<string, number> {
  const book = loadSeenBook()[examId];
  if (!book || typeof book !== 'object') return {};
  const clean: Record<string, number> = {};
  for (const [qid, stamp] of Object.entries(book)) {
    if (typeof stamp === 'number') clean[qid] = stamp;
  }
  return clean;
}

export function markSeen(examId: string, qids: string[], at = Date.now()): void {
  if (qids.length === 0) return;
  const book = loadSeenBook();
  const current = { ...(book[examId] ?? {}) };
  for (const qid of qids) current[qid] = at;
  book[examId] = current;
  writeJson(localStorage, SEEN_KEY, book);
}

export function resetSeen(examId?: string): void {
  if (!examId) {
    writeJson(localStorage, SEEN_KEY, {});
    return;
  }
  const book = loadSeenBook();
  delete book[examId];
  writeJson(localStorage, SEEN_KEY, book);
}
