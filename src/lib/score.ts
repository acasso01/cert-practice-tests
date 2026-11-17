export const SCALE_MIN = 100;
export const SCALE_MAX = 900;

/**
 * Linear stand-in for CompTIA's 100–900 scale.
 * 0% correct maps to 100 and 100% correct maps to 900.
 * The real exam is statistically scaled and is not this straight line.
 */
export function scaledScore(correct: number, total: number): number {
  if (total <= 0) return SCALE_MIN;
  const value = SCALE_MIN + (correct / total) * (SCALE_MAX - SCALE_MIN);
  return Math.max(SCALE_MIN, Math.min(SCALE_MAX, Math.round(value)));
}

export function percentScore(correct: number, total: number): number {
  if (total <= 0) return 0;
  return (correct / total) * 100;
}

export function isPassing(scaled: number, passScaled: number): boolean {
  return scaled >= passScaled;
}

/** Full exam keeps the published time. Shorter sets get one minute per question. */
export function examMinutes(questionCount: number, fullCount: number, fullMinutes: number): number {
  if (questionCount >= fullCount) return fullMinutes;
  return Math.max(1, questionCount);
}
