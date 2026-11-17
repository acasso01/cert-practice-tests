import type { Question } from '../types';
import { shuffle } from './shuffle';

type Bucket = {
  id: string;
  weight: number;
  available: number;
};

/** Spread `count` seats across buckets by weight, without exceeding what each bucket has. */
export function allocateByWeight(buckets: Bucket[], count: number): Record<string, number> {
  const usable = buckets.filter((bucket) => bucket.available > 0 && bucket.weight > 0);
  const result: Record<string, number> = {};
  for (const bucket of buckets) result[bucket.id] = 0;
  if (usable.length === 0 || count <= 0) return result;

  const weightSum = usable.reduce((sum, bucket) => sum + bucket.weight, 0);
  const ranked = usable
    .map((bucket) => {
      const exact = (bucket.weight / weightSum) * count;
      return { ...bucket, floor: Math.floor(exact), frac: exact - Math.floor(exact) };
    })
    .sort((a, b) => b.frac - a.frac);

  for (const bucket of ranked) {
    result[bucket.id] = Math.min(bucket.floor, bucket.available);
  }

  let short = count - Object.values(result).reduce((sum, value) => sum + value, 0);
  while (short > 0) {
    let progressed = false;
    for (const bucket of ranked) {
      if (short === 0) break;
      if (result[bucket.id]! < bucket.available) {
        result[bucket.id] = result[bucket.id]! + 1;
        short -= 1;
        progressed = true;
      }
    }
    if (!progressed) break;
  }
  return result;
}

export function drawQuestions(
  questions: Question[],
  domains: { id: string; weight: number }[],
  count: number,
  domainIds: string[] | null,
): Question[] {
  const pool = domainIds?.length
    ? questions.filter((question) => domainIds.includes(question.domain))
    : questions;
  if (count >= pool.length) return shuffle(pool);

  const activeDomains = domains.filter((domain) => pool.some((question) => question.domain === domain.id));
  const allocation = allocateByWeight(
    activeDomains.map((domain) => ({
      id: domain.id,
      weight: domain.weight,
      available: pool.filter((question) => question.domain === domain.id).length,
    })),
    Math.min(count, pool.length),
  );

  const picked: Question[] = [];
  for (const domain of activeDomains) {
    const take = allocation[domain.id] ?? 0;
    picked.push(...shuffle(pool.filter((question) => question.domain === domain.id)).slice(0, take));
  }
  return shuffle(picked);
}
