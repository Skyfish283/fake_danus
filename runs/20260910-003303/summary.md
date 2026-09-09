# Research summary

## Problem

Call a function f : ℝ → ℝ angelic (resp. devilish) if there exist polynomials p and q with real coefficients such that for all real numbers x, f(x) is equal to p(ceil(x)) + ceil(q(x)) (resp. p(floor(x)) + floor(q(x)).
 
Find the largest real number c with the following property: given non constant polynomials f and g that are angelic and devilish respectively, if there is a real number s such that f(s) ≠ g(s), then there is a real number t such that |f(t) - g(t)| ≥ c.

## Outcome

Stopped because: interrupted by user.
Graph: 7 nodes, 0 edges (IDEA=4, PROMISING=2, UNVERIFIED=1).
Planner calls: 6. Worker calls: 8. Elapsed: 231s.
Model usage: 14 model calls, 32,875 input tokens, 70,032 output tokens (gemini-3.5-flash x14).

## Promising directions

- **[note_1]** (note, by planner) Both angelic and devilish functions f and g are piecewise constant. For any interval of the form (n-1, n], the ceiling ceil(x) is constant, and q(x) crosses integers only finitely many times (if q is non-constant). Thus, f(x) is constant on each subinterval of (n-1, n] determined by the preimages of integers under q(x). Similarly, g(x) is constant on subintervals of [m, m+1) determined by the preimages of integers under its second polynomial.
- **[note_2]** (note, by planner) The definition of angelic functions $f(x) = p(\lceil x \rceil) + \lceil q(x) \rceil$ implies that $f$ is piecewise constant. Indeed, $p(\lceil x \rceil)$ is constant on $(n-1, n]$ for any integer $n$, and $\lceil q(x) \rceil$ is constant on any interval not containing preimages of integers under $q$. Thus, $f$ is piecewise constant with finitely many jumps in any bounded interval. If $f$ is also a polynomial, it must be continuous, which forces $f$ to be constant. Thus, there are no non-constant polynomials that are angelic (or devilish). This strongly suggests that 'polynomials $f$ and $g$' in the problem statement is a typo for 'functions $f$ and $g$', or perhaps the polynomials $p$ and $q$ are restricted in some other way.

## Open ideas and questions

- **[question_1]** (question, by planner) Is the phrase 'non-constant polynomials f and g' in the problem statement a typo for 'non-constant functions f and g', or can polynomials actually be angelic or devilish?
- **[idea_1]** (idea, by planner) Investigate basic examples of angelic and devilish functions, and determine the minimum possible supremum of $|f(t) - g(t)|$ when they are not identical. In particular, test the case where $f(x) = \lceil x \rceil$ and $g(x) = \lfloor x \rfloor$ or variations thereof.
- **[hypothesis_1]** (hypothesis, by planner) The constant $c$ is likely $1/2$ or $1$, based on the jump discontinuities of the ceiling and floor functions. If they are non-constant, the differences must accumulate at some point to at least a certain threshold.
- **[question_2]** (question, by planner) If $f$ and $g$ are non-constant functions (rather than polynomials) that are angelic and devilish respectively, can we construct a sequence of such pairs where the supremum of $|f(t) - g(t)|$ is arbitrarily small? For example, consider $f(x) = \frac{1}{n}\lceil x \rceil$ and $g(x) = \frac{1}{n}\lfloor x \rfloor$. For these functions, $|f(t) - g(t)| \le 1/n$ for all $t$. If $n \to \infty$, the supremum of the difference tends to 0. This would mean that if the problem meant 'functions $f$ and $g$', the constant $c$ would have to be 0, which is trivial. Therefore, there must be some other constraint or the typo is different.

---

Nothing above is verified. Statuses record how the system judged each claim, not whether it is true.