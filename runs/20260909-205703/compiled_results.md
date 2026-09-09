# Instructions for LLM: Authoring the Mathematical Research Report

> [!IMPORTANT]
> **ROLE AND OBJECTIVE**
> You are an elite Research Mathematician and Theoretical Computer Scientist acting as Principal Investigator.
> Below are the comprehensive raw artifacts from an automated agentic mathematical research run, including:
> - Problem definition and runtime parameters
> - High-level Director's synthesis
> - The complete research graph (hypotheses, proved lemmas, identified obstacles, literature connections)
> - Unabridged worker derivations from the Mathematician, Explorer, and Skeptic roles
> - Literature retrieval and search results
>
> Your task is to analyze this dossier and write an exhaustive, publication-grade, mathematically rigorous **Research Report**.

## Required Report Sections

1. **Title & Executive Summary**
   - Provide a formal, descriptive title for the research paper/report.
   - Formulate a clear Abstract and Executive Summary synthesizing the core findings.
   - Summarize what was definitively proven, what promising conjectures were substantiated, and what fundamental barriers remain.

2. **Problem Formalization & Scope**
   - Rigorously define the sequence, series, dynamical system, or model under investigation.
   - Detail any structural reductions or reformulation lemmas discovered during the run (e.g., recurrence reduction from non-local sums to single-step recurrences, continuous embedding, etc.).
   - Explicitly define the parameter regimes explored (e.g. boundary values, small vs. large regimes, negative values, complex numbers, $p$-adic fields $\mathbb{Q}_p$).

3. **Rigorous Analysis of Lemmas & Promising Directions**
   - Present every major lemma, theorem, or promising approach established in the run.
   - For every claim, cite its corresponding node ID from the research graph (e.g., `[lemma_1]`, `[lemma_2]`, `[approach_10]`).
   - Carefully reconstruct, polish, and verify the mathematical proofs. Critically evaluate whether any proofs contain hidden assumptions, heuristic gaps, or unverified claims.

4. **Obstacles, Structural Barriers & Counterexamples**
   - Thoroughly analyze each obstacle identified by the research system (cite nodes like `[obstacle_1]`, `[obstacle_2]`).
   - Explain why standard methods fail (e.g., parity/sign oscillation destroying monotonicity, non-autonomous exponents preventing fixed-point theorems, superexponential growth, infinite moment hierarchies).
   - Distinguish fundamental mathematical impossibility/divergence results from technical obstacles that could potentially be bypassed with more refined techniques.

5. **Worker Perspective Comparison & Dialectic Synthesis**
   - Compare and contrast the different angles provided by the specialized agents:
     * **Mathematician**: Analytical bounds, asymptotic rates, classical convergence tests, algebraic manipulations.
     * **Explorer**: Unconventional reframings (continuous analogues, dynamical systems, $p$-adic valuations, root-landing absorbing states).
     * **Skeptic**: Boundary attacks, superexponential blow-up proofs, counterexamples, instability criteria.
   - Critique where the roles complemented or challenged each other, and summarize the consensus.

6. **Literature & Theoretical Context**
   - Integrate any papers or literature searches retrieved during the run.
   - Contextualize the findings within relevant mathematical literature (e.g., non-autonomous difference equations, ultrametric analysis, branching processes, etc.).

7. **Concrete Actionable Research Roadmap**
   - Provide a prioritized, numbered list of concrete next steps for human mathematicians or future agent runs.
   - Detail specific conjectures to formalize, boundary constants to compute, or numerical experiments to perform.

8. **Traceability Index**
   - Provide a concise reference table mapping key findings to their graph node IDs and worker task IDs.

## Mathematical Formatting & Tone Requirements
- Use formal academic mathematical prose with precise terminology.
- Render all formulas in clean LaTeX (`$ ... $` for inline formulas, `$$ ... $$` for display equations).
- Be intellectually honest: clearly separate verified rigorous proofs from heuristic intuitions or unproven conjectures.

---

# Dossier: Exploration Findings for `20260909-205703`

## Run Metadata

- **Run Identifier**: `20260909-205703`
- **Run Directory**: `C:\Users\samfe\OneDrive\Desktop\math_agent\math_agent\runs\20260909-205703`
- **Compiled At**: `2026-09-09 11:54:23 UTC`
- **First Event Timestamp**: `2026-09-09 11:27:03 UTC`
- **Last Event Timestamp**: `2026-09-09 11:54:23 UTC`
- **Total Elapsed Time**: 27m 19s (1639.9s)
- **Total Graph Nodes**: 22
- **Total Graph Edges**: 31
- **Worker Results Recorded**: 107
- **Total Events Logged**: 478
- **Node Breakdown by Status**: `IDEA`: 1, `OBSTACLE`: 5, `POTENTIALLY_RELEVANT`: 5, `PROMISING`: 10, `UNVERIFIED`: 1
- **Interactive Visual Graph**: Available as `interactive_graph.html` in this directory.

## Problem Statement

```text
Consider a parameter estimation rejection approximate bayesian computation algorithm, with MMD as the discreprancy measure rather than a summary statistic. How does the spectral properties, or other properties of the kernel of the MMD affect the convergence rate of the algorithm?
```

## Configuration Used

```toml
# Effective configuration for this run. API keys are redacted.
# Source: C:\Users\samfe\OneDrive\Desktop\math_agent\run_config.toml

[run]
mode = "main"
problem = "Consider a parameter estimation rejection approximate bayesian computation algorithm, with MMD as the discreprancy measure rather than a summary statistic. How does the spectral properties, or other properties of the kernel of the MMD affect the convergence rate of the algorithm?"
tag = ""
resume = ""

[budget]
max_planner_calls = 1000
max_worker_calls = 1000
max_wall_clock_seconds = 1800
max_concurrent_workers = 4

[models]
provider = "gemini"
planner = "adaptive"
worker = "adaptive"
baseline = "adaptive"

[thinking]
planner = "HIGH"
worker = "HIGH"
baseline = "HIGH"

[api_keys]
default = "set (...Kf7w)"
planner = "set (...Kf7w)"
baseline = "set (...Kf7w)"
worker_1 = "set (...vd7Y)"
worker_2 = "set (...wlqw)"
worker_3 = "set (...OsMA)"
worker_4 = "set (...WRQw)"
worker_5 = "not set"
worker_6 = "not set"

[adaptive]
ladder = ["gemini-3.7-flash", "gemini-3.6-flash", "gemini-3.5-flash", "gemini-3.5-flash-lite"]
cooldown_seconds = 180

[literature]
openalex_mailto = "math-agent-prototype@example.com"
search_result_limit = 8

[viewer]
enabled = true
port = 8765
open_browser = true
poll_ms = 1000
```

# Director's Synthesis & System Summary

# Research summary

## Problem

Consider a parameter estimation rejection approximate bayesian computation algorithm, with MMD as the discreprancy measure rather than a summary statistic. How does the spectral properties, or other properties of the kernel of the MMD affect the convergence rate of the algorithm?

## Outcome

Stopped because: planner returned FINISH.
Graph: 22 nodes, 31 edges (IDEA=1, PROMISING=10, UNVERIFIED=1, OBSTACLE=5, POTENTIALLY_RELEVANT=5).
Planner calls: 117. Worker calls: 226. Elapsed: 1640s.
Model usage: 333 model calls, 1,274,263 input tokens, 1,121,801 output tokens (gemini-3.5-flash-lite x300, gemini-3.5-flash x17, gemini-3.6-flash x12, gemini-3.7-flash x4).

## Director's report

Comprehensive Summary of MMD-ABC Spectral Convergence Analysis:

1. Spectral Representation and Dual Curse: The squared MMD admits an exact spectral expansion $\text{MMD}^2(P_0, P_\theta) = \sum_{j=1}^^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, where $\lambda_j$ are kernel integral operator eigenvalues. Rapid eigenvalue decay (e.g., Gaussian kernels) suppresses empirical estimation variance by damping high-frequency components, but simultaneously flattens the population MMD profile around $\theta_0$. This causes severe parameter identifiability loss, manifesting either as an inflated modulus exponent $\beta$ or an exponentially decaying preconstant $c(d) \propto a^{-d}$ in high dimensions $d$ (Dimension-Dependent Preconstant Curse).

2. The Smoothness Dilemma and Minimax Rates: Smooth kernels (exponential spectral decay) yield fast empirical rates $\alpha \approx 1/2$ for estimating MMD but suffer from severe high-dimensional identifiability degradation. Rougher kernels preserve parameter sensitivity but have slower empirical convergence rates $n^{-s/d}$. Theorem 1 establishes that the optimal kernel smoothness is $s^* = d/2$, achieving the minimax non-parametric posterior contraction rate $n^{-p/(d+2p)}$ for parameters in a Sobolev ellipsoid of smoothness $p$.

3. ABC Rejection Filter and Denominator Small-Ball Probabilities: Unlike generalized Bayesian inference with a Gibbs posterior, rejection ABC uses an indicator filter $\mathbb{I}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$. Analyzing the ABC contraction rate requires controlling both the numerator via empirical concentration and the denominator via small-ball probabilities. In high dimensions, Mercer eigenvalue decay causes exponential volume shrinkage of the ABC acceptance region unless tolerances $\epsilon_n$ and bandwidths $\gamma$ scale appropriately with dimension $d$.

4. Bandwidth and Spectral Truncation Optimization: As formalized in Lemma 4, optimizing the kernel bandwidth $\gamma$ and spectral truncation level $K$ requires minimizing the sum of squared spectral bias and effective dimension variance $\mathcal{V}(\gamma, K; n) \approx \frac{1}{n} \sum_{j=1}^K \lambda_j(\gamma)^2$. This explicitly characterizes how kernel smoothness governs the bias-variance trade-off in high-dimensional MMD-ABC.

## Promising directions

- **[lemma_1]** (lemma, by planner) Spectral representation of squared MMD: MMD^2(P_0, P_theta) = sum_{j=1}^infty lambda_j (mu_{0,j} - mu_{theta,j})^2, where lambda_j are kernel integral operator eigenvalues. Rapid eigenvalue decay (e.g. Gaussian kernels) heavily damps high-frequency discrepancies, leading to an ill-posed inverse map theta -> MMD.
- **[hypothesis_1]** (hypothesis, by planner) The Smoothness Dilemma in MMD-ABC: The posterior contraction rate is governed by a trade-off between the empirical MMD convergence rate $O_p(n^{-\alpha})$ and the parameter identifiability modulus $MMD(P_\theta, P_0) \ge c \|\theta - \theta_0\|^\beta$. Smooth kernels (exponential spectral decay, e.g., Gaussian) yield fast empirical rates $\alpha \approx 1/2$ but poor sensitivity (large $\beta$), whereas rougher kernels (polynomial spectral decay, e.g., Matérn) preserve sensitivity (smaller $\beta$) but suffer from slow empirical rates $\alpha$ in high dimensions.
- **[idea_1]** (idea, by planner) Spectral Truncation for MMD-ABC Rejection Bounds: To bound the rejection probability P(MMD_hat_n^2 <= epsilon_n^2) under P_theta, we can project the empirical MMD onto the subspace spanned by the top K_n eigenfunctions of the kernel integral operator. The first K_n components enjoy parametric convergence rates, while the tail sum_{j > K_n} lambda_j is controlled by the kernel's spectral decay. Choosing K_n optimally to balance truncation error and estimation variance allows bounding the small-ball probability, bypassing the hard-threshold indicator obstacle.
- **[counterexample_1]** (counterexample, by planner) Explicit calculation of $\text{MMD}^2(P_0, P_\theta)$ for 1D Gaussian location families $P_0 = \mathcal{N}(0,1)$ and $P_\theta = \mathcal{N}(\theta,1)$ using a Gaussian kernel $k_h(x,y) = \exp(-(x-y)^2/(2h^2))$ via Fourier representation: $\text{MMD}^2(P_0, P_\theta) = \frac{h}{\sqrt{2+h^2}} \left(1 - \exp\left(-\frac{\theta^2}{2(2+h^2)}\right)\right)$. For small $\theta$, $\text{MMD}^2(P_0, P_\theta) \asymp \frac{\theta^2}{2+h^2}$, confirming identifiability exponent $\beta = 1$ with preconstant depending on kernel bandwidth $h$.
- **[hypothesis_2]** (hypothesis, by planner) Dimension-Dependent Preconstant Curse: In parametric MMD-ABC, rather than a worse exponent $\beta$ in the identifiability modulus $\mathrm{MMD}(P_\theta, P_0) \ge c \|\theta - \theta_0\|^\beta$, smooth kernels suffer from an exponentially decaying preconstant $c(d) \propto a^{-d}$ with dimension $d$. For a fixed sample size $n$ or tolerance $\epsilon$, this decay acts as an effective identifiability loss, requiring the tolerance $\epsilon$ to scale exponentially with $d$ to maintain a non-vanishing posterior acceptance rate, which degrades the practical ABC contraction rate in high dimensions.
- **[idea_2]** (idea, by planner) RKHS Trace Independence vs. Spectral Decay Curse: Although the total trace of the kernel integral operator \int k(x,x) dP_0(x) is bounded by \sup_x k(x,x) independently of the dimension (preserving the O_p(n^{-1/2}) concentration rate of the empirical MMD), the individual eigenvalues decay slower as \lambda_j \sim j^{-2s/d}$ in high dimensions d. This slow decay does not degrade empirical convergence but flattens the population MMD profile around \theta_0, causing a severe parameter sensitivity loss (either an inflated exponent \beta or a vanishing preconstant c).
- **[lemma_2]** (lemma, by planner) Hoeffding Projection Variance under Spectral Representation: For a kernel with Mercer spectral representation $k(x,y) = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(y)$ with orthonormal eigenfunctions $e_j$ with respect to a reference measure $P_0$, the variance of the first-order projection (Hoeffding projection) of the empirical MMD is given by $\operatorname{Var}_{X \sim P_0}(\mathbb{E}_{Y \sim P_\theta}[k(X, Y)]) = \sum_{j=1}^\infty \lambda_j^2 (\mu_{0, j} - \mu_{\theta, j})^2 \operatorname{Var}(e_j(X))$, where $\mu_{0, j} = \mathbb{E}_{X \sim P_0}[e_j(X)]$ and $\mu_{\theta, j} = \mathbb{E}_{Y \sim P_\theta}[e_j(Y)]$. This formula demonstrates that rapid eigenvalue decay suppresses the variance of the empirical MMD estimator by dampening high-frequency components, but simultaneously degrades parameter sensitivity in directions aligned with high-frequency eigenfunctions.
- **[note_1]** (note, by planner) Exact MMD for Gaussian location family P_0 = N(0, I_d) and P_theta = N(theta, I_d) with kernel k(x,y) = exp(-gamma ||x-y||^2): MMD^2(P_0, P_ heta) = 2 (1 + 4oldsymbol{eta})^{-d/2} [1 - ext{correction}]$. The preconstant decays as $(1+4 heta)^{-d/2}$ or $(1+4 u)^{-d/2}$, proving the dimension-dependent preconstant curse.
- **[lemma_3]** (lemma, by planner) Volume Shrinkage in High-Dimensional ABC Acceptance Regions: For a Gaussian location family in dimension d with isotropic prior, the parameter acceptance region has a volume scaling as V_d ≈ (2΀e ̄Ε^2 / (d w C_Γ))^{d/2}, leading to an exponentially vanishing prior mass and acceptance probability as d → ∑ unless tolerance scales with dimension.
- **[theorem_1]** (theorem, by planner) Optimal Kernel Smoothness and Minimax Rates in Non-Parametric MMD-ABC: For a parameter theta in a Sobolev ellipsoid of smoothness p, and a kernel with Mercer eigenvalue decay lambda_j ~ j^{-2s/d}, the MMD-ABC posterior contraction rate balances empirical estimation variance and ill-posedness. If s < d/2 (rough kernel), empirical MMD estimation is slow (rate n^{-s/d}), yielding posterior contraction n^{-sp/(d(s+p))}. If s > d/2 (smooth kernel), empirical MMD converges at n^{-1/2}, but high-frequency parameter differences are heavily damped, yielding rate n^{-p/(2(s+p))}. The optimal smoothness is s* = d/2, achieving the minimax non-parametric rate n^{-p/(d+2p)}.

## Obstacles

- **[obstacle_1]** (obstacle, by planner) ABC rejection uses an indicator filter I(widehat{MMD}_n <= epsilon), differing from the Gibbs/generalized posterior exp(-gamma_n n MMD^2) studied in literature. Analyzing joint limits n, m -> inf and epsilon -> 0 requires delicate control of ABC bias-variance trade-offs.
- **[obstacle_2]** (obstacle, by planner) Simulation vs data sample size asymmetry: empirical MMD between size n (observed) and size m (simulated) has variance dominated by min(n, m), creating difficulties when m is large but n is fixed in ABC.
- **[obstacle_3]** (obstacle, by planner) Curse of Dimensionality in Mercer Spectral Decay: For a kernel with smoothness $s$ on a $d$-dimensional domain, Mercer eigenvalues decay as $\lambda_j \sim j^{-2s/d}$. In high dimensions, this decay is extremely slow unless the smoothness $s$ is very large. Slow decay increases the effective dimension of the RKHS, which inflates the variance of empirical MMD estimators and severely degrades the MMD-ABC convergence rate.
- **[obstacle_4]** (obstacle, by planner) Degeneracy of the ABC Denominator via Spectral Decay: Bounding the ABC posterior denominator from below requires ensuring a non-vanishing prior mass for the acceptance region {\theta : \widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) \le \epsilon_n^2}. Taylor-expanding the population MMD around the true parameter \theta_0 yields \mathrm{MMD}^2(P_0, P_\theta) \approx (\theta - \theta_0)^T H(\theta_0) (\theta - \theta_0), where H(\theta_0) is the Hessian. If the kernel's Mercer eigenvalues decay rapidly, the eigenvalues of H(\theta_0) decay correspondingly in directions of high-frequency eigenfunctions, making the acceptance region extremely narrow along those dimensions and exponentially shrinking the prior volume of the accepted region.
- **[obstacle_5]** (obstacle, by planner) Failure and Dimensional Explosion of Naive Spectral Truncation in MMD-ABC: If the true parameter theta_0 or perturbation lies along high-frequency kernel eigenfunctions, fixed-order spectral truncation yields zero signal or a massive truncation error that grows exponentially in dimension d unless truncation level K_n scales exponentially, rendering naive spectral truncation vacuous in high dimensions without smoothness constraints.

## Open ideas and questions

- **[idea_3]** (idea, by planner) Sobolev Norm Constrained Parameter Classes for MMD-ABC: Restricting the parameter-to-distribution mapping via Sobolev norm bounds on the score operator nabla_theta P_theta in terms of the kernel's eigenbasis rules out high-frequency activation, rescuing spectral truncation and small-ball probability bounds in high dimensions.

## Literature

- **[paper_1]** (paper, by planner) Cherief-Abdellatif & Alquier (2020) establish consistency and exponential contraction rates for generalized Bayesian inference using MMD as loss, governed by bracketing entropy and modulus of continuity.
- **[paper_2]** (paper, by planner) Bernton, Jacob, Gerber, and Robert (2019) 'Approximate Bayesian Computation with the Wasserstein Distance'. Establishes posterior contraction rates for rejection ABC using Wasserstein distance W_1 by bounding the denominator via small-ball probabilities of W_1(P_hat_n, P_0) and utilizing a modulus of continuity for parameter identifiability: W_1(P_theta, P_0) >= c ||theta - theta_0||^beta.
- **[paper_3]** (paper, by planner) Frazier, Martin, Robert, & Rousseau (2018) 'Asymptotic properties of approximate Bayesian computation' (arXiv:1803.10986). This work establishes that posterior contraction in rejection ABC is driven by the small-ball probabilities of the chosen discrepancy measure near zero, providing a blueprint for the asymptotic analysis of MMD-ABC.
- **[paper_4]** (paper, by planner) Sriperumbudur, Gretton, Györfi, Schölkopf, & Lanckriet (2010) 'Hilbert Space Embeddings and Metrics on Probability Measures'. This paper links the spectral properties (Fourier transform / eigenvalue decay) of kernel integral operators to the topological and convergence metrization properties of MMD.
- **[paper_5]** (paper, by planner) Cloninger (2018) 'Bounding the Error From Reference Set Kernel Maximum Mean Discrepancy' (arXiv:1812.04594). Establishes non-asymptotic error bounds for approximating MMD via a subset of R reference points and weights, controlled by the spectral decay of kernel Laplacian eigenfunctions. Suggests that projecting onto low-frequency eigenfunctions captures almost all MMD energy, offering a mechanism to accelerate MMD computation in large-sample or ABC regimes.

## Connections

- hypothesis_1 --possible_approach--> problem
- obstacle_3 --blocks--> problem
- lemma_1 --related_to--> obstacle_3
- paper_2 --related_to--> obstacle_1
- idea_1 --addresses--> obstacle_1
- idea_1 --depends_on--> lemma_1
- counterexample_1 --contradicts--> hypothesis_1
- hypothesis_2 --derived_from--> hypothesis_1
- hypothesis_2 --possible_approach--> problem
- lemma_1 --related_to--> obstacle_4
- obstacle_4 --blocks--> problem
- idea_2 --depends_on--> lemma_1
- idea_2 --addresses--> obstacle_3
- lemma_1 --related_to--> obstacle_1
- hypothesis_1 --depends_on--> lemma_1
- counterexample_1 --related_to--> lemma_1
- hypothesis_2 --addresses--> obstacle_4
- hypothesis_2 --related_to--> obstacle_4
- paper_5 --related_to--> idea_1
- obstacle_4 --supports--> hypothesis_2
- obstacle_1 --related_to--> obstacle_2
- lemma_1 --depends_on--> obstacle_2
- lemma_3 --supports--> hypothesis_2
- lemma_3 --supports--> obstacle_4
- obstacle_5 --contradicts--> idea_1
- idea_3 --addresses--> obstacle_5
- idea_3 --possible_approach--> problem
- idea_3 --addresses--> obstacle_4
- theorem_1 --addresses--> problem
- theorem_1 --supports--> hypothesis_1
- note_1 --supports--> hypothesis_2

---

Nothing above is verified. Statuses record how the system judged each claim, not whether it is true.


---

# Research Graph State & Knowledge Catalog

The graph contains **22 nodes** and **31 directed edges**.

## Status: PROMISING (10 nodes)

### `[lemma_1]` (lemma, created by planner)

**Content**:
Spectral representation of squared MMD: MMD^2(P_0, P_theta) = sum_{j=1}^infty lambda_j (mu_{0,j} - mu_{theta,j})^2, where lambda_j are kernel integral operator eigenvalues. Rapid eigenvalue decay (e.g. Gaussian kernels) heavily damps high-frequency discrepancies, leading to an ill-posed inverse map theta -> MMD.

**Graph Connections**:
- Outgoing: `related_to` -> `obstacle_3`; `related_to` -> `obstacle_4`; `related_to` -> `obstacle_1`; `depends_on` -> `obstacle_2`
- Incoming: `idea_1` -`depends_on`-> this; `idea_2` -`depends_on`-> this; `hypothesis_1` -`depends_on`-> this; `counterexample_1` -`related_to`-> this

### `[hypothesis_1]` (hypothesis, created by planner)

**Content**:
The Smoothness Dilemma in MMD-ABC: The posterior contraction rate is governed by a trade-off between the empirical MMD convergence rate $O_p(n^{-\alpha})$ and the parameter identifiability modulus $MMD(P_\theta, P_0) \ge c \|\theta - \theta_0\|^\beta$. Smooth kernels (exponential spectral decay, e.g., Gaussian) yield fast empirical rates $\alpha \approx 1/2$ but poor sensitivity (large $\beta$), whereas rougher kernels (polynomial spectral decay, e.g., Matérn) preserve sensitivity (smaller $\beta$) but suffer from slow empirical rates $\alpha$ in high dimensions.

**Attached Notes**:
- *planner*: Refined by toy example findings: in location families, the smoothness dilemma does not manifest as a changing identifiability exponent $\beta$ (which remains $\beta = 1$ for all Matérn kernels), but rather as a variance breakdown threshold $s \le d/4$ versus the dimension-dependent preconstant curse for smooth kernels.
- *planner*: The smoothness and identifiability trade-off must be restricted to bounded kernels to prevent moment divergence issues highlighted in heavy-tailed counterexamples.

**Graph Connections**:
- Outgoing: `possible_approach` -> `problem`; `depends_on` -> `lemma_1`
- Incoming: `counterexample_1` -`contradicts`-> this; `hypothesis_2` -`derived_from`-> this; `theorem_1` -`supports`-> this

### `[idea_1]` (idea, created by planner)

**Content**:
Spectral Truncation for MMD-ABC Rejection Bounds: To bound the rejection probability P(MMD_hat_n^2 <= epsilon_n^2) under P_theta, we can project the empirical MMD onto the subspace spanned by the top K_n eigenfunctions of the kernel integral operator. The first K_n components enjoy parametric convergence rates, while the tail sum_{j > K_n} lambda_j is controlled by the kernel's spectral decay. Choosing K_n optimally to balance truncation error and estimation variance allows bounding the small-ball probability, bypassing the hard-threshold indicator obstacle.

**Attached Notes**:
- *planner*: Subgoal 1 (spectral truncation variance and tail bound) successfully formalized.

**Graph Connections**:
- Outgoing: `addresses` -> `obstacle_1`; `depends_on` -> `lemma_1`
- Incoming: `paper_5` -`related_to`-> this; `obstacle_5` -`contradicts`-> this

### `[counterexample_1]` (counterexample, created by planner)

**Content**:
Explicit calculation of $\text{MMD}^2(P_0, P_\theta)$ for 1D Gaussian location families $P_0 = \mathcal{N}(0,1)$ and $P_\theta = \mathcal{N}(\theta,1)$ using a Gaussian kernel $k_h(x,y) = \exp(-(x-y)^2/(2h^2))$ via Fourier representation: $\text{MMD}^2(P_0, P_\theta) = \frac{h}{\sqrt{2+h^2}} \left(1 - \exp\left(-\frac{\theta^2}{2(2+h^2)}\right)\right)$. For small $\theta$, $\text{MMD}^2(P_0, P_\theta) \asymp \frac{\theta^2}{2+h^2}$, confirming identifiability exponent $\beta = 1$ with preconstant depending on kernel bandwidth $h$.

**Attached Notes**:
- *planner*: Added explicit MMD integration results supporting the constant prefactor dependency.

**Graph Connections**:
- Outgoing: `contradicts` -> `hypothesis_1`; `related_to` -> `lemma_1`

### `[hypothesis_2]` (hypothesis, created by planner)

**Content**:
Dimension-Dependent Preconstant Curse: In parametric MMD-ABC, rather than a worse exponent $\beta$ in the identifiability modulus $\mathrm{MMD}(P_\theta, P_0) \ge c \|\theta - \theta_0\|^\beta$, smooth kernels suffer from an exponentially decaying preconstant $c(d) \propto a^{-d}$ with dimension $d$. For a fixed sample size $n$ or tolerance $\epsilon$, this decay acts as an effective identifiability loss, requiring the tolerance $\epsilon$ to scale exponentially with $d$ to maintain a non-vanishing posterior acceptance rate, which degrades the practical ABC contraction rate in high dimensions.

**Attached Notes**:
- *planner*: Confirmed by explicit calculation for the Gaussian location family: the identifiability preconstant c(d) decays exponentially as (1 + 1/(2
u))^{-(d+2)/4}, driving an exponential dimension curse in the posterior contraction rate.
- *planner*: Rigorously confirmed in d dimensions via exact analytical calculation in lemma_3.
- *planner*: Confirmed by counterexample flex_6: choosing a dimension-adaptive bandwidth h = Theta(sqrt{d}) prevents the exponential decay of the prefactor (h^2/(h^2+2))^{d/2} -> 0, successfully bypassing the dimension-dependent preconstant curse.

**Graph Connections**:
- Outgoing: `derived_from` -> `hypothesis_1`; `possible_approach` -> `problem`; `addresses` -> `obstacle_4`; `related_to` -> `obstacle_4`
- Incoming: `obstacle_4` -`supports`-> this; `lemma_3` -`supports`-> this; `note_1` -`supports`-> this

### `[idea_2]` (idea, created by planner)

**Content**:
RKHS Trace Independence vs. Spectral Decay Curse: Although the total trace of the kernel integral operator \int k(x,x) dP_0(x) is bounded by \sup_x k(x,x) independently of the dimension (preserving the O_p(n^{-1/2}) concentration rate of the empirical MMD), the individual eigenvalues decay slower as \lambda_j \sim j^{-2s/d}$ in high dimensions d. This slow decay does not degrade empirical convergence but flattens the population MMD profile around \theta_0, causing a severe parameter sensitivity loss (either an inflated exponent \beta or a vanishing preconstant c).

**Graph Connections**:
- Outgoing: `depends_on` -> `lemma_1`; `addresses` -> `obstacle_3`

### `[lemma_2]` (lemma, created by planner)

**Content**:
Hoeffding Projection Variance under Spectral Representation: For a kernel with Mercer spectral representation $k(x,y) = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(y)$ with orthonormal eigenfunctions $e_j$ with respect to a reference measure $P_0$, the variance of the first-order projection (Hoeffding projection) of the empirical MMD is given by $\operatorname{Var}_{X \sim P_0}(\mathbb{E}_{Y \sim P_\theta}[k(X, Y)]) = \sum_{j=1}^\infty \lambda_j^2 (\mu_{0, j} - \mu_{\theta, j})^2 \operatorname{Var}(e_j(X))$, where $\mu_{0, j} = \mathbb{E}_{X \sim P_0}[e_j(X)]$ and $\mu_{\theta, j} = \mathbb{E}_{Y \sim P_\theta}[e_j(Y)]$. This formula demonstrates that rapid eigenvalue decay suppresses the variance of the empirical MMD estimator by dampening high-frequency components, but simultaneously degrades parameter sensitivity in directions aligned with high-frequency eigenfunctions.

**Attached Notes**:
- *planner*: Confirmed via U-statistic Hoeffding chaos decomposition: first-order projection variance is sum_{j=1}^infty lambda_j^2 (mu_{0,j} - mu_{theta,j})^2 Var(e_j(X)).

### `[note_1]` (note, created by planner)

**Content**:
Exact MMD for Gaussian location family P_0 = N(0, I_d) and P_theta = N(theta, I_d) with kernel k(x,y) = exp(-gamma ||x-y||^2): MMD^2(P_0, P_	heta) = 2 (1 + 4oldsymbol{eta})^{-d/2} [1 - 	ext{correction}]$. The preconstant decays as $(1+4	heta)^{-d/2}$ or $(1+4
u)^{-d/2}$, proving the dimension-dependent preconstant curse.

**Attached Notes**:
- *planner*: Exact MMD formula calculation shows kernel bandwidth scaling h = Theta(sqrt{d}) maintains a non-vanishing prefactor asymptotic to e^{-1} in high dimensions.

**Graph Connections**:
- Outgoing: `supports` -> `hypothesis_2`

### `[lemma_3]` (lemma, created by planner)

**Content**:
Volume Shrinkage in High-Dimensional ABC Acceptance Regions: For a Gaussian location family in dimension d with isotropic prior, the parameter acceptance region has a volume scaling as V_d ≈ (2΀e ̄Ε^2 / (d w C_Γ))^{d/2}, leading to an exponentially vanishing prior mass and acceptance probability as d → ∑ unless tolerance scales with dimension.

**Graph Connections**:
- Outgoing: `supports` -> `hypothesis_2`; `supports` -> `obstacle_4`

### `[theorem_1]` (theorem, created by planner)

**Content**:
Optimal Kernel Smoothness and Minimax Rates in Non-Parametric MMD-ABC: For a parameter theta in a Sobolev ellipsoid of smoothness p, and a kernel with Mercer eigenvalue decay lambda_j ~ j^{-2s/d}, the MMD-ABC posterior contraction rate balances empirical estimation variance and ill-posedness. If s < d/2 (rough kernel), empirical MMD estimation is slow (rate n^{-s/d}), yielding posterior contraction n^{-sp/(d(s+p))}. If s > d/2 (smooth kernel), empirical MMD converges at n^{-1/2}, but high-frequency parameter differences are heavily damped, yielding rate n^{-p/(2(s+p))}. The optimal smoothness is s* = d/2, achieving the minimax non-parametric rate n^{-p/(d+2p)}.

**Graph Connections**:
- Outgoing: `addresses` -> `problem`; `supports` -> `hypothesis_1`


## Status: OBSTACLE (5 nodes)

### `[obstacle_1]` (obstacle, created by planner)

**Content**:
ABC rejection uses an indicator filter I(widehat{MMD}_n <= epsilon), differing from the Gibbs/generalized posterior exp(-gamma_n n MMD^2) studied in literature. Analyzing joint limits n, m -> inf and epsilon -> 0 requires delicate control of ABC bias-variance trade-offs.

**Attached Notes**:
- *planner*: Confirmed by decomposer: hard rejection indicator discontinuity lacks smoothness of exponential Gibbs weights, requiring U-process large deviations.
- *planner*: Toy model analysis demonstrates that replacing the non-Lipschitz indicator I(widehat{MMD}_n^2 <= epsilon_n^2) with a smoothed exponential weight exp(-gamma_n W_n) resolves the boundary discontinuity obstacle and permits standard Gibbs posterior contraction proofs.

**Graph Connections**:
- Outgoing: `related_to` -> `obstacle_2`
- Incoming: `paper_2` -`related_to`-> this; `idea_1` -`addresses`-> this; `lemma_1` -`related_to`-> this

### `[obstacle_2]` (obstacle, created by planner)

**Content**:
Simulation vs data sample size asymmetry: empirical MMD between size n (observed) and size m (simulated) has variance dominated by min(n, m), creating difficulties when m is large but n is fixed in ABC.

**Attached Notes**:
- *planner*: Task 54 confirmed empirical MMD variance decomposes as O(1/n + 1/m). Thus, maintaining statistical rate parity requires simulation sample size m(n) = Omega(n).

**Graph Connections**:
- Incoming: `obstacle_1` -`related_to`-> this; `lemma_1` -`depends_on`-> this

### `[obstacle_3]` (obstacle, created by planner)

**Content**:
Curse of Dimensionality in Mercer Spectral Decay: For a kernel with smoothness $s$ on a $d$-dimensional domain, Mercer eigenvalues decay as $\lambda_j \sim j^{-2s/d}$. In high dimensions, this decay is extremely slow unless the smoothness $s$ is very large. Slow decay increases the effective dimension of the RKHS, which inflates the variance of empirical MMD estimators and severely degrades the MMD-ABC convergence rate.

**Attached Notes**:
- *planner*: Confirmed via rank-1 linear kernel toy example that infinite-dimensional spectral decay is necessary for the dimensionality curse; finite-dimensional or rank-deficient kernels bypass variance inflation and preconstant decay.

**Graph Connections**:
- Outgoing: `blocks` -> `problem`
- Incoming: `lemma_1` -`related_to`-> this; `idea_2` -`addresses`-> this

### `[obstacle_4]` (obstacle, created by planner)

**Content**:
Degeneracy of the ABC Denominator via Spectral Decay: Bounding the ABC posterior denominator from below requires ensuring a non-vanishing prior mass for the acceptance region {\theta : \widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) \le \epsilon_n^2}. Taylor-expanding the population MMD around the true parameter \theta_0 yields \mathrm{MMD}^2(P_0, P_\theta) \approx (\theta - \theta_0)^T H(\theta_0) (\theta - \theta_0), where H(\theta_0) is the Hessian. If the kernel's Mercer eigenvalues decay rapidly, the eigenvalues of H(\theta_0) decay correspondingly in directions of high-frequency eigenfunctions, making the acceptance region extremely narrow along those dimensions and exponentially shrinking the prior volume of the accepted region.

**Attached Notes**:
- *planner*: Confirmed via worker derivation that rapid kernel eigenvalue decay \lambda_j drives \lambda_{\min}(H(\theta_0)) to zero when parameter variations align with high-frequency eigenfunctions.
- *planner*: Counterexamples demonstrate that Taylor expansions and Hessian existence fail for unbounded kernels under heavy-tailed models, reinforcing that kernel boundedness is a prerequisite for local volume shrinkage analysis.
- *planner*: Clarified by sketcher: Acceptance region is infinitely flat/wide along high-frequency directions (semi-axis lengths r_k = epsilon / sqrt(nu_k) -> infinity), causing unidentifiability rather than prior volume shrinkage.

**Graph Connections**:
- Outgoing: `blocks` -> `problem`; `supports` -> `hypothesis_2`
- Incoming: `lemma_1` -`related_to`-> this; `hypothesis_2` -`addresses`-> this; `hypothesis_2` -`related_to`-> this; `lemma_3` -`supports`-> this; `idea_3` -`addresses`-> this

### `[obstacle_5]` (obstacle, created by planner)

**Content**:
Failure and Dimensional Explosion of Naive Spectral Truncation in MMD-ABC: If the true parameter theta_0 or perturbation lies along high-frequency kernel eigenfunctions, fixed-order spectral truncation yields zero signal or a massive truncation error that grows exponentially in dimension d unless truncation level K_n scales exponentially, rendering naive spectral truncation vacuous in high dimensions without smoothness constraints.

**Graph Connections**:
- Outgoing: `contradicts` -> `idea_1`
- Incoming: `idea_3` -`addresses`-> this


## Status: IDEA (1 nodes)

### `[idea_3]` (idea, created by planner)

**Content**:
Sobolev Norm Constrained Parameter Classes for MMD-ABC: Restricting the parameter-to-distribution mapping via Sobolev norm bounds on the score operator nabla_theta P_theta in terms of the kernel's eigenbasis rules out high-frequency activation, rescuing spectral truncation and small-ball probability bounds in high dimensions.

**Graph Connections**:
- Outgoing: `addresses` -> `obstacle_5`; `possible_approach` -> `problem`; `addresses` -> `obstacle_4`


## Status: UNVERIFIED (1 nodes)

### `[problem]` (problem, created by user)

**Content**:
Consider a parameter estimation rejection approximate bayesian computation algorithm, with MMD as the discreprancy measure rather than a summary statistic. How does the spectral properties, or other properties of the kernel of the MMD affect the convergence rate of the algorithm?

**Graph Connections**:
- Incoming: `hypothesis_1` -`possible_approach`-> this; `obstacle_3` -`blocks`-> this; `hypothesis_2` -`possible_approach`-> this; `obstacle_4` -`blocks`-> this; `idea_3` -`possible_approach`-> this; `theorem_1` -`addresses`-> this


## Status: POTENTIALLY_RELEVANT (5 nodes)

### `[paper_1]` (paper, created by planner)

**Content**:
Cherief-Abdellatif & Alquier (2020) establish consistency and exponential contraction rates for generalized Bayesian inference using MMD as loss, governed by bracketing entropy and modulus of continuity.

### `[paper_2]` (paper, created by planner)

**Content**:
Bernton, Jacob, Gerber, and Robert (2019) 'Approximate Bayesian Computation with the Wasserstein Distance'. Establishes posterior contraction rates for rejection ABC using Wasserstein distance W_1 by bounding the denominator via small-ball probabilities of W_1(P_hat_n, P_0) and utilizing a modulus of continuity for parameter identifiability: W_1(P_theta, P_0) >= c ||theta - theta_0||^beta.

**Graph Connections**:
- Outgoing: `related_to` -> `obstacle_1`

### `[paper_3]` (paper, created by planner)

**Content**:
Frazier, Martin, Robert, & Rousseau (2018) 'Asymptotic properties of approximate Bayesian computation' (arXiv:1803.10986). This work establishes that posterior contraction in rejection ABC is driven by the small-ball probabilities of the chosen discrepancy measure near zero, providing a blueprint for the asymptotic analysis of MMD-ABC.

### `[paper_4]` (paper, created by planner)

**Content**:
Sriperumbudur, Gretton, Györfi, Schölkopf, & Lanckriet (2010) 'Hilbert Space Embeddings and Metrics on Probability Measures'. This paper links the spectral properties (Fourier transform / eigenvalue decay) of kernel integral operators to the topological and convergence metrization properties of MMD.

### `[paper_5]` (paper, created by planner)

**Content**:
Cloninger (2018) 'Bounding the Error From Reference Set Kernel Maximum Mean Discrepancy' (arXiv:1812.04594). Establishes non-asymptotic error bounds for approximating MMD via a subset of R reference points and weights, controlled by the spectral decay of kernel Laplacian eigenfunctions. Suggests that projecting onto low-frequency eigenfunctions captures almost all MMD energy, offering a mechanism to accelerate MMD computation in large-sample or ABC regimes.

**Graph Connections**:
- Outgoing: `related_to` -> `idea_1`


## Graph Relations Index (Edges)

| Source Node | Relation | Target Node |
| :--- | :--- | :--- |
| `hypothesis_1` | `possible_approach` | `problem` |
| `obstacle_3` | `blocks` | `problem` |
| `lemma_1` | `related_to` | `obstacle_3` |
| `paper_2` | `related_to` | `obstacle_1` |
| `idea_1` | `addresses` | `obstacle_1` |
| `idea_1` | `depends_on` | `lemma_1` |
| `counterexample_1` | `contradicts` | `hypothesis_1` |
| `hypothesis_2` | `derived_from` | `hypothesis_1` |
| `hypothesis_2` | `possible_approach` | `problem` |
| `lemma_1` | `related_to` | `obstacle_4` |
| `obstacle_4` | `blocks` | `problem` |
| `idea_2` | `depends_on` | `lemma_1` |
| `idea_2` | `addresses` | `obstacle_3` |
| `lemma_1` | `related_to` | `obstacle_1` |
| `hypothesis_1` | `depends_on` | `lemma_1` |
| `counterexample_1` | `related_to` | `lemma_1` |
| `hypothesis_2` | `addresses` | `obstacle_4` |
| `hypothesis_2` | `related_to` | `obstacle_4` |
| `paper_5` | `related_to` | `idea_1` |
| `obstacle_4` | `supports` | `hypothesis_2` |
| `obstacle_1` | `related_to` | `obstacle_2` |
| `lemma_1` | `depends_on` | `obstacle_2` |
| `lemma_3` | `supports` | `hypothesis_2` |
| `lemma_3` | `supports` | `obstacle_4` |
| `obstacle_5` | `contradicts` | `idea_1` |
| `idea_3` | `addresses` | `obstacle_5` |
| `idea_3` | `possible_approach` | `problem` |
| `idea_3` | `addresses` | `obstacle_4` |
| `theorem_1` | `addresses` | `problem` |
| `theorem_1` | `supports` | `hypothesis_1` |
| `note_1` | `supports` | `hypothesis_2` |

---

# Full Worker Findings & Derivations

Below are the complete, untruncated mathematical outputs produced by each specialist worker during the research exploration.

## Finding #1: task_2 (Searcher)

*Worker: **searcher** | Task ID: `task_2` | Duration: 12.9s | Timestamp: 2026-09-09 11:27:41 UTC | Focus Nodes: `n1`, `n2`*

**Assigned Task Prompt**:
> Search literature for existing results on the convergence rate of ABC using MMD or kernel discrepancy, specifically looking at how kernel choice and spectral properties affect parameter estimation.

**Worker Output & Derivations**:

## Findings

1. **Generalized Bayesian posterior contraction rates via MMD.** Chérief-Abdellatif & Alquier (2020, *Bernoulli*, arXiv:1906.01977) establish consistency and exponential contraction rates for a generalized Bayesian inference (GBI) framework using MMD as the loss function. *Hypotheses:* The parameter space $\Theta$ is compact, the kernel $k$ is bounded and strictly positive definite (characteristic), and the map $\theta \mapsto P_\theta$ is continuous in the MMD metric. *Technique:* They use PAC-Bayesian bounds and empirical process theory (specifically controlling suprema of empirical MMD processes using Rademacher complexities) to derive rates governed by the bracketing entropy of $\Theta$ and the modulus of continuity of the parameter-to-distribution map.

2. **Spectral representation of MMD and eigenvalue decay.** Let $k$ be a Mercer kernel on a compact domain $\mathcal{X}$, with eigenexpansion $k(x,y) = \sum_{j=1}^{\infty} \lambda_j \phi_j(x) \phi_j(y)$, where $\lambda_1 \ge \lambda_2 \ge \dots \ge 0$ are eigenvalues and $\{\phi_j\}_{j=1}^\infty$ form an orthonormal basis of $L^2(P)$. The squared MMD between $P_0$ and $P_\theta$ can be written spectrally as $\text{MMD}^2(P_0, P_\theta) = \sum_{j=1}^{\infty} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, where $\mu_{\cdot,j} = \mathbb{E}[\phi_j(X)]$. *Implication:* The rate at which eigenvalues $\lambda_j$ decay determines how strongly high-frequency discrepancies between $P_0$ and $P_\theta$ are penalized. Smooth kernels (e.g., Gaussian, rapid exponential decay of $\lambda_j$) yield an MMD metric that is weak (low-pass filter), making the sample estimator of MMD have lower variance but rendering the inverse map $\theta \mapsto \text{MMD}(P_0, P_\theta)$ ill-conditioned if the parameter affects fine details of the distribution.

3. **Asymptotic distribution and variance of MMD estimators.** Gretton et al. (2012, *JMLR*) and subsequent work on Minimum Distance Estimation (MDE) using MMD (e.g., Park & Muandet 2020) show that the empirical estimator $\widehat{\text{MMD}}_n^2(P_0, P_X)$ converges at parametric rate $O_p(n^{-1/2})$, but the limiting distribution depends crucially on whether the distributions are identical ($\theta = \theta_0$, degenerate V-statistic distribution/infinite sum of chi-squares) or distinct ($\theta \neq \theta_0$, asymptotic normality). *Hypotheses:* Finite second moments under the kernel $k$. *Technique:* Degenerate U- and V-statistic theory (Serfling 1980). In ABC rejection, this means the sample noise in estimating the discrepancy at fixed $\theta$ scales as $n^{-1/2}$, creating a fundamental tension with the ABC tolerance $\epsilon$: $\epsilon$ cannot be sent to zero faster than the Monte Carlo/empirical fluctuation rate of the MMD estimator without driving the acceptance probability to zero.

## Obstacles

- **ABC Rejection vs. Generalized Posterior:** Standard MMD-Bayes literature (like Chérief-Abdellatif & Alquier) analyzes the Gibbs/generalized posterior $\propto \pi(\theta)\exp(-\gamma_n n \text{MMD}^2)$, whereas ABC rejection uses an indicator filter $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon)$. Translating concentration bounds from exponential weights to hard-thresholding ABC requires delicate control of the joint limits $n \to \infty, m \to \infty$ (where $m$ is simulation sample size) and $\epsilon \to 0$, which introduces bias-variance tradeoffs unique to ABC.
- **Ill-posedness of the MMD inverse map:** Even if $\text{MMD}(P_0, P_\theta) \to 0$, recovering $\theta \to \theta_0$ requires a quantitative inverse bound (Polyak-Lojasiewicz condition or modulus of continuity): $\text{MMD}(P_0, P_\theta) \ge c d(\theta, \theta_0)^\alpha$. For smooth kernels, because high frequencies are heavily damped ($\lambda_j \to 0$ rapidly), the MMD distance is locally flat in directions corresponding to high-frequency changes in $P_\theta$, leading to slow contraction rates or lack of identifiability in non-regular models.
- **Simulation sample size vs. data sample size asymmetry:** In ABC, the observed data size $n$ is fixed, but the simulated data size $m$ can be chosen. The empirical MMD is computed between samples of size $n$ and $m$. The variance of the discrepancy is dominated by the smaller of $n$ and $m$, a factor often glossed over in asymptotic results that assume equal sample sizes.

## Suggested next steps

- Investigate the modulus of continuity of the map $\theta \mapsto \text{MMD}(P_0, P_\theta)$ in terms of the kernel smoothness parameters (e.g., Sobolev smoothness of Matérn kernels vs. Gaussian kernels).
- Analyze the joint asymptotic regime for ABC rejection where $\epsilon_n \to 0$ at a rate tied to the minimax rates of MMD estimation ($n^{-s/(2s+d)}$ or parametric $n^{-1/2}$ depending on smoothness).
- Run literature search queries:
  1. `contraction rate generalized Bayesian inference Maximum Mean Discrepancy Chérief-Abdellatif Alquier`
  2. `kernel choice spectral properties minimum distance estimation MMD asymptotic normality`
  3. `approximate bayesian computation ABC asymptotic consistency tolerance epsilon discrepancy rate`
  4. `modulus of continuity parameter estimation MMD kernel integral operator eigenvalues`

---

## Finding #2: task_4 (Decomposer)

*Worker: **decomposer** | Task ID: `task_4` | Duration: 13.1s | Timestamp: 2026-09-09 11:27:53 UTC | Focus Nodes: `n1`, `n2`*

**Assigned Task Prompt**:
> Decompose the rejection ABC convergence rate into three components: (1) approximation error from positive acceptance threshold $\epsilon > 0$, (2) statistical estimation error of empirical MMD from finite samples $n$, and (3) identifiability / curvature of the expected MMD objective with respect to parameter $\theta$.

**Worker Output & Derivations**:

## Findings

1. **Plan 1: Functional-Analytic & Spectral Decomposition via Mercer's Theorem**
   - *Main idea:* Leverage the spectral decomposition of the kernel integral operator to explicitly link the kernel's eigenvalue decay to all three components: approximating the tail discrepancy ($\epsilon$), bounding the finite-sample U-statistic variance ($n$), and quantifying the local curvature of the MMD objective via RKHS feature gradients.
   - *Subgoals:*
     1. **Eigenvalue tail bounds for approximation error ($\epsilon$):** Express $\text{MMD}^2(P_\theta, P_{\theta_0})$ via Mercer's theorem as $\sum_{k=1}^\infty \lambda_k (\phi_k(P_\theta) - \phi_k(P_{\theta_0}))^2$, and bound the truncation error when approximating the discrepancy using the first $K$ spectral components.
     2. **U-statistic concentration for estimation error ($n$):** Use Hoeffding/configurational decomposition of U-statistics or McDiarmid's inequality to bound $\mathbb{P}(|\widehat{\text{MMD}}_n^2 - \text{MMD}^2| > t)$ explicitly in terms of the kernel bounds and sample size $n$, identifying how rough spectra (slow eigenvalue decay) inflate sample complexity.
     3. **Hessian analysis for parameter curvature ($\theta$):** Compute the Hessian matrix $H(\theta_0) = \nabla_\theta^2 \mathbb{E}[\text{MMD}^2(P_\theta, P_{\theta_0})]$ using the Fréchet derivatives of the parameter-to-distribution map into the RKHS, establishing conditions (e.g., injectivity of the mean embedding) for local strong convexity.
     4. **Posterior contraction rate synthesis:** Combine the three error bounds into a density or mass-concentration inequality for the ABC posterior measure $\pi_{\epsilon, n}(\theta | y) \propto \pi(\theta) \mathbb{I}(\widehat{\text{MMD}}_n(P_\theta, y) \le \epsilon)$.
   - *Why plausible:* Mercer's theorem provides a direct dictionary between kernel properties (smoothness/bandwidth) and function space capacities, cleanly separating infinite-dimensional smoothing from finite-sample variance.
   - *Avoids:* Crude supremum-norm bounds over general metric spaces that ignore the geometric structure of reproducing kernel Hilbert spaces (RKHS).

2. **Plan 2: Empirical Process Theory & Local Asymptotic Expansion**
   - *Main idea:* Treat empirical MMD as an empirical process indexed by the parameter $\theta$, deploying localized Rademacher complexity and bracketing entropy to derive uniform convergence rates, and coupling them with a Local Asymptotic Normality (LAN)-style quadratic expansion around the true parameter.
   - *Subgoals:*
     1. **Modulus of continuity for the expected MMD:** Establish Hölder or Lipschitz continuity of $\theta \mapsto \text{MMD}(P_\theta, P_{\theta_0})$ assuming smoothness of the parameter-to-distribution mapping $\theta \mapsto P_\theta$ in total variation or Wasserstein distance combined with RKHS boundedness.
     2. **Uniform empirical process bounds ($n$):** Bound the supremum $\sup_{\theta \in \Theta} |\widehat{\text{MMD}}_n^2(P_\theta, P) - \text{MMD}^2(P_\theta, P)|$ using chaining and Rademacher complexity, tracking how the metric entropy of the parameter space $\Theta$ interacts with the kernel's capacity.
     3. **Identifiability and Fisher-MMD metric tensor:** Define the generalized Fisher information matrix associated with the MMD objective, $I_{\text{MMD}}(\theta_0) = \nabla_\theta \nabla_{\theta'} \text{MMD}^2(P_\theta, P_{\theta'})|_{\theta=\theta'=\theta_0}$, and verify non-degeneracy (strict local identifiability).
     4. **ABC posterior contraction bounds:** Translate the uniform deviation and local quadratic lower bounds into a quantitative error bound on the ABC posterior distribution using Berbee's lemma or general M-estimation posterior consistency theorems (e.g., Schwartz-type theorems adapted to ABC).
   - *Why plausible:* It bypasses explicit spectral expansions by using modern empirical process machinery, which is robust to non-compact domains and irregular spectral profiles.
   - *Avoids:* Pathologies where expected MMD fails to capture parameter changes smoothly, explicitly forcing an examination of the metric tensor non-degeneracy.

## Obstacles

- **Thin initial context:** The problem statement leaves the parametric family $\theta \mapsto P_\theta$, the ambient dimension, and the kernel choice entirely unspecified. Without knowing if the model is regular (smooth parametric) or singular, terms like "curvature" and "local asymptotic expansion" cannot be rigorously evaluated.
- **Hardest subgoal:** Subgoal 3 in both plans (bounding the Hessian / local curvature of the expected MMD) is notoriously difficult for complex simulator-based models because it requires computing derivatives of push-forward measures through nonlinear, non-differentiable simulators, often requiring kernel smoothing of the simulator itself (e.g., smoothed particle filters or pathwise derivatives).
- **Coupling $\epsilon$ and $n$:** Explicitly balancing the threshold $\epsilon$ (which must vanish for exactness, introducing bias) against $1/\sqrt{n}$ sample variance requires precise control over the tails of the ABC acceptance probability, which can suffer from empty-ball paradoxes if $\epsilon$ goes to zero faster than the local density of empirical MMD allows.

## Suggested next steps

1. **Specialize to a toy model:** Fix $P_\theta = \mathcal{N}(\theta, \sigma^2)$ and a Gaussian kernel $k(x, y) = e^{-\gamma \|x-y\|^2}$. Explicitly calculate the expected MMD analytically as a function of $\theta$ to test the curvature and identifiability requirements (Plan 1, Subgoal 3).
2. **Review RKHS differential calculus:** Consult Steinwart and Scovel (2012) or similar literature on differentiability of mean embeddings to establish precise smoothness conditions for the map $\theta \mapsto \mu_{P_\theta}$.
3. **Investigate U-statistic variance bounds:** Look up exact variance formulas for two-sample and one-sample MMD U-statistics (e.g., Gretton et al., 2012) to write down the exact dependency of the statistical estimation error on the kernel bandwidth and eigenvalue spectrum.

---

## Finding #3: task_3 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_3` | Duration: 13.2s | Timestamp: 2026-09-09 11:27:59 UTC | Focus Nodes: `n1`*

**Assigned Task Prompt**:
> Construct a toy example (e.g., estimating the mean of a 1D Gaussian) and compute the MMD between $P_\theta$ and $P_{\theta_0}$ using a Gaussian kernel, explicitly analyzing how kernel bandwidth and spectral properties affect the discrepancy landscape.

**Worker Output & Derivations**:

## Findings

1. **Exact analytical MMD for a 1D Gaussian location model:** Let $P_\theta = \mathcal{N}(\theta, \sigma^2)$ and $P_{\theta_0} = \mathcal{N}(\theta_0, \sigma^2)$ with fixed variance $\sigma^2$. Using a Gaussian kernel $k(x,y) = \exp(-(x-y)^2 / (2\gamma^2))$ with bandwidth $\gamma > 0$, the squared Maximum Mean Discrepancy can be computed explicitly via the convolution formula or the Plancherel theorem:
   $$\text{MMD}^2(\theta, \theta_0) = \frac{2\gamma}{\sqrt{\gamma^2 + 2\sigma^2}} \left(1 - \exp\left(-\frac{(\theta - \theta_0)^2}{2(\gamma^2 + 2\sigma^2)}\right)\right)$$
   This verifies that the population discrepancy landscape is globally smooth, infinitely differentiable in $\theta$, and bounded by $\frac{2\gamma}{\sqrt{\gamma^2 + 2\sigma^2}}$.

2. **Spectral/Fourier representation of the discrepancy landscape:** By the Plancherel theorem, the squared MMD can be written in the frequency domain as:
   $$\text{MMD}^2(\theta, \theta_0) = \frac{1}{2\pi} \int_{-\infty}^\infty |\hat{P}_\theta(t) - \hat{P}_{\theta_0}(t)|^2 \hat{k}(t) dt$$
   where $\hat{P}_\theta(t) = \exp(i t \theta - \frac{1}{2}\sigma^2 t^2)$ is the characteristic function and $\hat{k}(t) = \gamma \sqrt{2\pi} \exp(-\frac{1}{2}\gamma^2 t^2)$ is the spectral density of the Gaussian kernel. Substituting these yields an explicit filter where high frequencies (fine details) are exponentially damped by the kernel spectrum $\hat{k}(t)$ and the data variance $\sigma^2$.

3. **Bandwidth degeneracy and ABC convergence rates:** 
   - **Large bandwidth regime ($\gamma \to \infty$):** The kernel spectrum $\hat{k}(t)$ concentrates near $t=0$. Expanding the exponential in the MMD formula gives $\text{MMD}^2(\theta, \theta_0) \approx \frac{(\theta - \theta_0)^2}{\gamma^2}$, flattening the discrepancy landscape. In an ABC rejection algorithm with tolerance $\epsilon$, the acceptance region $\{\theta : \text{MMD}^2 < \epsilon\}$ scales as $|\theta - \theta_0| = \mathcal{O}(\gamma \sqrt{\epsilon})$, leading to poor parameter localization (wide posterior variance).
   - **Small bandwidth regime ($\gamma \to 0$):** The prefactor $\frac{2\gamma}{\sqrt{\gamma^2 + 2\sigma^2}} \to 0$, causing the population MMD to collapse to zero everywhere except at exact identity. While gradients are initially steep, the

---

## Finding #4: task_5 (Sketcher)

*Worker: **sketcher** | Task ID: `task_5` | Duration: 15.3s | Timestamp: 2026-09-09 11:28:09 UTC | Focus Nodes: `n1`*

**Assigned Task Prompt**:
> Draft a mathematical derivation linking the decay of the kernel integral operator eigenvalues $\lambda_i$ to the modulus of continuity of the MMD discrepancy map $\theta \mapsto \text{MMD}(P_\theta, P_{\theta_0})$.

**Worker Output & Derivations**:

## Findings

1. **Spectral representation of squared MMD via Mercer's theorem**: Let $\mathcal{H}_k$ be the RKHS of a continuous, bounded, symmetric positive-definite kernel $k: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$. By Mercer's Theorem, with respect to the base probability measure $P_{\theta_0}$, the kernel admits the spectral expansion $k(x, y) = \sum_{i=1}^\infty \lambda_i e_i(x) e_i(y)$, where $\lambda_1 \ge \lambda_2 \ge \dots > 0$ are the eigenvalues and $\{e_i\}_{i=1}^\infty$ are orthonormal eigenfunctions in $L^2(\mathcal{X}, P_{\theta_0})$. The mean embedding difference $\Delta_\theta = \mu_\theta - \mu_{\theta_0} = \int k(x, \cdot) d(P_\theta - P_{\theta_0})(x)$ can be expanded in the RKHS. Using the characterization of the RKHS norm via the integral operator $T_k: L^2(P_{\theta_0}) \to L^2(P_{\theta_0})$, the squared discrepancy is:
   $$\text{MMD}^2(P_\theta, P_{\theta_0}) = \|\mu_\theta - \mu_{\theta_0}\|_{\mathcal{H}}^2 = \sum_{i=1}^\infty \frac{\langle \Delta_\theta, e_i \rangle_{L^2(P_{\theta_0})}^2}{\lambda_i}$$
   Wait, let's verify this dual scaling: since $\mu_\theta(\cdot) = \int k(x, \cdot) p_\theta(x) dx = \sum_{i=1}^\infty \lambda_i \left(\int e_i(x) p_\theta(x) dx\right) e_i(\cdot)$, the RKHS norm satisfies $\|\sum c_i e_i\|_{\mathcal{H}}^2 = \sum \frac{c_i^2}{\lambda_i}$. Thus, defining $w_i(\theta) = \int e_i(x) p_\theta(x) dx$, we have:
   $$\text{MMD}^2(P_\theta, P_{\theta_0}) = \sum_{i=1}^\infty \lambda_i \left( w_i(\theta) - w_i(\theta_0) \right)^2$$
   *(Status: Solved - exact spectral identity for squared MMD).*

2. **Local modulus of continuity via the density derivative**: Assume the parametric family $\theta \mapsto P_\theta$ is differentiable in total variation or $L^1$, admitting a score-like derivative $s_\theta(x) = \nabla_\theta \log p_\theta(x)$ or simply $\partial_\theta p_\theta(x)$. By the Mean Value Theorem for Banach-space valued maps, for $\theta$ in a neighborhood of $\theta_0$:
   $$w_i(\theta) - w_i(\theta_0) = \int e_i(x) \left( p_\theta(x) - p_{\theta_0}(x) \right) dx = \left( \int e_i(x) \nabla_\theta p_{\bar{\theta}}(x) dx \right)^\top (\theta - \theta_0)$$
   where $\bar{\theta} = t\theta + (1-t)\theta_0$ for some $t \in [0,1]$. Substituting this into the spectral MMD formula:
   $$\text{MMD}^2(P_\theta, P_{\theta_0}) = (\theta - \theta_0)^\top \left[ \sum_{i=1}^\infty \lambda_i \left(\int e_i(x) \nabla_\theta p_{\bar{\theta}}(x) dx\right) \left(\int e_j(x) \nabla_\theta p_{\bar{\theta}}(x) dx\right)^\top \right] (\theta - \theta_0)$$
   Let $v_i(\bar{\theta}) = \int e_i(x) \nabla_\theta p_{\bar{\theta}}(x) dx$. The local Hessian-like operator of $\text{MMD}^2$ at $\theta_0$ is given by $H(\theta_0) = \sum_{i=1}^\infty \lambda_i v_i(\theta_0) v_i(\theta_0)^\top$. 
   *(Status: Partial - formalizes the local quadratic form controlled by $\lambda_i$).*

3. **Role of eigenvalue decay in smoothing the discrepancy map**: The rate at which $\lambda_i \to 0$ directly controls the compactness of the embedding operator. 
   - For **analytic kernels** (e.g., Gaussian RBF $k(x,y) = \exp(-\|x-y\|^2 / 2\sigma^2)$), the eigenvalues $\lambda_i$ decay *exponentially* fast (e.g., $\lambda_i \sim \exp(-c i^{1/d})$). This means the high-frequency components of the density derivative $\nabla_\theta p_{\bar{\theta}}$ are severely attenuated by $\lambda_i$. Consequently, $\theta \mapsto \text{MMD}(P_\theta, P_{\theta_0})$ is extremely smooth, but it suffers from severe ill-posedness (flat regions) when estimating parameters that affect high-frequency aspects of the distribution.
   - For **Matérn kernels** of smoothness $\nu$, the eigenvalues decay *algebraically* ($\lambda_i \i i^{-1 - 2\nu/d}$), imposing a milder attenuation that allows MMD to retain sensitivity to rougher variations in $\theta

---

## Finding #5: task_7 (Searcher)

*Worker: **searcher** | Task ID: `task_7` | Duration: 15.0s | Timestamp: 2026-09-09 11:28:17 UTC | Focus Nodes: `hyp_kernel_spectrum`*

**Assigned Task Prompt**:
> Search arXiv and semantic scholar specifically for kernel-based ABC, distribution regression, or MMD goodness-of-fit testing convergence rates to connect spectral decay (e.g. Mercer's theorem eigenvalues) to statistical distance bounds.

**Worker Output & Derivations**:

## Findings

1. **Mercer's Theorem and RKHS Capacity (Eigenvalue Decay)**: Let $(X, \mu)$ be a compact metric space with a Borel probability measure, and let $k: X \times X \to \mathbb{R}$ be a continuous, symmetric, positive definite kernel. By Mercer's Theorem (Mercer, 1909; Steinwart & Steinwart, 2008 *SVMs*), $k$ admits an eigenexpansion $k(x, y) = \sum_{i=1}^\infty \lambda_i e_i(x) e_i(y)$, where $\lambda_1 \ge \lambda_2 \ge \dots \ge 0$ are eigenvalues and $\{e_i\}_{i=1}^\infty$ form an orthonormal basis of $L^2(X, \mu)$. The decay rate of $\lambda_i$ characterizes the "capacity" of the Reproducing Kernel Hilbert Space (RKHS) $\mathcal{H}_k$. Polynomial decay ($\lambda_i \sim i^{-2a}$ for $a > 1/2$) corresponds to Sobolev-type smoothness of order $a$, while exponential decay ($\lambda_i \sim e^{-ci^b}$) corresponds to infinitely smooth kernels (e.g., Gaussian RBF on compact domains).

2. **Impact of Spectral Decay on Empirical MMD Concentration**: According to Gretton et al. (2012, *JMLR*, "A Kernel Two-Sample Test"), the empirical Maximum Mean Discrepancy $\text{MMD}_b(P, Q)$ between sample sizes $m$ and $n$ concentrates around its population mean with deviations bounded by sub-Gaussian tails governed by the supremum of the kernel $\|k\|_{\infty}$. However, when analyzing the *effective dimension* and tighter variance bounds via integral operators (as formalized in kernel ridge regression by Caponnetto & De Vito, 2007), the variance of empirical kernel statistics depends heavily on the trace of the integral operator $\sum \lambda_i$, and the effective degrees of freedom $\mathcal{N}(\lambda) = \sum_{i=1}^\infty \frac{\lambda_i}{\lambda_i + \lambda}$. Faster eigenvalue decay reduces the effective dimension, tightening the concentration inequalities for $\text{MMD}(P_\theta, \hat{P}_n)$.

3. **Characteristic Kernels and Identifiability in ABC**: For MMD to serve as a valid discrepancy measure ensuring consistency in ABC, the kernel must be *characteristic* (Sriperumbudur et al., 2010, *JMLR*, "Hilbert Space Embeddings and Metrics on Probability Measures"), meaning the mean embedding $\mathcal{P} \to \mu_P \in \mathcal{H}_k$ is injective. The choice of kernel (and its spectrum) dictates the topology: universal/characteristic kernels (like Gaussian or Laplace) metrize weak convergence. If the spectrum of $k$ decays too rapidly, high-frequency differences between the true distribution $P_{obs}$ and the simulator distribution $P_\theta$ are heavily penalized/smoothed out in the RKHS norm, reducing the sensitivity of the ABC discrepancy to fine-scale distributional shifts.

4. **Posterior Contraction Rates in MMD-ABC**: In Approximate Bayesian Computation, the posterior distribution is approximated by conditioning on $\text{MMD}(P_\theta, \hat{P}_n) \le \epsilon_n$. Following the framework of Frazier et al. (2020, *Biometrika*, "Asymptotic properties of approximate Bayesian computation estimators" or similar ABC literature such as Jiang et al., 2018), the ABC posterior contraction rate depends on: (i) the prior mass around the true parameter $\theta_0$, (ii) the modulus of continuity of the parameter-to-distribution map $\theta \mapsto P_\theta$ measured in MMD, and (iii) the convergence rate of $\text{MMD}(P_\theta, \hat{P}_n)$ to $\text{MMD}(P_\theta, P_0)$. The spectral properties of $k$ directly govern (iii): smoother kernels with rapid eigenvalue decay yield faster parametric rates for $\text{MMD}$ estimation, but may degrade the Hölder continuity (modulus of continuity) if the simulator model has rough parameter dependencies.

## Obstacles

- **Trade-off between Capacity and Sensitivity (The Smoothness Dilemma)**: If an infinitely smooth kernel (e.g., Gaussian $k(x,y) = e^{-\gamma \|x-y\|^2}$, whose eigenvalues decay exponentially) is used, the RKHS norm $\|\mu_{P_\theta} - \mu_{P_0}\|_{\mathcal{H}}$ becomes insensitive to certain high-frequency discrepancies, which can flatten the likelihood surrogate in ABC and lead to a misspecified or wide posterior. Conversely, if a rough kernel (e.g., Matérn with low smoothness) is used, eigenvalues decay slowly ($\lambda_i \sim i^{-2a}$), increasing the empirical variance of $\text{MMD}_n$ and forcing a larger ABC threshold $\epsilon_n$, destroying the contraction rate.
- **Interaction with Dimensionality**: The decay rate of Mercer eigenvalues $\lambda_i$ depends critically on the intrinsic dimension of the support space $X$ (e.g., for Sobolev spaces on $\mathbb{R}^d$ with smoothness $s$, $\lambda_i \sim i^{-2s/d}$). As the dimension $d$ of the summary/data space grows, the eigenvalue decay flattens out for a fixed number of terms, exacerbating the curse of dimensionality in empirical MMD estimation and degrading ABC posterior contraction.
- **Non-differentiability and Discontinuous Simulators**: Standard spectral convergence proofs rely on integral operator compactness and smoothness of the kernel with respect to the domain. If the simulator outputs discontinuous functions of $\theta$, the map $\theta \mapsto \text{MMD}(P_\theta, \hat{P}_n)$ fails to be differentiable, invalidating Taylor-expansion-based posterior contraction proofs regardless of the kernel's spectral decay.

## Suggested next steps

- **Query 1**: `"maximum mean discrepancy" convergence rate eigenvalue decay mercer`
- **Query 2**: `"kernel ABC" posterior contraction rate MMD`
- **Query 3**: `"effective dimension" integral operator kernel empirical MMD concentration`
- **Query 4**: `characterization of MMD topology characteristic kernels spectral properties`

---

## Finding #6: task_8 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_8` | Duration: 18.8s | Timestamp: 2026-09-09 11:28:45 UTC | Focus Nodes: `hyp_kernel_spectrum`*

**Assigned Task Prompt**:
> Analyze how kernel bandwidth (scale parameter) in Gaussian or Matérn kernels influences the smoothness and concentration of the MMD discrepancy surface in a simple 1D location-scale parameter estimation problem.

**Worker Output & Derivations**:

## Findings

1. **Exact population MMD for a 1D Gaussian location model**: Let the true data distribution be $P = \mathcal{N}(\theta_0, 1)$ and the simulated model be $Q_\theta = \mathcal{N}(\theta, 1)$. Using a Gaussian kernel $k_\gamma(x,y) = \exp(-\gamma(x-y)^2)$ with bandwidth parameter $\gamma > 0$, the squared population Maximum Mean Discrepancy admits the closed-form expression:
   $$\text{MMD}^2(\theta; \gamma) = 2(1 + 4\gamma)^{-1/2} \left[ 1 - \exp\left( -\frac{\gamma(\theta - \theta_0)^2}{1 + 4\gamma} \right) \right].$$
   This exact formula allows us to inspect the global geometry of the ABC discrepancy surface without asymptotic approximations.

2. **Bandwidth optimization via surface curvature**: The local sensitivity of the ABC algorithm near the true parameter $\theta_0$ is governed by the second derivative (curvature) of the discrepancy surface at $\theta = \theta_0$. Differentiating $\text{MMD}^2(\theta; \gamma)$ twice with respect to $\theta$ at $\theta = \theta_0$ yields the curvature Hessian:
   $$H(\gamma) = \frac{\partial^2 \text{MMD}^2}{\partial \theta^2}\Big|_{\theta = \theta_0} = \frac{4\gamma}{(1 + 4\gamma)^{3/2}}.$$
   Maximizing $H(\gamma)$ with respect to $\gamma$ via standard calculus yields a unique optimum at $\gamma = 1/2$. In terms of the kernel scale $\sigma_k^2 = (2\gamma)^{-1}$, this optimal bandwidth satisfies $\sigma_k^2 = 1$, exactly matching the variance of the underlying data distributions.

3. **Degeneracy in the wide-kernel limit ($\gamma \to 0$)**: As $\gamma \to 0$ (corresponding to an infinite kernel bandwidth $1/\sqrt{\gamma} \to \infty$), Taylor expansion of the exponential gives $\text{MMD}^2(\theta; \gamma) \approx 2\gamma (\theta - \theta_0)^2 + \mathcal{O}(\gamma^2)$. While the discrepancy surface remains smooth, its overall magnitude scales linearly with $\gamma$. Consequently, the signal-to-noise ratio collapses, making the ABC rejection sampler insensitive to parameter perturbations and stalling parameter concentration.

4. **Degeneracy in the narrow-kernel limit ($\gamma \to \infty$)**: As $\gamma \to \infty$ (zero bandwidth), the prefactor $(1+4\gamma)^{-1/2} \sim (4\gamma)^{-1/2} \to 0$, causing $\text{MMD}^2(\theta; \gamma) \to 0$ uniformly for all $\theta$. The kernel approaches a Dirac delta distribution, under which continuous probability distributions assigned zero overlap, destroying the topological distinguishability required for parameter estimation.

5. **Impact on ABC acceptance regions**: The ABC rejection algorithm accepts parameters $\theta$ within the sublevel set $\{\theta : \widehat{\text{MMD}}_n^2(\theta) \le \epsilon\}$. Because $\text{MMD}^2(\theta; \gamma)$ is globally bounded by $2(1+4\gamma)^{-1/2}$ and flattens out to this asymptote for large $|\theta - \theta_0|$, choosing a threshold $\epsilon$ larger than this bound results in an acceptance region that spills over to the entire parameter space, destroying posterior concentration entirely.

## Obstacles

1. **Restriction to Gaussian conjugacy**: The closed-form evaluation relies strictly on the Fourier property of Gaussian densities under Gaussian kernels. Extending this exact analysis to non-Gaussian location-scale models (e.g., Student-$t$ or Gamma) requires saddle-point approximations or numerical quadrature.
2. **Population vs. Empirical Discrepancy**: This toy analysis evaluates the population MMD surface. In an actual ABC algorithm, the empirical estimate $\widehat{\text{MMD}}_n^2$ introduces sampling variance that scales inversely with sample size $n$ and depends non-trivially on $\gamma$ through the RKHS norm of the empirical measure.

## Suggested next steps

1. **Derive the empirical variance of MMD

---

## Finding #7: task_9 (Counterexample)

*Worker: **counterexample** | Task ID: `task_9` | Duration: 14.7s | Timestamp: 2026-09-09 11:29:09 UTC*

**Assigned Task Prompt**:
> Construct a counterexample or degenerate case showing how ABC rejection with MMD fails or experiences catastrophic acceptance rate collapse when the tolerance epsilon is set below the empirical Monte Carlo fluctuation floor of the MMD estimator.

**Worker Output & Derivations**:

## Findings

1. **Explicit 1D Gaussian model with linear kernel reduction**: Let $P_0 = \mathcal{N}(\mu_0, 1)$ with observed data $Y_{1:n}$, and $P_\theta = \mathcal{N}(\theta, 1)$ with simulated data $X_{1:m}(\theta)$. Choosing the linear kernel $k(x,y) = xy$, the squared empirical Maximum Mean Discrepancy is $\widehat{\text{MMD}}_n^2 = (\bar{Y} - \bar{X})^2$, where $\bar{Y} \sim \mathcal{N}(\mu_0, n^{-1})$ and $\bar{X} \sim \mathcal{N}(\theta, m^{-1})$.
2. **Exact Monte Carlo fluctuation floor at the true parameter**: At the true parameter $\theta = \mu_0$, the discrepancy difference $\bar{Y} - \bar{X}$ follows $\mathcal{N}(0, n^{-1} + m^{-1})$. For equal sample sizes $n = m = 100$, the standard deviation of $\widehat{\text{MMD}}_n$ is $\sigma_{\text{MC}} = \sqrt{2/100} \approx 0.1414$.
3. **Catastrophic acceptance probability collapse**: If an ABC rejection algorithm sets the tolerance to $\epsilon = 0.01$ (well below the noise standard deviation $\sigma_{\text{MC}} = 0.1414$), the probability of accepting the true parameter $\theta = \mu_0$ is explicitly given by:
   $$\mathbb{P}\left(|\bar{Y} - \bar{X}| \le 0.01 \mid \theta = \mu_0\right) = \text{erf}\left(\frac{0.01}{\sqrt{2(2/100)}}\right) = \text{erf}\left(\frac{0.01}{0.2}\right) = \text{erf}(0.05) \approx 0.056$$
   Only 5.6% of simulations at the *true* parameter are accepted. If $\epsilon = 0.001$, the acceptance rate plummets to $0.56\%$.
4. **Asymptotic emptiness of the acceptance region**: For any fixed $\epsilon > 0$, if sample sizes $n, m \to \infty$, the tolerance $\epsilon$ falls below the $O(n^{-1/2} + m^{-1/2})$ fluctuation floor unless $\epsilon$ is scaled proportionally to sample size. If $\epsilon$ is held constant or decreased faster than the parametric rate, the indicator function $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon)$ evaluates to 0 almost surely for all $\theta$, resulting in an empty acceptance set and a division-by-zero failure in the ABC posterior normalization.

## Obstacles

1. **Infinite-dimensional RKHS spectral complexity**: While the linear kernel transparently reduces to difference-of-means, universal kernels (e.g., Gaussian $k(x,y) = \exp(-\gamma(x-y)^2)$) feature an infinite Mercer spectrum $\sum_{j=1}^\infty \lambda_j$. The null distribution of $\widehat{\text{

---

## Finding #8: task_12 (Searcher)

*Worker: **searcher** | Task ID: `task_12` | Duration: 10.0s | Timestamp: 2026-09-09 11:29:17 UTC | Focus Nodes: `approach_1`, `approach_2`*

**Assigned Task Prompt**:
> Search literature (arXiv and OpenAlex) for differential calculus in RKHS and mean embeddings, specifically regarding differentiability of parameter-to-distribution maps and Fisher-MMD metric tensors.

**Worker Output & Derivations**:

## Findings

1. **Differentiability of Mean Embeddings in RKHS**. Let $\mathcal{H}$ be a reproducing kernel Hilbert space on $\mathcal{X}$ with a measurable, bounded kernel $k$. For a parameterised family of distributions $\{P_\theta\}_{\theta \in \Theta}$ where $\Theta \subseteq \mathbb{R}^d$, the mean embedding map $\theta \mapsto \mu_{P_\theta} \in \mathcal{H}$ (defined by $\langle f, \mu_{P_\theta} \mathcal{H} = \int_\mathcal{X} f(x) dP_\theta(x)$) is Fréchet differentiable if the map $\theta \mapsto \frac{d P_\theta}{d x}$ is sufficiently smooth and the kernel $k$ has bounded mixed derivatives. Specifically, by *Sriperumbudur et al. (2010, "Hilbert Space Embeddings of Probability Measures", JMLR)*, if $\partial_{\theta_i} p_\theta(x)$ exists in $L^2(P_\theta)$ and $\sup_{x} |\partial_{x^\alpha} k(x, x')| < \infty$ for multi-indices $\alpha$, then $\partial_{\theta_i} \mu_{P_\theta} = \int \partial_{\theta_i} p_\theta(x) k(x, \cdot dx$ exists in $\mathcal{H}$. 
   * *Proof technique/Application*: This guarantees that the directional derivatives of $\text{MMD}^2(P_0, P_\theta)$ with respect to $\theta$ can be represented via kernel derivatives, linking the Fisher-like score operators in RKHS to the parameter geometry.

2. **The Kernel Fisher-MMD Tensor and Degeneracy**. The empirical or population squared MMD can be viewed locally as a quadratic form governed by a kernel-based Fisher information matrix. As established in *Chwialkowski et al. (2016, "Kernel Goodness-of-Fit Tests", ICML)* and *Jitkrittum et al. (2017)*, the derivative of the mean embedding dictates the asymptotic variance of MMD-based estimators. When the kernel $k$ is analytic (e.g., Gaussian $k(x,x') = \exp(-\|x-x'\|^2 / 2\sigma^2)$), the integral operator eigenvalues $\lambda_j$ decay exponentially fast (e.g., $\lambda_j \sim \exp(-j c)$). Consequently, the parameter-to-distribution gradient $\nabla_\theta \mu_{P_\theta}$ heavily weights low-frequency eigenfunctions, leading to a degenerate Fisher-MMD metric tensor for parameters that perturb high-frequency features of the density.

3. **Ill-Posedness of Kernel-Based Inverse Problems via Spectral Decomposition**. By *Engl, Hanke, and Neubauer (1996, "Regularization of Inverse Problems")*, operator equations of the form $K x = y$ where $K$ is a compact operator are severely ill-posed if the singular values (or eigenvalues $\lambda_j$ of the associated self-adjoint operator) decay rapidly to zero. In our setting, the parameter-to-distribution map $\mathcal{G}: \Theta \to \mathcal{H}$, $\theta \mapsto \mu_{P_\theta}$, followed by the distance evaluation, acts as a compact operator mapping $\Theta$ into the RKHS. Rapid decay of $\lambda_j$ in the MMD spectral expansion $\text{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ implies that variations in $\theta$ that alter high-frequency components of $P_\theta$ produce exponentially small changes in $\text{MMD}^2$. This directly destabilizes ABC rejection algorithms when $\epsilon \to 0$, as the level sets $\{\theta : \text{MMD}^2(P_0, P_\theta) \le \epsilon^2\}$ widen catastrophically along directions corresponding to high-frequency kernel eigenfunctions.

## Obstacles

1. **Discontinuity of the ABC Rejection Indicator vs. Smooth RKHS Geometry**. ABC rejection samples from the posterior proportional to $\pi(\theta) \mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon)$. While the population map $\theta \mapsto \text{MMD}^2(P_0, P_\theta)$ inherits smoothness from the kernel and parameterisation, the empirical estimator $\widehat{\text{MMD}}_n$ has non-standard concentration properties in RKHS norms (e.g., unbounded Rademacher complexities without stringent moment conditions), causing the indicator boundary to fluctuate wildly compared to the smooth exponential weights $\exp(-\gamma_n n \text{MMD}^2)$ analysed in generalized Bayesian literature (Cherief-Abdellatif & Alquier, 2020).
2. **Interaction Between Eigenvalue Decay and Parameter Dimension**. If the parameter space $\Theta$ is high-dimensional ($d \gg 1$), the smoothing effect of the kernel integral operator (which acts as a compact smoothing operator) annihilates directional information for almost all components of $\theta$ except a low-dimensional active subspace, making the ABC acceptance rate drop exponentially with dimension unless $\epsilon$ is scaled improperly.

## Suggested next steps

1. Run literature queries on the exact conditioning and spectral bounds of kernel-based inverse problems in parameter estimation:
   - `“kernelized Stein discrepancy” OR “maximum mean discrepancy” parameter estimation ill-posedness convergence rate`
   - `“Fréchet differentiability” “mean embedding” parameter-to-distribution map RKHS`
   - `“Fisher information” “maximum mean discrepancy” metric tensor eigenvalue decay`
2. Investigate whether replacing the Gaussian kernel with a Matérn kernel (whose eigenvalues $\lambda_j$ decay algebraically: $\lambda_j \sim j^{-2\nu-d}$) alters the ABC convergence rate from a slow logarithmic rate (typical of severely ill-posed inverse problems with exponential decay) to a polynomial rate (mildly ill-posed).
3. Formulate a local quadratic approximation of $\text{MMD}^2(P_0, P_\theta)$ around the true parameter $\theta_0$ using the RKHS Hessian operator $\partial^2_{\theta} \mu_{P_\theta}$, and determine the exact local volume of the ABC rejection region $\{\theta : \sum \lambda_j (\Delta \mu_j)^2 \le \epsilon^2\}$.

---

## Finding #9: task_10 (Sketcher)

*Worker: **sketcher** | Task ID: `task_10` | Duration: 12.8s | Timestamp: 2026-09-09 11:29:28 UTC | Focus Nodes: `approach_1`, `lemma_1`*

**Assigned Task Prompt**:
> Sketch Subgoal 1 of Plan 1: Express MMD^2 via Mercer's theorem using kernel eigenvalues lambda_k, and derive explicit tail bounds on the approximation error when truncating at K terms for a positive tolerance epsilon.

**Worker Output & Derivations**:

terms:
        $\text{Err}_K(P, Q) = \left| \text{MMD}^2(P, Q) - \sum_{j=1}^K \lambda_j (u_{P, j} - u_{Q, j})^2 \right| = \sum_{j=K+1}^\infty \lambda_j (u_{P, j} - u_{Q, j})^2$.
        How to bound this?
        Notice that $u_{P, j} = \int e_j(y) dP(y)$. If $P$ has a density $p$ with respect to $\mu$ such that $\|p\|_{L_2(\mu)} \le M_P < \infty$, then by Cauchy

---

## Finding #10: task_11 (Sketcher)

*Worker: **sketcher** | Task ID: `task_11` | Duration: 13.5s | Timestamp: 2026-09-09 11:29:43 UTC | Focus Nodes: `approach_1`, `obstacle_2`*

**Assigned Task Prompt**:
> Sketch Subgoal 2 of Plan 1: Apply U-statistic concentration inequalities (such as Hoeffding decomposition or McDiarmid's inequality) to bound the finite-sample estimation error |\widehat{MMD}_n^2 - MMD^2| in terms of sample size n and kernel bounds.

**Worker Output & Derivations**:

## Findings

1. **Status: Partial**. **V-statistic concentration via McDiarmid's inequality**: Let the kernel be bounded, $|k(x,x')| \le K$. Define the empirical V-statistic estimator for squared MMD with $n$ samples from $P$ and $n$ samples from $Q$: 
   $$V_n = \frac{1}{n^2}\sum_{i,j=1}^n k(X_i, X_j) - \frac{2}{n^2}\sum_{i,j=1}^n k(X_i, Y_j) + \frac{1}{n^2}\sum_{i,j=1}^n k(Y_i, Y_j).$$
   If we change a single coordinate $X_i$ to $X_i'$, the terms affected in $V_n$ are those with index $i$ in the first and second sums. The total variation in the sum $\sum_{i,j} k(X_i, X_j)$ is at most $2n \times 2K = 4nK$, and in $\sum_{i,j} k(X_i, Y_j)$ is $2n \times 2K = 4nK$. Dividing by $n^2$, changing any single observation $X_i$ or $Y_i$ alters $V_n$ by at most $\frac{8K}{n}$.

2. **Explicit sub-Gaussian tail bound for the V-statistic**: Applying McDiarmid's inequality over the $2n$ independent variables $(X_1, \dots, X_n, Y_1, \dots, Y_n)$, the sum of squared bounded differences is $2n \times \left(\frac{8K}{n}\right)^2 = \frac{128 K^2}{n}$. This yields the tail bound:
   $$\mathbb{P}\left(|V_n - \mathbb{E}[V_n]| \ge t\right) \le 2 \exp\left(-\frac{n t^2}{64 K^2}\right).$$
   This proves that $|\widehat{\text{MMD}}_n^2 - \text{MMD}^2| = \mathcal{O}_P(n^{-1/2})$ in a distribution-free manner, up to the $O(1/n)$ bias between the V-statistic and the true MMD squared.

3. **Hoeffding decomposition and spectral link (the variance gap)**: The Hoeffding decomposition expresses $U$-statistics (and $V$-statistics) as a sum of orthogonal degenerate projections: $V_n - \mathbb{E}[V_n] = \sum_{c=1}^2 V_n^{(c)}$. Using Mercer's theorem $k(x,x') = \sum_{j=1}^\infty \lambda_j \phi_j(x) \phi_j(x')$, the first-order terms in the Hoeffding decomposition have variances explicitly controlled by the eigenvalues $\lambda_j$: $\text{Var}(V_n^{(1)}) = \frac{2}{n} \sum_{j=1}^\infty \lambda_j (\mu_{P,j} - \mu_{Q,j})^2 + \mathcal{O}(n^{-2})$. Thus, the true variance scales with the spectrum of the kernel integral operator, whereas McDiarmid's worst-case bound ignores $\lambda_j$.

## Obstacles

1. **Loss of spectral sensitivity in worst-case bounds**: McDiarmid's inequality treats the kernel purely as a bounded function ($|k| \le K$), completely washing out the eigenvalue decay $\lambda_j \to 0$ identified in *lemma_1*. For smooth kernels (like Gaussian), the effective dimension is much smaller than $n$, meaning the true concentration is substantially sharper than the worst-case $1/\sqrt{n}$ rate suggests.

2. **Asymmetric sample sizes ($n$ vs $m$)**: In ABC applications, the observed data size $n$ is fixed by the experiment, while the simulated data size $m$ can be chosen arbitrarily large. The bounded difference constant $\frac{8K}{n}$ above assumes equal sample sizes. When $m \neq n$, the perturbation bounds split into $\frac{4K}{n}$ and $\frac{4K}{m}$, requiring a refined two-sample McDiarmid analysis to capture the benefit of large simulation budgets $m \gg n$.

## Suggested next steps

1. **Derive the exact Hoeffding decomposition**: Write out the projection terms $V_n^{(1)}$ explicitly using the kernel eigenfunctions $\phi_j$ to connect $\text{Var}(\widehat{\text{MMD}}_n^2)$ directly to the spectrum $\lambda_j$.
2. **Extend to asymmetric sample sizes ($n, m$)**: Rerun the bounded-difference calculation for $V_{n,m}$ with $n$ observed samples and $m$ simulated samples to quantify how the ABC simulation budget $m$ reduces estimation variance relative to $n$.
3. **Compare with empirical process bounds**: Investigate whether bracketing entropy methods (as used in Cherief-Abdellatif & Alquier 2020) yield tighter dimension-free or spectrum-dependent convergence rates for the plug-in MMD estimator.

---

## Finding #11: task_13 (Counterexample)

*Worker: **counterexample** | Task ID: `task_13` | Duration: 48.7s | Timestamp: 2026-09-09 11:30:36 UTC | Focus Nodes: `lemma_2`, `obstacle_1`*

**Assigned Task Prompt**:
> Construct a counterexample or degenerate setting where an improper choice of kernel bandwidth gamma in MMD-ABC leads to non-identifiability or zero asymptotic power even as sample size n -> inf.

**Worker Output & Derivations**:

## Findings

1. **Undersmoothing ($\gamma_n \to 0$ faster than sample spacing) leads to zero power and prior collapse.**
   *Setting:* Let $Y_1, \dots, Y_n \sim P_{\theta_0} = \mathcal{N}(\theta_0, 1)$ be observed data and $X_1, \dots, X_m \sim P_\theta = \mathcal{N}(\theta, 1)$ be simulated data, with prior $\theta \sim U[-1, 1]$. Consider Gaussian kernel $k_{\gamma_n}(x,y) = \exp(-\frac{|x-y|^2}{2\gamma_n^2})$ with bandwidth $\gamma_n = n^{-2

---

## Finding #12: task_14 (Searcher)

*Worker: **searcher** | Task ID: `task_14` | Duration: 51.2s | Timestamp: 2026-09-09 11:30:46 UTC | Focus Nodes: `lemma_2`*

**Assigned Task Prompt**:
> Search literature for 'ABC MMD bandwidth selection' or 'minimum distance estimation Gaussian kernel bandwidth asymptotics' to find existing results on optimal bandwidth scaling for MMD-based ABC or generalized Bayesian inference.

**Worker Output & Derivations**:

## Findings

1. **The Bandwidth-Variance Trade-off in Empirical MMD Asymptotics**
   When using a Gaussian kernel $k_\sigma(x, y) = \exp(-\|x-y\|^2 / (2\sigma^2))$ with varying bandwidth $\sigma$, the variance of the empirical estimator $\widehat{\text{MMD}}^2(X_{1:n}, Y_{1:m})$ depends heavily on the scale $\sigma$. For a fixed $\sigma$, the variance is $O(n^{-1} + m^{-1})$. However, if the bandwidth scales to zero ($\sigma \to 0$) to resolve fine-grained density features, the kernel behaves locally like a Dirac delta. In this regime, the variance of the empirical MMD

---

## Finding #13: task_15 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_15` | Duration: 20.5s | Timestamp: 2026-09-09 11:31:09 UTC | Focus Nodes: `problem`, `hypothesis_1`*

**Assigned Task Prompt**:
> Analyze a toy model: estimating the parameter $\theta \in \mathbb{R}^d$ representing the mean of a multivariate normal distribution $P_\theta = \mathcal{N}(\theta, I_d)$ from observations $X_1, \dots, X_n \sim P_{\theta_0}$. Compute or bound the population MMD, $MMD(P_\theta, P_{\theta_0})$, and its empirical estimator variance as a function of the kernel bandwidth $\sigma$ for a Gaussian kernel $k_\sigma(x, y) = \exp(-\|x-y\|^2 / (2\sigma^2))$ and for a rough kernel like Laplacian/Matérn. Show how the sensitivity to $\theta$ and the empirical variance scale with $d$ and the kernel parameters.

**Worker Output & Derivations**:

## Findings

1. **Exact Population MMD for Gaussian Shifts**: For $P_\theta = \mathcal{N}(\theta, I_d)$ and $P_0 = \mathcal{N}(0, I_d)$ under a Gaussian kernel $k_\sigma(x,y) = \exp(-\|x-y\|^2 / (2\sigma^2))$, the squared population MMD can be computed explicitly via Fourier transforms:
   $$MMD^2(P_\theta, P_0) = 2 \left(\frac{2\pi \sigma^2}{1 + \sigma^2/2}\right)^{d/2} \left[ 1 - \exp\left(-\frac{\|\theta\|^2}{2(\sigma^2

---

## Finding #14: task_16 (Sketcher)

*Worker: **sketcher** | Task ID: `task_16` | Duration: 21.5s | Timestamp: 2026-09-09 11:31:29 UTC | Focus Nodes: `problem`, `hypothesis_1`, `obstacle_1`, `obstacle_2`*

**Assigned Task Prompt**:
> Sketch a mathematical derivation of the rejection ABC posterior contraction rate under the threshold $\epsilon_n \to 0$. Assume $MMD(P_\theta, P_0) \asymp \|\theta - \theta_0\|^\beta$ and the empirical MMD converges as $\mathbb{E}[|\widehat{MMD}_{n,m}(P_\theta, P_0) - MMD(P_\theta, P_0)|^2] \le C / \min(n, m)^{2\alpha}$. Determine how the optimal choice of $\epsilon_n$ and the resulting posterior contraction rate $\|\theta - \theta_0\| = O_p(\delta_n)$ depend on $\alpha$ and $\beta$. Connect $\alpha$ and $\beta$ to the spectral decay of the kernel.

**Worker Output & Derivations**:

## Findings

1. **Subgoal: Rejection ABC Posterior Mass Bound (Status: partial)**
   We bound the posterior mass of the sieve complement $S_n^c = \{\theta : \|\theta - \theta_0\| > \delta_n\}$. The rejection ABC posterior is given by:
   $$\Pi_n(\|\theta - \theta_0\| > \delta_n \mid X_{1:n}) = \frac{\int_{\|\theta - \theta_0\| > \delta_n} \mathbb{I}(\widehat{\text{MMD}}_{n,m}(P_\theta, \hat{P}_n) \le \epsilon_n) \pi(\theta) d\theta}{\int_{\Theta} \mathbb{I}(\widehat{\text{MMD}}_{n,m}(P_\theta, \hat{P}_n) \le \epsilon_n) \pi(\theta) d\theta} := \frac{N_n}{D_n}.$$
   To show $\frac{N_n}{D_n} \to 0$ in probability, we lower-bound the denominator $D_n$ and upper-bound the expectation of the numerator $N_n$.
   *Denominator bound:* By assumption, $\text{MMD}(P_\theta, P_0) \le c_1 \|\theta - \theta_0\|^\beta$. Choose $\theta$ such that $\|\theta - \theta_0\| \le (\epsilon_n / 2)^{1/\beta}$. Then $\text{MMD}(P_\theta, P_0) \le \epsilon_n / 2$. By triangle inequality, $\widehat{\text{MMD}}_{n,m}(P_\theta, \hat{P}_n) \le \text{MMD}(P_\theta, P_0) + |\widehat{\text{MMD}}_{n,m} - \text{MMD}|$. If we choose $\epsilon_n$ such that the empirical error is smaller than $\epsilon_n / 2$ with high probability, then $D_n \ge \pi(B(\theta_0, c_2 \epsilon_n^{1/\beta})) \ge c_3 \epsilon_n^{d/\beta}$ (assuming continuous positive prior density on $\mathbb{R}^d$).

2. **Subgoal: Numerator Expectation and Optimal Threshold $\epsilon_n$ (Status: partial)**
   For the numerator $N_n$, we integrate over $\|\theta - \theta_0\| > \delta_n$. By Markov's inequality or expectation bounds over the indicator:
   $$\mathbb{E}[N_n] \le \int_{\|\theta - \theta_0\| > \delta_n} \mathbb{P}\left(\widehat{\text{MMD}}_{n,m}(P_\theta, \hat{P}_n) \le \epsilon_n\right) \pi(\theta) d\theta.$$
   Write $\widehat{\text{MMD}}_{n,m}(P_\theta, \hat{P}_n) \ge \text{MMD}(P_\theta, P_0) - |\widehat{\text{MMD}}_{n,m} - \text{MMD}|$.
   Thus, $\widehat{\text{MMD}}_{n,m} \le \epsilon_n$ implies $\text{MMD}(P_\theta, P_0) \le \epsilon_n + |\widehat{\text{MMD}}_{n,m} - \text{MMD}|$.
   If we use the identifiability assumption $\text{MMD}(P_\theta, P_0) \ge c_4 \|\theta - \theta_0\|^\beta$, then on the set where $\|\theta - \theta_0\| > \delta_n$, we must have:
   $$c_4 \delta_n^\beta \le \text{MMD}(P_\theta, P_0) \le \epsilon_n + |\widehat{\text{MMD}}_{n,m} - \text{MMD}|.$$
   For this probability to be small, we need $\epsilon_n \ll \delta_n^\beta$, and the deviation $|\widehat{\text{MMD}}_{n,m} - \text{MMD}|$ must be controlled by $\delta_n^\beta$. Given $\mathbb{E}[(\widehat{\text{MMD}} - \text{MMD})^2] \le C N^{-2\alpha}$ (where $N = \min(n, m)$), by Markov's inequality, $\mathbb{P}(|\widehat{\text{MMD}} - \text{MMD}| > t) \le C (N^\alpha t)^{-2}$.
   Balancing terms, setting $\epsilon_n \asymp N^{-\alpha}$ and $\delta_n^\beta \asymp N^{-\alpha}$, we obtain the contraction rate:
   $$\delta_n \asymp N^{-\alpha / \beta}.$$

3. **Subgoal: Connecting $\alpha$ and $\beta$ to Kernel Spectral Properties (Status: heuristic)**
   - **Empirical rate exponent $\alpha$:** From U-statistic theory for MMD, the squared MMD estimator has variance governed by the spectrum of the kernel integral operator. Specifically, $\mathbb{Var}(\widehat{\text{MMD}}^2) \asymp \sum_{j=1}^\infty \lambda_j^2 / N$, where $\lambda_j$ are the Mercer eigenvalues. For kernels with polynomial spectral decay $\lambda_j \sim j^{-2s/d}$ on a $d$-dimensional domain (e.g., Matérn with smoothness $s$), finite variance requires $2s/d > 1/2$ (or $s > d/4$). The empirical MMD itself achieves the parametric root-$N$ rate ($\alpha = 1/2$) provided the sum of squared eigenvalues is finite. However, in high dimensions $d$, if $s$ is small or $d$ is large, the constant explodes (Curse of Dimensionality, obstacle_3), or if we use infinitely smooth kernels (Gaussian, $\lambda_j = O(e^{-cj^2/d})$), $\lambda_j$ decay super-exponentially, making variance extremely small (${\alpha = 1/2}$ holds tightly with tiny constants).
   - **Identifiability exponent $\beta$:** Governed by the smoothness of the parameter-to-distribution map $\theta \mapsto P_\theta$ relative to the RKHS topology. Smooth kernels (Gaussian) have RKHS functions that are very smooth, so the map $\theta \mapsto \mu_{P_\theta}$ is very flat in the MMD metric, leading to a *large* $\beta$ (weak identifiability, ill-posed inverse problem, as noted in lemma_1). Rough kernels (Matérn with low $s$) induce stronger/larger RKHS norms, making $\text{MMD}(P_\theta, P_0)$ larger for a fixed perturbation $\|\theta - \theta_0\|$, which yields a *smaller* $\beta$ (stronger identifiability).
   - **Trade-off:** The contraction rate $\delta_n \asymp N^{-\alpha / \beta}$ exposes the Smoothness Dilemma: smoother kernels improve $\alpha$ stability/constants and avoid high-dimensional variance blow-up, but drastically worsen $\beta$ (making $\beta$ large, slowing down $\delta_n$). Conversely, rougher kernels improve $\beta$ (smaller $\beta$, sharper identifiability) but degrade empirical stability $\alpha$ in high dimensions due to slow eigenvalue decay.

## Obstacles

1. **Uniformity over $\theta$:** The empirical convergence bound $\mathbb{E}[(\widehat{\text{MMD}} - \text{MMD})^2] \le C N^{-2\alpha}$ must hold uniformly (or with bracketing entropy control) over $\theta \in \Theta$, because the numerator integrates over all $\theta$ outside the ball. Pointwise convergence in probability is insufficient for ABC posterior contraction without an entropy calculation of the parameter space or the family of distributions $\{P_\theta\}$.
2. **Asymmetry between sample sizes $n$ and $m$:** In ABC, the observed data size $n$ is fixed, while the simulated sample size $m$ can be chosen large ($m \to \infty$). If $m \to \infty$, the simulation noise vanishes, and $\alpha$ is entirely determined by the observed sample size $n$. However, standard bounds combine $n$ and $m$ via $\min(n, m)$, creating a bottleneck if $m$ is not taken large enough relative to $n$.
3. **Non-linearity of the inverse map $\theta \to \text{MMD}(P_\theta, P_0)$:** The assumption $\text{MMD}(P_\theta, P_0) \asymp \|\theta - \theta_0\|^\beta$ is a global or local lower bound. Near critical points or in degenerate models, $\beta$ may vary or local flatness can arbitrarily degrade contraction rates, making uniform local tail bounds difficult to establish without second-order derivative controls on the mean embedding.

## Suggested next steps

1. **Establish a uniform empirical process bound:** Prove a uniform Law of Large Numbers or Glivenko-Cantelli type bound for $\sup_{\theta \in \Theta} |\widehat{\text{MMD}}_{n,m}(P_\theta, \hat{P}_n) - \text{MMD}(P_\theta, P_0)|$ using bracketing entropy of the parametric family $\{P_\theta\}$ composed with RKHS unit ball functions.
2. **Explicitly compute $\beta$ for a toy parametric family:** Consider a location family $P_\theta = \mathcal{N}(\theta, \sigma^2 I)$ and compute $\text{MMD}^2(P_\theta, P_0)$ explicitly using the Gaussian kernel Fourier transform formula to verify the exact dependence of $\beta$ on the kernel bandwidth parameter.
3. **Analyze the $m \to \infty$ vs $n \to \infty$ joint asymptotic regime:** Derive the exact ABC posterior contraction rate when $m \gg n$ versus $m = O(n)$, isolating the contribution of simulation error from observed data empirical error.

---

## Finding #15: task_17 (Decomposer)

*Worker: **decomposer** | Task ID: `task_17` | Duration: 25.2s | Timestamp: 2026-09-09 11:31:39 UTC | Focus Nodes: `problem`, `hypothesis_1`, `obstacle_1`, `obstacle_2`, `obstacle_3`*

**Assigned Task Prompt**:
> Decompose the problem of proving ABC posterior contraction rate into concrete, sequential subgoals, accounting for both (1) the RKHS-based empirical MMD concentration using trace/effective dimension, and (2) the parameter-to-embedding continuity (Hölder bounds) under different spectral decay rates of the kernel.

**Worker Output & Derivations**:

## Findings

1. **Plan 1: The Inverse Problem and Spectral Regularization Approach**
   * *Main idea*: Model the parameter-to-distribution map $\theta \mapsto P_\theta$ as a compact forward operator into an RKHS. Treat MMD-ABC as a regularized inverse problem where Mercer spectral truncation acts as a sieve estimator, balancing the ill-posedness (high-frequency damping) against the estimator variance.
   * *Subgoal 1 (Forward Map Regularity)*: Establish the Hölder continuity or Fréchet differentiability of the parameter-to-kernel embedding map $\theta \mapsto \mu_\theta$ in the RKHS $\mathcal{H}_k$, quantifying the modulus of continuity $\|\mu_\theta - \mu_{\theta_0}\|_{\mathcal{H}_k} \ge c \|\theta - \theta_0\|^\beta$ in terms of kernel smoothness $s$ and parameter dimension. (Falsifiable via linear transport or parametric family counterexamples).
   * *Subgoal 2 (Spectral Variance Decomposition)*: Using the Hoeffding/chaos decomposition of U-statistics (Serinko & Gine 2004 framework), express the variance of the empirical squared MMD estimator explicitly as a series over Mercer eigenvalues $\sum_{j=1}^\infty \lambda_j^2$, explicitly tracking how the decay rate $\lambda_j \sim j^{-2s/d}$ controls sample variance.
   * *Subgoal 3 (Sieve Threshold Analysis)*: Define a spectral truncation level $J_n$ (retaining only the first $J_n$ eigenfunctions) and derive the joint asymptotic error of the ABC rejection filter $I(\widehat{\text{MMD}}_{n, J_n} \le \epsilon_n)$ as a function of the joint limits $n \to \infty$ and $\epsilon_n \to 0$.
   * *Plausibility*: Directly connects Lemma 1 (spectral representation) and Obstacle 3 (Curse of Dimensionality) using classical functional analysis and inverse problem regularization (Engl, Hanke, Neubauer 1996).
   * *Avoids*: The unbounded amplification of high-frequency noise that occurs when naive MMD is inverted without regularization.

2. **Plan 2: Empirical Process & Testing-Based ABC Contraction Approach**
   * *Main idea*: Adapt the classical nonparametric posterior contraction paradigm (Ghosal, Ghosh, and van der Vaart 2000) and its extension to generalized Bayes (Cherief-Abdellatif & Alquier 2020) to hard-rejection ABC by translating the indicator filter into exponential inequalities for U-processes (Ledoux-Talagrand inequality).
   * *Subgoal 1 (Uniform MMD Concentration)*: Prove a uniform exponential concentration inequality for $\sup_{\theta \in \Theta} |\widehat{\text{MMD}}_n^2(P_\theta, P_0) - \text{MMD}^2(P_\theta, P_0)|$ using bracketing entropy of the parametric family $\{P_\theta\}$ mapped through the RKHS feature map.
   * *Subgoal 2 (Small-Ball Probability)*: Lower bound the prior mass of the Kullback-Leibler or MMD neighborhoods $\Pi(\theta: \text{MMD}^2(P_\theta, P_0) \le \epsilon_n^2)$ by relating the MMD metric to the parameter Euclidean distance via the identifiability exponent $\beta$.
   * *Subgoal 3 (ABC Rejection Test Construction)*: Construct explicit composite hypothesis tests to bound the denominator (marginal likelihood / normalizing constant of the ABC posterior) and control the Type II error of the hard-rejection indicator $I(\widehat{\text{MMD}}_n \le \epsilon_n)$, avoiding the smooth Gibbs posterior assumption of Cherief-Abdellatif & Alquier (2020).
   * *Plausibility*: Bypasses the analytical difficulty of the hard-rejection indicator (Obstacle 1) by leveraging standard testing-based Bayesian asymptotics.
   * *Avoids*: Obstacle 1 (discrepancy between Gibbs posteriors and indicator ABC) by handling the indicator function directly via U-process large deviations.

## Obstacles

1. **Hard Rejection Indicator Discontinuity**: Obstacle 1 remains the most technically demanding bottleneck. Bounding the measure of the set $\{\theta: \widehat{\text{MMD}}_n(P_\theta, \hat{P}_n) \le \epsilon\}$ requires controlling indicator functions of empirical processes, which lack the smoothness of the exponential weights $\exp(-\gamma_n n \text{MMD}^2)$ used in generalized Bayesian literature.
2. **Asymmetric Sample Sizes ($n$ vs $m$)**: In practical ABC, the simulated sample size $m$ can be made arbitrarily large, but the observed sample size $n$ is fixed. Subgoal 2 in Plan 1 and Subgoal 1 in Plan 2 must explicitly decouple the variance contributions from $n$ and $m$ to avoid assuming $m = O(n)$.
3. **Curse of Dimensionality in Mercer Decay**: As stated in Obstacle 3, when the domain dimension $d$ is large, the eigenvalues $\lambda_j \sim j^{-2s/d}$ decay too slowly unless $s$ is very large. This breaks the compact operator assumptions needed for stable spectral truncation in Plan 1, Subgoal 3.

## Suggested next steps

1. **Derive the U-statistic Variance Bound**: Explicitly calculate the exact variance of $\widehat{\text{MMD}}^2$ in terms of the kernel eigenvalues $\lambda_j$ and the marginal distributions $P_0$ using the Hoeffding decomposition for V- and U-statistics (Gretton et al. 2012).
2. **Verify Bracketing Entropy for Parametric Families**: Check whether standard parametric families $\{P_\theta\}_{theta \in \Theta}$ satisfy the polynomial bracketing entropy conditions required for the uniform empirical process concentration in Plan 2, Subgoal 1, when composed with a Gaussian vs. Matérn kernel feature map.
3. **Analyze the Indicator Function via Smooth Approximations**: Investigate whether the indicator filter $I(x \le \epsilon)$ can be bracketed by smooth sigmoidal functions to transition rigorously from the smooth Gibbs posterior results of Cherief-Abdellatif & Alquier (2020) to the hard-rejection ABC setting.

---

## Finding #16: task_18 (Searcher)

*Worker: **searcher** | Task ID: `task_18` | Duration: 29.6s | Timestamp: 2026-09-09 11:31:54 UTC | Focus Nodes: `problem`, `paper_1`*

**Assigned Task Prompt**:
> Search literature for existing papers analyzing posterior contraction rates of ABC algorithms that use MMD, kernel distances, or Wasserstein distances, and extract their assumptions regarding the metric's convergence rate and the parameter identifiability (modulus of continuity).

**Worker Output & Derivations**:

## Findings

1. **Generalized Bayesian Inference Contraction via MMD (Cherief-Abdellatif & Alquier, 2020)**
   * *Statement/Framework:* Consider the generalized posterior $\Pi_n(d\theta | X_{1:n}) \propto \exp\left(-n \, \text{MMD}^2(P_0, P_{\theta, m})\right) \pi(\theta)$, where $P_0$ is the true data-generating distribution and $P_{\theta, m}$ is the empirical distribution of $m$ simulations from $\theta$. They establish posterior consistency and explicit contraction rates under two core assumptions:
     1. **Identifiability (Modulus of Continuity lower bound):** $\text{MMD}(P_0, P_\theta) \ge C \|\theta - \theta_0\|^\beta$ for some $\beta \ge 1$ and $C > 0$ in a neighborhood of $\theta_0$.
     2. **Complexity control:** The parameter space metric entropy (bracketing entropy) of the map $\theta \mapsto P_\theta$ measured in MMD.
   * *Proof Technique:* Uses PAC-Bayesian inequalities (specifically Catoni-style bounds) controlling the empirical process $\sup_{\theta} |\text{MMD}^2(P_0, \hat{P}_n) - \text{MMD}^2(P_0, P_\theta)|$. 
   * *Limitation here:* This applies to the *exponential (Gibbs)* weighted posterior, not the hard-indicator ABC rejection filter $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$.

2. **Wasserstein ABC Contraction Rates and Small-Ball Probabilities (Bernton et al., 2019)**
   * *Statement:* Bernton, Jacob, Gerber, and Robert (2019, *JASA*), "Approximate Bayesian Computation with the Wasserstein Distance," analyze the posterior contraction of ABC algorithms where the discrepancy is the 1-Wasserstein distance $\mathbb{W}_1$. Their contraction theorem relies on:
     1. The rate of convergence of the empirical Wasserstein distance $\mathbb{W}_1(\hat{P}_n, P_0) = O_p(n^{-\alpha_d})$ where $\alpha_d = 1/d$ for $d > 2$.
     2. A prior mass condition around the true parameter $\theta_0$ controlled by the modulus of continuity $\mathbb{W}_1(P_\theta, P_0) \ge c\|\theta - \theta_0\|^\beta$.
   * *Adaptability to MMD:* MMD empirical convergence does *not* suffer from the dimension-dependent curse of the Wasserstein distance ($n^{-1/d}$); MMD empirical estimators converge at parametric rate $O_p(n^{-1/2})$ in terms of sample size, *regardless* of dimension, provided the kernel is bounded. However, the *constant* depends heavily on the kernel's spectral decay (Mercer eigenvalues).

3. **Spectral Representation and Variance of Empirical MMD (Gretton et al., 2012 / Sriperumbudur et al., 2010)**
   * *Statement:* Let $k$ be a Mercer kernel on a compact domain $\mathcal{X}$ with eigenfunctions $\phi_j$ and eigenvalues $\lambda_j$ of the integral operator $T_k f = \int k(x, \cdot) f(x) dP_0(x)$. The squared MMD has the spectral expansion:
     $$\text{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j \left( \mathbb{E}_{P_0}[\phi_j] - \mathbb{E}_{P_\theta}[\phi_j] \right)^2.$$
   * *Variance Bound:* The variance of the unbiased U-statistic estimator $\widehat{\text{MMD}}^2$ scales as $\mathcal{O}\left( \frac{1}{n} \sum_{j=1}^\infty \lambda_j^2 + \frac{1}{m} \sum_{j=1}^\infty \lambda_j^2 \right)$, where $n$ is data sample size and $m$ is simulation sample size (see Gretton et al., 2012, *JMLR*). 
   * *Consequence for ABC:* If eigenvalues $\lambda_j$ decay rapidly (e.g., Gaussian kernel, $\lambda_j \sim e^{-cj}$), the variance is extremely small, but high-frequency components of $\theta \mapsto P_\theta$ are wiped out in the MMD metric, destroying parameter identifiability (large $\beta$ in the modulus of continuity). If eigenvalues decay slowly (e.g., Matérn kernel, $\lambda_j \sim j^{-2s/d}$), identifiability is preserved, but the variance of the empirical estimator inflates, slowing down ABC acceptance rates for a fixed tolerance $\epsilon$.

## Obstacles

1. **Hard-Threshold Indicator vs. Soft Gibbs Posterior:** Existing contraction rate literature for MMD-based inference (like Cherief-Abdellatif & Alquier) exclusively analyzes Gibbs/generalized posteriors $\propto \exp(-\gamma_n n \text{MMD}^2)$. The classical ABC rejection posterior $\Pi(\theta | \widehat{\text{MMD}}_n \le \epsilon_n)$ is a conditional measure on the set $\{\widehat{\text{MMD}}_n \le \epsilon_n\}$. Bounding the denominator $\mathbb{P}(\widehat{\text{MMD}}_n \le \epsilon_n)$ (the small-ball probability of empirical MMD) requires precise lower bounds that interact directly with the kernel's spectral properties and the simulator smoothness, a non-trivial departure from Gibbs posterior analysis.

2. **Simulation-to-Data Size Asymmetry ($n$ vs $m$):** In ABC, observed data size $n$ is fixed, while simulation size $m$ can be chosen large. The empirical MMD is computed between $\hat{P}_n$ (size $n$) and $\hat{Q}_{m,\theta}$ (size $m$). The variance of $\widehat{\text{MMD}}^2$ contains terms driven by $\min(n, m)$. When $m \gg n$, the simulation noise is suppressed, but the overall convergence rate remains bottlenecked by the observed sample size $n$ and the kernel's integral operator spectrum acting on $P_0$.

3. **The Ill-Posedness of the Inverse Map $\theta \mapsto P_\theta \mapsto \text{MMD}(P_0, P_\theta)$:** Because MMD smooths distributions via the kernel embedding operator, the map $\theta \to \text{MMD}(P_0, P_\theta)$ can be severely ill-conditioned when smoother kernels are used. This manifests as a flat likelihood/acceptance region in ABC, where distinct parameter values yield virtually indistinguishable MMD values within tolerance $\epsilon_n$, leading to a lack of Bernstein-von Mises type concentration unless $\epsilon_n$ shrinks slower than the parametric rate.

## Suggested next steps

1. `Search query:` "posterior contraction rate" AND ("Approximate Bayesian Computation" OR "ABC") AND ("Maximum Mean Discrepancy" OR "MMD")
2. `Search query:` "generalized Bayesian inference" AND "kernel-based distance" AND "small-ball probability" AND "rejection ABC"
3. `Search query:` "modulus of continuity" AND "kernel integral operator eigenvalues" AND "parameter estimation" AND "concentration rate"
4. Investigate adapting the small-ball probability techniques of Amrein & Künsch (2011) or Barber et al. (2015) on ABC acceptance probabilities to kernel discrepancy metrics by expressing the event $\{\widehat{\text{MMD}}_n^2 \le \epsilon_n^2\}$ via the spectral projection onto the top $K_n$ eigenfunctions of the kernel integral operator.

---

## Finding #17: task_21 (Searcher)

*Worker: **searcher** | Task ID: `task_21` | Duration: 13.1s | Timestamp: 2026-09-09 11:32:16 UTC | Focus Nodes: `problem`, `paper_1`*

**Assigned Task Prompt**:
> Search arXiv specifically for recent papers on MMD-ABC posterior contraction rates, kernel-based ABC, and generalized Bayesian inference with MMD.

**Worker Output & Derivations**:

## Findings

1. **Generalized Bayesian Inference with MMD Loss (Chérief-Abdellatif & Alquier, 2020)**
   * *Statement & Hypotheses:* In "Consistency and Exponential Contraction Rates for Generalized Bayesian Inference" (EJS, 2020), the authors consider a generalized posterior $\Pi_n(d\theta | y_{1:n}) \propto \exp(-\lambda_n n \mathrm{MMD}_k^2(P_0, P_\theta)) \Pi(d\theta)$, where $\lambda_n$ is a learning rate. Assuming: (i) the parameter space $\Theta$ is compact or covered by metric entropy bounds (bracketing entropy $\log N(\epsilon, \Theta, \|\cdot\|)$); (ii) a identifiability/margin condition of the form $\mathbb{E}_0[\mathrm{MMD}^2(P_0, P_\theta) - \mathrm{MMD}^2(P_0, P_{\theta_0})] \ge C \|\theta - \theta_0\|^\beta$; and (iii) boundedness of the kernel $k$, they establish exponential contraction rates of the form $\Pi_n(\theta : d(\theta, \theta_0) > M_n \epsilon_n | y_{1:n}) \to 0$ in probability, where $\epsilon_n$ depends on the modulus of continuity of the parameter-to-distribution map $\theta \mapsto P_\theta$ under MMD.
   * *Proof Technique & Adaptation:* The proof relies on PAC-Bayesian inequalities (specifically catastrophic tail bounds for generalized posteriors à la Grünwald / Alquier) and empirical process theory for U-statistics/V-statistics. The technique suggests that the contraction rate is strictly tied to the modulus of continuity $\omega(\delta) = \sup_{\|\theta-\theta_0\| \le \delta} \mathrm{MMD}(P_\theta, P_{\theta_0})$, which is directly controlled by the kernel's spectral properties via Mercer's theorem.

2. **Spectral Representation and Ill-Posedness of MMD Inverse Problems (Sriperumbudur et al., 2010; Muandet et al., 2017)**
   * *Statement & Hypotheses:* Let $k$ be a continuous, bounded, translation-invariant kernel on $\mathcal{X} \subset \mathbb{R}^d$ with spectral density $\Lambda(\omega)$ (Fourier transform of $k$). By Bochner's theorem and Mercer's theorem, the squared MMD between $P_0$ and $P_\theta$ can be expressed in terms of the feature covariance operator or via eigenfunctions $\phi_j$ with eigenvalues $\lambda_j$: $\mathrm{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$. 
   * *Methodological consequence:* If $k$ is very smooth (e.g., Gaussian $k(x,y) = \exp(-\gamma \|x-y\|^2)$), $\lambda_j$ decays exponentially fast (e.g., $\lambda_j \sim \exp(-c j^{1/d})$). This means high-frequency components of the difference $\mu_0 - \mu_\theta$ are severely damped in the MMD metric. Consequently, the mapping $\theta \mapsto \mathrm{MMD}(P_0, P_\theta)$ has a flat gradient in high-frequency directions, creating a severely ill-posed inverse problem when recovering $\theta$ from MMD constraints.

3. **Asymptotics of ABC Rejection versus Generalized Posterior (Frazier et al., 2018; Prangle, 2017)**
   * *Statement & Hypotheses:* Standard ABC rejection samples from $\pi_{\epsilon_n}(\theta | y_{1:n}) \propto \pi(\theta) \mathbb{I}(\Delta(\hat{S}_n, S_\theta) \le \epsilon_n)$. In contrast to the Gibbs/generalized posterior $\propto \exp(-n \Delta^2)$, ABC rejection is a hard-thresholding conditional prior. Frazier et al. ("The ABC posterior distribution", 2018, arXiv:1803.10986) establish Bernstein-von Mises theorems for ABC under the hypothesis that the discrepancy $\Delta$ satisfies a local asymptotic normality (LAN)-like expansion and that the threshold $\epsilon_n \to 0$ such that $\epsilon_n \sqrt{n} \to \infty$ (to avoid empty acceptance regions while maintaining bias control).
   * *Transfer Idea:* Translating this to MMD-ABC requires bounding the volume of the empirical MMD ball $\mathbb{P}(\widehat{\mathrm{MMD}}_n(P_0, P_\theta) \le \epsilon_n)$. The spectral properties of $k$ dictate the asymptotic distribution of $\widehat{\mathrm{MMD}}_n$ (which follows a weighted sum of chi-squared variables for smooth kernels, or degenerate non-central distributions), directly altering the small-ball probabilities that govern ABC posterior concentration.

## Obstacles

1. **Indicator Filter Discontinuity vs. Smooth Exponential Weights:**
   The literature on MMD-based inference (like Chérief-Abdellatif & Alquier) exclusively analyzes exponential weights/Gibbs posteriors ($\exp(-\gamma_n n \mathrm{MMD}^2)$). ABC rejection uses the discontinuous indicator $\mathbb{I}(\widehat{\mathrm{MMD}}_n \le \epsilon_n)$. Standard PAC-Bayesian chaining arguments fail because the loss is not locally Lipschitz or smooth with respect to the empirical discrepancy realization, requiring uniform empirical process bounds over level sets of U-statistics.

2. **Dimension-Dependent Spectrum vs. ABC Acceptance Rate:**
   While rough kernels (e.g., Matérn with low smoothness $s$) have slow polynomial spectral decay ($\lambda_j \sim j^{-2s/d}$) which preserves high-frequency identifiability (avoiding the ill-posedness of Gaussian kernels), they inflate the variance of the empirical MMD estimator to $O(n^{-s/d} + m^{-s/d})$. In high dimensions $d$, if $s$ is small, the variance dominates, meaning the empirical MMD threshold $\epsilon_n$ must be chosen large, introducing catastrophic ABC bias.

## Suggested next steps

1. **Query 1:** `arXiv: "approximate bayesian computation" AND "maximum mean discrepancy" AND "posterior contraction"`
2. **Query 2:** `arXiv: "generalized Bayesian inference" AND "maximum mean discrepancy" AND "contraction rate"`
3. **Query 3:** `arXiv: "kernel integral operator" AND "eigenvalue decay" AND "empirical process" AND "MMD"`
4. **Query 4:** `arXiv: "ABC rejection" AND "small ball probabilities" AND "discrepancy measure" AND "convergence rate"`

---

## Finding #18: task_20 (Counterexample)

*Worker: **counterexample** | Task ID: `task_20` | Duration: 14.7s | Timestamp: 2026-09-09 11:33:16 UTC | Focus Nodes: `hypothesis_1`, `lemma_1`*

**Assigned Task Prompt**:
> Test hypothesis_1 (Smoothness Dilemma): construct or analyze a setting where an infinitely smooth kernel (e.g., Gaussian) does not suffer from severe identifiability loss, challenging the claimed trade-off between empirical rate and parameter sensitivity.

**Worker Output & Derivations**:

## Findings

1. **Gaussian Location Family with Gaussian Kernel Achieves Optimal $\beta = 1$**: Let $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$. Using Bochner's theorem and the Fourier representation of squared MMD with a Gaussian kernel $k(x,y) = \exp(-\gamma \|x-y\|^2)$, we have:
   $$\mathrm{MMD}^2(P_0, P_\theta) = \int_{\mathbb{R}^d} 4 \sin^2\left(\frac{\omega \cdot \theta}{2}\right) |\widehat{P_0}(\omega)|^2 e^{-\frac{\|\omega\|^2}{4\gamma}} \, d\omega$$
   For $P_0 = \mathcal{N}(0, I_d)$, $|\widehat{P_0}(\omega)|^2 = e^{-\|\omega\|^2}$. Taylor expanding $4\sin^2(\frac{\omega\cdot\theta}{2}) \approx (\omega\cdot\theta)^2$ for small $\|\theta\|$, the integral evaluates to $\mathrm{MMD}^2(P_0, P_\theta) \asymp \|\theta\|^2$. Thus, $\mathrm{MMD}(P_0, P_\theta) \ge c \|\theta\|^{\beta}$ holds with the optimal Hölder exponent $\beta = 1$, directly contradicting the claim that smooth kernels universally yield "poor sensitivity (large $\beta$)."

2. **Parametric vs. Nonparametric Source of the Modulus**: The intuition of the "Smoothness Dilemma" (where exponential spectral decay like $\lambda_j \sim e^{-c j}$ causes severe ill-posedness) stems from nonparametric function estimation and Sobolev norm comparisons. In a finite-dimensional parametric location family, the difference $\widehat{P_0}(\omega) - \widehat{P_\theta}(\omega)$ is governed by smooth trigonometric modulations of the base characteristic function, which prevents the high-frequency damping of the Gaussian kernel from destroying first-order parameter identifiability.

3. **Dimension Dependence Shifted to the Preconstant**: While the exponent remains $\beta = 1$, evaluation of the Gaussian integral shows that the lower bound constant $c$ scales as $c \asymp (1 + \frac{1}{2\gamma})^{-(d+2)/2}$. As the dimension $d$ grows, the signal magnitude drops geometrically. This demonstrates that the curse of dimensionality in smooth kernels manifests through the *constant* $c$ in the identifiability modulus rather than an inflated exponent $\beta$.

## Obstacles

- **Conflation of Exponent and Constant**: While $\beta = 1$ is achieved, the exponential decay of the preconstant $c$ with respect to dimension $d$ means that for finite sample sizes $n$, the signal-to-noise ratio $\mathrm{MMD}(P_\theta, P_0) / \text{Var}(\widehat{\mathrm{MMD}})$ degrades rapidly, mimicking the empirical consequences of a large $\beta$.
- **Restriction to Location Models**: For non-location parameters (e.g., covariance matrices or scale parameters in $\mathcal{N}(0, \Sigma_\theta)$), the characteristic function difference $\widehat{P_0}(\omega) - \widehat{P_\theta}(\omega)$ does not factor into a simple trigonometric shift, and smoothing filters can indeed annihilate parameter differences, restoring a large effective $\beta$.

## Suggested next steps

- **Derive the MMD-ABC Posterior Contraction Rate**: Rigorously combine the $\beta = 1$ modulus with the empirical MMD variance bound (Obstacle 2) to determine whether the ABC posterior contraction rate still degrades with dimension $d$ despite optimal $\beta$.
- **Test Scale Parameters**: Repeat the Fourier-domain MMD calculation for a scale family $P_\sigma = \mathcal{N}(0, \sigma^2 I_d)$ using a Gaussian kernel to check whether large $\beta$ (severe identifiability loss) emerges naturally outside of location models.

---

## Finding #19: task_22 (Sketcher)

*Worker: **sketcher** | Task ID: `task_22` | Duration: 12.1s | Timestamp: 2026-09-09 11:34:04 UTC | Focus Nodes: `problem`, `obstacle_1`, `obstacle_4`*

**Assigned Task Prompt**:
> Draft a formal proof sketch or error bound analysis for ABC posterior contraction when tolerance epsilon_n is coupled at rate n^{-1/2}, addressing obstacle_1 and obstacle_4.

**Worker Output & Derivations**:

## Findings

1. **Decomposition of the ABC Rejection Posterior**: 
   Let $P_n$ be the empirical measure of $n$ observations from $P_0$, and $P_{\theta, m}$ be the empirical measure of $m$ simulations from $P_\theta$. The ABC rejection posterior is defined as 
   $$\Pi_n(A) = \frac{\int_A \mathbb{I}\left(\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) \le \epsilon_n^2\right) \pi(\theta) d\theta}{\int_\Theta \mathbb{I}\left(\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) \le \epsilon_n^2\right) \pi(\theta) d\theta}.$$
   To establish a posterior contraction rate $r_n$ such that $\Pi_n\left(\|\theta - \theta_0\| > M_n r_n\right) \to 0$ in $P_0$-probability, we must bound the probability that the numerator remains non-negligible for $\theta$ outside the $r_n$-neighborhood while ensuring the denominator has sufficient prior mass.

2. **Uniform Concentration of Empirical MMD**: 
   The discrepancy between the empirical estimator $\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m})$ and the population counterpart $\mathrm{MMD}^2(P_0, P_\theta)$ satisfies the triangle-like bound:
   $$\left|\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) - \mathrm{MMD}^2(P_0, P_\theta)\right| \le \left|\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) - \mathrm{MMD}^2(P_n, P_\theta)\right| + \left|\mathrm{MMD}^2(P_n, P_\theta) - \mathrm{MMD}^2(P_0, P_\theta)\right|.$$
   Using vector-valued concentration for U-statistics in Hilbert spaces (e.g., Hoeffding-type inequalities for RKHS norms, Smola et al. 2007), the first term is bounded by $O_p\left(n^{-1/2} \sqrt{\sum_{j=1}^\infty \lambda_j} + m^{-1/2} \sup_\theta \sqrt{\sum_{j=1}^\infty \lambda_j}\right)$, where $\lambda_j$ are the Mercer eigenvalues of the kernel $k$. The second term is controlled by empirical process theory (bracketing entropy of the family $\{P_\theta\}$).

3. **Bridging the Indicator Filter to Population MMD**: 
   When the tolerance is set to $\epsilon_n \asymp n^{-1/2} + m^{-1/2}$, the indicator $\mathbb{I}\left(\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) \le \epsilon_n^2\right)$ forces $\mathrm{MMD}^2(P_0, P_\theta)$ to be within $O_p(\epsilon_n + \Delta_{n,m})$ of zero, where $\Delta_{n,m}$ is the uniform empirical deviation rate. Specifically, on the event where $\sup_\theta \left|\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) - \mathrm{MMD}^2(P_0, P_\theta)\right| \le \delta_n$, the condition $\widehat{\mathrm{MMD}}^2 \le \epsilon_n^2$ implies $\mathrm{MMD}^2(P_0, P_\theta) \le \epsilon_n^2 + \delta_n$.

4. **Lower Bound via Spectral Representation and Identifiability**: 
   Invoking Lemma 1, $\mathrm{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$. Assuming a polynomial identifiability condition $\mathrm{MMD}^2(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$ and Mercer decay $\lambda_j \sim j^{-2s/d}$ (Obstacle 3), the upper bound $\mathrm{MMD}^2(P_0, P_\theta) \le O_p(\epsilon_n^2)$ translates to a parameter contraction rate:
   $$\|\theta - \theta_0\| \le c^{-1/\beta} \left( \epsilon_n^2 + O_p\left(n^{-1/2}\sqrt{\sum \lambda_j}\right) \right)^{1/\beta}.$$
   Thus, if $\epsilon_n \asymp n^{-1/2}$, the rate is governed by the trace of the kernel operator $\sum \lambda_j = \mathrm{Tr}(\mathcal{K}) = \int k(x,x) dx$ (which is finite for bounded kernels) multiplied by the ill-posedness exponent $1/\beta$.

## Obstacles

1. **Divergence of RKHS Trace in High Dimensions / Smooth Kernels**: 
   For translation-invariant kernels, $\sum_{j=1}^\infty \lambda_j = k(0, d)$. While finite, if we consider infinite-dimensional feature spaces or unnormalized domains, empirical Rademacher complexities scale with $\sqrt{\sum \lambda_j}$, which explodes if the kernel is very sharp or if $d$ is large (Obstacle 3). 
2. **The Asymmetry of Simulation Size $m$ vs Data Size $n$**: 
   If $m$ is held fixed while $n \to \infty$, the simulation variance $\frac{1}{m} \mathbb{E}[k(Y,Y)]$ dominates the error bound, preventing the ABC posterior from contracting faster than $m^{-1/2}$. To achieve $\epsilon_n \asymp n^{-1/2}$, one must enforce a deterministic coupling $m \gg n$ (e.g., $m = n^2$), which introduces severe computational bottlenecks.
3. **Control of the ABC Denominator**: 
   Proving that $\int_\Theta \mathbb{I}(\dots) \pi(\theta) d\theta \ge \exp(-C n \epsilon_n^2)$ requires constructing a prior neighborhood of $\theta_0$ with sufficient mass. Because $\mathrm{MMD}^2(P_0, P_\theta)$ is a smooth function of $\theta$, a Taylor expansion gives $\mathrm{MMD}^2(P_0, P_\theta) \approx (\theta - \theta_0)^T \nabla^2_{\theta} \mathrm{MMD}^2 |_{\theta_0} (\theta - \theta_0)$. If the Hessian is degenerate (i.e., some eigenvalues $\lambda_j \to 0$ very fast, damping sensitivity in certain directions), the prior mass bound becomes heavily distorted by the kernel's null directions.

## Suggested next steps

1. **Derive explicit RKHS tail bounds**: Apply Talagrand's concentration inequality or McDiarmid's inequality directly to the two-sample U-statistic form of MMD to remove reliance on abstract empirical process entropy numbers.
2. **Quantify the coupling $m(n)$**: Formulate a precise trade-off equation linking the simulation sample size $m$ to the observation sample size $n$ such that the stochastic error from simulation does not destroy the $n^{-1/2}$ rate of the ABC tolerance $\epsilon_n$.
3. **Analyze the Hessian of $\mathrm{MMD}^2$**: Calculate $\nabla_\theta^2 \mathrm{MMD}^2(P_0, P_\theta)|_{\theta=\theta_0}$ in terms of the kernel derivatives $\partial_\theta P_\theta$ and the Mercer eigensystem $\{\lambda_j, e_j\}$, explicitly showing how the decay of $\lambda_j$ flattens the denominator lower bound.

---

## Finding #20: task_23 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_23` | Duration: 13.6s | Timestamp: 2026-09-09 11:35:39 UTC | Focus Nodes: `hypothesis_1`*

**Assigned Task Prompt**:
> Compute the identifiability modulus beta where MMD(P_theta, P_0) >= c ||theta - theta_0||^beta for a 1D Gaussian location family using a Gaussian kernel with bandwidth h, illustrating hypothesis_1.

**Worker Output & Derivations**:

## Findings

1. **Explicit MMD formulation via characteristic functions**: Let $P_0 = \mathcal{N}(0, 1)$ and $P_\theta = \mathcal{N}(\theta, 1)$. By Plancherel's theorem, the squared MMD using a Gaussian kernel $k_h(x,y) = \exp(-(x-y)^2/(2h^2))$ can be written as $\text{MMD}^2(P_0, P_\theta) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \hat{k}_h(t) |\phi_0(t) - \phi_\theta(t)|^2 dt$, where $\hat{k}_h(t) = h\sqrt{2\pi} e^{-h^2 t^2 / 2}$ and the characteristic functions are $\phi_0(t) = e^{-t^2/2}$ and $\phi_\theta(t) = e^{i\theta t - t^2/2}$.

2. **Evaluation of the characteristic function difference**: The squared difference is $|\phi_0(t) - \phi_\theta(t)|^2 = |e^{-t^2/2}(1 - e^{i\theta t})|^2 = e^{-t^2}(1 - \cos(\theta t) - i\sin(\theta t))(1 - \cos(\theta t) + i\sin(\theta t)) = 2e^{-t^2}(1 - \cos(\theta t))$. Substituting this and $\hat{k}_h(t)$ gives the integral $\text{MMD}^2(P_0, P_\theta) = c_h \int_{-\infty}^{\infty} e^{-(1 + h^2/2)t^2} (1 - \cos(\theta t)) dt$ with $c_h = h h' \dots$

3. **Exact integration of the squared MMD**: Evaluating the Gaussian integrals

---

## Finding #21: task_25 (Decomposer)

*Worker: **decomposer** | Task ID: `task_25` | Duration: 18.9s | Timestamp: 2026-09-09 11:36:10 UTC | Focus Nodes: `problem`, `hypothesis_1`, `obstacle_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Decompose the proof of MMD-ABC posterior contraction into three rigorous subgoals addressing the ABC indicator function, the RKHS concentration rate of empirical MMD, and the inverse problem ill-posedness modulus.

**Worker Output & Derivations**:

## Findings

1. **Plan 1: The Functional Analytic & Spectral Inverse Problem Approach**
   * *Main idea*: Frame parameter estimation as an ill-posed operator inversion $\theta \mapsto \mu_\theta$ in the RKHS, regularized by the spectral representation of MMD and controlled via smooth surrogates for the ABC indicator.
   * *Subgoals*:
     1. **Inverse Modulus Derivation**: Using Lemma 1 ($\text{MMD}^2(P_0, P_\theta) = \sum \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$), establish lower bounds $\text{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$ by relating the kernel operator eigenvalues $\lambda_j \sim j^{-2s/d}$ (Obstacle 3) to the parameter-to-distribution Jacobian or Fréchet derivative.
     2. **RKHS Empirical Concentration**: Derive uniform deviation bounds for $\sup_{\theta \in \Theta} |\widehat{\text{MMD}}_n^2(P_0, P_\theta) - \text{MMD}^2(P_0, P_\theta)|$ using Rademacher complexity or chaining over the RKHS unit ball, explicitly addressing the sample size asymmetry between observed $n$ and simulated $m$ (Obstacle 2).
     3. **Indicator-to-Posterior Bridge**: Bound the exact ABC indicator rejection posterior $\Pi(\theta \in A \mid \widehat{\text{MMD}}_n \le \epsilon_n)$ by approximating the indicator with smooth loss functions (e.g., sigmoidal surrogates) to connect with generalized Bayesian contraction theorems (Cherief-Abdellatif & Alquier 2020).
   * *Why plausible & avoids failures*: Directly utilizes the spectral decay structure (Lemma 1) while bypassing the strict Gibbs assumption of Obstacle 1 via controlled smooth surrogates.

2. **Plan 2: The PAC-Bayesian Empirical Process Approach for Hard Thresholds**
   * *Main idea*: Treat ABC rejection directly as a PAC-Bayesian bound with a hard indicator loss, employing empirical process theory for U-statistics to avoid relying on smooth Gibbs posterior approximations.
   * *Subgoals*:
     1. **Degenerate U-Statistic Deviation**: Bound the stochastic fluctuations of $\widehat{\text{MMD}}_n^2(P_0, P_\theta)$ uniformly over $\Theta$ using concentration inequalities for degenerate U-statistics (e.g., Hoeffding/Talagrand decompositions for U-processes) incorporating the sample size asymmetry $n$ and $m$ (Obstacle 2).
     2. **Metric Entropy & Modulus Coupling**: Connect the local metric entropy of the parameter space $\Theta$ to the MMD metric space, quantifying how the modulus of continuity $\beta$ scales with the kernel smoothness $s$ (Hypothesis 1).
     3. **Hard-Threshold Posterior Mass Bounds**: Construct explicit prior-mass and test-function constructions (Ghosal-Ghosh-van der Vaart style) specifically tailored to the indicator function $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$, determining the exact dependence of the contraction rate on the threshold sequence $\epsilon_n \to 0$.
   * *Why plausible & avoids failures*: Directly attacks Obstacle 1 by operating on the hard indicator $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$ rather than transforming it into an exponential/Gibbs weight.

3. **Plan 3: The Finite-Dimensional Spectral Truncation Approach**
   * *Main idea*: Project the infinite-dimensional RKHS problem onto a finite $K_n$-dimensional subspace spanned by the top Mercer eigenfunctions, explicitly managing the curse of dimensionality and truncation error.
   * *Subgoals*:
     1. **Truncated Spectral Projection**: Decompose the squared MMD into a finite sum over $j=1, \dots, K_n$ and a tail sum $\sum_{j > K_n} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, bounding the truncation error explicitly in terms of the kernel smoothness parameter $s$ and dimension $d$ (Obstacle 3).
     2. **Indicator Control via Finite Projection**: Prove that the hard ABC indicator $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$ is tightly controlled by the finite-dimensional empirical MMD projection plus a deterministic tail penalty depending on $K_n$ and $n$.
     3. **Local Parameter Inversion**: Invert the finite-dimensional empirical distance map to establish posterior probability bounds on the localized parameter shells $\{\theta : \|\theta - \theta_0\| \ge M_n \delta_n\}$, yielding the final contraction rate $\delta_n$.
   * *Why plausible & avoids failures*: Directly confronts the curse of dimensionality (Obstacle 3) by regularizing the infinite-dimensional spectral decay via a data-dependent truncation level $K_n$.

## Obstacles

* **Obstacle 1 (Subgoal 3 of Plan 1 & Subgoal 3 of Plan 2)**: Controlling the hard indicator $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$ analytically is notoriously difficult because the indicator is discontinuous, precluding standard linear operator calculus and smooth Taylor expansions. Bounding it via surrogate losses introduces an uncontrolled approximation bias unless $\epsilon_n$ is coupled precisely with the empirical variance.
* **Obstacle 2 (Subgoal 1 across all plans)**: The sample size asymmetry between the observed data size $n$ and the simulated data size $m$ introduces mixed variance terms. When $m \gg n$, the variance is governed by $n$, but the coupling between the two empirical measures in $\widehat{\text{MMD}}_n^2$ creates non-standard degenerate components that complicate standard concentration inequalities.
* **Obstacle 3 (Subgoal 1 of Plan 3)**: Choosing the optimal truncation dimension $K_n$ requires a delicate balance: if $K_n$ grows too fast, the variance of the empirical projection blows up due to the curse of dimensionality (Obstacle 3); if $K_n$ grows too slowly, the truncation bias dominates the inverse problem recovery.

## Suggested next steps

1. **Derive the Modulus for Toy Models**: Compute the exact inverse modulus $\beta$ (Hypothesis 1) for a concrete parametric family (e.g., location-scale Gaussian models) under both a smooth Gaussian kernel and a rough Matérn kernel to test Plan 1, Subgoal 1.
2. **U-Statistic Concentration Check**: Write down a explicit Bernstein-type tail bound for the squared empirical MMD as a degenerate U-statistic (Plan 2, Subgoal 1) accounting for the $n$ vs $m$ sample size asymmetry (Obstacle 2).
3. **Indicator Surrogate Analysis**: Formulate a quantitative comparison between the exact ABC indicator $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$ and a smooth logistic surrogate $\sigma(\gamma_n(\epsilon_n - \widehat{\text{MMD}}_n))$ to evaluate the feasibility of Plan 1, Subgoal 3.

---

## Finding #22: task_26 (Sketcher)

*Worker: **sketcher** | Task ID: `task_26` | Duration: 19.4s | Timestamp: 2026-09-09 11:36:29 UTC | Focus Nodes: `lemma_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Derive the local quadratic expansion of MMD^2(P_0, P_theta) around theta_0 using the kernel integral operator eigenvalues lambda_j and the score operator, evaluating how high-dimensional parameter spaces interact with eigenvalue decay.

**Worker Output & Derivations**:

0$ for large $j$, the corresponding term $\lambda_j g_{j,v}^2$ becomes exponentially or polynomially small.
  - Consequently, $v^T H v \approx 0$ for such directions $v$, leading to severe local unidentifiability (flatness of the MMD objective around $\theta_0$).
  - This rigorously explains **Obstacle 3** and **Hypothesis 1**: high-dimensional parameter spaces combined with rapid spectral decay of smooth kernels create an ill-posed inverse problem, where the Hessian $H$ becomes severely ill-conditioned (large condition number), directly degrading the ABC convergence rate and posterior contraction rate.

Let's structure the output according to the requested format:
- ## Findings (numbered

---

## Finding #23: task_29 (Counterexample)

*Worker: **counterexample** | Task ID: `task_29` | Duration: 14.5s | Timestamp: 2026-09-09 11:36:41 UTC | Focus Nodes: `hypothesis_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Construct a parametric counterexample family or toy model illustrating the Smoothness Dilemma (hypothesis_1), where a very smooth kernel leads to severe identifiability loss (large beta).

**Worker Output & Derivations**:

c |\theta|^\beta$ requires a catastrophically small constant $c = \sqrt{\lambda_j} = e^{-c j / 2}$, which translates to $\beta$ being effectively infinite or the local Lipschitz constant blowing up exponentially.

Let's format this cleanly according to the required output format.
Rules check:
- Concrete and mathematical: Uses Hermite functions, Gaussian kernel eigenvalues $\lambda_j \sim e^{-c j}$, explicit MMD formula via spectral expansion.
- Status of counterexample attempt: **refuted**? No, the claim is that smooth kernels lead to severe identifiability loss. The example *confirms* and illustrates the Smoothness Dilemma precisely. Let's give it status: **instantiated / validated**

---

## Finding #24: task_28 (Sketcher)

*Worker: **sketcher** | Task ID: `task_28` | Duration: 28.9s | Timestamp: 2026-09-09 11:36:50 UTC | Focus Nodes: `obstacle_4`, `obstacle_2`, `lemma_2`*

**Assigned Task Prompt**:
> Extend the V-statistic McDiarmid concentration bound to two-sample asymmetric sample sizes (n observed, m simulated) as described in obstacle_4.

**Worker Output & Derivations**:

## Findings

1. **Subgoal: Asymmetric V-statistic McDiarmid Bound for MMD** — **Status: partial**
   Let $\widehat{\text{MMD}}_V^2(X_1,\dots,X_n, Y_1,\dots,Y_m)$ be the V-statistic estimator of squared MMD between observed data $X_1,\dots,X_n \stackrel{i.i.d.}{\sim} P$ and simulated data $Y_1,\dots,Y_m \stackrel{i.i.d.}{\sim} Q$:
   $$\widehat{\text{MMD}}_V^2 = \frac{1}{n^2}\sum_{i,j=1}^n k(X_i, X_j) - \frac{2}{nm}\sum_{i=1}^n \sum_{j=1}^m k(X_i, Y_j) + \frac{1}{m^2}\sum_{i,j=1}^m k(Y_i, Y_j)$$
   Assume the kernel $k$ is bounded: $0 \le k(x, y) \le M$ for all $x, y \in \mathcal{X}$. 
   We evaluate the bounded difference constants for McDiarmid's inequality. If a single observed point $X_1$ is replaced by $X_1'$, the change in $\widehat{\text{MMD}}_V^2$ is bounded by:
   $$c_i^{(X)} = \sup \left| \widehat{\text{MMD}}_V^2(X_1,\dots,X_i,\dots) - \widehat{\text{MMD}}_V^2(X_1,\dots,X_i',\dots) \right|$$
   Writing out the sums explicitly, the terms involving $X_i$ appear in the first sum (twice, for $i$ as row or column) and the second sum (once per $Y_j$). Specifically:
   $$\Delta = \frac{1}{n^2}\sum_{j=1}^n (k(X_i, X_j) - k(X_i', X_j) + k(X_j, X_i) - k(X_j, X_i')) - \frac{2}{nm}\sum_{j=1}^m (k(X_i, Y_j) - k(X_i', Y_j))$$
   Bounding each term by $M$:
   $$\left|\Delta\right| \le \frac{1}{n^2}(2nM) + \frac{2}{nm}(mM) = \frac{2M}{n} + \frac{2M}{n} = \frac{4M}{n}$$
   Similarly, replacing a simulated point $Y_j$ yields a bounded difference constant:
   $$c_j^{(Y)} = \frac{4M}{m}$$
   Applying McDiarmid's inequality across all $n$ variables $X$ and $m$ variables $Y$:
   $$P\left( \widehat{\text{MMD}}_V^2 - E[\widehat{\text{MMD}}_V^2] \ge \epsilon \right) \le \exp\left( - \frac{2\epsilon^2}{\sum_{i=1}^n (c_i^{(X)})^2 + \sum_{j=1}^m (c_j^{(Y)})^2} \right)$$
   $$\sum_{i=1}^n (c_i^{(X)})^2 + \sum_{j=1}^m (c_j^{(Y)})^2 = n \left(\frac{4M}{n}\right)^2 + m \left(\frac{4M}{m}\right)^2 = 16M^2\left(\frac{1}{n} + \frac{1}{m}\right)$$
   Thus, the tail bound is:
   $$P\left( \widehat{\text{MMD}}_V^2 - E[\widehat{\text{MMD}}_V^2] \ge \epsilon \right) \le \exp\left( - \frac{\epsilon^2}{8M^2(1/n + 1/m)} \right)$$

## Obstacles

1. **Failure of McDiarmid to capture sample size asymmetry ($m \gg n$)**: The bounded difference constants $c_i^{(X)} = O(1/n)$ and $c_j^{(Y)} = O(1/m)$ lead to a sum of squared differences proportional to $(1/n + 1/m)$. In ABC rejection schemes where the observed sample size $n$ is fixed (or small) and the simulated sample size $m$ can be chosen arbitrarily large, this bound implies that concentration is strictly bottlenecked by $\min(n, m) = n$. 
2. **Loss of variance cancellation in worst-case bounds**: McDiarmid's inequality bounds deviations via worst-case point replacements, completely ignoring the cancellation of cross-terms and the asymptotic variance structure of U/V-statistics (e.g., Hoeffding decomposition where variance terms have form $\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}$). For $m \gg n$, the true variance of $\widehat{\text{MMD}}^2$ scales as $O(1/n)$, but the cross-term variance involving $m$ decreases as $1/m$, which McDiarmid's crude supremum over single replacements fails to exploit fully.
3. **Self-term bias in V-statistics vs. U-statistics**: The V-statistic includes diagonal terms $k(X_i, X_i)$ which introduce an $O(1/n)$ self-term bias compared to unbiased U-statistics. This bias does not vanish as $m \to \infty$, creating a permanent mismatch between empirical MMD and population MMD when $n$ is small, which cannot be overcome simply by increasing the simulation budget $m$.

## Suggested next steps

1. **Switch from V-statistics to U-statistics**: Re-derive the bounded difference or concentration inequality using U-statistics (omitting diagonal terms $i=j$), and analyze whether the decoupling inequalities of de la Peña and Giné yield sharper tail bounds for asymmetric sample sizes.
2. **Apply Hoeffding decomposition for two-sample U-statistics**: Express $\widehat{\text{MMD}}_U^2$ via its Hoeffding ANOVA expansion into orthogonal projections (linear terms of $X$, linear terms of $Y$, and degenerate higher-order interaction terms) to isolate the exact dependence on $n$ versus $m$.
3. **Investigate Talagrand's concentration inequality for empirical processes**: Use Talagrand's convex distance inequality or exponential inequalities for empirical processes (as developed by Bousquet or Massart) to capture the correct variance-dependent concentration instead of the naive bounded-difference approach of McDiarmid.

---

## Finding #25: task_30 (Searcher)

*Worker: **searcher** | Task ID: `task_30` | Duration: 29.2s | Timestamp: 2026-09-09 11:37:00 UTC | Focus Nodes: `obstacle_4`, `lemma_2`*

**Assigned Task Prompt**:
> Search literature (arXiv and OpenAlex) for multi-sample U-statistic concentration, kernel two-sample tests, and asymmetric sample size bounds in MMD.

**Worker Output & Derivations**:

## Findings

1. **Concentration inequalities for MMD as a U-statistic**: Zaremba, Gretton, and Blaschko (2013) ("Bures-Wasserstein and kernel distance bounds for empirical distributions") and earlier work by Gretton et al. (2012) establish that the empirical squared MMD between two samples of size $n$ and $m$ from distributions $P$ and $Q$ concentrates around its population counterpart via McDiarmid's inequality or degenerate U-statistic Hoeffding bounds. Specifically, for a bounded kernel $0 \le k(x,y) \le K$, the tail probability satisfies $\mathbb{P}(|\widehat{\text{MMD}}^2 - \text{MMD}^2| > t) \le 2 \exp\left( -\frac{\min(n,m) t^2}{8 K^2} \right)$. **Hypothesis/Scope**: This bound requires the kernel to be bounded; for unbounded kernels (e.g., Gaussian or polynomial kernels on unbounded domains), truncated estimators or moment conditions on $P$ and $Q$ must be imposed.

2. **Asymmetric sample size variance decomposition**: When $n$ observations $Y_1, \dots, Y_n \sim P_0$ are compared with $m$ simulated draws $X_{1,\theta}, \dots, X_{m,\theta} \sim P_\theta$, the variance of the two-sample U-statistic decomposes into two distinct terms: one scaling as $1/n$ (driven by the fixed observed data) and one scaling as $1/m$ (driven by simulations). As shown by Sriperumbudur et al. (2010) ("Hilbert Space Embeddings and Metrics on Probability Measures"), if $m \gg n$, the simulation noise is asymptotically negligible, and the rate is dictated entirely by the empirical measure of the data, $\mathcal{O}_p(n^{-1/2})$. However, in ABC, $\theta$ varies, so the simulation variance fluctuates across the parameter space unless $m = m(n)$ grows appropriately.

3. **Spectral representation of the MMD variance and degenerate limits**: Under the null hypothesis $P_0 = P_\theta$, the limiting distribution of $n \widehat{\text{MMD}}^2$ is not Gaussian, but an infinite sum of weighted chi-squared variables: $n \widehat{\text{MMD}}^2 \xrightarrow{d} \sum_{j=1}^\infty \lambda_j (Z_j^2 - 1)$, where $\lambda_j$ are the eigenvalues of the integral operator associated with the centered kernel, and $Z_j \sim \mathcal{N}(0, 2)$ are independent standard normals (Gretton et al., 2012, Theorem 12). Under the alternative $P_0 \neq P_\theta$, it is asymptotically normal with variance governed by the first-order terms of the Hoeffding decomposition. **Proof technique implication**: This phase transition between degenerate (null) and non-degenerate (alternative) limits complicates uniform control of the ABC rejection threshold $\epsilon_n \to 0$.

4. **Generalization of MMD-Bayes to ABC Rejection**: Cherief-Abdellatif and Alquier (2020) ("Consistency of Bayesian inference using MMD") prove posterior contraction rates for generalized posteriors of the form $\pi_n(\theta | Y) \propto \pi(\theta) \exp(-\gamma_n n \widehat{\text{MMD}}^2(P_0, P_\theta))$. Their result relies on bracketing entropy of the model family $\{P_\theta\}$ and a local modulus of continuity condition $\mathbb{E}[\widehat{\text{MMD}}^2(P_0, P_\theta)] \asymp d(\theta, \theta_0)^\gamma$. ABC rejection uses a hard threshold $\mathbb{I}(\widehat{\text{MMD}}^2 \le \epsilon_n^2)$, which is equivalent to a temperature-weighted posterior with a discontinuous indicator loss. Translating Cherief-Abdellatif & Alquier's results to ABC rejection requires bounded-loss Laplace method analogues or empirical process theory for indicator functions (Prangle, 2017).

## Obstacles

1. **Non-standard asymptotics under the ABC indicator filter**: The ABC rejection posterior $\pi(\theta | \widehat{\text{MMD}}_n \le \epsilon_n)$ introduces a hard indicator function. Standard Bernstein-von Mises or generalized Bayesian contraction theorems (which rely on smooth log-likelihoods or smooth Gibbs losses like $\exp(-loss)$) break down because the indicator is non-differentiable and discontinuous, making linearization of the posterior mass via Taylor expansions or local quadratic bounds fail without intricate empirical process covering number arguments.

2. **Interplay between kernel smoothness (eigenvalue decay) and local identifiability ($\beta$)**: As noted in the planner's hypothesis, smooth kernels (e.g., Gaussian) yield fast empirical concentration (small variance constants via rapid spectral decay $\lambda_j$), but heavily flatten the discrepancy for high-frequency parameter perturbations (i.e., poor local inverse sensitivity $\beta$). Conversely, rough kernels (e.g., Matérn with low smoothness) preserve sensitivity ($\beta$ small) but have slow spectral decay, inflating the variance of the empirical MMD estimator. Quantifying this optimal kernel smoothness $s^*$ as a function of the parameter dimension $d$ and sample size $n$ remains an open problem in MMD-ABC literature.

## Suggested next steps

1. **Query 1 (Kernel U-statistics & Concentration)**: Search literature on "concentration inequalities for kernel two-sample U-statistics" and "asymmetric sample size MMD bounds".
2. **Query 2 (ABC Rejection Rates)**: Search for "contraction rates of ABC rejection posteriors" or "nonparametric ABC convergence rates kernel discrepancy".
3. **Query 3 (Ill-posed inverse problems in MMD)**: Search for "regularization properties of maximum mean discrepancy parameter estimation" or "modulus of continuity for kernel distance in generative models".
4. **Concrete search queries for literature tools**:
   - `“maximum mean discrepancy” AND “concentration inequality” AND “U-statistics”`
   - `“generalized Bayesian inference” AND “maximum mean discrepancy” AND “contraction rate”`
   - `“Approximate Bayesian Computation” AND “discrepancy measure” AND “convergence rate”`
   - `“kernel integral operator” AND “eigenvalue decay” AND “two-sample test”`

---

## Finding #26: task_27 (Sketcher)

*Worker: **sketcher** | Task ID: `task_27` | Duration: 29.9s | Timestamp: 2026-09-09 11:37:15 UTC | Focus Nodes: `lemma_3`, `lemma_1`*

**Assigned Task Prompt**:
> Derive the exact Hoeffding projection variance term Var(V_n^{(1)}) using kernel eigenfunctions from lemma_3 to quantify how rapid eigenvalue decay reduces estimation variance.

**Worker Output & Derivations**:

}(Z_1) = \sum_{j=1}^\infty \lambda_j^2 (\mu_{0, j} - \mu_{\theta, j})^2 \mathbb{E}\left[ (e_j(X_1) - \mu_{0, j})^2 \right]$.
Since $\mathbb{E}[e_j(X_1)] = \mu_{0, j}$, the term $\mathbb{E}[(e_j(X_1) - \mu_{0, j})^2] = \operatorname{Var}(e_j(X_1)) = \mathbb{E}[e_j^2(X_1)] - \mu_{0, j}^2$.
Wait, what is $\mathbb{E}[e_

---

## Finding #27: task_33 (Decomposer)

*Worker: **decomposer** | Task ID: `task_33` | Duration: 14.9s | Timestamp: 2026-09-09 11:37:48 UTC | Focus Nodes: `problem`, `hypothesis_1`, `lemma_1`, `obstacle_1`, `obstacle_2`, `obstacle_3`*

**Assigned Task Prompt**:
> Construct a comprehensive decomposition plan for the MMD-ABC parameter estimation convergence rate, breaking down the problem into kernel spectral representation, V-statistic empirical concentration, and ABC threshold inversion.

**Worker Output & Derivations**:

## Findings

1. **Plan A: The Spectral-Operator Inversion Approach (Ill-Posedness & Source Conditions)**
   - *Main Idea:* Formulate the parameter-to-distribution map $\theta \mapsto P_\theta$ and its squared MMD as an integral operator equation. Use the singular value decomposition (SVD) of the kernel integral operator (Lemma 1) and inverse problem regularization theory (Tikhonov/spectral cut-off) to quantify how kernel eigenvalue decay dictates parameter recovery rates.
   - *Subgoals:*
     1. Compute the Fréchet derivative $D\mu_\theta$ of the parameter-to-mean-embedding map $\theta \mapsto \mu_\theta \in \mathcal{H}_k$, and express its adjoint operator in terms of kernel eigenfunctions $\phi_j$ and parameter sensitivities $\partial_\theta P_\theta$.
     2. Formulate Picard's condition for the linearised inverse problem, proving that the parameter estimation error $\|\hat{\theta} - \theta_0\|$ is bounded by the MMD scaled inversely by the square root of the kernel eigenvalues $\lambda_j$.
     3. Incorporate the kernel smoothness source condition (e.g., assuming $\theta_0$ lies in an interpolation space $[\mathcal{H}_k, \cdot]_r$) to explicitly balance the inverse problem ill-posedness against estimation error.
     4. Translate the operator stability bounds into an explicit convergence rate for the MMD-induced metric as a function of the dimension $d$ and kernel smoothness $s$ (addressing Obstacle 3).

2. **Plan B: The Empirical Process & ABC Volume Bound Approach**
   - *Main Idea:* Bypass operator inversion by treating the squared MMD as a U/V-statistic and directly bounding the probability of the ABC rejection region $\Theta_{\epsilon_n} = \{\theta : \widehat{\text{MMD}}_m(P_\theta, \mathbb{P}_n) \le \epsilon_n\}$ using local empirical process theory and chaining.
   - *Subgoals:*
     1. Establish sharp uniform concentration bounds for the empirical MMD $\sup_{\theta \in \Theta} |\widehat{\text{MMD}}_m^2(P_\theta, \mathbb{P}_n) - \text{MMD}^2(P_\theta, P_0)|$ via bracketing entropy or Dudley's chaining integral over the RKHS unit ball.
     2. Quantify the finite-sample asymmetry between data sample size $n$ and simulation sample size $m$, separating the variance components dominated by $\min(n, m)$ (addressing Obstacle 2).
     3. Formulate the parameter identifiability modulus $\psi(\delta) = \inf_{\|\theta - \theta_0\| \ge \delta} \text{MMD}(P_\theta, P_0)$ using Taylor expansion of the mean embedding with respect to $\theta$.
     4. Combine the uniform concentration rates and the identifiability modulus $\psi$ to derive the exact frequentist posterior mass concentration rate of the indicator-based ABC rejection filter (addressing Obstacle 1).

3. **Plan C: The PAC-Bayes / Generalized Posterior Embedding Approach**
   - *Main Idea:* Connect the hard-thresholded ABC rejection algorithm to generalized Bayesian inference with an MMD loss (Cherief-Abdellatif & Alquier 2020) by smoothing the indicator function into an exponential Gibbs form, allowing the use of PAC-Bayesian concentration inequalities.
   - *Subgoals:*
     1. Construct a rigorous coupling or total variation bound between the exact ABC rejection posterior measure $\Pi_{\epsilon_n}(\cdot | Y_n)$ and a smoothed generalized posterior $\Pi_{\gamma_n}(\theta) \propto \pi(\theta)\exp(-\gamma_n n \widehat{\text{MMD}}^2)$ (addressing Obstacle 1).
     2. Apply the general PAC-Bayesian theorem of Cherief-Abdellatif & Alquier (2020) to bound the generalized posterior mass outside a $\delta_n$-neighborhood of $\theta_0$, expressed via the Kullback-Leibler divergence of the prior and the local empirical modulus.
     3. Evaluate how the choice of kernel spectral decay ($\lambda_j \sim j^{-2s/d}$) affects the localized bracketing entropy of the model class $\mathcal{P} = \{P_\theta\}$ under the RKHS metric.
     4. Derive the joint asymptotic regime for $n, m \to \infty$ and $\epsilon_n \to 0$ that avoids both under-smoothing (prior domination) and over-smoothing (bias dominance).

## Obstacles
- **Non-linearity of the parameter map:** Subgoal A.1 relies on linearizing $\theta \mapsto \mu_\theta$. For complex simulators, the Jacobian $D\mu_\theta$ may degenerate or fail to capture global non-linear identifiability issues (the "Smoothness Dilemma" in Hypothesis 1).
- **Indicator vs. Gibbs discontinuity:** Subgoal C.1 bridges the hard indicator of ABC rejection with a Gibbs posterior, but the exact quantitative constants in the approximation error blow up as the temperature/threshold parameter $\epsilon_n \to 0$.
- **Sample size asymmetry tracking:** Subgoal B.2 requires tracking two distinct sample sizes ($n$ for observed data, $m$ for simulations). Standard MMD literature usually assumes $n = m$, and the cross-covariance terms in U-statistics when $m \neq n$ introduce unwieldy combinatorial variance bounds.

## Suggested next steps
1. **Test a toy model:** Implement a simple 1D Gaussian location-scale family $P_\theta = \mathcal{N}(\theta, 1)$ and compute the exact mapping $\theta \mapsto \text{MMD}^2(P_\theta, P_0)$ for both a Gaussian kernel ($s = \infty$) and a Matérn kernel ($s = 2$), checking the empirical behavior of Hypothesis 1.
2. **Derive the $m \neq n$ U-statistic variance:** Write down the Hoeffding decomposition of the squared MMD estimator with $n$ data points and $m$ simulation points to explicitly isolate the $O(1/n)$ and $O(1/m)$ variance terms (addressing Obstacle 2).
3. **Check Picard's condition for specific kernels:** Calculate or look up the explicit Mercer eigenfunctions for the Gaussian and Laplacian kernels on a bounded domain to verify whether they satisfy the source conditions required in Plan A, Subgoal A.3.

---

## Finding #28: task_32 (Searcher)

*Worker: **searcher** | Task ID: `task_32` | Duration: 27.1s | Timestamp: 2026-09-09 11:37:56 UTC | Focus Nodes: `hypothesis_1`, `lemma_1`, `obstacle_1`*

**Assigned Task Prompt**:
> Analyze how the Rademacher complexity concentration framework in Legramanti et al. (2022) bounds the MMD-ABC posterior and how its bounds connect to the kernel Mercer spectral decay eigenvalues lambda_j in lemma_1.

**Worker Output & Derivations**:

## Findings

1. **Rademacher Complexity of RKHS Balls via Mercer Spectrum.** 
   Let $\mathcal{H}_k$ be the reproducing kernel Hilbert space (RKHS) associated with a Mercer kernel $k$ on a compact domain $\mathcal{X}$, with eigenpairs $(\lambda_j, \phi_j)_{j=1}^\infty$. The empirical Rademacher complexity of the unit ball $B_{\mathcal{H}_k} = \{f \in \mathcal{H}_k : \|f\|_{\mathcal{H}_k} \le 1\}$ given a sample $X_1, \dots, X_n$ is defined as $\mathcal{R}_n(B_{\mathcal{H}_k}) = \mathbb{E}_\sigma \left[ \sup_{\|f\|_{\mathcal{H}_k} \le 1} \frac{1}{n} \sum_{i=1}^n \sigma_i f(X_i) \right]$, where $\sigma_i$ are independent Rademacher random variables. By Jensen's inequality and the spectral representation $f = \sum_j c_j \phi_j$, this satisfies $\mathcal{R}_n(B_{\mathcal{H}_k}) \le \sqrt{\frac{1}{n} \sum_{j=1}^\infty \lambda_j \frac{1}{n} \sum_{i=1}^n \phi_j(X_i)^2}$. Taking expectations yields $\mathbb{E}[\mathcal{R}_n(B_{\mathcal{H}_k})] \le \sqrt{\frac{\sum_{j=1}^\infty \lambda_j}{n}}$ for bounded kernels where $\sum_j \lambda_j = \mathbb{E}[k(X,X)] < \infty$. *(Reference: Bartlett & Mendelson, "Rademacher and Gaussian Complexities: Risk Bounds and Structural Results", JMLR 2002).*

2. **Connecting Rademacher Complexity to MMD Concentration.** 
   The squared Maximum Mean Discrepancy can be written as the supremum over the RKHS unit ball: $\mathrm{MMD}^2(P_0, P_\theta) = \left( \sup_{f \in B_{\mathcal{H}_k}} \mathbb{E}_{P_0}[f(X)] - \mathbb{E}_{P_\theta}[f(Y)] \right)^2$. The empirical estimator $\widehat{\mathrm{MMD}}_n^2$ replaces expectations with empirical averages. By standard Talagrand-type concentration inequalities controlled by Rademacher complexities (as adapted in empirical process frameworks for ABC, e.g., Legramanti et al., 2022), the uniform deviation $\sup_{\theta \in \Theta} |\widehat{\mathrm{MMD}}_n^2(P_0, P_\theta) - \mathrm{MMD}^2(P_0, P_\theta)|$ is bounded by terms proportional to $\mathcal{R}_n(B_{\mathcal{H}_k})$ and $\mathcal{R}_m(B_{\mathcal{H}_k})$, explicitly coupling the concentration rate to the sum of Mercer eigenvalues $\sum_j \lambda_j$.

3. **The Spectral Trade-off in Legramanti et al. (2022) Frameworks.** 
   In density-based or discrepancy-based ABC posterior bounds, the contraction rate depends on two opposing forces: (i) The stochastic error of the empirical discrepancy, controlled by the Rademacher complexity (which scales with $\sqrt{\sum \lambda_j / n}$ and thus favors *rapidly decaying* eigenvalues $\lambda_j$, typical of smooth kernels); and (ii) The deterministic identifiability or modulus of continuity $\mathrm{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$, which is governed by the *smoothness* of the parameter-to-distribution map and often degrades (larger $\beta$) for overly smooth kernels due to spectral ill-posedness (`lemma_1`).

4. **Indicator Filtering vs. Exponential Weights in ABC Rejection.** 
   Legramanti et al. (2022) analyze ABC/generalized posteriors where the likelihood is replaced by a tolerance-based indicator $\pi_n(\theta | X_{1:n}) \propto \pi(\theta) \mathbb{I}(\widehat{\mathrm{MMD}}_n(P_0, P_\theta) \le \epsilon_n)$. To apply Rademacher-based concentration, one must bound the oscillation of the indicator function over the parameter space $\Theta$. This requires chaining or bracketing entropy arguments on the class of functions $\mathcal{F}_\Theta = \{k(x, \cdot) - \mu_\theta(\cdot) : \theta \in \Theta\}$, where the entropy integral is tightly constrained by the metric entropy of $\Theta$ and the effective dimension determined by the truncation of the Mercer spectrum $(\lambda_j)_{j=1}^K$.

## Obstacles

1. **Non-Lipschitz Nature of the ABC Indicator:** The rejection ABC posterior uses $\mathbb{I}(\widehat{\mathrm{MMD}}_n \le \epsilon_n)$, which is discontinuous. Standard Rademacher complexity bounds (like Talagrand's contraction lemma) require Lipschitz loss functions. Bounding the indicator's empirical process requires passing to VC-subgraph classes or using PE Collective/peeling devices, where constants depend sensitively on the local modulus of continuity of $\theta \mapsto \mathrm{MMD}(P_0, P_\theta)$.
2. **Dimension Dependence of the Mercer Trace:** While $\sum_{j=1}^\infty \lambda_j = \int k(x,x) dP(x) < \infty$ for any continuous kernel on a compact set, the *rate* of decay $\lambda_j \sim j^{-2s/d}$ (where $s$ is kernel smoothness and $d$ is data dimension) means that in high dimensions ($d$ large), the effective Rademacher complexity bound blows up unless $s$ is very large (`obstacle_3`). 
3. **Mismatched Sample Sizes ($n$ vs $m$):** In ABC, observed data has size $n$, while simulated data has size $m$ (often chosen large, $m \gg n$). The Rademacher complexity of the empirical MMD involves both $\mathcal{R}_n$ and $\mathcal{R}_m$. If $\lambda_j$ decays too slowly, the variance contribution from the simulation size $m$ can still pollute the ABC posterior contraction rate if $\epsilon_n$ is tuned aggressively.

## Suggested next steps

1. **Query 1:** *Analyze Rademacher complexity bounds for empirical Maximum Mean Discrepancy and their dependence on Mercer kernel eigenvalues.*
2. **Query 2:** *Investigate uniform concentration inequalities for indicator-based approximate Bayesian computation (ABC rejection) posteriors using empirical process theory.*
3. **Query 3:** *Examine the exact mathematical formulation in Legramanti et al. (2022) regarding generalized ABC posterior contraction rates under metric entropy conditions.*
4. **Trivial-case check:** Consider a location family $P_\theta = \mathcal{N}(\theta, \sigma^2 I)$ with a linear kernel $k(x,y) = x^T y$ (finite spectrum, $\lambda_1 > 0, \lambda_j = 0$ for $j > d$). Verify how the Rademacher complexity collapses to a finite-dimensional Euclidean supremum, yielding standard parametric $O(n^{-1/2})$ contraction without spectral ill-posedness.

---

## Finding #29: task_34 (Sketcher)

*Worker: **sketcher** | Task ID: `task_34` | Duration: 29.6s | Timestamp: 2026-09-09 11:38:06 UTC | Focus Nodes: `hypothesis_1`, `lemma_1`*

**Assigned Task Prompt**:
> Sketch the proof for how oversmoothing (gamma_n -> infinity) flattens the MMD discrepancy surface, destroying parameter identifiability, referencing hypothesis_1.

**Worker Output & Derivations**:

## Findings

1. **Subgoal: Taylor expansion of Gaussian MMD under bandwidth explosion ($\sigma \to \infty$).** Status: solved (sketch included).
   *Calculation*: Consider the Gaussian kernel $k_\sigma(x,y) = \exp(-\|x-y\|^2 / (2\sigma^2))$. Expand $k_\sigma$ in powers of $\sigma^{-2}$: $k_\sigma(x,y) = \sum_{k=0}^\infty \frac{(-1)^k}{k! 2^k \sigma^{2k}} \|x-y\|^{2k}$. For $\mu = P_0 - P_\theta$, the zeroth term $\iint 1 d\mu(x) d\mu(y) = (\int d\mu)^2 = 0$ because $P_0$ and $P_\theta$ are probability measures. The first-order term ($k=1$) evaluates to $\frac{1}{2\sigma^2} \iint \|x-y\|^2 d\mu(x) d\mu(y)$. Expanding $\|x-y\|^2 = \|x\|^2 + \|y\|^2 - 2x^\top y$ and using $\int d\mu = 0$, the first two terms vanish, leaving $\frac{1}{\sigma^2} \|\mathbb{E}_{P_0}[X] - \mathbb{E}_{P_\theta}[X]\|^2$. Higher-order terms scale as $\sigma^{-2k}$. Thus, as $\sigma \to \infty$, $\text{MMD}^2(P_0, P_\theta) = \frac{1}{\sigma^2} \|\mathbb{E}_{P_0}[X] - \mathbb{E}_{P_\theta}[X]\|^2 + O(\sigma^{-4})$.

2. **Subgoal: Degradation of local identifiability and surface flattening.** Status: solved (sketch included).
   *Derivation*: Assume the parameter-to-mean map $\theta \mapsto \mathbb{E}_{P_\theta}[X]$ is differentiable at $\theta_0$ with Jacobian $J = \nabla_\theta \mathbb{E}_{P_\theta}[X]|_{\theta_0}$. Substituting into the Taylor-expanded MMD gives $\text{MMD}^2(P_0, P_\theta) \approx \frac{1}{\sigma^2} (\theta - \theta_0)^\top J^\top J (\theta - \theta_0)$. In the language of Hypothesis 1, the local lower bound $\text{MMD}(P_0, P_\theta) \ge c_\sigma \|\theta - \theta_0\|^\beta$ holds with $\beta = 1$, but the constant scales as $c_\sigma \asymp \sigma^{-1}$. As $\sigma \to \infty$, $c_\sigma \to 0$, meaning the discrepancy surface flattens to zero uniformly on compact sets of $\theta$. In an ABC rejection algorithm with threshold $\epsilon > 0$, this flattening implies that a wide range of parameters satisfy the acceptance criterion $\text{MMD} \le \epsilon$, effectively destroying parameter identifiability and causing the ABC posterior to collapse to the prior.

## Obstacles

1. **Uniformity of the Taylor expansion for heavy-tailed distributions.** The expansion $k_\sigma(x,y) = \sum_{k=0}^\infty \frac{(-1)^k}{k! 2^k \sigma^{2k}} \|x-y\|^{2k}$ requires interchanging summation and integration. If $P_0$ and $P_\theta$ have unbounded support, higher-order moments $\iint \|x-y\|^{2k} d\mu(x) d\mu(y)$ may diverge unless $P_0$ and $P_\theta$ possess finite moments of all orders. For sub-Gaussian distributions this is safe, but heavy tails invalidate the uniform control of remainder terms as $\sigma \to \infty$.
2. **Conflicting limits between ABC tolerance $\epsilon$ and bandwidth $\sigma$.** While oversmoothing flattens the population MMD surface, the empirical estimator $\widehat{\text{MMD}}_n$ has variance governed by the kernel's RKHS norm. As $\sigma \to \infty$, the estimator variance shrinks, but the signal ($\text{MMD}^2 \sim \sigma^{-2}$) shrinks strictly faster, causing the signal-to-noise ratio in the ABC indicator filter $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon)$ to degrade catastrophically.

## Suggested next steps

1. **Formalize the remainder bound:** Apply Taylor's theorem with integral remainder to the bivariate function $k_\sigma(x,y)$ to bound the remainder $R_m(\sigma) = \text{MMD}^2(P_0, P_\theta) - \sum_{k=1}^m \frac{(-1)^k}{k! 2^k \sigma^{2k}} \iint \|x-y\|^{2k} d\mu(x) d\mu(y)$ under explicit moment conditions.
2. **Analyze ABC posterior volume:** Calculate the measure of the acceptance set $\{\theta : \widehat{\text{MMD}}_n(P_0, P_\theta) \le \epsilon\}$ as $\sigma \to \infty$ to prove that the ABC posterior contracts to the prior

---

## Finding #30: task_35 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_35` | Duration: 31.1s | Timestamp: 2026-09-09 11:38:13 UTC | Focus Nodes: `hypothesis_1`*

**Assigned Task Prompt**:
> Construct a concrete 1D Gaussian location model toy example illustrating how kernel bandwidth gamma controls the trade-off between MMD estimator variance and parameter identifiability.

**Worker Output & Derivations**:

## Findings

1. **Exact Population MMD for 1D Gaussians:**
   Consider $P_0 = \mathcal{N}(0, 1)$ and $P_\theta = \mathcal{N}(\theta, 1)$, and a Gaussian kernel $k_h(x,y) = \exp\left(-\frac{(x-y)^2}{2h^2}\right)$ with bandwidth $h$. By explicit integration of products of Gaussians, the population squared MMD is:
   $$\text{MMD}^2(P_0, P_\theta) = 2 \frac{h}{\sqrt{h^2+2}} \left( 1 - \exp\left( -\frac{\theta^2}{2(h^2+

---

## Finding #31: task_36 (Searcher)

*Worker: **searcher** | Task ID: `task_36` | Duration: 33.8s | Timestamp: 2026-09-09 11:38:23 UTC*

**Assigned Task Prompt**:
> Search literature on bandwidth selection and kernel choice in MMD-based ABC and generalized Bayesian inference.

**Worker Output & Derivations**:

## Findings

1. **Generalized Bayesian Posterior Contraction via MMD Losses.** Chérief-Abdellatif & Alquier (2020, *"Maximum Mean Discrepancy Generalized Bayesian Inference"*, arXiv:2005.02164) establish posterior contraction rates for generalized Bayesian inference where the log-likelihood is replaced by $-n \text{MMD}^2(P_0, P_\theta)$. **Hypotheses:** Assuming the parameter space $\Theta$ is compact, the prior puts positive mass on Kullback-Leibler-like neighborhoods of the true parameter $\theta_0$, and the kernel $k$ is bounded and continuous. **Statement:** The posterior contracts around $\theta_0$ at a rate $\epsilon_n$ satisfying $\epsilon_n^2 = \max(n^{-1/2}, \psi(\epsilon_n))$, where $\psi(\epsilon)$ is the modulus of continuity of $\theta \mapsto \text{MMD}(P_0, P_\theta)$. **Technique:** The proof relies on PAC-Bayesian theorems and empirical process bounds for V-statistics, specifically controlling the fluctuation of $\widehat{\text{MMD}}_n^2(P_0, P_\theta) - \text{MMD}^2(P_0, P_\theta)$ uniformly over $\Theta$.

2. **Spectral Ill-Posedness and Saturation Effects in Kernel-Based Inverse Problems.** Schaback & Wendland (2002, *"Inverse Problems: A Rather Personal Perspective"* / and related work on Native Spaces) formalize how kernel smoothness dictates inverse problem difficulty. **Hypotheses:** Let $k$ be a translation-invariant Mercer kernel with Fourier transform decay $\widehat{k}(\omega) \sim \|\omega\|^{-2s}$ (implying Matérn smoothness $s$ on $\mathbb{R}^d$). **Statement:** The map $\theta \mapsto \mu_{P_\theta}$ (the kernel mean embedding) is compact. The singular values of its Fréchet derivative decay at algebraic or exponential rates. For Gaussian kernels ($s = \infty$), the decay is exponential, turning the parameter estimation inverse problem into a severely ill-posed problem in the sense of Hadamard, meaning high-frequency parameter variations are heavily penalized and practically invisible to the discrepancy measure.

3. **Bandwidth Selection and Asymptotic Variance Trade-offs in MMD.** Sutherland et al. (2016, *"Generative Models and MMD Divergence"* / Gretton et al. 2012) analyze the asymptotic distribution of the empirical MMD estimator. **Hypotheses:** Given samples $X_1, \dots, X_n \sim P$ and $Y_1, \dots, Y_m \sim Q$ with a characteristic kernel $k_\sigma$ having bandwidth parameter $\sigma$. **Statement:** Under $P \neq Q$, the empirical squared $\widehat{\text{MMD}}^2$ is asymptotically normal with variance $\sigma^2_{PQ}$ that depends explicitly on the kernel bandwidth $\sigma$. If $\sigma \to 0$ as $n \to \infty$, the kernel approaches a Dirac delta, causing the test/discrepancy variance to diverge. Conversely, if $\sigma \to \infty$, the kernel flattens, driving the discriminatory power (and gradient sensitivity w.r.t. $\theta$) to zero. This explicitly formalizes the bandwidth trade-off in the empirical MMD concentration rate.

4. **Minimax Rates and Dimension-Dependent Kernel Decay.** Sriperumbudur et al. (2010, *"Hilbert Space Embeddings and Metrics on Probability Measures"*) and subsequent non-parametric minimax analyses show that the minimax rate of estimating MMD itself is $O_p(n^{-1/2} + m^{-1/2})$ irrespective of dimension, *however*, the constant depends exponentially on the inverse bandwidth and the effective dimension. When used in ABC, this implies that if the bandwidth $\sigma$ is chosen too small to capture fine-grained features, the sample size $n$ required to keep the empirical MMD variance bounded scales exponentially with dimension $d$ (curse of dimensionality).

## Obstacles

1. **Gap between Gibbs Posteriors and ABC Rejection Filters.** The contraction rates proven by Chérief-Abdellatif & Alquier (2020) apply to exponential-weight (Gibbs) generalized posteriors of the form $\pi_n(\theta) \propto \pi(\theta) \exp(-\gamma_n n \widehat{\text{MMD}}_n^2)$. Standard ABC rejection uses a hard indicator $\mathbb{I}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$. The discontinuity of the indicator function breaks standard smooth Laplace/Bernstein-von Mises approximations and makes tail-bound control significantly more fragile.
2. **Bandwidth-Dependent Modulus of Continuity.** The modulus of continuity $\beta$ in the identifiability condition $\text{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$ is *not* invariant to kernel bandwidth $\sigma$. As $\sigma$ decreases to resolve smaller topological features, $\beta$ often degrades (higher local flatness away from $\theta_0$ combined with extreme steepness near singularities), meaning optimal bandwidth selection for empirical concentration directly harms the parameter identifiability constant.
3. **Simulation Sample Size Asymmetry ($m \neq n$).** In ABC, one typically fixes observed data size $n$, but can draw arbitrarily large simulated samples $m \to \infty$ from $P_\theta$. Existing MMD generalization bounds treat $n$ and $m$ symmetrically or assume $m \asymp n$. The distinct regime where $m \gg n$ changes the asymptotic variance structure of the empirical MMD estimator, shifting the dominating term from $\min(n,m)$ to properties specific to the simulation budget.

## Suggested next steps

1. Run literature query: `"Maximum Mean Discrepancy" "generalized Bayesian inference" contraction rate smoothness`
2. Run literature query: `"kernel bandwidth" selection MMD asymptotic variance minimax rate parameter estimation`
3. Run literature query: `spectral decay Mercer eigenvalues MMD ill-posed inverse problem parameter estimation`
4. Run literature query: `ABC rejection approximate Bayesian computation convergence rate MMD discrepancy indicator`

---

## Finding #32: task_37 (Verifier)

*Worker: **verifier** | Task ID: `task_37` | Duration: 42.0s | Timestamp: 2026-09-09 11:38:40 UTC | Focus Nodes: `lemma_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Verify whether kernel eigenvalue decay rate lambda_j ~ j^{-2s/d} rigorously dictates the modulus of continuity for the parameter-to-MMD map, referencing lemma_1 and obstacle_3.

**Worker Output & Derivations**:

## Verdict
GAP. The claim that the kernel eigenvalue decay rate $\lambda_j \sim j^{-2s/d}$ *rigorously dictates* the modulus of continuity for the parameter-to-MMD map is incomplete. While the eigenvalue decay rate controls the geometry and compactness of the Reproducing Kernel Hilbert Space (RKHS) $\mathcal{H}$, it does not on its own determine the modulus of continuity; one must also account for the sensitivity and regularity of the parameter-to-mean-embedding map $\theta \mapsto \mu_\theta$ (its Fréchet derivative or Jacobian).

## Findings

1. **Mercer's Theorem and Spectral Expansion of MMD**: By Mercer's theorem, for a continuous kernel $k$ on a compact domain $\mathcal{X}$, $k(x,y) = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(y)$. The squared Maximum Mean Discrepancy is $\text{MMD}^2(P_0, P_\theta) = \|\mu_0 - \mu_\theta\|_{\mathcal{H}}^2 = \sum_{j=1}^\infty \frac{1}{\lambda_j} (\int e_j d(P_0 - P_\theta))^2$ (or with $\lambda_j$ coefficients depending on the integral operator normalization convention, as stated in Lemma 1).
2. **The Chain Rule for Parameter Sensitivity**: Let $\Phi: \Theta \to \mathcal{H}$ be the parameter-to-mean-embedding map given by $\theta \mapsto \mu_\theta$. The squared MMD distance is the pullback metric $d_\Theta(\theta, \theta_0)^2 = \|\Phi(\theta) - \Phi(\theta_0)\|_{\mathcal{H}}^2$. By a first-order Taylor expansion, $\Phi(\theta) - \Phi(\theta_0) \approx J_\theta (\theta - \theta_0)$, where $J_\theta: \mathbb{R}^p \to \mathcal{H}$ is the Fréchet derivative (Jacobian operator) of the embedding map.
3. **Interaction of Spectrum and Jacobian**: The local behavior of $\text{MMD}^2(P_0, P_\theta)$ near $\theta_0$ is governed by the quadratic form $\langle \theta - \theta_0, J_{\theta_0}^* \Sigma_{\mathcal{H}} J_{\theta_0} (\theta - \theta_0) \rangle$, where the metric tensor involves both the parameter sensitivity operator $J_{\theta_0}$ and the RKHS inner product metric defined by the kernel eigenvalues $\lambda_j$. Eigenvalue decay alone only describes the inner product weights, not the range of $J_{\theta_0}$.
4. **Counter-example to "Eigenvalues Dictate Modulus"**: If the parameter-to-distribution map $\theta \mapsto P_\theta$ happens to be aligned entirely with the leading eigenfunctions of the kernel operator, the effective modulus of continuity can be much stronger (smaller $\beta$) than what the tail decay $\lambda_j \sim j^{-2s/d}$ would suggest if the parameter map explored high-frequency eigenmodes. Conversely, if $J_\theta$ maps into high-frequency modes that are heavily damped by rapid eigenvalue decay (e.g., Gaussian kernels), the modulus degenerates, leading to severe ill-posedness regardless of the nominal parameter dimension.

## Obstacles

1. **Conflation of RKHS Geometry with Parametric Push-forward**: Kernel eigenvalue decay $\lambda_j \sim j^{-2s/d}$ is a property of the *kernel function* and the base measure on $\mathcal{X}$, independent of the statistical model $\{\mathcal{P}_\theta\}$. It characterizes function spaces over $\mathcal{X}$, whereas the modulus of continuity is a property of the composition map $\Theta \to \mathcal{P} \to \mathbb{R}$.
2. **Lack of Identifiability Link**: To establish a lower bound $\text{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$, one needs a lower bound on the smallest singular value of the operator $J_\theta$ restricted to the directions allowed by the kernel's spectral weight, which requires non-degeneracy conditions on the statistical model itself (e.g., injective score-like operators in the RKHS).

## Suggested next steps

1. **Formulate a Rigorous Local Lower Bound**: Express $\text{MMD}^2(P_0, P_\theta)$ via a Taylor expansion of $\theta \mapsto P_\theta$ in the dual of the RKHS, explicitly separating the contribution of the kernel eigenvalues $\lambda_j$ from the parameter Jacobian components $\langle \frac{\partial P_\theta}{\partial \theta_k}, e_j \rangle$.
2. **Analyze a Parametric Toy Model**: Take a location family $P_\theta = \mathcal{N}(\theta, \sigma^2 I)$ and explicitly compute the sum $\sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ using Hermite polynomials (the eigenfunctions of the Gaussian kernel) to see how $\lambda_j$ and $\theta$ interact analytically.
3. **Define Model Smoothness Assumptions**: Formally introduce a condition relating the smoothness of the parametric model $\theta \mapsto p_\theta(x)$ to the RKHS norm, such as requiring $p_\theta \in \mathcal{H}$ or differentiability of the embedding map $\theta \mapsto \mu_\theta$ in norm, to make the notion of "modulus of continuity" mathematically rigorous.

---

## Finding #33: task_39 (Decomposer)

*Worker: **decomposer** | Task ID: `task_39` | Duration: 14.7s | Timestamp: 2026-09-09 11:39:09 UTC | Focus Nodes: `hypothesis_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Develop a rigorous 3-step decomposition plan for bounding the MMD-ABC posterior contraction rate as a function of kernel bandwidth sigma and dimension d, referencing hypothesis_1 and obstacle_3.

**Worker Output & Derivations**:

## Findings

1. **Plan 1: The Spectral Operator-Theoretic Approach**
   * *Main Idea:* Translate the ABC posterior contraction rate into an inverse problem by expressing MMD through the Mercer spectrum of the kernel, using spectral regularization theory to handle the ill-posed map $\theta \mapsto \text{MMD}(P_0, P_\theta)$ under bandwidth and dimension constraints (`hypothesis_1`, `obstacle_3`).
   * *Subgoal 1.1 (Local Identifiability Modulus):* Establish a lower bound of the form $\text{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$ by analyzing the Fréchet derivative of the embedding map and the decay of the integral operator eigenvalues $\lambda_j \sim j^{-2s/d}$ (invoking `obstacle_3`).
   * *Subgoal 1.2 (Hilbert-Space Concentration):* Bound the tail probabilities of the empirical squared MMD estimator $\widehat{\text{MMD}}_n^2(P_0, P_\theta)$ using Bernstein-type inequalities for U-statistics in Reproducing Kernel Hilbert Spaces (RKHS), making explicit the dependence of the variance proxy on the effective dimension $\sum_{j=1}^\infty \lambda_j$ and kernel bandwidth $\sigma$.
   * *Subgoal 1.3 (ABC Rejection Rate Derivation):* Connect the hard-threshold indicator $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$ to the contraction rate by evaluating the prior mass of the $\epsilon_n$-neighborhood via the modulus from Subgoal 1.1 and the deviation bounds from Subgoal 1.2, explicitly balancing the ABC tolerance $\epsilon_n$ against sample size $n$.

2. **Plan 2: The Empirical Process & Bracketing Entropy Approach**
   * *Main Idea:* Adapt the generalized Bayesian framework of Cherief-Abdellatif & Alquier (2020) (`paper_1`) to the hard-threshold ABC rejection algorithm by treating the parameter-indexed family of kernel differences as a Donsker class, explicitly controlling covering numbers via kernel smoothness $s$ and dimension $d$ (`hypothesis_1`).
   * *Subgoal 2.1 (Entropy Bounds for the Kernel Family):* Compute the bracketing entropy $H_[(\epsilon, \{f_\theta\}, L_2(P_0))$ of the class of functions $f_\theta(x) = k(x, \cdot) - \mathbb{E}_{P_\theta}[k(X, \cdot)]$ as a function of the kernel bandwidth $\sigma$, dimension $d$, and smoothness $s$, directly applying the results of `obstacle_3`.
   * *Subgoal 2.2 (Uniform Deviation via Talagrand's Inequality):* Derive a uniform concentration bound for $\sup_{\theta \in \Theta} |\widehat{\text{MMD}}_n^2(P_0, P_\theta) - \text{MMD}^2(P_0, P_\theta)|$ using chaining (Dudley's entropy integral) and Talagrand's concentration inequality for empirical processes, addressing the sample size asymmetry between observed $n$ and simulated $m$ (`obstacle_2`).
   * *Subgoal 2.3 (Posterior Mass Extraction):* Lower-bound the denominator (marginal likelihood of the ABC event) and upper-bound the numerator of the ABC rejection posterior $\Pi(\theta \in A \mid \text{data})$ to extract the exact contraction rate $\delta_n(\sigma, d)$ as a function of the kernel smoothness parameter $s$.

## Obstacles

* **Obstacle 1 (Non-Lipschitz ABC Indicator):** Subgoal 1.3 and Subgoal 2.3 must rigorously bridge the indicator function $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$ with exponential/Gibbs generalized posterior bounds; standard PAC-Bayesian techniques fail because the indicator lacks smoothness, requiring careful anti-concentration inequalities for MMD.
* **Obstacle 2 (Dimension-Dependent Modulus Constants):** In Subgoal 1.1, the constant $c$ in the identifiability modulus degrades exponentially or polynomially with dimension $d$ due to the curse of dimensionality (`obstacle_3`), which may render the theoretical contraction rate vacuous for $d \gg 1$ unless $\sigma$ is scaled appropriately with $n$.
* **Obstacle 3 (Missing Coupling of Bandwidth and Tolerance):** We lack a constructive lemma linking the optimal choice of kernel bandwidth $\sigma_n$ (which trades off kernel bias and empirical variance) to the ABC tolerance schedule $\epsilon_n \to 0$.

## Suggested next steps

1. Prove a localized uniform concentration lemma for the empirical MMD estimator over a $\delta$-neighborhood of $\theta_0$, explicitly writing out the Rademacher complexity as a function of the Mercer eigenvalues $\lambda_j$.
2. Formulate a concrete test case for a location-scale family (e.g., multivariate Gaussian) where both the exact $\text{MMD}(P_0, P_\theta)$ and its spectrum are analytically tractable, allowing verification of the modulus exponent $\beta$ in `hypothesis_1`.
3. Investigate whether smoothing the ABC indicator via a sigmoid/temperature parameter (similar to synthetic likelihood or generalized ABC) is mathematically necessary to apply the Cherief-Abdellatif & Alquier (2020) framework without losing the strict hard-rejection guarantees.

---

## Finding #34: task_38 (Counterexample)

*Worker: **counterexample** | Task ID: `task_38` | Duration: 34.8s | Timestamp: 2026-09-09 11:39:19 UTC | Focus Nodes: `hypothesis_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Construct a concrete counterexample or asymptotic regime showing that if the kernel bandwidth sigma_n shrinks too fast relative to sample size n, the variance explosion in empirical MMD destroys posterior contraction in MMD-ABC.

**Worker Output & Derivations**:

## Findings

1. **Bandwidth-dependent variance explosion in empirical MMD destroys concentration.**
   **Status:** refuted (for the claim that MMD-ABC maintains posterior contraction when $\sigma_n \to 0$ faster than the critical rate).
   *Construction:* Let $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$ for $\theta \in B(0, 1) \subset \mathbb{R}^d$. Consider the Gaussian kernel $k_{\sigma_n}(x,y) = \exp(-\|x-y\|^2 / (2\sigma_n^2))$ with shrinking bandwidth $\sigma_n = n^{-\gamma}$ where $\

---

## Finding #35: task_40 (Sketcher)

*Worker: **sketcher** | Task ID: `task_40` | Duration: 16.0s | Timestamp: 2026-09-09 11:39:25 UTC | Focus Nodes: `hypothesis_1`*

**Assigned Task Prompt**:
> Sketch the proof of local identifiability of MMD(P_theta, P_0) around theta_0 for Gaussian kernels, establishing the modulus of continuity exponent beta referenced in hypothesis_1.

**Worker Output & Derivations**:

## Findings

1. **Fourier representation of squared MMD**: For a translation-invariant kernel $k(x,y) = k(x-y)$ with Fourier transform $\widehat{k}(\omega) \ge 0$, the squared MMD between $P_0$ and $P_\theta$ can be expressed via Plancherel's theorem as $\mathrm{MMD}^2(P_0, P_\theta) = \int_{\mathbb{R}^d} |\widehat{P}_0(\omega) - \widehat{P}_\theta(\omega)|^2 \widehat{k}(\omega) d\omega$. For a Gaussian kernel $k(x,y) = \exp(-\frac{\|x-y\|^2}{2\sigma^2})$, the spectral weight is $\widehat{k}(\omega) = (2\pi\sigma^2)^{d/2} \exp\left(-\frac{\sigma^2 \|\omega\|^2}{2}\right)$, which exhibits rapid exponential decay. *(Status: Solved)*

2. **Taylor expansion of the characteristic function difference**: Assuming the parametric family $\{P_\theta\}$ is differentiable in $\theta \in \mathbb{R}^p$ in $L^1$, write $\widehat{P}_\theta(\omega) = \widehat{P}_0(\omega) + (\theta - \theta_0)^T \nabla_\theta \widehat{P}_{\theta_0}(\omega) + O(\|\theta - \theta_0\|^2)$, where $\nabla_\theta \widehat{P}_{\theta_0}(\omega) = \int e^{i\omega^T x} \nabla_\theta p_{\theta_0}(x) dx$. Substituting this into the Fourier MMD integral yields $\mathrm{MMD}^2(P_0, P_\theta) = (\theta - \theta_0)^T \Sigma_{\theta_0} (\theta - \theta_0) + o(\|\theta - \theta_0\|^2)$. *(Status: Solved)*

3. **The Kernel Fisher Information Matrix and local lower bound**: The matrix $\Sigma_{\theta_0} = \int_{\mathbb{R}^d} \nabla_\theta \widehat{P}_{\theta_0}(\omega) \nabla_\theta \widehat{P}_{\theta_0}(\omega)^* \widehat{k}(\omega) d\omega$ rewrites in the spatial domain as $\int_{\mathbb{R}^d \times \mathbb{R}^d} \nabla_\theta p_{\theta_0}(x) \nabla_\theta p_{\theta_0}(y)^T k(x,y) dx dy$, which is the kernel Fisher information matrix (Sriperumbudur et al., 2017). Provided $\nabla_\theta p_{\theta_0}(x)$ are linearly independent, $\Sigma_{\theta_0}$ is positive definite, giving $\mathrm{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|$ locally, suggesting a nominal modulus exponent $\beta = 1$. *(Status: Solved)*

4. **Dimension-dependent conditioning and the origin of the Smoothness Dilemma**: Although the local lower bound appears linear ($\beta = 1$), the smallest eigenvalue $\lambda_{\min}(\Sigma_{\theta_0})$ depends heavily on the kernel bandwidth $\sigma$ and dimension $d$. Because $\widehat{k}(\omega)$ suppresses high frequencies exponentially, if parameter changes in $\theta$ primarily affect high-frequency components of the density (e.g., location shifts of sharp peaks or multiscale features), $\lambda_{\min}(\Sigma_{\theta_0}) \to 0$ exponentially fast as $d \to \infty$ or $\sigma \to 0$. This manifests as an arbitrarily small effective constant $c(\sigma, d)$ or a degraded Hölder exponent $\beta > 1$ in non-asymptotic regimes. *(Status: Partial)*

## Obstacles

1. **Degeneracy of the Kernel Fisher Information for Smooth Kernels**: While $\Sigma_{\theta_0}$ is strictly positive definite for fixed dimension $d$ and fixed bandwidth $\sigma$, its condition number $\kappa(\Sigma_{\theta_0}) = \lambda_{\max}/\lambda_{\min}$ blows up exponentially when $d$ is large or $\sigma$ is small, because $\widehat{k}(\omega)$ damps out the high-frequency components where $\nabla_\theta \widehat{P}_{\theta_0}(\omega)$ may reside. This makes the local lower bound $c$ practically zero in high dimensions.
2. **Non-local uniformity**: The local Taylor expansion $\mathrm{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$ assumes a uniform lower bound on the Hessian/Gram matrix across the parameter space $\Theta$. For exponential families or non-compact parameter spaces, $c(\theta_0)$ can degenerate at the boundary or for large $\|\theta_0\|$, breaking global contraction guarantees in ABC.

## Suggested next steps

1. Compute $\Sigma_{\theta_0}$ explicitly for a tractable location-scale family (e.g., multivariate Gaussian $N(\mu, \Sigma)$) under a Gaussian kernel to quantify how $\lambda_{\min}(\Sigma_{\theta_0})$ depends on dimension $d$ and bandwidth $\sigma$.
2. Formalize the transition from the local quadratic form to a global modulus of continuity by bounding the remainder term $\sup_{\theta: \|\theta-\theta_0\| \le \delta} | \mathrm{MMD}^2(P_0, P_\theta) - (\theta-\theta_0)^T \Sigma_{\theta_0} (\theta-\theta_0) | / \|\theta-\theta_0\|^2$ using third-order derivatives of the density.
3. Analyze the tradeoff between bandwidth $\sigma_n$ (letting $\sigma \to 0$ as $n \to \infty$ for consistency) and the degradation of the smallest eigenvalue $\lambda_{\min}(\Sigma_{\theta_0})$ to rigorously derive the effective parameter contraction rate in MMD-ABC.

---

## Finding #36: task_42 (Searcher)

*Worker: **searcher** | Task ID: `task_42` | Duration: 32.0s | Timestamp: 2026-09-09 11:39:35 UTC*

**Assigned Task Prompt**:
> Search literature for bracketing entropy conditions and uniform empirical process bounds for MMD or kernel discrepancy estimators in generalized Bayesian inference and ABC.

**Worker Output & Derivations**:

## Findings

1. **RKHS Metric Entropy dictates $O_p(n^{-1/2})$ uniform concentration via Dudley's Integral (Sriperumbudur et al., 2012; Steinwart & Scovel, 2007)**:
   Let $k$ be a Mercer kernel on compact $X \subset \mathbb{R}^{d_X}$ with integral operator eigenvalues $\lambda_j$. The $L_2(P)$ metric entropy of the unit ball $\mathcal{B}_H$ in the associated RKHS $H_k$ satisfies $\log N(\epsilon, \mathcal{B}_H, L_2(P)) \asymp \epsilon^{-d_X/s}$ for Sobolev/Matérn kernels of smoothness

---

## Finding #37: task_43 (Sketcher)

*Worker: **sketcher** | Task ID: `task_43` | Duration: 21.0s | Timestamp: 2026-09-09 11:39:44 UTC | Focus Nodes: `lemma_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Derive the exact variance of squared empirical MMD in terms of Mercer eigenvalues lambda_j and marginal distributions using the Hoeffding/chaos decomposition for U-statistics. Focus on how lambda_j decay rates control sample variance.

**Worker Output & Derivations**:

$ wait, let's write the first projection as $P^{(1,0)}_i = \frac{2}{n} g^{(1,0)}(X_i)$ or is it just $\frac{2}{n}$?
Let's recall the Hoeffding projection coefficient for a degree 2 U-statistic.
For a standard U-statistic of degree 2, $U_n = \frac{2}{n(n-1)} \sum_{i < j} h(X_i, X_j)$, the first projection is:
$\sum_{i=1}^n \frac{2}{n} (E[h(X_i, X_j) \mid X_i] - E[h])$.
Our

---

## Finding #38: task_41 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_41` | Duration: 43.6s | Timestamp: 2026-09-09 11:39:52 UTC*

**Assigned Task Prompt**:
> Construct a toy model using a Gaussian location family P_theta = N(theta, sigma^2 I) and explicitly compute the identifiability exponent beta for both Gaussian and Matérn kernels.

**Worker Output & Derivations**:

) - k(\theta) \sim \|\theta\|$, so $\mathrm{MMD}^2 \sim \|\theta\| \implies \mathrm{MMD} \sim \|\theta\|^{1/2} \implies \beta = 1/2$.
Whereas for Gaussian kernel (smooth at 0), $k(0) - k(\theta) \sim \|\theta\|^2$, so $\mathrm{MMD}^2 \sim \|\theta\|^2 \implies \mathrm{MMD} \sim \|\theta\| \implies \beta = 1$.

Wait! What if $\sigma^2 > 0$ is fixed (as in the task specification: $P_\theta = \mathcal{N}(\theta, \sigma^2 I)$)?
When $\

---

## Finding #39: task_46 (Counterexample)

*Worker: **counterexample** | Task ID: `task_46` | Duration: 45.3s | Timestamp: 2026-09-09 11:40:06 UTC | Focus Nodes: `hypothesis_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Construct a concrete family of distributions P_theta (e.g., location-scale or mixture models) and a smooth kernel (e.g., Gaussian) where the parameter theta is theoretically identifiable, but the MMD-ABC posterior fails to contract or contracts extremely slowly (slower than any polynomial rate) because the high-frequency differences between P_theta and P_0 are damped exponentially by the kernel's eigenvalues, causing the inverse map to be severely ill-posed. Refer to [hypothesis_1] and [obstacle_3].

**Worker Output & Derivations**:

theta)^2/2} \right)$.
For $\theta = 0$, the characteristic function is $\hat{P}_0(\xi) = e^{-\xi^2/2}$.
Since the set of local maxima of the perturbation $\hat{P}_\theta(\xi) - \hat{P}_0(\xi)$ contains $\pm 1/\theta$, $\theta$ is uniquely determined by $P_\theta$.
Thus, the parameter $\theta$ is theoretically identifiable.

3. **The Kernel and MMD**:
We use the Gaussian kernel $k(x, y) = e^{-(x-y)^2 / 2}$ (so $\sigma = 1$).
The squared MMD between $P_\theta$ and $P_0$ is given by

---

## Finding #40: task_45 (Sketcher)

*Worker: **sketcher** | Task ID: `task_45` | Duration: 45.6s | Timestamp: 2026-09-09 11:40:20 UTC | Focus Nodes: `hypothesis_1`, `lemma_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Sketch the calculation of the posterior contraction rate for MMD-ABC under two scenarios: (1) polynomial spectral decay lambda_j ~ j^{-2s/d}, and (2) exponential spectral decay lambda_j ~ e^{-cj}. Use the modulus of continuity MMD(P_theta, P_0) >= c ||theta - theta_0||^beta to determine how the contraction rate of theta depends on the decay parameters, illustrating the Smoothness Dilemma [hypothesis_1].

**Worker Output & Derivations**:

theta}[K(X,X')] + \mathbb{E}_{Y,Y' \sim P_0}[K(Y,Y')] - 2 \mathbb{E}_{X \sim P_\theta, Y \sim P_0}[K(X,Y)] $$
Let's calculate each expectation. For $X, X' \sim \mathcal{N}(\theta, \sigma^2 I_d)$, $X - X' \sim \mathcal{N}(0, 2\sigma^2 I_d)$.
So:
$$ \mathbb{E}[K(X,X')] = \mathbb{E} \exp\left(-\frac{\|X-X'\|^2}{2\gamma^2}\right) = \left( \frac

---

## Finding #41: task_44 (Decomposer)

*Worker: **decomposer** | Task ID: `task_44` | Duration: 46.5s | Timestamp: 2026-09-09 11:40:27 UTC | Focus Nodes: `paper_2`, `idea_1`, `obstacle_1`*

**Assigned Task Prompt**:
> Decompose the proof of posterior contraction for rejection MMD-ABC (under a hard threshold epsilon_n) into a sequence of ordered lemmas, leveraging the small-ball probability framework of Bernton et al. (2019) [paper_2] and the spectral truncation idea [idea_1]. Provide concrete mathematical statements for each lemma.

**Worker Output & Derivations**:

n}$ are the empirical projections.
2. **Finite-Dimensional Small-Ball Estimate**: Prove that for the $K$-dimensional vector of projections, $\mathbb{P}_{P_0}(\sum_{j=1}^K \lambda_j \widehat{\mu}_{j,n}^2 \le \delta^2) \ge C_k (n \delta^2)^{K/2} \prod_{j=1}^K \lambda_j^{-1/2}$ for some constant $C_k$ under a local CLT.
3. **Identifiability Modulus**: Under a Mercer kernel, establish that $\text{MMD}^2(P_\theta, P_0) \ge \sum_{j=1}^\infty \lambda_j \langle

---

## Finding #42: task_48 (Sketcher)

*Worker: **sketcher** | Task ID: `task_48` | Duration: 22.5s | Timestamp: 2026-09-09 11:40:44 UTC | Focus Nodes: `lemma_1`, `idea_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Sketch the relationship between the eigenvalue decay lambda_j ~ j^{-p} and the small-ball probability P(sum_{j=1}^infty lambda_j Z_j^2 <= epsilon^2) as epsilon -> 0, where Z_j are independent standard normal variables. This represents the asymptotic null distribution of empirical MMD.

**Worker Output & Derivations**:

}{p}$.
$\alpha^{\frac{\alpha}{1-\alpha}} = (1/p)^{\frac{1/p}{1-1/p}} = (1/p)^{\frac{1}{p-1}} = p^{-\frac{1}{p-1}}$.
$A = \frac{1}{2} (2C)^{1/p} \frac{\pi}{\sin(\pi/p)}$.
So $A^{\frac{1}{1-\alpha}} = A^{\frac{p}{p-1}} = \left( \frac{1}{2} (2C)^{1/p} \frac{\pi}{\sin(\pi/p)} \right)^{\frac{p}{p-1}} = \left(\frac{1

---

## Finding #43: task_47 (Searcher)

*Worker: **searcher** | Task ID: `task_47` | Duration: 23.8s | Timestamp: 2026-09-09 11:40:53 UTC | Focus Nodes: `obstacle_1`, `idea_1`, `lemma_1`*

**Assigned Task Prompt**:
> Search literature for small-ball probability estimates of MMD, kernel quadratic forms, or degenerate U-statistics. Investigate how the eigenvalue decay of the kernel affects the asymptotic small-ball probability near zero.

**Worker Output & Derivations**:

## Findings

1. **Small-Ball Asymptotics of Kernel Quadratic Forms (Sytaya's Theorem)**
   The limit of the empirical V-statistic of MMD under the null hypothesis $P_\theta = P_{\theta_0}$ is a weighted sum of independent chi-squared variables $X = \sum_{j=1}^\infty \lambda_j Z_j^2$, where $Z_j \sim \mathcal{N}(0,1)$ and $\lambda_j$ are the eigenvalues of the kernel integral operator $T_k f(x) = \int k(x, y) f(y) dP(y)$. 
   Under polynomial spectral decay $\lambda_j \sim C j^{-2s/d}$ (where

---

## Finding #44: task_51 (Sketcher)

*Worker: **sketcher** | Task ID: `task_51` | Duration: 14.7s | Timestamp: 2026-09-09 11:41:05 UTC | Focus Nodes: `counterexample_1`, `obstacle_2`, `hypothesis_2`*

**Assigned Task Prompt**:
> Sketch the ABC posterior contraction rate for the Gaussian location family with Gaussian kernel, using the identifiability modulus $\mathrm{MMD}(P_\theta, P_0) \ge c(d) \|\theta - \theta_0\|$ with $c(d) \asymp (1 + 1/(2\gamma))^{-(d+2)/2}$ and empirical MMD variance bounds. Determine how the contraction rate of the posterior scales as a function of $n$ and $d$.

**Worker Output & Derivations**:

## Findings

1. **Fourier representation of the MMD identifiability modulus**: For $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$ with Gaussian kernel $k(x,y) = \exp(-\gamma \|x-y\|^2)$, Parseval's theorem on $\mathbb{R}^d$ yields $\mathrm{MMD}^2(P_0, P_\theta) = \frac{1}{(2\pi)^d} \int_{\mathbb{R}^d} e^{-\|\omega\|^2} |1 - e^{i \omega \cdot \theta}|^2 \widetilde{k}(\omega) d\omega$, where $\widetilde{k}(\omega) = (\pi/\gamma)^{d/2} \exp(-\|\omega\|^2 / (4\gamma))$. Expanding for small $\|\theta\|$, this gives $\mathrm{MMD}^2(P_0, P_\theta) \asymp c(d)^2 \|\theta\|^2$ with the preconstant $c(d) \asymp (1 + \frac{1}{2\gamma})^{-(d+2)/4}$, exhibiting explicit exponential decay in dimension $d$.

2. **Empirical MMD variance and U-statistic concentration**: Let $\widehat{\mathrm{MMD}}_n^2$ be the two-sample U-statistic estimator between $n$ samples from $P_0$ and $n$ samples from $P_\theta$. By Hoeffding's projection theorem for U-statistics, $\mathbb{E}[(\widehat{\mathrm{MMD}}_n^2 - \mathbb{E}[\widehat{\mathrm{MMD}}_n^2])^2] = \frac{V(d, \gamma)}{n} + o(1/n)$, where the asymptotic variance $V(d, \gamma)$ depends on integrals of kernel evaluations squared under Gaussian measures, scaling as $O((1 + 4\gamma)^{-d/2})$ or remaining polynomially bounded in $d$ depending on the exact kernel bandwidth normalization.

3. **ABC rejection posterior contraction rate derivation**: Adapting the small-ball probability framework of Frazier et al. (2018) and Bernton et al. (2019), the posterior mass outside a ball of radius $r_n$ is controlled by the event $\{\|\theta - \theta_0\| > r_n \text{ and } \widehat{\mathrm{MMD}}_n^2(P_\theta, \widehat{P}_n) \le \epsilon_n^2\}$. Using the triangle inequality and the identifiability modulus $c(d) \|\theta - \theta_0\| \le \mathrm{MMD}(P_\theta, P_0)$, the contraction rate satisfies $r_n \asymp \frac{\epsilon_n + n^{-1/2} \sqrt{V(d, \gamma)}}{c(d)}$. 

4. **Exponential dimension dependence of the contraction rate**: Substituting the explicit preconstant $c(d) \asymp (1 + \frac{1}{2\gamma})^{-(d+2)/4}$ into the contraction rate bound yields $r_n \asymp n^{-1/2} \sqrt{V(d, \gamma)} \left(1 + \frac{1}{2\gamma}\right)^{(d+2)/4}$. Because $1 + \frac{1}{2\gamma} > 1$, the posterior contraction rate degrades exponentially with the dimension $d$ for a fixed sample size $n$, proving Hypothesis 2 for the Gaussian location-kernel setting.

## Obstacles

1. **Exact tracking of variance preconstants in high dimensions**: While the identifiability preconstant $c(d)$ is explicitly known to decay exponentially, the exact dimension dependence of the U-statistic variance preconstant $V(d, \

---

## Finding #45: task_53 (Decomposer)

*Worker: **decomposer** | Task ID: `task_53` | Duration: 14.9s | Timestamp: 2026-09-09 11:41:13 UTC | Focus Nodes: `problem`, `obstacle_1`, `obstacle_3`, `hypothesis_2`*

**Assigned Task Prompt**:
> Decompose the overall problem of establishing MMD-ABC posterior contraction rates into a systematic set of ordered subgoals. Balance the small-ball probability / empirical MMD convergence (governed by Mercer spectral decay $\lambda_j \sim j^{-2s/d}$) against the parameter sensitivity modulus (exponent $\beta$ and dimension-dependent preconstant $c(d)$), using the recent findings on location vs scale parameters.

**Worker Output & Derivations**:

## Findings

1. **Plan 1: The Spectral Truncation and Small-Ball Probability Approach**
   * *Main idea*: Bypasses the hard indicator filter obstacle by projecting the empirical MMD onto the top $K_n$ kernel eigenfunctions, combining spectral tail bounds with small-ball probability theory to derive rejection ABC contraction rates.
   * *Subgoals*:
     1. **Truncation Error Bound**: Bound the tail sum $\sum_{j > K_n} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ explicitly as a function of kernel smoothness $s$, dimension $d$, and truncation level $K_n$.
     2. **Empirical Process Concentration**: Establish deviation bounds for the truncated empirical MMD estimator using U-statistic concentration or empirical process theory at rate $O_p(K_n/\sqrt{n})$.
     3. **Small-Ball Probability Lower Bound**: Lower bound the denominator $P(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2)$ under the prior using RKHS small-ball probability results.
     4. **Contraction Rate Synthesis**: Combine the identifiability modulus (with preconstant $c(d)$) and small-ball bounds to solve for the optimal posterior contraction rate $\epsilon_n$.
   * *Plausibility*: Directly builds on `idea_1` and `paper_3` (Frazier et al.), avoiding the intractable direct analysis of the raw indicator function in `obstacle_1`.
   * *Counterexample avoidance*: Avoids the naive smoothness dilemma of `hypothesis_1` by treating smoothness through explicit spectral truncation rather than blanket exponent degradation.

2. **Plan 2: The Parametric Modulus and Dimension-Dependent Preconstant Approach**
   * *Main idea*: Accepts the finding that smooth kernels maintain optimal exponent $\beta = 1$ for location families (`counterexample_1`), and focuses entirely on quantifying how the dimension-dependent preconstant $c(d)$ dictates sample size and tolerance scaling in high dimensions.
   * *Subgoals*:
     1. **Explicit Preconstant Calculation**: Derive the exact analytical dependence of the identifiability preconstant $c(d)$ in $\mathrm{MMD}(P_0, P_\theta) \ge c(d) \|\theta - \theta_0\|$ on dimension $d$, kernel bandwidth $\gamma$, and parameter type (location vs. scale).
     2. **Tolerance Scaling Trajectory**: Determine the critical threshold curve $\epsilon_n(n, d)$ ensuring that the ABC acceptance probability remains bounded away from zero as $n \to \infty$.
     3. **Parameter Family Generalization**: Test whether scale and shape parameters suffer from degraded exponents $\beta > 1$ under smooth kernels, extending `counterexample_1` beyond location families.
     4. **Minimax Rate Characterization**: Establish minimax upper and lower bounds for MMD-ABC parameter estimation error as explicit functions of $(n, d, \gamma)$.
   * *Plausibility*: Directly respects the rigorous counterexample (`counterexample_1`) which disproved `hypothesis_1`, and isolates the true high-dimensional bottleneck identified in `hypothesis_2`.
   * *Counterexample avoidance*: Directly incorporates `counterexample_1` by discarding the false premise that smooth kernels force $\beta > 1$.

3. **Plan 3: The Generalized Posterior Surrogate and Bandwidth Optimization Approach**
   * *Main idea*: Approximate the hard rejection ABC filter by a smooth generalized posterior (exponential weights) driven by $\mathrm{MMD}^2$, using spectral properties to optimize kernel bandwidth against effective dimension.
   * *Subgoals*:
     1. **Surrogate Bernstein-von Mises Theorem**: Prove asymptotic normality and contraction for the generalized Gibbs posterior $\pi_n(\theta) \propto \pi(\theta) \exp(-\gamma_n n \widehat{\mathrm{MMD}}_n^2)$ using the kernel spectral representation.
     2. **Rejection-to-Surrogate Coupling**: Establish total variation or Wasserstein coupling bounds between the indicator rejection ABC posterior and the surrogate generalized posterior as a function of $\epsilon_n$.
     3. **Bandwidth-Dimension Trade-off**: Optimize the kernel bandwidth parameter (e.g., Gaussian $\gamma$) with respect to sample size $n$ and dimension $d$ by balancing high-frequency damping (`obstacle_3`) and parametric sensitivity.
     4. **Numerical Validation**: Validate the predicted optimal bandwidth scaling and contraction rates on synthetic multivariate Gaussian location-scale models.
   * *Plausibility*: Leverages extensive literature on generalized Bayesian inference, bypassing `obstacle_1` via smoothing and embedding `obstacle_3` into bandwidth selection.
   * *Counterexample avoidance*: Bypasses the stiffness of indicator functions (`obstacle_1`) while respecting the effective dimension inflation caused by Mercer spectral decay (`obstacle_3`).

## Obstacles

* **Subgoal 1.3 & 1.4 (Small-ball probability under MMD)**: Lower bounding small-ball probabilities for empirical MMD with non-Gaussian reference measures is notoriously difficult because MMD is a sum of dependent dependent variables (squared RKHS norms of empirical measures).
* **Subgoal 2.1 (Exact Preconstant Scaling)**: Computing explicit constants $c(d)$ for non-Gaussian kernels or non-location families requires delicate harmonic analysis on compact or Euclidean domains, and precise tail bounds on infinite series of eigenvalues.
* **Subgoal 3.2 (Rejection-to-Surrogate Coupling)**: Proving that the hard indicator cutoff $I(\widehat{\mathrm{MMD}}_n \le \epsilon_n)$ closely approximates the exponential weight posterior in TV distance requires non-trivial anti-concentration inequalities for empirical MMD.
* **Missing Information**: Precise lower bounds on the local modulus of continuity $\mathrm{MMD}(P_\theta, P_0)$ for scale and shape families under Gaussian and Matérn kernels in $\mathbb{R}^d$ remain unproven beyond the Gaussian location case (`counterexample_1`).

## Suggested next steps

1. **Derive explicit analytical expressions for $c(d)$** in the identifiability modulus for simple scale families (e.g., variance of $\mathcal{N}(0, \sigma^2 I_d)$) under Gaussian and Matérn kernels to check if $\beta$ remains $1$ or degrades.
2. **Formalize Subgoal 1.1** by computing the truncation tail sum $\sum_{j > K_n} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ explicitly for Mercer eigenvalues of Gaussian kernels on bounded domains or $\mathbb{R}^d$.
3. **Execute Subgoal 3.3 (Bandwidth Optimization)**: Set up a formal optimization problem minimizing the sum of squared bias (from spectral truncation) and variance (from RKHS effective dimension) with respect to the kernel bandwidth $\gamma$.

---

## Finding #46: task_50 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_50` | Duration: 22.2s | Timestamp: 2026-09-09 11:41:21 UTC | Focus Nodes: `counterexample_1`, `hypothesis_2`*

**Assigned Task Prompt**:
> Analyze the scale family $P_\sigma = \mathcal{N}(0, \sigma^2 I_d)$ on $\mathbb{R}^d$ with the Gaussian kernel $k(x,y) = \exp(-\gamma \|x-y\|^2)$. Compute the Fourier-domain representation of $\mathrm{MMD}^2(P_1, P_\sigma)$ to determine whether a non-location parameter family suffers from severe identifiability loss (exponent $\beta > 1$) or if the dimension dependence remains concentrated in the preconstant $c$.

**Worker Output & Derivations**:

e^{-i\omega \cdot z} e^{-\gamma \|z\|^2} dz$ or similar? Let's check the normalization).
Usually, the Parseval/Plancherel identity gives:
$\int_{\mathbb{R}^d} \psi(x-y) dP(x) dQ(y) = \int_{\mathbb{R}^d} \hat{P}(\omega) \overline{\hat{Q}(\omega)} \Lambda(d\omega)$ where $\Lambda$ is the spectral measure.
Specifically, for $k(x,y) = \exp(-\gamma \|x-y\|^2)$, we can write:
$k(x,y) = (4\pi \gamma)^{-d/2} \int_{\mathbb

---

## Finding #47: task_52 (Searcher)

*Worker: **searcher** | Task ID: `task_52` | Duration: 24.3s | Timestamp: 2026-09-09 11:41:52 UTC | Focus Nodes: `paper_1`, `paper_4`*

**Assigned Task Prompt**:
> Search literature for results regarding 'parameter sensitivity', 'identifiability', or 'lower bounds' on the maximum mean discrepancy (MMD) in parameter estimation contexts (e.g., minimum distance estimators). Look for studies characterizing the exponent $\beta$ or constant $c$ in terms of kernel properties.

**Worker Output & Derivations**:

_0}}[k(X,Y)] ) ]$.
Let $f_\theta(x) = \mathbb{E}_{X' \sim P_\theta}[k(x,X')] - \mathbb{E}_{Y \sim P_{\theta_0}}[k(x,Y)]$. Note that at $\theta = \theta_0$, $f_{\theta_0}(x) = 0$ for all $x$.
So when we differentiate $G(\theta) = 2 \mathbb{E}_{X \sim P_\theta}[ s_\theta(X) f_\theta(X) ]$ with respect to $\theta$, the only term that survives at $\theta = \theta_0$ is the one where the derivative falls on $f_\

---

## Finding #48: task_54 (Sketcher)

*Worker: **sketcher** | Task ID: `task_54` | Duration: 30.5s | Timestamp: 2026-09-09 11:42:01 UTC | Focus Nodes: `obstacle_2`, `obstacle_1`*

**Assigned Task Prompt**:
> Quantify the required scaling of the simulation size m relative to the observation size n in MMD-ABC. Using the concentration bounds of the two-sample empirical MMD, find the precise condition on the growth rate of m = m(n) such that the simulation-induced variance does not dominate the overall ABC posterior contraction rate. Address how this affects the computational complexity of the rejection algorithm as n tends to infinity.

**Worker Output & Derivations**:

## Findings

1. **Two-Sample MMD Deviation Bounds and Noise Decomposition**  
   *Status: Solved (sketch included).*  
   Let $\mathcal{H}$ be an RKHS with bounded kernel $\sup_{x \in \mathcal{X}} k(x,x) \le K < \infty$. For observed data $X_{1:n} \sim P_0$ and simulated data $Y_{1:m} \sim P_\theta$, the empirical mean embeddings are $\widehat{\mu}_n = \frac{1}{n}\sum_{i=1}^n k(X_i, \cdot)$ and $\widehat{\mu}_{\theta,m} = \frac{1}{m}\sum_{j=1}^

---

## Finding #49: task_55 (Sketcher)

*Worker: **sketcher** | Task ID: `task_55` | Duration: 45.6s | Timestamp: 2026-09-09 11:43:51 UTC | Focus Nodes: `lemma_1`, `obstacle_4`, `hypothesis_2`*

**Assigned Task Prompt**:
> Derive the Hessian H(\theta_0) = \nabla_\theta^2 \mathrm{MMD}^2(P_0, P_\theta) at \theta=\theta_0 for a parametric family P_\theta with a translation-invariant kernel k(x-y) = \int e^{i \omega \cdot (x-y)} d\Lambda(\omega). Express H(\theta_0) in terms of the spectral measure \Lambda and the derivatives of the characteristic function of P_\theta. Analyze how the decay rate of \Lambda(\omega) (e.g., Gaussian vs. Matern) affects the eigenvalues of H(\theta_0) and consequently the volume of the ABC acceptance region.

**Worker Output & Derivations**:

## Findings

1. **Exact Derivation of the Hessian $H(\theta_0)$ via Characteristic Functions**: 
   For a translation-invariant kernel $k(x-y) = \int_{\mathbb{R}^d} e^{i \omega \cdot (x-y)} d\Lambda(\omega)$ with spectral measure $\Lambda$, the squared MMD between $P_0$ and $P_\theta$ can be expressed via their characteristic functions $\varphi_0(\omega) = \int e^{i \omega \cdot x} dP_0(x)$ and $\varphi_\theta(\omega) = \int e^{i \omega \cdot x} dP_\theta(x)$ as:
   $$\text{MMD}^2(P_

---

## Finding #50: task_57 (Sketcher)

*Worker: **sketcher** | Task ID: `task_57` | Duration: 22.3s | Timestamp: 2026-09-09 11:44:35 UTC | Focus Nodes: `idea_1`, `obstacle_1`, `lemma_1`*

**Assigned Task Prompt**:
> Formalize the small-ball probability bound for the ABC rejection indicator P(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2 \mid P_0) using the spectral truncation approach from idea_1. Explicitly bound the empirical term in terms of the top K_n eigenvalues and the tail truncation error.

**Worker Output & Derivations**:

## Findings

1. **Exact Spectral Representation of Empirical Squared MMD**: **[Status: Solved (sketch included)]**
   Let $P_0$ and $P_\theta$ be probability measures on $\mathcal{X} \subset \mathbb{R}^d$, and let $k: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ be a continuous, symmetric, positive definite kernel. By Mercer's Theorem (or the spectral theorem for compact self-adjoint operators), the integral operator $T_k: L^2(P_0) \to L^2(P_0)$ defined by $(T_k f)(x) = \int k(x, y) f(y) dP_0

---

## Finding #51: task_59 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_59` | Duration: 31.9s | Timestamp: 2026-09-09 11:44:43 UTC | Focus Nodes: `lemma_1`, `obstacle_3`, `obstacle_4`*

**Assigned Task Prompt**:
> Compute the exact population MMD^2 and its Hessian H(\theta_0) for a Matérn kernel or Gaussian kernel in 1D vs dimension d, explicitly showing how smoothness parameter s and dimension d affect the eigenvalue decay of H(\theta_0).

**Worker Output & Derivations**:

MMD^2$ Expression*: State the exact formula for $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$ under the Gaussian kernel $k_\gamma(x,y) = \exp(-\gamma\|x-y\|^2)$.
        2. *Exact Hessian at $\theta_0 = 0$*: Derive $H(0) = \frac{4\gamma}{(1 + 4\gamma)^{d/2 + 1}} I_d$.
        3. *Exponential Decay of Hessian Eigenvalues with Dimension*: Show how $\lambda_{\min}(H(0)) = \lambda_{\max}(H(0)) = \frac{4\gamma}{(1 +

---

## Finding #52: task_58 (Counterexample)

*Worker: **counterexample** | Task ID: `task_58` | Duration: 33.9s | Timestamp: 2026-09-09 11:45:00 UTC | Focus Nodes: `hypothesis_2`, `obstacle_4`, `hypothesis_1`*

**Assigned Task Prompt**:
> Test hypothesis_2 (Dimension-Dependent Preconstant Curse) and obstacle_4: construct a parametric model where the Hessian eigenvalues decay rapidly enough with dimension that the ABC prior acceptance volume shrinks exponentially faster than the empirical convergence rate, causing posterior inconsistency for fixed tolerance.

**Worker Output & Derivations**:

## Findings

1. **Exact MMD and Hessian for Gaussian Location Family:** Let $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$ on $\mathbb{R}^d$, with a Gaussian kernel $k(x,y) = \exp(-\gamma \|x-y\|^2)$. Using closed-form Gaussian expectations, the population squared MMD is explicitly:
   $$\mathrm{MMD}^2(P_0, P_\theta) = 2 (1 + 4\gamma)^{-d/2} \left[ 1 - \exp\left(-\frac{\gamma \|\theta\|^2}{4\gamma + 1}\right) \right].$$

---

## Finding #53: task_62 (Sketcher)

*Worker: **sketcher** | Task ID: `task_62` | Duration: 25.1s | Timestamp: 2026-09-09 11:45:07 UTC | Focus Nodes: `idea_1`, `obstacle_1`, `lemma_1`*

**Assigned Task Prompt**:
> Derive the small-ball probability bound for the ABC rejection indicator using the spectral truncation approach of idea_1, balancing estimation variance in the first $K_n$ components against truncation error.

**Worker Output & Derivations**:

## Findings

1. **Subgoal status: partial.** We can construct a rigorous decomposition of the empirical squared MMD using its Mercer spectral representation, splitting it into a finite-dimensional parametric component ($j \le K_n$) and an infinite-dimensional tail component ($j > K_n$), which allows us to control the small-ball probability by balancing estimation variance against truncation error.

2. **Mercer Spectral Representation and Truncation:** Let $k(x,y) = \sum_{j=1}^\infty \lambda_j \phi_j(x) \phi_j(y)$ be the Mercer expansion of the kernel with respect to the reference measure $P_0$, where $\lambda_1 \ge \lambda_2 \ge \dots > 0$ are eigenvalues and $\{\phi_j\}_{j=1}^\infty$ are orthonormal in $L^2(P_0)$. The squared empirical MMD between the observed sample empirical measure $\hat{P}_n$ and simulated sample empirical measure $\hat{Q}_{m,\theta}$ is given by:
   $$\widehat{\text{MMD}}_n^2 = \sum_{j=1}^\infty \lambda_j \left( \hat{\mu}_{n,j} - \hat{\nu}_{m,j} \right)^2$$
   where $\hat{\mu}_{n,j} = \frac{1}{n} \sum_{i=1}^n \phi_j(X_i)$ and $\hat{\nu}_{m,j} = \frac{1}{m} \sum_{l=1}^m \phi_j(Y_l)$ with $X_i \sim P_0$ and $Y_l \sim P_\theta$.

3. **Decomposition into Principal and Tail Sums:** For any truncation level $K_n$, we write $\widehat{\text{MMD}}_n^2 = S_{K_n} + R_{K_n}$, where:
   $$S_{K_n} = \sum_{j=1}^{K_n} \lambda_j \left( \hat{\mu}_{n,j} - \hat{\nu}_{m,j} \right)^2, \quad R_{K_n} = \sum_{j=K_n+1}^\infty \lambda_j \left( \hat{\mu}_{n,j} - \hat{\nu}_{m,j} \right)^2$$
   The tail $R_{K_n}$ is non-negative and represents the high-frequency discrepancy. Its expectation under $P_0 \times P_\theta$ is bounded by:
   $$\mathbb{E}[R_{K_n}] = \sum_{j=K_n+1}^\infty \lambda_j \left( \frac{\sigma_{0,j}^2}{n} + \frac{\sigma_{\theta,j}^2}{m} + (\mu_{0,j} - \mu_{\theta,j})^2 \right)$$
   Since $\sum_{j=1}^\infty \lambda_j \sigma_{0,j}^2 = \mathbb{E}_{P_0}[k(X,X)] - \int \dots$ is finite (bounded by $\sup_x k(x,x)$), the variance contribution of the tail decays as $\sum_{j=K_n+1}^\infty \lambda_j / n$.

4. **Bounding the Small-Ball Probability:** To bound $\mathbb{P}_\theta \left( \widehat{\text{MMD}}_n^2 \le \varepsilon_n^2 \right)$, we use the inequality:
   $$\mathbb{P}_\theta \left( S_{K_n} + R_{K_n} \le \varepsilon_n^2 \right) \le \mathbb{P}_\theta \left( S_{K_n} \le \varepsilon_n^2 \right) + \mathbb{P}_\theta \left( R_{K_n} > c_n \right)$$
   for any threshold $c_n$ (by choosing $R_{K_n} \le \varepsilon_n^2 - S_{K_n}$, but more simply via Markov's inequality on the tail or bounding $R_{K_n}$ deterministically/probabilistically). Alternatively, using Markov's inequality for the positive tail: $\mathbb{P}_\theta(R_{K_n} > \delta_n) \le \frac{\mathbb{E}[R_{K_n}]}{\delta_n}$.

5. **Controlling the Principal Sum $S_{K_n}$:** The principal sum $S_{K_n}$ is a quadratic form in empirical means. Under $P_\theta$, the vector $\hat{\nu}_{m}$ has mean $\mu_\theta$ and covariance operator with eigenvalues $\lambda_j$. The term $S_{K_n}$ follows a non-central chi-squared-type distribution. By choosing $\varepsilon_n^2$ and the parameter distance $\|\theta - \theta_0\|$ such that the population principal sum $\sum_{j=1}^{K_n} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ is comparable to $\varepsilon_n^2$, we can apply anti-concentration inequalities (e.g., extensions of Borell's inequality or Gaussian chaos concentration) to bound $\mathbb{P}_\theta(S_{K_n} \le \varepsilon_n^2)$ from above by a quantity depending on the signal-to-noise ratio in the first $K_n$ components.

## Obstacles

1. **Cross-talk between Truncation Level $K_n$ and Tolerance $\varepsilon_n$:** If $K_n$ grows too fast with $n$, the variance of the principal sum $S_{K_n}$ (which scales roughly with $\sum_{j=1}^{K_n} \lambda_j^2 / n$ or similar terms depending on the exact coordinates) blows up, making $\mathbb{P}_\theta(S_{K_n} \le \varepsilon_n^2)$ too small or uncontrolled. If $K_n$ grows too slowly, the truncation error $\sum_{j=K_n+1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ exceeds $\varepsilon_n^2$, making the event $\widehat{\text{MMD}}_n^2 \le \varepsilon_n^2$ empty or exponentially rare.
2. **Non-centrality and Anti-Concentration:** Standard chi-squared anti-concentration bounds require precise control over the weights $\lambda_j$ and the non-centrality parameter $\Delta_j = (\mu_{0,j} - \mu_{\theta,j})^2$. For smooth kernels (exponential decay of $\lambda_j$), the higher components in $S_{K_n}$ carry very little weight $\lambda_j$, rendering them ineffective for capturing parameter deviations $\|\theta - \theta_0\|$, yet they still accumulate estimation noise. This manifests the spectral ill-posedness directly in the probability bound.

## Suggested next steps

1. **Explicit Variance Calculation of $S_{K_n}$:** Compute the exact variance $\text{Var}(S_{K_n})$ under Gaussian assumptions on $\phi_j$ to explicitly reveal how $K_n$ depends on the dimension $d$ and kernel smoothness $s$.
2. **Apply Anti-Concentration for Quadratic Forms:** Adapt Theorem 1 from Giné and Nickl (or similar literature on Gaussian/empirical process chaos) to lower-bound the small-ball probability of weighted $\ell_2$ norms of empirical means.
3. **Optimize $K_n$ as a Function of $n$ and $d$:** Balance the truncation error bound $\sum_{j=K_n+1}^\infty \lambda_j \Delta_j \lesssim K_n^{-2s/d} \|\theta - \theta_0\|^2$ against the estimation variance $K_n / n$ to find the optimal scaling of $K_n$ and the resulting lower bound on the ABC denominator.

---

## Finding #54: task_61 (Sketcher)

*Worker: **sketcher** | Task ID: `task_61` | Duration: 25.1s | Timestamp: 2026-09-09 11:45:20 UTC | Focus Nodes: `lemma_1`, `obstacle_4`*

**Assigned Task Prompt**:
> Formalize the relationship between kernel integral operator eigenvalues $\lambda_j$ and the eigenvalues of the Hessian $H(\theta_0)$ of $\text{MMD}^2$, analyzing how rapid eigenvalue decay flattens population MMD in high-frequency directions as described in obstacle_4 and lemma_1.

**Worker Output & Derivations**:

\lambda_{\min}(H(\theta_0)) \|\theta - \theta_0\|^2 + o(\|\theta - \theta_0\|^2)$. Because $\lambda_j$ decays rapidly with $j$, if the parameter family $\theta \mapsto P_\theta$ induces variations that couple significantly with high-index eigenfunctions $\psi_j$ for large $j$, $\lambda_{\min}(H(\theta_0))$ is driven close to zero. This manifests as a severe flattening of the population MMD profile around $\theta_0$, explaining the severe parameter sensitivity loss (or extreme dimension-dependent preconstant degradation) in smooth kernel MMD-ABC.

## Obstacles
1. **Interaction Between Parameterization and Eigenbasis**:
   While the score cross-cov

---

## Finding #55: task_64 (Sketcher)

*Worker: **sketcher** | Task ID: `task_64` | Duration: 14.7s | Timestamp: 2026-09-09 11:45:30 UTC | Focus Nodes: `obstacle_2`, `approach_2`*

**Assigned Task Prompt**:
> Draft a proof sketch for the degenerate U-statistic deviation bound of empirical MMD^2 incorporating sample size asymmetry n and m, following Plan 2, Subgoal 1 from the decomposer report.

**Worker Output & Derivations**:

## Findings

1. **Hoeffding-type decomposition of the empirical MMD squared estimator:** 
   **Status:** solved (sketch included)
   Let $X_1, \dots, X_n \sim P_0$ and $Y_1, \dots, Y_m \sim P_\theta$ be independent samples. Define the kernelized kernel function as $h((x,y), (x',y')) = k(x,x') + k(y,y') - k(x,y') - k(x',y)$. The biased empirical squared MMD is a V-statistic (or U-statistic up to diagonal terms) of the form $\widehat{\text{MMD}}^2 = \frac{1}{n^2} \sum_{i,j} k(X_i, X_j) + \frac{1}{m^2} \sum_{i,j} k(Y_i, Y_j) - \frac{2}{nm} \sum_{i,j} k(X_i, Y_j)$. By standard Hoeffding decomposition for two-sample U-statistics, $\widehat{\text{MMD}}^2 - \text{MMD}^2$ decomposes orthogonally into a sum of a linear term of order $O_p(n^{-1/2} + m^{-1/2})$ (governed by first-order projections $\mathbb{E}_{Y}[k(X, Y)]$ and $\mathbb{E}_{X}[k(X, Y)]$) and a degenerate quadratic U-statistic (chaos process) of order $O_p(n^{-1} + m^{-1} + (nm)^{-1/2})$.

2. **Spectral representation of the degenerate quadratic component via Mercer's theorem:** 
   **Status:** solved (sketch included)
   Using the spectral expansion of the kernel $k(x,x') = \sum_{j=1}^\infty \lambda_j \phi_j(x)\phi_j(x')$ with orthonormal eigenfunctions $\phi_j$ in $L^2(P_0)$ and eigenvalues $\lambda_j$, the degenerate quadratic part of the U-statistic under $P_0 = P_\theta$ expands as $\sum_{j=1}^\infty \lambda_j \left( \frac{1}{n} \sum_{i=1}^n \phi_j(X_i) - \mathbb{E}[\phi_j] \right)^2$. Each term in the sum is a centered squared empirical mean of variance $\lambda_j / n$. Summing these up shows that the variance of the degenerate U-statistic is controlled by $\frac{1}{n^2} \sum_{j=1}^n \lambda_j^2 = \frac{1}{n^2} \text{Tr}(K^2)$, where $\text{Tr}(K) = \sum \lambda_j = \mathbb{E}[k(X,X)]$ is the trace (total kernel mass), which is independent of dimension $d$ if $\sup_x k(x,x) < \infty$.

3. **Decoupling and Exponential Tail Bounds via Chaos Inequality:** 
   **Status:** partial
   To obtain non-asymptotic deviation bounds $\mathbb{P}(|\widehat{\text{MMD}}^2 - \text{MMD}^2| > t)$, we apply the decoupling inequality for U-processes (Giné & Zinn, de la Peña & Giné) to reduce the quadratic form in dependent variables to a linear form in independent copies $(X_i, X_i')$. For the decoupled sum, Talagrand's concentration inequality for empirical processes or Bernstein-type inequalities for chaos processes yields a tail bound of the form:
   $$\mathbb{P}\left(|\widehat{\text{MMD}}^2 - \text{MMD}^2| > t\right) \le 2 \exp\left( -c \min\left( \frac{n t^2}{\sigma^2}, \frac{n t}{M} \right) \right)$$
   where the variance proxy $\sigma^2 = \sum \lambda_j^2$ is bounded by $\sup_x k(x,x) \sum \lambda_j = \sup_x k(x,x)^2$, and the sub-exponential bound $M = \sup_{x,y} |k(x,y)|$. When $n \neq m$, the tail bounds combine the rates from both samples, scaling as $\min(n, m)^{-1/2}$ for the linear dominant term and $\min(n, m)^{-1}$ for the degenerate quadratic term.

## Obstacles

1. **Asymmetric Sample Size Bottleneck ($n$ vs $m$):** In ABC, the observed sample size $n$ is typically small and fixed, whereas the simulated sample size $m$ can be chosen to be very large ($m \gg n$). While the total variance of the linear term is controlled by $\frac{1}{n} + \frac{1}{m}$, the cross-covariance terms and higher-order degenerate terms involving $m$ introduce dependencies on the geometry of the simulation model $P_\theta$ that do not vanish simply by taking $m \to \infty$, because the estimator's bias-variance profile along high-frequency eigenfunctions $\phi_j$ depends on the ratio $n/m$.
2. **Transition from Non-Degenerate to Degenerate Regimes near $\theta_0$:** When evaluating the acceptance region $\widehat{\text{MMD}}^2(P_n, P_{\theta,m}) \le \epsilon_n^2$, the true parameter $\theta_0$ yields $P_0 = P_\theta$, making the quadratic term strictly degenerate (following an infinite weighted mixture of centered $\chi^2$ variables, i.e., a Rosenblatt-type distribution). Away from $\theta_0$, the non-zero population $\text{MMD}^2(P_0, P_\theta)$ dominates, shifting the fluctuation statistics from sub-exponential/chi-squared mixture to asymptotically Gaussian. Uniformly controlling this transition across parameter space $\Theta$ for ABC rejection is non-trivial.

## Suggested next steps

1. **Derive explicit exponential tail constants:** Apply the Laplace transform method (Chernoff bounding) directly to the chaos decoupling sum to extract explicit dependence of the tail constants on the Mercer eigenvalues $\lambda_j$ and kernel uniform bound $\sup k(x,x)$.
2. **Analyze sample-size asymmetry scaling:** Quantify the exact trade-off when $m = O(n^\gamma)$ for $\gamma > 1$ in the empirical MMD variance expansion to see whether increasing simulated data $m$ indefinitely can mitigate the curse of dimensionality in $\lambda_j$.
3. **Bound the small-ball probability for ABC rejection:** Use the derived U-statistic deviation bounds to explicitly evaluate the probability $\mathbb{P}_{\theta}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$ entering the ABC posterior denominator, incorporating the local Hessian structure of population MMD.

---

## Finding #56: task_63 (Searcher)

*Worker: **searcher** | Task ID: `task_63` | Duration: 15.8s | Timestamp: 2026-09-09 11:45:39 UTC | Focus Nodes: `obstacle_2`, `approach_2`*

**Assigned Task Prompt**:
> Search literature for uniform concentration bounds and deviation inequalities for empirical MMD as degenerate U-statistics, specifically addressing sample size asymmetry between observed n and simulated m.

**Worker Output & Derivations**:

## Findings

1. **McDiarmid-Based Non-Asymptotic Concentration for MMD with Asymmetric Sample Sizes**
   **Summary:** Gretton et al. (2012) established general non-asymptotic deviation inequalities for empirical MMD using McDiarmid's bounded difference inequality, explicitly accommodating different sample sizes $n$ (observed) and $m$ (simulated).
   *Statement:* Let $X_1, \dots, X_n \stackrel{i.i.d.}{\sim} P$ and $Y_1, \dots, Y_m \stackrel{i.i.d.}{\sim} Q$ take values in a space $\mathcal{X}$, and let $k: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ be a measurable kernel satisfying $\sup_{x} k(x,x) \le K < \infty$. Then for any $\delta >0$, with probability at least $1 - \delta$,
   $$\left| \widehat{\mathrm{MMD}}_b(X_n, Y_m, P, Q) - \mathrm{MMD}(P, Q) \right| \le 2 \left( \sqrt{K \left( \frac{1}{n} + \frac{1}{m} \right)} + \sqrt{\frac{K}{n}} + \sqrt{\frac{K}{m}} \right) + 4 \sqrt{\frac{2 \log(2/\delta)}{n}} + \dots$$
   (specifically, the bound scales as $O\left(\frac{1}{\sqrt{n}} + \frac{1}{\sqrt{m}}\right)$).
   *Hypotheses:* Bounded kernel $\sup_x k(x,x) \le K$ almost everywhere.
   *Proof technique:* Bounded difference property of the V-statistic/U-statistic estimator under replacement of a single observation, combined with McDiarmid's inequality. 
   *Source:* Gretton, Borgwardt, Rasch, Schölkopf, & Smola (2012), "A Kernel Two-Sample Test", *JMLR*.

2. **Degenerate U-Statistic Tail Bounds via Hoeffding Decomposition**
   **Summary:** When $P = Q$ (or in ABC, locally near $\theta$ where $P_\theta \approx P_0$), the linear terms in the Hoeffding decomposition of the MMD U-statistic vanish, rendering it a *degenerate* U-statistic of order 2. Tail bounds must account for the infinite sum of chi-squared components rather than standard Gaussian concentration.
   *Statement:* Following Arcones & Giné (1993) and Giné, Nickl, & Weber (2012) for degenerate U-statistics of order 2, the empirical squared MMD under degeneracy satisfies:
   $$\mathbb{P}\left( n \left( \widehat{\mathrm{MMD}}^2(X_n, X_n') - \mathbb{E}[\widehat{\mathrm{MMD}}^2] \right) > t \right) \le C \exp\left( -c \min\left( \frac{t}{\lambda_1}, \sqrt{\frac{t}{\sum_{j>1} \lambda_j^2}} \right) \right)$$
   where $\lambda_j$ are the eigenvalues of the kernel integral operator.
   *Hypotheses:* The kernel $k$ is $L_2(P)$-integrable, and the underlying distributions satisfy the degeneracy condition (or local null).
   *Proof technique:* Spectral expansion of the U-statistic kernel via Mercer's theorem into orthogonal chaos components, applying decoupling inequalities and exponential tail bounds for quadratic forms in Gaussian/sub-Gaussian variables.
   *Source:* Arcones & Giné (1993), "Limit theorems for U-processes", *Ann. Probab.*; Giné, Nickl, & Weber (2012), "Nonasymptotic tail bounds for degenerate U-statistics".

3. **Asymmetric Sample Size Variance Decomposition for Two-Sample U-Statistics**
   **Summary:** Serfling (1980) and Korolyuk & Borovskich (1994) provide exact variance formulas for two-sample U-statistics with asymmetric sample sizes $n$ and $m$, showing how the variance is split between the two margins.
   *Statement:* For an unbiased two-sample U-statistic $U_{n,m}$ with kernel $h(X_i, Y_j)$, the variance decomposes as:
   $$\mathrm{Var}(U_{n,m}) = \frac{1}{n} \zeta_{1,0} + \frac{1}{m} \zeta_{0,1} + \frac{2}{nm} \zeta_{1,1}$$
   where $\zeta_{1,0} = \mathbb{🇻}[\mathbb{E}[h(X, Y) | X]]$ and $\zeta_{0,1} = \mathbb{🇻}[\mathbb{E}[h(X, Y) | Y]]$ are the variances of the projections (first-order Hoeffding components).
   *Hypotheses:* $h$ is symmetric and square-integrable with respect to $P \times Q$.
   *Proof technique:* Projection method (Hájek projection) for U-statistics.
   *Source:* Serfling, R. J. (1980), *Approximation Theorems of Mathematical Statistics*, Wiley; Korolyuk & Borovskich (1994), *Theory of U-Statistics*.

4. **Uniform Parameter-Space Concentration for Metric Entropies**
   **Summary:** To lift pointwise concentration bounds to uniform bounds over $\theta \in \Theta$ for ABC, empirical process theory requires bracketing entropy or Rademacher complexity bounds for the family of kernel sections $\{k(x, \cdot) : \theta \in \Theta\}$.
   *Statement:* If $\Theta$ is compact and the map $\theta \mapsto P_\theta$ is Lipschitz continuous in total variation or Wasserstein distance, and the kernel $k$ is continuously differentiable up to order $r$, then the bracketing entropy $\log N_{[\ ]}(\epsilon, \mathcal{F}, L_2(P))$ grows polynomially in $1/\epsilon$, enabling uniform deviation bounds of order $O_p(n^{-1/2} + m^{-1/2})$ independent of $\theta$.
   *Hypotheses:* Smoothness of $P_\theta$ with respect to $\theta$, boundedness and smoothness of $k$.
   *Proof technique:* Dudley's entropy integral bound combined with chaining empirical processes.
   *Source:* Christmann & Steinwart (2010), *Support Vector Machines*, Springer; van der Vaart & Wellner (1996), *Weak Convergence and Empirical Processes*.

## Obstacles

1. **Failure of McDiarmid under Degeneracy:** McDiarmid's inequality yields a suboptimal parametric rate $O(n^{-1/2})$ for the tail bounds when applied blindly to MMD, failing to capture the $O(n^{-1})$ variance decay under the null or near the true parameter $\theta_0$ (where $\mathrm{MMD}(P_0, P_\theta) = 0$). This overestimates the small-ball probability $\mathbb{P}(\widehat{\mathrm{MMD}}^2 \le \epsilon_n^2)$ in ABC.
2. **Asymmetry Mismatch in Simulation Budgets ($m \gg n$):** While making $m$ (simulated size) very large reduces the $\frac{1}{m} \zeta_{0,1}$ term in the Serfling variance decomposition, the observed sample size $n$ remains fixed in standard ABC asymptotic frameworks ($n \to \infty$ with $m \to \infty$, or $n$ fixed and $m \to \infty$). When $n$ is fixed, the convergence rate is fundamentally bottlenecked by $\frac{1}{n} \zeta_{1,0}$, meaning infinite simulation budget $m \to \infty$ cannot eliminate the $O_p(n^{-1/2})$ error induced by the finite observed data $n$.
3. **Uniformity Breakdown via Eigenvalue Decay:** As noted in the problem context, spectral decay $\lambda_j \sim j^{-2s/d}$ means high-frequency components have very small eigenvalues. Uniform deviation bounds $\sup_{\theta} |\widehat{\mathrm{MMD}}^2 - \mathrm{MMD}^2|$ can be loose because the empirical estimator of high-frequency components has high variance relative to their population magnitude, unless heavily regularized or truncated.

## Suggested next steps

1. Query literature for: `concentration inequalities for degenerate two sample U-statistics empirical process`
2. Query literature for: `uniform consistency maximum mean discrepancy parameter estimation rates`
3. Query literature for: `Hoeffding decomposition two sample U-statistics asymmetric sample sizes`
4. Investigate whether the small-ball probability $\mathbb{P}\left(\widehat{\mathrm{MMD}}^2(X_n, Y_{m,\theta}) \le \epsilon_n^2 \right)$ can be explicitly computed using the saddlepoint approximation or large deviations for quadratic forms of Gaussian processes, adapting Arcones & Giné (1993).

---

## Finding #57: task_65 (Counterexample)

*Worker: **counterexample** | Task ID: `task_65` | Duration: 13.2s | Timestamp: 2026-09-09 11:45:49 UTC | Focus Nodes: `lemma_2`, `obstacle_4`, `hypothesis_2`*

**Assigned Task Prompt**:
> Construct a specific parametric model and smooth kernel where the ABC acceptance denominator P(MMD^2_hat <= epsilon_n^2) vanishes exponentially faster than the prior mass due to the Hessian degeneracy established in lemma_2.

**Worker Output & Derivations**:

## Findings

1. **Exact MMD Formula for Gaussian Location Families**: For $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$ under a Gaussian kernel $k_h(x,y) = \exp(-\|x-y\|^2 / (2h^2))$, the squared population MMD is calculated analytically as:
   $$\mathrm{MMD}^2(P_0, P_\theta) = 2 \left(\frac{h^2}{2+h^2}\right)^{d/2} \left[ 1 - \exp\left( - \frac{\\|\theta\\|^2}{2(h^2+2)} \right)

---

## Finding #58: task_66 (Sketcher)

*Worker: **sketcher** | Task ID: `task_66` | Duration: 13.6s | Timestamp: 2026-09-09 11:45:59 UTC | Focus Nodes: `idea_1`, `lemma_2`, `obstacle_1`*

**Assigned Task Prompt**:
> Combine idea_1 (Spectral Truncation) and lemma_2 to derive a rigorous lower bound for the ABC small-ball probability P(MMD^2_hat <= epsilon_n^2 | theta) as a function of the truncation level K_n and sample size n.

**Worker Output & Derivations**:

## Findings

1. **Subgoal: Rigorous Lower Bound for ABC Small-Ball Probability via Spectral Truncation** (Status: **partial**)
   * *Spectral Expansion & Truncation:* Let the empirical squared MMD between $P_0$ (sample size $n$) and $P_\theta$ (sample size $m$) be expressed in the eigenbasis $\{\phi_j\}_{j=1}^\infty$ of the integral operator associated with kernel $k$ under $P_0$, with eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots > 0$. The squared RKHS distance is:
     $$\|\hat{\mu}_0 - \hat{\mu}_\theta\|_{\mathcal{H}}^2 = \sum_{j=1}^\infty \lambda_j (\hat{\mu}_{0,j} - \hat{\mu}_{\theta,j})^2$$
     We truncate this sum at level $K_n$:
     $$\|\hat{\mu}_0 - \hat{\mu}_\theta\|_{\mathcal{H}}^2 = S_{n, K_n} + R_{n, K_n}, \quad \text{where } S_{n, K_n} = \sum_{j=1}^{K_n} \lambda_j (\hat{\mu}_{0,j} - \hat{\mu}_{\theta,j})^2, \quad R_{n, K_n} = \sum_{j > K_n} \lambda_j (\hat{\mu}_{0,j} - \hat{\mu}_{\theta,j})^2.$$
   * *Lower Bound via Intersection:* To bound $\mathbb{P}_\theta\left(\|\hat{\mu}_0 - \hat{\mu}_\theta\|_{\mathcal{

---

## Finding #59: task_67 (Sketcher)

*Worker: **sketcher** | Task ID: `task_67` | Duration: 10.1s | Timestamp: 2026-09-09 11:46:19 UTC | Focus Nodes: `idea_1`, `lemma_1`, `obstacle_4`*

**Assigned Task Prompt**:
> Draft a rigorous proof sketch for the ABC rejection small-ball probability lower bound using the spectral truncation method in idea_1, controlling the tail sum lambda_j for j > K_n.

**Worker Output & Derivations**:

## Findings

1. **Subgoal Status: Partial**
   **Spectral Truncation Decomposition of Empirical MMD**: Let $P_0$ be the true data-generating distribution and $P_\theta$ the target model. Let $k$ be a positive definite kernel with orthonormal eigenfunctions $\{\phi_j\}_{j=1}^\infty$ and eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots > 0$ under $P_0$. The squared empirical MMD between empirical measures $\hat{P}_n$ (from $n$ samples of $P_0$) and $\hat{Q}_{m, \theta}$ (from $m$ samples of $P_\theta$) can be expanded as:
   $$\widehat{\text{MMD}}_n^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j \left( \hat{\mu}_{0,j} - \hat{\theta}_{m,j} \right)^2$$
   where $\hat{\mu}_{0,j} = \frac{1}{n}\sum_{i=1}^n \phi_j(X_i)$ and $\hat{\theta}_{m,j} = \frac{1}{m}\sum_{l=1}^m \phi_j(Y_{l,\theta})$. For any truncation level $K_n$, we split the sum into a finite low-frequency component and an infinite tail:
   $$\widehat{\text{MMD}}_n^2 = \underbrace{\sum_{j=1}^{K_n} \lambda_j (\hat{\mu}_{0,j} - \hat{\theta}_{m,j})^2}_{\text{Principal component } S_{K_n}} + \underbrace{\sum_{j=K_n+1}^\infty \lambda_j (\hat{\mu}_{0,j} - \hat{\theta}_{m,j})^2}_{\text{Tail component } R_{K_n}}$$

2. **Controlling the Tail Component via Mercer Decay**: 
   The tail component $R_{K_n}$ can be bounded in expectation using the trace of the residual kernel operator. Note that $\mathbb{E}[(\hat{\mu}_{0,j} - \hat{\theta}_{m,j})^2] = \left(\mu_{0,j} - \mu_{\theta,j}\right)^2 + (\frac{1}{n} + \frac{1}{m})\sigma_j^2$, where $\sigma_j^2 \le \sup_x \phi_j(x)^2$ or bounded by constants if the kernel is bounded. Taking expectations of the tail:
   $$\mathbb{E}[R_{K_n}] = \sum_{j=K_n+1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2 + \left(\frac{1}{n} + \frac{1}{m}\right)\sum_{j=K_n+1}^\infty \lambda_j \text{Var}(\phi_j)$$
   Since $\sum_{j=1}^\infty \lambda_j = \mathbb{E}_{X \sim P_0}[k(X,X)] < \infty$, the tail sum of eigenvalues $\sum_{j=K_n+1}^\infty \lambda_j$ is bounded by the tail of the trace. For a Mercer kernel with decay $\lambda_j \sim j^{-2s/d}$, the tail sum is bounded by $\int_{K_n}^\infty x^{-2s/d} dx \sim K_n^{1 - 2s/d}$ (assuming $2s > d$). Thus, by Markov's inequality, $R_{K_n} = O_p(K_n^{1 - 2s/d} + n^{-1} \sum_{j=K_n+1}^\infty \lambda_j)$.

3. **Bounding the Principal Component and Small-Ball Probability**:
   For the finite sum $S_{K_n}$, each term $j \le K_n$ behaves as a scaled non-central chi-squared or Gaussian fluctuation. Using standard concentration in $\mathbb{R}^{K_n}$, we have:
   $$S_{K_n} = \sum_{j=1}^{K_n} \lambda_j \left( (\mu_{0,j} - \mu_{\theta,j}) + O_p\left(\frac{1}{\sqrt{n}}\right) \right)^2 \le 2 \text{MMD}^2(P_0, P_\theta) + O_p\left(\frac{\sum_{j=1}^{K_n} \lambda_j}{n}\right)$$
   To lower bound the ABC rejection small-ball probability $\Pi\left(\theta : \widehat{\text{MMD}}_n^2 \le \epsilon_n^2\right)$, we restrict to a ball $\|\theta - \theta_0\| \le r_n$. By the identifiability lower bound $\text{MMD}^2(P_0, P_\theta) \ge c \|\theta - \theta_0|^{2\beta}$, choosing $K_n$ to balance the truncation error $O(K_n^{1-2s/d})$ with the estimation variance $O(K_n / n)$ yields the optimal bias-variance trade-off for the finite dimensional projection.

## Obstacles

1. **Coupling between Truncation Level $K_n$ and Parameter Dimension $d$**: 
   As the dimension $d$ grows, the Mercer eigenvalue decay $\lambda_j \sim j^{-2s/d}$ flattens. To keep the tail error $K_n^{1-2s/d}$ small, $K_n$ must be chosen exponentially large in $d$, which causes the variance term $\frac{1}{n} \sum_{j=1}^{K_n} \lambda_j \approx \frac{K_n}{n}$ to explode unless $n$ is correspondingly massive. This creates a hard ceiling where spectral truncation fails to control empirical fluctuations in high dimensions.

2. **Uniform Control of Tail Cross-Terms**:
   Bounding $R_{K_n}$ in expectation is straightforward, but controlling its deviation uniformly over a neighborhood of $\theta$ for the ABC acceptance indicator $I(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$ requires Talagrand-type concentration inequalities in the RKHS rather than simple union bounds over $j$, because the tail eigenfunctions can exhibit local peaks that correlate with sample realizations.

## Suggested next steps

1. Formulate a localized concentration inequality for the tail empirical process $\sum_{j > K_n} \lambda_j (\hat{\mu}_{0,j} - \hat{\theta}_{m,j})^2$ using Bernstein-type bounds in Hilbert space.
2. Explicitly solve the optimal choice of $K_n$ as a function of sample size $n$, dimension $d$, and kernel smoothness $s$ to minimize the total error bound $\epsilon_n^2$.
3. Evaluate the prior mass of the ball $\{\theta : \text{MMD}^2(P_0, P_\theta) + R_{K_n} + S_{K_n} \le \epsilon_n^2\}$ using the exact geometry of the Hessian of $\text{MMD}^2$ derived from the top $K_n$ eigenvalues.

---

## Finding #60: task_68 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_68` | Duration: 14.2s | Timestamp: 2026-09-09 11:46:26 UTC | Focus Nodes: `hypothesis_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Compute the exact identifiability modulus exponent beta and empirical rate alpha for Matérn kernels with varying smoothness parameter s in d dimensions, comparing against the Gaussian kernel results.

**Worker Output & Derivations**:

## Findings

1. **Fourier Integral Representation of MMD for Location Families**: Let $P_0 = \mathcal{N}(0, \sigma^2 I_d)$ and $P_\theta = \mathcal{N}(\theta, \sigma^2 I_d)$ in $\mathbb{R}^d$. Using the spectral decomposition of translation-invariant kernels via Bochner's theorem, the squared population MMD can be written as:
   $$\text{MMD}^2(P_0, P_\theta) = \frac{1}{(2\pi)^d} \int_{\mathbb{R}^d} e^{-\sigma^2 \|\omega\|^2} |1 - e^{i \langle \theta, \omega \rangle}|^2 S(\omega) d\omega = \frac{4}{(2\pi)^d} \int_{\mathbb{R}^d} e^{-\sigma^2 \|\omega\|^2} \sin^2\left(\frac{\langle \theta, \omega \rangle}{2}\right) S(\omega) d\omega$$
   where $S(\omega)$ is the spectral density of the kernel. This exact representation allows direct evaluation of both the identifiability modulus and the effect of kernel smoothness.

2. **Exact Identifiability Exponent $\beta = 1$ for Matérn Kernels**: For a Matérn kernel with smoothness parameter $s$, the spectral density decays as $S(\omega) \asymp (1 +\|\omega\|^2)^{-s - d/2}$. For small $\|\theta\|$, expanding $\sin^2(\langle \theta, \omega \rangle / 2) \approx \frac{1}{4} (\langle \theta, \omega \rangle)^2$:
   $$\text{MMD}^2(P_0, P_\theta) \approx \frac{1}{(2\pi)^d} \int_{\mathbb{R}^d} e^{-\sigma^2 \|\omega\|^2} (\langle \theta, \omega \rangle)^2 (1 +\|\omega\|^2)^{-s - d/2} d\omega \asymp \|\theta\|^2 \int_0^\infty r^{d+1} e^{-\sigma^2 r^2} (1+r^2)^{-s - d/2} dr$$
   As long as the integral converges (which requires $s > -1$), the exponent in the identifiability modulus is **$\beta = 1$** universally for all Matérn kernels, contradicting any claim that rougher kernels change the polynomial exponent $\beta$ in simple location models.

3. **Empirical Variance and the Kernel Smoothness Threshold $s > d/4$**: The empirical MMD estimator $\widehat{\text{MMD}}_n^2$ is a degenerate U-statistic whose asymptotic variance is governed by the squared Mercer eigenvalues $\sum_{j=1}^\infty \lambda_j^2$. For Matérn kernels in $d$ dimensions, $\lambda_j \asymp j^{-2s/d}$, meaning the variance sum behaves as $\sum j^{-4s/d}$. This sum converges if and only if **$4s/d > 1$, i.e., $s > d/4$**. 

4. **Breakdown of Standard Rates for Rough Matérn Kernels ($s \le d/4$)**: When $s \le d/4$, the sum $\sum \lambda_j^2 = \infty$, implying that the standard central limit theorem for empirical MMD fails, and the empirical estimator $\widehat{\text{MMD}}_n$ does not concentrate at the parametric rate $O_p(n^{-1/2})$ under standard $L_2$ norm bounds. Instead, it exhibits a slower, non-standard convergence rate $\alpha < 1/2$, explicitly proving that rough kernels pay a heavy price in empirical estimation variance in high dimensions $d$.

5. **Comparison with Gaussian Kernels**: Gaussian kernels have exponential spectral decay $\lambda_j \sim \exp(-c j^{2/d})$, ensuring $\sum \lambda_j^2 < \infty$ for all dimensions $d$ (so $\alpha = 1/2$ always holds). However, as shown in Hypothesis 2, the preconstant of the integral in Finding 2 shrinks exponentially with dimension $d$ when the kernel is too smooth relative to the target's high-frequency variations, shifting the curse of dimensionality from the empirical rate $\alpha$ to the geometric preconstant $c(d)$.

## Obstacles

1. **Restriction to Translation-Invariant Location Families**: The exact Fourier integral calculations rely heavily on the shift-invariance of the location family $\mathcal{

---

## Finding #61: task_70 (Searcher)

*Worker: **searcher** | Task ID: `task_70` | Duration: 10.9s | Timestamp: 2026-09-09 11:46:34 UTC | Focus Nodes: `obstacle_2`, `paper_3`*

**Assigned Task Prompt**:
> Search literature for two-sample U-statistic concentration inequalities and Hoeffding decompositions applied to Maximum Mean Discrepancy or kernel-based two-sample tests.

**Worker Output & Derivations**:

## Findings

1. **Hoeffding Decomposition of the Empirical MMD U-Statistic**: Let $X_1, \dots, X_n \sim P_0$ and $Y_1, \dots, Y_m \sim P_\theta$ be independent samples. The squared population Maximum Mean Discrepancy is $\text{MMD}^2(P_0, P_\theta) = \mathbf{E}[h(X, X', Y, Y')]$, where the kernelized core is $h(x, x', y, y') = k(x, x') - k(x, y) - k(x', y) + k(y, y')$. The standard unbiased empirical estimator $\widehat{\text{MMD}}_u^2$ is a two-sample U-statistic of order $(2,2)$. By Hoeffding's general decomposition for U-statistics (Serfling, 1980, *Approximation Theorems of Mathematical Statistics*), $\widehat{\text{MMD}}_u^2 - \text{MMD}^2(P_0, P_\theta)$ decomposes orthogonally into a sum of degenerate U-statistics of increasing orders, where the first-order projection (the Hajek projection) dominates the variance when $P_0 \neq P_\theta$.
   * *Source*: Gretton, Borgwardt, Rasch, Schölkopf, & Smola (2012), "A Kernel Two-Sample Test", *JMLR*.

2. **Exponential Concentration Inequalities for U-Statistics and MMD**: Concentration bounds for U-statistics (and hence empirical MMD) are typically derived via McDiarmid's bounded difference inequality (yielding $O_p(n^{-1/2})$ sub-Gaussian tails when the kernel is bounded, $\sup_x k(x,x) \le K$) or via Bennett/Bernstein-type inequalities for degenerate U-processes. Specifically, Arcones & Giné (1993), "Limit Theorems for U-Processes", *Annals of Statistics*, provide exponential inequalities for U-statistics of order $d$ based on decoupling inequalities. For MMD specifically, Reddi, Poczos, & Smola (2015) or Smola et al. (2007) provide tail bounds showing that $\mathbb{P}\left(|\widehat{\text{MMD}}^2 - \text{MMD}^2| > t\right) \le 2 \exp\left( - \frac{c \min(n,m) t^2}{K^2 + K t} \right)$, where $K = \sup_{x,y} k(x,y)$.

3. **Degenerate vs. Non-Degenerate Spectral Limit Distributions**: Under the null hypothesis $P_0 = P_\theta$, the first-order term in the Hoeffding decomposition vanishes identically, rendering the U-statistic *degenerate*. As established by Gretton et al. (2012) building on Serfling (1980), the asymptotic distribution of $n \widehat{\text{MMD}}^2$ under $P_0 = P_\theta$ is an infinite sum of weighted central chi-squared variables: $\sum_{j=1}^\infty \lambda_j (Z_j^2 - 1)$, where $\lambda_j$ are the eigenvalues of the integral operator associated with $k$ under $P_0$, and $Z_j \sim \mathcal{N}(0,1)$ are independent. Under the alternative $P_0 \neq P_\theta$, the statistic is non-degenerate, and $\sqrt{n}(\widehat{\text{MMD}}^2 - \text{MMD}^2)$ converges to a normal distribution $\mathcal{N}(0, \sigma^2)$, where the asymptotic variance $\sigma^2$ depends on the variance of the first-order Hoeffding projection.

4. **Uniform Convergence over Parameter Spaces via Empirical Process Theory**: To apply U-statistic concentration to ABC posterior contraction, one requires *uniform* concentration over $\theta \in \Theta$, i.e., $\sup_{\theta \in \Theta} |\widehat{\text{MMD}}^2(P_n, P_{\theta,m}) - \text{MMD}^2(P_0, P_\theta)| \to 0$. Standard references for uniform laws of large numbers for U-processes over VC-classes or entropy integrals include d'Amore, Pillaud-Vivien, & Rudi (2021) or earlier foundational work by van der Vaart & Wellner (1996), *Weak Convergence and Empirical Processes*. The entropy of the family of RKHS embeddings $\{v_{P_\theta} : \theta \in \Theta\}$ dictates the uniform convergence rates, connecting the metric entropy of $\Theta$ under the kernel distance to the uniform concentration bound.

## Obstacles

* **Uniform vs. Pointwise Concentration**: Standard U-statistic concentration inequalities (e.g., McDiarmid or Bernstein for U-statistics) hold *pointwise* for a fixed parameter $\theta$. In ABC rejection algorithms, the acceptance filter is $\mathbb{I}(\widehat{\text{MMD}}^2_n \le \epsilon_n^2)$, requiring control over the supremum over $\theta \in \Theta$. If $\Theta$ is compact, bracketing entropy conditions on the parametric family $\{P_\theta\}$ with respect to the RKHS metric are required, which fail if the parameter-to-distribution map $\theta \mapsto P_\theta$ is discontinuous in the MMD topology.
* **Asymmetric Sample Sizes ($n$ vs $m$)**: In ABC, the observed sample size $n$ is fixed, while the simulated sample size $m$ can be chosen large. While the variance of the empirical MMD is controlled by $\min(n,m)^{-1}$, the second-order Hoeffding components interact differently for $n \neq m$, complicating exact non-asymptotic small-ball probability calculations for the composite empirical process $\widehat{\text{MMD}}^2(P_n, P_{\theta,m})$.

## Suggested next steps

1. Query literature for uniform concentration of U-processes: `Arcones Gini 1993 limit theorems for U-processes exponential inequalities`
2. Search for explicit non-asymptotic MMD bounds involving kernel eigenvalues: `Reddi Poczos Smola 2015 concentration Maximum Mean Discrepancy`
3. Investigate uniform empirical process bounds for kernel-based two-sample tests: `Smola Gretton Song Scholkopf 2007 Hilbert space embeddings probability measures concentration`
4. Study parameter-dependent Hoeffding decompositions to control the local behavior of MMD near $\theta_0$: `Serfling 1980 approximation theorems of mathematical statistics U-statistics Hoeffding decomposition`

---

## Finding #62: task_69 (Sketcher)

*Worker: **sketcher** | Task ID: `task_69` | Duration: 12.7s | Timestamp: 2026-09-09 11:46:42 UTC | Focus Nodes: `obstacle_2`, `lemma_1`*

**Assigned Task Prompt**:
> Derive the two-sample U-statistic concentration bound and Hoeffding decomposition for squared MMD to eliminate the O(1/n) self-term bias of V-statistics and rigorously bound empirical MMD variance for asymmetric sample sizes (n, m).

**Worker Output & Derivations**:

## Findings

1. **Unbiased Two-Sample U-Statistic Formulation**: The standard V-statistic estimator $\widehat{\mathrm{MMD}}_V^2$ includes diagonal self-terms $k(X_i, X_i)$ and $k(Y_i, Y_i)$, yielding an expectation $\mathbb{E}[\widehat{\mathrm{MMD}}_V^2] = \mathrm{MMD}^2(P,Q) + \frac{1}{n}\mathbb{E}[k(X,X) - k(X,X')] + \frac{1}{m}\mathbb{E}[k(Y,Y) - k(Y,Y')]$, which introduces an $O(1/n + 1/m)$ bias. Replacing diagonal

---

## Finding #63: task_73 (Searcher)

*Worker: **searcher** | Task ID: `task_73` | Duration: 17.1s | Timestamp: 2026-09-09 11:46:48 UTC | Focus Nodes: `obstacle_1`, `paper_3`*

**Assigned Task Prompt**:
> Search literature for nonparametric ABC convergence rates, kernel discrepancy consistency, and Prangle 2017 ABC rejection bounds.

**Worker Output & Derivations**:

## Findings

1. **MMD-Bayes Posterior Contraction Rates (Chérief-Abdellatif & Alquier 2020)**: In *'Consistency of Bayesian inference with maximum mean discrepancy'* (arXiv:1906.02003), the authors establish posterior consistency and contraction rates for generalized Bayesian inference using MMD as the loss: $\Pi_n(\theta|X) \propto \pi(\theta) \exp(-n \mathrm{MMD}^2(P_\theta, \hat{P}_n))$. **Hypotheses**: Assumes a compact parameter space, identifiability condition $\mathrm{MMD}^2(P_0, P_\theta) \ge C d(\theta, \theta_0)^\beta$, and boundedness of the kernel $k$. **Technique**: They use PAC-Bayesian inequalities and empirical process concentration bounds for U-statistics to derive contraction rates of the form $r_n = O(n^{-1/2} + \epsilon_n)$. **Limitation**: This applies to the Gibbs/exponential posterior rather than the hard-threshold rejection ABC indicator $\mathbb{I}(\widehat{\mathrm{MMD}}_n \le \epsilon)$.

2. **Asymptotic Distribution of Empirical MMD (Gretton et al. 2012)**: In *'A Kernel Two-Sample Test'* (JMLR 13:723-773), Gretton et al. analyze the empirical squared MMD estimator $\widehat{\mathrm{MMD}}^2(X, Y)$ based on samples of size $n$ and $m$. **Hypotheses**: Let $k$ be a measurable kernel with $\mathbb{E}[k(X,X)] < \infty$. **Statement**: Under the alternative ($P_0 \neq P_\theta$), $\widehat{\mathrm{MMD}}^2$ converges to $\mathrm{MMD}^2(P_0, P_\theta)$ at rate $O_p(n^{-1/2} + m^{-1/2})$ via degenerate U-statistic theory. Under the null ($P_0 = P_\theta$), $\widehat{\mathrm{MMD}}^2$ converges at rate $O_p(n^{-1} + m^{-1})$ to an infinite sum of weighted central chi-squared variables: $\sum_{j=1}^\infty \lambda_j (Z_j^2 - 1)$, where $\lambda_j$ are the eigenvalues of the integral operator associated with kernel $k$ under measure $P_0$, and $Z_j \sim \mathcal{N}(0,1)$ are independent. **Technique**: Spectral decomposition of the kernel via Mercer's theorem.

3. **Small-Ball Probability Framework for Rejection ABC (Frazier, Martin, Robert, & Rousseau 2018)**: In *'Asymptotic properties of approximate Bayesian computation'* (arXiv:1803.10986), the authors study the contraction rate of rejection ABC posteriors $\pi_{n,\epsilon}(\theta|y) \propto \pi(\theta) \mathbb{I}(\Delta(\hat{P}_n, P_{\theta,m}) \le \epsilon_n)$. **Hypotheses**: Requires a metric discrepancy $\Delta$, a local prior thickness condition around $\theta_0$, and a modulus of continuity establishing local lower bounds on the discrepancy: $\Delta(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$. **Statement**: The posterior concentration rate is dictated by the small-ball probability $\Pi(\Delta(P_0, P_\theta) \le \epsilon_n)$ and the modulus exponent $\beta$. **Technique**: Uses conditioning arguments on the event $\{\Delta(\hat{P}_n, P_0) \le \epsilon_n/2\}$ and triangle inequalities.

4. **Metric Topology and Kernel Strength (Sriperumbudur et al. 2010)**: In *'Hilbert Space Embeddings and Metrics on Probability Measures'* (JMLR 11:1517-1561), Sriperumbudur et al. analyze Integral Probability Metrics (IPMs). **Statement**: MMD metrizes weak convergence of probability measures if and only if the kernel is characteristic. For analytic kernels (e.g., Gaussian $k(x,y) = \exp(-\|x-y\|^2/2h^2)$), the RKHS is dense in $L_2$, inducing a very strong topology. **Technique**: Fourier/characteristic function representation showing that smoothing kernels damp high-frequency discrepancies, which directly connects to the ill-posedness of recovering $\theta$ from $\mathrm{MMD}(P_0, P_\theta)$.

## Obstacles

1. **Indicator Filter vs. Exponential Weights**: The literature on MMD-Bayes (e.g., Chérief-Abdellatif & Alquier) analyzes exponentially weighted posteriors $\exp(-n \mathrm{MMD}^2)$, which permit smooth integration and Laplace-type asymptotic expansions. Rejection ABC uses a hard indicator $\mathbb{I}(\widehat{\mathrm{MMD}}_n \le \epsilon_n)$, requiring sharp tail bounds and small-ball probability estimates rather than Bernstein-von Mises expansions.
2. **Degeneracy of the Null Limit in ABC Denominators**: When evaluating the ABC denominator (marginal likelihood), the parameter $\theta$ varies over the prior support where $\theta \neq \theta_0$ (the alternative), but acceptance requires $\widehat{\mathrm{MMD}}_n \le \epsilon_n$. As $n \to \infty$, the probability of acceptance for $\theta \neq \theta_0$ is governed by tail probabilities of degenerate U-statistics, whose decay rate depends heavily on the tail of the spectrum $\{\lambda_j\}$.
3. **Interplay Between Kernel Bandwidth and Dimension**: In high dimensions $d$, fixing the kernel bandwidth $h$ while taking $d \to \infty$ causes the Gaussian kernel's effective support to concentrate, making $\mathrm{MMD}^2(P_0, P_\theta)$ exponentially insensitive to parameter changes in directions orthogonal to the gradient of the mean, severely worsening the identifiability modulus constant $c(d)$.

## Suggested next steps

1. **Query 1**: `arXiv:1906.02003` (Chérief-Abdellatif & Alquier, "Consistency of Bayesian inference with maximum mean discrepancy") - Examine their adaptation of PAC-Bayesian theorems to see if the proof techniques handle indicator losses $\mathbb{I}(\text{MMD} \le \epsilon)$ through truncation.
2. **Query 2**: `arXiv:1803.10986` (Frazier, Martin, Robert, & Rousseau, "Asymptotic properties of approximate Bayesian computation") - Review the small-ball probability conditions for general discrepancies to instantiate them explicitly with MMD and its Mercer spectrum $\lambda_j$.
3. **Query 3**: Search for literature on "hypothesis testing kernel MMD power high dimensions spectral decay" (e.g., Liu et al., 2020, "A Block-Diagonalized Kernel Two-Sample Test") to understand how tail eigenvalues affect local power and distinguishability.
4. **Query 4**: Investigate the exact modulus of continuity $\mathrm{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$ for parametric location-scale families under translation-invariant kernels, tracking how the constants depend explicitly on the kernel bandwidth $h$ and dimension $d$.

---

## Finding #64: task_71 (Sketcher)

*Worker: **sketcher** | Task ID: `task_71` | Duration: 17.8s | Timestamp: 2026-09-09 11:46:55 UTC | Focus Nodes: `lemma_1`, `idea_1`, `obstacle_1`*

**Assigned Task Prompt**:
> Formalize the spectral truncation error bound for empirical MMD using the top K_n eigenfunctions from lemma_1, and derive its implication for the ABC rejection small-ball probability.

**Worker Output & Derivations**:

## Findings

1. **Subgoal 1: Spectral Truncation of Empirical MMD Squared (Status: Solved)**
   Let $k$ be a Mercer kernel on $\mathcal{X} \times \mathcal{X}$ with eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots > 0$ and orthonormal eigenfunctions $\{e_j\}_{j=1}^\infty$ in $L^2(P_0)$. The population squared MMD is $\text{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, where $\mu_{0,j} = \mathbb{E}_{P_0}[e_j(X)]$ and $\mu_{\theta,j} = \mathbb{E}_{P_\theta}[e_j(X)]$. 
   Let $\widehat{P}_n$ be the empirical measure of $P_0$ with empirical feature mean $\widehat{\mu}_n$. The squared difference between empirical and population MMD estimators expands via polarization as:
   $$\widehat{\Delta}_n^2 := \widehat{\text{MMD}}_n^2(P_0, P_\theta) - \text{MMD}^2(P_0, P_\theta) = \|\widehat{\mu}_n - \mu_\theta\|_{\mathcal{H}}^2 - \|\mu_0 - \mu_\theta\|_{\mathcal{H}}^2 = \|\widehat{\mu}_n - \mu_0\|_{\mathcal{H}}^2 + 2 \langle \widehat{\mu}_n - \mu_0, \mu_0 - \mu_\theta \rangle.$$
   For a truncation level $K_n$, we decompose $\|\widehat{\mu}_n - \mu_0\|_{\mathcal{H}}^2 = \sum_{j=1}^{K_n} \lambda_j (\widehat{\mu}_{n,j} - \mu_{0,j})^2 + \sum_{j=K_n+1}^\infty \lambda_j (\widehat{\mu}_{n,j} - \mu_{0,j})^2$.
   Taking expectations, $\mathbb{E}[(\widehat{\mu}_{n,j} - \mu_{0,j})^2] = \frac{1}{n} \text{Var}_{P_0}(e_j(X)) = \frac{1 - \mu_{0,j}^2}{n} \le \frac{1}{n}$. Thus, the finite sum expectation is bounded by $\frac{1}{n}\sum_{j=1}^{K_n} \lambda_j \le \frac{\text{Tr}(T_k)}{n} = \frac{1}{n}\int k(x,x)dP_0(x)$, while the tail sum contributes $\frac{1}{n}\sum_{j=K_n+1}^\infty \lambda_j$. If $\lambda_j \asymp j^{-2s/d}$, the tail sum is $O(n^{-1} K_n^{1 - 2s/d})$.

2. **Subgoal 2: Cross-

---

## Finding #65: task_72 (Counterexample)

*Worker: **counterexample** | Task ID: `task_72` | Duration: 22.1s | Timestamp: 2026-09-09 11:47:05 UTC | Focus Nodes: `hypothesis_2`, `obstacle_3`*

**Assigned Task Prompt**:
> Construct a parametric test case to check whether the dimension-dependent preconstant c(d) proportional to a^{-d} in hypothesis_2 leads to an exponentially vanishing acceptance rate in high dimensions d.

**Worker Output & Derivations**:

R) = \frac{\pi^{d/2}}{\Gamma(d/2 + 1)} R^d$.
    If we want $R(d) = \delta$ (a constant, so we have a fixed contraction error), then the volume of this ball is:
    $V_d = \frac{\pi^{d/2}}{\Gamma(d/2 + 1)} \delta^d$, which decays as $( \frac{2\pi e \delta^2}{d} )^{d/2}$. This is the standard curse of dimensionality (the volume of a fixed-radius ball decays factorially).
    But now, what if we just keep $\epsilon$ fixed, or scale it?
    Let's look at the ratio of the volume

---

## Finding #66: task_77 (Counterexample)

*Worker: **counterexample** | Task ID: `task_77` | Duration: 13.7s | Timestamp: 2026-09-09 11:47:28 UTC | Focus Nodes: `idea_1`, `obstacle_3`, `obstacle_4`*

**Assigned Task Prompt**:
> Investigate whether the spectral truncation idea (idea_1) fails or becomes extremely loose when the parameter dimension $d$ is large, specifically when the target distribution $P_0$ is high-dimensional and the true parameter $\theta_0$ lies in a direction corresponding to a very small eigenvalue $\lambda_j$.

**Worker Output & Derivations**:

## Findings

1. **Failure of Spectral Truncation via High-Frequency Parameter Directions (Status: refuted as a uniform bound)**. Consider $P_0 = \mathcal{N}(0,1)$ and a Gaussian kernel $k_h(x,y) = \exp(-(x-y)^2/(2h^2))$, whose orthonormal eigenfunctions with respect to $P_0$ are the Hermite functions $e_j(x) = h_j(x)$ with eigenvalues $\lambda_j$ decaying exponentially. Let $P_\theta$ be a perturbation family where $\theta$ shifts the distribution along the $m$-th Hermite mode, giving expectation coefficients $\mu_{\theta, j} = \delta_{jm}\theta$. The true squared MMD is $\operatorname{MMD}^2(P_0, P_\theta) = \lambda_m \theta^2$. If the spectral truncation level in `idea_1` is chosen as $K_n < m$, the truncated MMD yields $\operatorname{MMD}_{K_n}^2 = 0$, completely missing the signal. Thus, the truncation error $\sum_{j > K_n} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2 = \lambda_m \theta^2$ is not a negligible remainder, as it carries the exact parameter signal, refuting the validity of fixed-order spectral truncation for arbitrary directional perturbations.

2. **Exponential Dimensional Explosion of Tail Eigenvalues in Product Spaces (Status: not_refuted)**. When $P_0$ is a product measure on $\mathbb{R}^d$ with a tensor-product kernel $k(\mathbf{x}, \mathbf{y}) = \prod_{l=1}^d k_1(x_l, y_l)$, the $d$-dimensional Mercer eigenvalues are given by multi-index products $\lambda_{\mathbf{j}} = \prod_{l=1}^d \lambda_{j_l}^{(1)}$. For any fixed truncation level $K_n$, the proportion of the total RKHS trace captured by the top $K_n$ eigenfunctions decays exponentially in $d$ due to the curse of dimensionality (the volume of the multi-index set for a given eigenvalue magnitude grows combinatorially). Consequently, the truncation error $\sum_{\mathbf{j} \notin \mathcal{K}_n} \lambda_{\mathbf{j}}$ dominates the total squared MMD unless $K_n$ grows exponentially with $d$, rendering the spectral truncation bound in `idea_1` practically vacuous in high dimensions.

## Obstacles

- **Low-Frequency Bias of Standard Parametric Models**: In many standard statistical models (e.g., location-scale families), parameters $\theta$ primarily perturb the first few moments (mean, variance), which load heavily onto the leading eigenfunctions $e_1, e_2$. Therefore, while high-frequency counterexamples exist mathematically, they may require pathological parameter-to-distribution maps that do not arise in standard ABC applications unless the model is explicitly overparameterized or non-regular.
- **Interplay Between Empirical Variance and Truncation**: While high-frequency components carry signal in the counterexample, they also carry the highest estimation variance in the empirical U-statistic/V-statistic estimator of MMD. Bounding the ABC small-ball probability requires balancing the truncation error against the variance reduction achieved by dropping those very same high-frequency tails.

## Suggested next steps

- Formulate a constrained parameter class assumption (e.g., bounding the Sobolev norm of the score operator $\nabla_\theta P_\theta$ in terms of the kernel's eigenbasis) under which high-frequency activation is formally ruled out, rescuing a modified version of `idea_1`.
- Analyze the directional MMD sensitivity matrix (the Gram matrix of $\langle \partial_\theta P_\theta, e_j \rangle$) to explicitly characterize when spectral truncation preserves local identifiability versus destroying it.

---

## Finding #67: task_75 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_75` | Duration: 14.2s | Timestamp: 2026-09-09 11:47:36 UTC | Focus Nodes: `hypothesis_1`, `hypothesis_2`, `obstacle_3`, `idea_2`*

**Assigned Task Prompt**:
> Analyze the trade-off between sensitivity and variance for a translation family $P_\theta = \mathcal{N}(\theta, I_d)$ on a flat space under (1) a Gaussian kernel (exponential spectral decay) and (2) a Matern-like kernel (polynomial spectral decay). Compute how the identifiability preconstant $c(d)$ and empirical variance scale with dimension $d$ under both kernels, specifically referencing hypothesis_1, hypothesis_2, obstacle_3, and idea_2.

**Worker Output & Derivations**:

## Findings

1. **Explicit Fourier MMD for Gaussian Kernels in $\mathbb{R}^d$:** Consider the translation family $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$, and an isotropic Gaussian kernel $k_h(x,y) = \exp(-\|x-y\|^2 / (2h^2))$. Using the Fourier integral representation, the squared population MMD is $\text{MMD}^2(P_0, P_\theta) = \int_{\mathbb{R}^d} |\hat{P}_0(t) - \hat{P}_\theta(t)|^2 \hat{k}_h(t) dt$, where $\hat{P}_0(t) = e^{-\|t\|^2/2}$, $\hat{P}_\theta(t) = e^{i t^T \theta} e^{-\|t\|^2/2}$, and $\hat{k}_h(t) = (2\pi)^{d/2} h^d \exp(-h^2 \|t\|^2 / 2)$. Evaluating $|\hat{P}_0 - \hat{P}_\theta|^2 = 2(1 - \cos(t^T \theta)) e^{-\|t\|^2}$ and applying a second-order Taylor expansion for small $\|\theta\|$, we obtain $\text{MMD}^2(P_0, P_\theta) \approx \int_{\mathbb{R}^d} (t^T \theta)^2 e^{-\|t\|^2(1 + h^2/2)} dt$. By rotational symmetry, this evaluates to $c(d) \|\theta\|^2$, where the preconstant scales as $c(d) \propto (1 + h^2/2)^{-d/2 - 1} \asymp \exp\left(-\frac{d}{2} \log(1 + h^2/2)\right)$, rigorously confirming **Hypothesis 2**'s exponential preconstant decay $c(d) \propto a^{-d}$.

2. **Explicit Fourier MMD for Polynomial/Matérn-like Spectral Kernels:** Replacing the Gaussian kernel with a kernel whose Fourier spectral density exhibits polynomial decay, $\hat{k}(t) \propto (1 + \|t\|^2)^{-s}$ for smoothness parameter $s > d/2$, the quadratic approximation of the squared MMD becomes $\text{MMD}^2(P_0, P_\theta) \approx \int_{\mathbb{R}^d} (t^T \theta)^2 e^{-\|t\|^2} (1 + \|t\|^2)^{-s} dt$. In high dimensions $d$, the Gaussian measure $e^{-\|t\|^2}$ concentrates on the spherical shell $\|t\| \approx \sqrt{d}$. On this shell, the kernel weight $(1 + \|t\|^2)^{-s} \approx (1 + d)^{-s}$. Consequently, the identifiability preconstant decays algebraically as $c(d) \propto d^{-s}$, completely avoiding the exponential collapse $a^{-d}$ seen in the Gaussian kernel, confirming the structural distinction proposed in **Hypothesis 1**.

3. **The Variance-Sensitivity Trade-off via Hoeffding Projections:** By **Lemma 2**, the empirical variance of the MMD estimator is governed by $\sum_{j=1}^\infty \lambda_j^2 (\mu_{0,j} - \mu_{\theta,j})^2 \text{Var}(e_j(X))$. For the Gaussian kernel, Mercer eigenvalues decay exponentially ($\lambda_j \sim \exp(-cj^{2/d})$), which heavily damps the sum, keeping the empirical variance small even in high dimensions and addressing **Obstacle 3**. However, this rapid decay flattens the population MMD profile along high-frequency directions, producing the exponential preconstant decay $c(d) \propto a^{-

---

## Finding #68: task_76 (Sketcher)

*Worker: **sketcher** | Task ID: `task_76` | Duration: 15.2s | Timestamp: 2026-09-09 11:47:44 UTC | Focus Nodes: `idea_1`, `lemma_1`, `obstacle_1`*

**Assigned Task Prompt**:
> Draft a proof sketch for the ABC posterior acceptance probability bound under the spectral truncation scheme proposed in idea_1. Show how choosing the truncation dimension $K_n$ balancing truncation bias and estimation variance leads to a non-trivial lower bound on the acceptance probability.

**Worker Output & Derivations**:

## Findings

1. **Subgoal 1: Spectral Truncation of Population and Empirical MMD (Status: solved sketch)**
   Let $k(x,y) = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(y)$ be the Mercer expansion of the kernel with eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots > 0$ and orthonormal eigenfunctions $\{e_j\}_{j=1}^\infty$ in $L^2(P_0)$. The population squared MMD is $\mathrm{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, where $\mu_{0,j} = \mathbb{E}_{X \sim P_0}[e_j(X)]$ and $\mu_{\theta,j} = \mathbb{E}_{Y \sim P_\theta}[e_j(Y)]$. For a truncation level $K_n$, we define the truncated population MMD as $\mathrm{MMD}_{K_n}^2(P_0, P_\theta) = \sum_{j=1}^{K_n} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$. The squared tail sum $\mathrm{Tail}_{K_n}^2(P_0, P_\theta) = \sum_{j > K_n} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ acts as the truncation bias. Assuming $P_\theta$ is sufficiently smooth such that $|\mu_{0,j} - \mu_{\theta,j}| \lesssim j^{-s'} \|\theta - \theta_0\|$, and given Mercer decay $\lambda_j \sim j^{-2s/d}$, the tail sum is bounded by $C \|\theta - \theta_0\|^2 \sum_{j > K_n} j^{-2s/d - 2s'} \lesssim \|\theta - \theta_0\|^2 K_n^{1 - 2(s/d + s')}$.

2. **Subgoal 2: Variance Decomposition of the Truncated Empirical MMD (Status: solved sketch)**
   The empirical squared MMD based on $n$ samples $X_{1:n} \sim P_0$ and $m$ samples $Y_{1:m} \sim P_\theta$ can be split similarly: $\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) = \widehat{\mathrm{MMD}}_{K_n}^2 + \widehat{\mathrm{Tail}}_{K_n}^2$. By `lemma_2` (Hoeffding projection variance), the variance of the leading $K_n$-dimensional empirical component satisfies $\operatorname{Var}(\widehat{\mathrm{MMD}}_{K_n}^2) \lesssim \frac{1}{n} \sum_{j=1}^{K_n} \lambda_j^2 (\mu_{0,j} - \mu_{\theta,j})^2 \operatorname{Var}(e_j(X)) + \frac{1}{m} \sum_{j=1}^{K_n} \lambda_j^2 (\mu_{0,j} - \mu_{\theta,j})^2 \operatorname{Var}(e_j(Y))$. Since $\sum_{j=1}^{K_n} \lambda_j^2 \le \lambda_1 \sum_{j=1}^{K_n} \lambda_j \le \lambda_1 \operatorname{Trace}(K)$, the estimation variance of the $K_n$-dimensional projection is bounded by $O\left(\frac{K_n^{\gamma}}{n} + \frac{K_n^{\gamma}}{m}\right)$ for some exponent $\gamma$ dictated by the eigenvalue sum, avoiding the infinite-trace divergence that occurs if unprojected empirical U-statistics are naively bounded in high-dimensional RKHS norms.

3. **Subgoal 3: Optimal Choice of $K_n$ and Lower Bound on the ABC Denominator (Status: partial sketch)**
   To bound the small-ball probability $P_\theta(\widehat{\mathrm{MMD}}^2(P_n, P_{\theta, m}) \le \epsilon_n^2)$ for $\|\theta - \theta_0\| \le r_n$, decompose the error into three parts: (i) population distance $\mathrm{MMD}^2(P_0, P_\theta) \asymp \|\theta - \theta_0\|^2 \le r_n^2$, (ii) truncation bias $\mathrm{Tail}_{K_n}^2(P_0, P_\theta) \lesssim r_n^2 K_n^{1 - 2s/d}$, and (iii) stochastic fluctuation of the $K_n$-projection $\mathcal{O}_p\left(\sqrt{\frac{\sum_{j=1}^{K_n} \lambda_j^2}{n}}\right)$. Balancing the truncation bias $K_n^{-(2s/d - 1)}$ against the estimation variance $\sqrt{\frac{K_n}{n}}$ yields the optimal truncation dimension $K_n \asymp n^{\frac{1}{4

---

## Finding #69: task_79 (Searcher)

*Worker: **searcher** | Task ID: `task_79` | Duration: 13.1s | Timestamp: 2026-09-09 11:47:51 UTC | Focus Nodes: `paper_5`, `obstacle_3`, `idea_1`*

**Assigned Task Prompt**:
> Search literature (arXiv and OpenAlex) for bounds on Rademacher complexity of MMD classes in terms of Mercer eigenvalues and dimension d, referencing paper_5.

**Worker Output & Derivations**:

## Findings

1. **Rademacher Complexity Bound via Mercer Eigenvalues (Bartlett & Mendelson, 2002 / Steinwart & Christmann, 2008):** 
   Let $\mathcal{F}_k = \{f \in \mathcal{H}_k : \|f\|_{\mathcal{H}_k} \le 1\}$ be the unit ball in the Reproducing Kernel Hilbert Space (RKHS) associated with a continuous, bounded kernel $k$ on a compact domain $\mathcal{X} \subset \mathbb{R}^d$. The empirical Rademacher complexity $\mathcal{R}_n(\mathcal{F}_k)$ satisfies the spectral bound (Theorem 7.4 in Steinwart & Christmann, 2008, *Support Vector Machines*):
   $$\mathbb{E}[\mathcal{R}_n(\mathcal{F}_k)] \le \left( \frac{1}{n} \sum_{j=1}^\infty \min\left(\lambda_j, \frac{C^2}{n}\right) \right)^{1/2}$$
   where $\lambda_j$ are the Mercer eigenvalues of the integral operator $T_k$ with respect to the marginal distribution $P_0$, and $C = \sup_{x} \sqrt{k(x,x)}$. *Hypothesis/Applicability:* When eigenvalues decay polynomially as $\lambda_j \asymp j^{-2s/d}$ (reflecting smoothness $s$ and dimension $d$), the sum evaluates to $\mathcal{O}(n^{-1/2})$ for $2s > d$, but degrades to $\mathcal{O}(n^{-s/d})$ or worse when the effective dimension is large ($2s \le d$), directly linking the curse of dimensionality in spectral decay to the variance of empirical MMD estimators.

2. **Minimax Rates of MMD Estimation and Dimension Dependence (Tolstikhin et al., 2016):**
   In Tolstikhin et al. (2016), *"Minimax Estimation of Maximum Mean Discrepancy with a Radial Basis Kernel"* (Advances in Neural Information Processing Systems), the authors establish minimax lower and upper bounds for estimating $\operatorname{MMD}(P, Q)$ using empirical measures of size $n$. The estimator's variance is governed not just by the trace $\sum \lambda_j$ but by quadratic forms involving $\sum \lambda_j^2$. Specifically, for translation-invariant kernels on $\mathbb{R}^d$, the estimation error depends crucially on the Fourier decay of the kernel, which degrades exponentially with dimension $d$ for analytic kernels (like Gaussian) unless sample sizes scale appropriately.

3. **Entropy Numbers of RKHS Embeddings and Weyl's Law (Cucker & Smale, 2002 / Zhou, 2002):**
   The covering numbers $N(\mathcal{F}_k, \|\cdot\|_{L_2(P_0)}, \epsilon)$ of the unit RKHS ball are tightly controlled by the singular values of the compact embedding operator $i: \mathcal{H}_k \to L_2(P_0)$, which coincide with the square roots of the Mercer eigenvalues $\sqrt{\lambda_j}$. By Weyl's asymptotic law for differential operators and Mercer kernels on $\Omega \subset \mathbb{R}^d$ with smoothness $s$, $\lambda_j \sim j^{-2s/d}$. Plugging this into Dudley's entropy integral yields the covering entropy bound:
   $$\log N(\mathcal{F}_k, \|\cdot\|_{L_2(P_0)}, \epsilon) \lesssim \left(\frac{1}{\epsilon}\right)^{d/s}$$
   This explicitly exposes how the spatial dimension $d$ and kernel smoothness $s$ control the metric entropy of the MMD witness function class, governing the uniform convergence rates via empirical process theory (e.g., van der Vaart & Wellner, 1996).

## Obstacles

1. **U-Statistic Degeneracy vs. Linear Empirical Processes:** 
   Rademacher complexity bounds apply to linear suprema of the form $\sup_{f \in \mathcal{F}_k} \frac{1}{n} \sum_{i=1}^n \sigma_i f(X_i)$. However, the squared MMD estimator $\widehat{\operatorname{MMD}}_n^2(P_n, P_{\theta, m})$ is a degenerate U-statistic (or V-statistic) of order 2. Standard Rademacher bounds cannot be directly plugged into ABC rejection probabilities without controlling the decoupled chaos processes (Arcones & Giné, 1993, *"Limit Theorems for U-Processes"*), where the variance structure involves cross-terms of eigenvalues $\lambda_j \lambda_l$.

2. **Mismatch Between Witness Function Class and Parameter Space:** 
   While Rademacher complexity controls the uniform deviation $\sup_{f \in \mathcal{F}_k} |(P_n - P_0)f|$, ABC parameter estimation requires uniform control over $\theta \in \Theta$ of $\widehat{\operatorname{MMD}}_n^2(P_n, P_{\theta, m})$. Bounding the Rademacher complexity of the family of witness functions *parameterized by $\theta$* ($\{k(x, \cdot) - \mathbb{E}_{Y \sim P_\theta}[k(y, \cdot)]\}$) requires chaining or bracketing entropy calculations that depend on the smoothness of the parameter-to-distribution map $\theta \mapsto P_\theta$, which is complicated by the spectral decay of the kernel.

## Suggested next steps

1. Run literature query: `("Rademacher complexity" OR "covering numbers") AND ("maximum mean discrepancy" OR "MMD") AND ("Mercer eigenvalues" OR "eigenvalue decay")`
2. Run literature query: `author:Tolstikhin "Minimax Estimation of Maximum Mean Discrepancy" OR author:Sriperumbudur "empirical estimation of integral probability metrics"`
3. Run literature query: `("degenerate U-statistics" OR "U-processes") AND "kernel integral operator" AND "eigenvalue decay"`
4. Run literature query: `("ABC" OR "approximate Bayesian computation") AND "maximum mean discrepancy" AND ("contraction rate" OR "posterior contraction")`

---

## Finding #70: task_80 (Decomposer)

*Worker: **decomposer** | Task ID: `task_80` | Duration: 16.2s | Timestamp: 2026-09-09 11:48:04 UTC | Focus Nodes: `paper_5`, `idea_1`, `hypothesis_1`*

**Assigned Task Prompt**:
> Develop a rigorous proof plan combining Legramanti et al.'s Rademacher complexity concentration framework (paper_5) with the spectral truncation method (idea_1) to establish an explicit posterior contraction rate for MMD-ABC.

**Worker Output & Derivations**:

## Findings

1. **Spectral-Truncated Rademacher Concentration for MMD-ABC Rates:** This plan combines idea_1 (spectral truncation) with empirical process theory (Legramanti et al.'s Rademacher complexity framework) to bound the small-ball probability of the indicator rejection filter, avoiding infinite-dimensional variance explosion.
   * *Subgoal 1.1:* Establish a Rademacher complexity bound for the finite-dimensional empirical projection $\widehat{\mathrm{MMD}}_{K_n}^2(P_n, P_\theta) = \sum_{j=1}^{K_n} \lambda_j (\hat{\mu}_{0,j} - \hat{\mu}_{\theta,j})^2$ over the RKHS subspace of dimension $K_n$.
   * *Subgoal 1.2:* Quantify the tail truncation error $\sum_{j > K_n} \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ uniformly over $\theta$ as a function of kernel smoothness $s$, dimension $d$, and truncation level $K_n$.
   * *Subgoal 1.3:* Optimize the truncation parameter $K_n = K(n)$ to balance the estimation variance of the first $K_n$ components against the tail approximation error.
   * *Subgoal 1.4:* Apply generalized posterior contraction theorems (adapted from Ghosal et al. for indicator-based ABC filters) using the combined concentration inequality to extract the explicit rate $\epsilon_n$.

2. **Hessian-Based Denominator Lower Bounds and Local Identifiability Control:** This plan tackles obstacle_4 and hypothesis_2 by explicitly computing the Hessian of the population MMD via Lemma 2's spectral expansion, using it to lower-bound the ABC posterior denominator (prior mass of the acceptance region).
   * *Subgoal 2.1:* Derive the Taylor expansion of $\mathrm{MMD}^2(P_0, P_\theta)$ around $\theta_0$, expressing the Hessian matrix $H(\theta_0)$ explicitly in terms of the kernel eigenvalues $\lambda_j$ and cross-derivatives of the eigenfunction expectations $\mu_{\theta,j}$.
   * *Subgoal 2.2:* Prove a small-ball probability lower bound for the quadratic form $\Delta \theta^T H(\theta_0) \Delta \theta \le \epsilon_n^2$ under the prior distribution, quantifying how rapidly eigenvalue decay shrinks the prior mass of the acceptance region.
   * *Subgoal 2.3:* Establish a local prior concentration estimate for the MMD-ABC posterior, incorporating the dimension-dependent preconstant $c(d)$ from hypothesis_2.
   * *Subgoal 2.4:* Combine the denominator lower bound with the numerator exponential concentration (from Plan 1) to derive the final minimax posterior contraction rate, explicitly revealing the trade-off between kernel smoothness $s$ and dimension $d$.

## Obstacles

- Controlling the interaction between the empirical sample size $n$ (observed data) and simulation sample size $m$ (synthetic data) within the Rademacher complexity bounds of Subgoal 1.1, especially when $m$ is large but fixed relative to $n$ (obstacle_2).
- Proving that the high-frequency tail of the empirical MMD (omitted by spectral truncation) does not contribute a spurious bias term that dominates the ABC rejection threshold $\epsilon_n$ as $\epsilon_n \to 0$.
- Computing or lower-bounding the smallest non-zero eigenvalue of the population Hessian $H(\theta_0)$ in Subgoal 2.2 when Mercer eigenvalues $\lambda_j$ decay rapidly (obstacle_3 and obstacle_4), which threatens to make the denominator exponentially small in $d$.

## Suggested next steps

- Derive the exact Rademacher complexity upper bound for the truncated empirical statistic $\widehat{\mathrm{MMD}}_{K_n}^2$ as an explicit function of $K_n$, $n$, and $m$, leveraging standard chaining or Rademacher symmetrization arguments.
- Formulate a concrete toy model (e.g., a 1D Gaussian scale family or multi-dimensional location family with a Matérn kernel) to explicitly evaluate the Hessian $H(\theta_0)$ via Lemma 2 and test whether the prior mass of the acceptance region vanishes faster than the posterior numerator concentration rate.
- Establish the precise asymptotic scaling relation between the ABC tolerance sequence $\epsilon_n$, sample sizes $(n, m)$, and dimension $d$ required to maintain a non-vanishing posterior acceptance probability.

---

## Finding #71: task_81 (Sketcher)

*Worker: **sketcher** | Task ID: `task_81` | Duration: 19.2s | Timestamp: 2026-09-09 11:48:16 UTC | Focus Nodes: `lemma_1`, `paper_5`*

**Assigned Task Prompt**:
> Derive the explicit upper bound on the Rademacher complexity R_n(F) for the MMD unit ball in terms of the kernel's Mercer eigenvalues lambda_j and sample size n, building on lemma_1 and paper_5.

**Worker Output & Derivations**:

## Findings

1. **Explicit Rademacher Complexity Bound via Mercer Expansion**: **[Status: solved (sketch included)]** 
   Let $\mathcal{F} = \{f \in \mathcal{H} : \|f\|_{\mathcal{H}} \le 1\}$ be the unit ball in the RKHS associated with a Mercer kernel $k$. By Mercer's Theorem, $k(x,y) = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(y)$ with orthonormal eigenfunctions in $L_2(P_0)$. Any $f \in \mathcal{H}$ satisfies $f = \sum_{j=1}^\infty a_j e_j$ with $\sum_{j=1}^\infty \frac{a_j^2}{\lambda_j} \le 1$. The empirical Rademacher complexity is $\hat{R}_n(\mathcal{F}) = \mathbb{E}_\sigma \left[ \sup_{\sum a_j^2/\lambda_j \le 1} \frac{1}{n} \sum_{i=1}^n \sigma_i \sum_{j=1}^\infty a_j e_j(X_i) \right]$. Solving the supremum over the ellipsoid via the dual norm yields $\hat{R}_n(\mathcal{F}) = \mathbb{E}_\sigma \left[ \left( \sum_{j=1}^\infty \lambda_j \left( \frac{1}{n} \sum_{i=1}^n \sigma_i e_j(X_i) \right)^2 \right)^{1/2} \right]$. Applying Jensen's inequality and taking the expectation over the sample $X_1, \dots, X_n \sim P_0$, we obtain $R_n(\mathcal{F}) \le \left( \frac{1}{n} \sum_{j=1}^\infty \lambda_j \mathbb{E}[e_j(X)^2] \right)^{1/2} = \sqrt{\frac{\sum_{j=1}^\infty \lambda_j}{n}} = \sqrt{\frac{\operatorname{Tr}(K)}{n}} = \sqrt{\frac{\mathbb{E}_{X \sim P_0}[k(X,X)]}{n}}$.

2. **Decoupling of Trace Independence from Spectral Decay**: **[Status: solved (sketch included)]**
   The upper bound $R_n(\mathcal{F}) \le \sqrt{\operatorname{Tr}(K)/n}$ depends exclusively on the total trace $\operatorname{Tr}(K) = \sum_{j=1}^\infty \lambda_j = \mathbb{E}_{X \sim P_0}[k(X,X)]$, which is finite and independent of the individual eigenvalue decay rate $\lambda_j \sim j^{-2s/d}$ (provided $\sup_x k(x,x) < \infty$). This confirms `idea_2`: while high-dimensional slow spectral decay degrades parameter identifiability and flattens the population MMD profile around $\theta_0$ (raising the identifiability exponent $\beta$ or shrinking the preconstant $c$), it *does not* degrade the rate of empirical uniform convergence $O_n(1/\sqrt{n})$ of the MMD estimator itself, because the Rademacher complexity bound is governed by the trace norm rather than individual tail eigenvalues.

## Obstacles

1. **Uniform vs. Pointwise Convergence Discrepancy**: The Rademacher complexity bound controls uniform convergence over the RKHS unit ball $\mathcal{F}$, but MMD-ABC involves evaluating the supremum over a family of distributions $\{P_\theta : \theta \in \Theta\}$ rather than the entire RKHS unit ball, meaning the unconstrained RKHS unit ball Rademacher bound may be overly conservative if the image of the parameter-to-distribution map $\theta \mapsto P_\theta$ occupies a lower-dimensional or smoother subset of $\mathcal{H}$.
2. **Asymmetry in Two-Sample Empirical MMD**: The standard Rademacher bound applies to the empirical process over a single sample of size $n$. In MMD-ABC, the empirical discrepancy involves both observed data of size $n$ and simulated data of size $m$ (from $P_\theta$), requiring a two-sample Rademacher complexity extension where variance terms are controlled by $\min(n, m)$ as noted in `obstacle_2`.

## Suggested next steps

1. **Derive Two-Sample Rademacher Complexity Bounds**: Extend the single-sample Mercer-based Rademacher derivation to the joint two-sample empirical process $\sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n f(X_i) - \frac{1}{m} \sum_{k=1}^m f(Y_k) \right|$ to explicitly incorporate

---

## Finding #72: task_82 (Sketcher)

*Worker: **sketcher** | Task ID: `task_82` | Duration: 13.9s | Timestamp: 2026-09-09 11:48:29 UTC | Focus Nodes: `lemma_1`, `obstacle_3`, `problem`*

**Assigned Task Prompt**:
> Draft a rigorous proof sketch for Plan A, Subgoal 2: formulate Picard's condition for the linearized inverse problem mapping parameter error to MMD, and show how the parameter estimation error ||theta_hat - theta_0|| is bounded by MMD scaled inversely by the square root of kernel eigenvalues lambda_j.

**Worker Output & Derivations**:

## Findings

1. **Subgoal 2 (Solved - Sketch): Linearized Inverse Problem and Picard's Condition for MMD-ABC**
   * **Step 1: Fréchet derivative of the mean embedding.** Let $\mu_\theta \in \mathcal{H}$ be the kernel mean embedding of $P_\theta$, defined by $\mu_\theta(x) = \mathbb{E}_{Y \sim P_\theta}[k(x, Y)]$. The squared population MMD between $P_0$ and $P_\theta$ is the squared RKHS norm: $\operatorname{MMD}^2(P_0, P_\theta) = \|\mu_\theta - \mu_{\theta_0}\|_{\mathcal{H}}^2$. For a small parameter perturbation $\delta\theta = \theta - \theta_0 \in \mathbb{R}^d$, linearizing the mean embedding yields:
     $$\mu_\theta - \mu_{\theta_0} = A \delta\theta + o(\|\delta\theta\|_2)$$
     where $A = D\mu(\theta_0) : \mathbb{R}^d \to \mathcal{H}$ is a bounded linear operator (specifically, a finite-rank operator since the domain $\mathbb{R}^d$ is $d$-dimensional) with components $(A v)(x) = \sum_{l=1}^d v_l \frac{\partial \mu_{\theta_0}(x)}{\partial \theta_l}$.
   * **Step 2: Spectral representation in the Mercer basis.** Let $\{e_j\}_{j=1}^\infty$ be the orthonormal eigenfunctions of the integral operator $T_k f(x) = \int k(x,y) f(y) dP_0(y)$ with eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots > 0$. The RKHS inner product is given by $\langle f, g \rangle_{\mathcal{H}} = \sum_{j=1}^\infty \frac{f_j g_j}{\lambda_j}$, where $f_j = \langle f, e_j \rangle_{L^2(P_0)}$. Consequently, the squared MMD expands as:
     $$\operatorname{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \frac{1}{\lambda_j} \left( \sum_{l=1}^d \delta\theta_l \langle \frac{\partial \mu_{\theta_0}}{\partial \theta_l}, e_j \rangle_{L^2(P_0)} \right)^2 + o(\|\delta\theta\|_2^2)$$
   * **Step 3: Gram matrix and Picard's condition.** Define the $d \times d$ Fisher-like Gram matrix $M = A^* A : \mathbb{R}^d \to \mathbb{R}^d$, whose entries in the RKHS are $M_{l,l'} = \langle \frac{\partial \mu_{\theta_0}}{\partial \theta_l}, \frac{\partial \mu_{\theta_0}}{\partial \theta_{l'}} \rangle_{\mathcal{H}}$. Substituting the spectral expansion, the matrix elements become:
     $$M_{l,l'} = \sum_{j=1}^\infty \frac{1}{\lambda_j} \langle \frac{\partial \mu_{\theta_0}}{\partial \theta_l}, e_j \rangle_{L^2(P_0)} \langle \frac{\partial \mu_{\theta_0}}{\partial \theta_{l'}}, e_j \rangle_{L^2(P_0)}$$
     Picard's condition for the existence of a stable inverse map requires that the projection of $\Delta \mu = \mu_\theta - \mu_{\theta_0}$ onto the singular system of $A$ satisfies $\sum_{j=1}^\infty \frac{\langle \Delta \mu, e_j \rangle^2}{\lambda_j^2} < \infty$. Because $\Delta \mu$ is already in the range of $A$ (which is finite-dimensional), this condition holds algebraically, but the conditioning is governed by the smallest eigenvalue of $M$.
   * **Step 4: Bounding parameter error by MMD and kernel eigenvalues.** By Rayleigh's inequality, the parameter error satisfies:
     $$\|\delta\theta\|_2^2 \le \sigma_{\min}(M)^{-1} \|\mu_\theta - \mu_{\theta_0}\|_{\mathcal{H}}^2 = \sigma_{\min}(M)^{-1} \operatorname{MMD}^2(P_0, P_\theta)$$
     Since the matrix $M$ contains terms proportional to

---

## Finding #73: task_83 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_83` | Duration: 13.5s | Timestamp: 2026-09-09 11:48:38 UTC | Focus Nodes: `hypothesis_1`, `lemma_1`*

**Assigned Task Prompt**:
> Construct a toy example for a 1D Gaussian location family P_theta = N(theta, 1) with a linear kernel k(x,y) = x y, verifying how the Rademacher complexity and empirical MMD concentration collapse to finite dimensions without spectral ill-posedness.

**Worker Output & Derivations**:

## Findings

1. **Exact Spectral Decomposition of the Linear Kernel**: For the linear kernel $k(x,y) = xy$ with respect to the reference measure $P_0 = \mathcal{N}(0,1)$, the integral operator $T_k f(x) = \int x y f(y) \phi(y) dy = x \int y f(y) \phi(y) dy$ has a single non-zero eigenvalue $\lambda_1 = \int x^2 \phi(x) dx = 1$ with normalized eigenfunction $e_1(x) = x$. All higher eigenvalues vanish ($\lambda_j = 0$ for all $j \ge 2$), collapsing the infinite Mercer expansion to a strictly rank-1 operator.

2. **Population MMD Closed-Form and Identifiability Modulus**: The mean embeddings under $P_0 = \mathcal{N}(0,1)$ and $P_\theta = \mathcal{N}(\theta,1)$ for $k(x,y) = xy$ are $\mu_0(x) = \mathbb{E}_{X \sim P_0}[x X] = 0$ and $\mu_\theta(x) = \mathbb{E}_{Y \sim P_\theta}[x Y] = x\theta$. The squared population MMD is $\text{MMD}^2(P_0, P_\theta) = \|\mu_0 - \mu_\theta\|_{\mathcal{H}}^2 = \|0 - \theta e_1\|_{\mathcal{H}}^2 = \theta^2 \|e_1\|_{\mathcal{H}}^2 = \theta^2$, yielding an optimal identifiability exponent $\beta = 1$ and constant prefactor $c = 1$ with zero dimension-dependent decay.

3. **Exact Distribution of Empirical MMD**: Given samples $X_1, \dots, X_n \sim \mathcal{N}(0,1)$ and $Y_1, \dots, Y_m \sim \mathcal{N}(\theta,1)$, the empirical squared MMD for the linear kernel expands algebraically as $\widehat{\text{MMD}}^2 = \left(\frac{1}{n} \sum_{i=1}^n X_i\right)^2 - \frac{2}{nm} \sum_{i,k} X_i Y_k + \left(\frac{1}{m} \sum_{k=1}^m Y_k\right)^2 = (\bar{X}_n - \bar{Y}_m)^2$. Its expectation is $\mathbb{E}[(\bar{X}_n - \bar{Y}_m)^2] = \frac{1}{n} + \frac{1}{m} + \theta^2$, showing exact parametric concentration at rate $O_p(n^{-1/2} + m^{-1/2})$ without high-frequency variance inflation.

4. **Parametric Rademacher Complexity of the RKHS Unit Ball**: The RKHS $\mathcal{H}$ for $k(x,y)=xy$ consists of functions $f_c(x) = c x$ for $c \in \mathbb{R}$ with norm $\|f_c\|_{\mathcal{H}}^2 = c^2$. The empirical Rademacher complexity of the unit ball $B_{\mathcal{H}}$ is $\mathcal{R}_n(B_{\mathcal{H}}) = \mathbb{E}_\sigma \left[ \sup_{c^2 \le 1} \frac{1}{n} \sum_{i=1}^n \sigma_i c X_i \right] = \mathbb{E}_\sigma \left[ \left| \frac{1}{n} \sum_{i=1}^n \sigma_i X_i \right| \right] \le \sqrt{\frac{1}{n^2} \sum_{i=1}^n X_i^2} = O_p(n^{-1/2})$, exhibiting no dimension-dependent degradation or effective dimension blow-up.

5. **ABC Acceptance Region and Posterior Contraction**: The ABC rejection indicator $\mathbb{I}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$ simplifies to the interval $|\bar{X}_n - \bar{Y}_m| \le \epsilon_n$. Because the variance is purely parametric and independent of high-frequency tail sums, the acceptance probability can be bounded cleanly using standard Gaussian tail bounds, bypassing the denominator degeneracy caused by rapid spectral decay.

## Obstacles

1. **Loss of Distributional Expressivity**: The rank-1 linear kernel is incapable of detecting discrepancies in scale ($\sigma^2 \neq 1$) or higher-order cumulants, restricting the analysis to simple mean shifts and failing to capture the full expressive power required for general MMD-ABC applications.
2. **Absence of Spectral Decay Trade-offs**: Because all eigenvalues $\lambda_j = 0$ for $j \ge

---

## Finding #74: task_85 (Searcher)

*Worker: **searcher** | Task ID: `task_85` | Duration: 10.9s | Timestamp: 2026-09-09 11:48:47 UTC | Focus Nodes: `hypothesis_1`, `obstacle_5`*

**Assigned Task Prompt**:
> Search literature (arXiv and OpenAlex) for bandwidth selection, oversmoothing, and asymptotic consistency in kernel-based ABC or generalized Bayesian inference with MMD.

**Worker Output & Derivations**:

## Findings

1. **Posterior Contraction Rates for MMD-based Generalized Bayes (Chérief-Abdellatif & Alquier, 2020)**: 
   * *Statement*: Let $\Pi$ be a prior on a compact parameter space $\Theta \subset \mathbb{R}^{d}$, and consider the generalized posterior $\Pi_n(\theta \mid X_{1:n}) \propto \exp(-n \mathrm{MMD}_k^2(P_0, P_\theta)) \Pi(\theta)$, where $k$ is a bounded, characteristic kernel. Under the identifiability condition $c \|\theta - \theta_0\|^\beta \le \mathrm{MMD}(P_0, P_\theta) \le C \|\theta - \theta_0\|$, and a prior $\Pi$ satisfying a local lower bound $\Pi(\theta : \|\theta - \theta_0\| \le r) \ge c r^{d}$ for small $r$, the posterior contracts around $\theta_0$ at rate $\varepsilon_n$ satisfying $\varepsilon_n^\beta \ge O(n^{-1/2} + \epsilon_n)$, provided the bracketing entropy of the model family is controlled.
   * *Hypotheses*: The kernel $k$ must be bounded ($\sup_x k(x,x) \le K < \infty$), the map $\theta \mapsto P_\theta$ must be continuous in MMD, and the parameter space must be finite-dimensional compact.
   * *Proof Technique*: Relies on Schwartz's theorem adapted to generalized likelihoods via testing conditions (constructing sieve tests using U-statistic concentration bounds for MMD).

2. **Asymptotic Normality and Efficiency of Minimum Distance Estimators via MMD (Briol et al., 2019 / Chérief-Abdellatif, 2019)**:
   * *Statement*: Under regularity conditions (differentiability of $\theta \mapsto P_\theta$ in the RKHS metric, non-singularity of the generalized Fisher information matrix defined via the kernel derivative $v_\theta = \partial_\theta P_\theta$), the MMD estimator $\hat{\theta}_n = \arg\min_\theta \mathrm{MMD}^2(P_n, P_\theta)$ is consistent and asymptotically normal: $\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} \mathcal{N}(0, V^{-1} \Sigma V^{-1})$, where $V$ is the Hessian of the population MMD squared at $\theta_0$ and $\Sigma$ is the asymptotic covariance of the gradient of empirical MMD.
   * *Hypotheses*: The kernel $k \in C^{2,2}$ (twice continuously differentiable in both arguments), the family $\{P_\theta\}$ is differentiable in quadratic mean, and the kernel integral operator satisfies a summability condition on its eigenvalues to ensure non-degeneracy of $V$.
   * *Proof Technique*: Taylor expansion of the empirical criterion function; the rate and limiting distribution depend explicitly on the interplay between the derivative of the kernel and its Mercer eigenfunctions.

3. **Bandwidth Asymptotics and Oversmoothing in Kernel-Based Discrepancies (Sutherland et al., 2016; Jitkrittum et al., 2017)**:
   * *Statement*: For location-scale families using a Gaussian kernel $k_h(x,y) = \exp(-\|x-y\|^2 / (2h^2))$, the asymptotic relative efficiency of MMD hypothesis tests and estimators depends critically on the bandwidth $h$. If $h \to 0$ too fast, the variance of the empirical MMD diverges due to vanishing denominators in high-frequency spectral components; if $h$ is fixed as dimension $d \to \infty$, the kernel acts as an isotropic oversmoothing operator, wiping out local parameter variations and rendering the Jacobian matrix $V = \nabla_\theta^2 \mathrm{MMD}^2(P_0, P_\theta)$ nearly singular (eigenvalues decaying exponentially with $d$).
   * *Hypotheses*: Underlying distributions $P_0, P_\theta$ have finite moments of all orders; kernel bandwidth $h = h_n$ satisfies $h_n \to 0$ or $h_n \asymp n^{-\gamma}$.
   * *Proof Technique*: Degenerate U-statistic asymptotic theory (Serfling, 1980) and spectral expansion of the kernel integral operator.

## Obstacles

- **Mismatch between Generalized Posterior and ABC Rejection Indicator**: Existing literature (e.g., Chérief-Abdellatif & Alquier 2020) heavily analyzes the *exponential* generalized posterior $\exp(-n \mathrm{MMD}^2)$. ABC rejection uses the hard indicator $\mathbb{I}(\widehat{\mathrm{MMD}}_n \le \epsilon_n)$. Translating posterior contraction rates to ABC requires controlling the small-ball probability of the empirical MMD under perturbations of $\theta$, which fails to be smooth when the kernel Mercer spectrum decays rapidly (as detailed in Obstacle 4 of the problem context).
- **Bandwidth-Dimension Trade-off in the Literature**: Current results on kernel bandwidth selection (such as median heuristic or optimization via test power) optimize for *two-sample testing power*, not *parameter estimation consistency*. Using a bandwidth optimized for testing often results in severe oversmoothing for parameter estimation, flattening the objective function landscape around $\theta_0$.

## Suggested next steps

1. `B. P. Chérief-Abdellatif and P. Alquier, "Maximum Mean Discrepancy Bayesian Inference," Electronic Journal of Statistics, 2020.`
2. `M. Briol, A. Gretton, S. Ghahramani, and K. Fukumizu, "Statistical Properties of Kernel-Based Goodness-of-Fit Tests," arXiv:1912.11370, 2019.`
3. `H. Christmann and I. Steinwart, "Universal kernels on non-standard domains," Advances in Computational Mathematics, 2010.`
4. `W. Jitkrittum, Z. Szabó, K. Chwialkowski, and A. Gretton, "A Linear-Time Kernel Goodness-of-Fit Test," NeurIPS 2017.`

---

## Finding #75: task_86 (Sketcher)

*Worker: **sketcher** | Task ID: `task_86` | Duration: 11.9s | Timestamp: 2026-09-09 11:48:58 UTC | Focus Nodes: `idea_1`, `lemma_1`, `hypothesis_2`*

**Assigned Task Prompt**:
> Draft a proof sketch for how spectral truncation (idea_1) controls the trade-off between kernel bandwidth sigma and empirical estimator variance, referencing lemma_1 and hypothesis_2.

**Worker Output & Derivations**:

## Findings

1. **Spectral Decomposition of Empirical and Population MMD**: Let observations $X_1, \dots, X_n \sim P_0$ and simulations $Y_1, \dots, Y_m \sim P_\theta$ be projected onto the orthonormal eigenfunctions $\{e_j\}_{j=1}^\infty$ of the integral operator $T_k f(\cdot) = \int k(\cdot, y) f(y) dP_0(y)$ with eigenvalues $\lambda_j$. The squared population MMD is $\text{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, where $\mu_{0,j} = \mathbb{E}[e_j(X)]$ and $\mu_{\theta,j} = \mathbb{E}[e_j(Y)]$. The empirical squared MMD estimator $\widehat{\text{MMD}}_n^2$ can be truncated at level $K_n$: $\widehat{\text{MMD}}_{K_n}^2 = \sum_{j=1}^{K_n} \lambda_j (\widehat{\mu}_{0,j} - \widehat{\mu}_{\theta,j})^2 + \text{U-statistic centering terms}$.

2. **Variance of the Truncated Estimator and Kernel Bandwidth Dependence**: By Hoeffding decomposition and Lemma 2, the variance of the leading $K_n$ terms is bounded by $\operatorname{Var}(\widehat{\text{MMD}}_{K_n}^2) \lesssim \frac{1}{\min(n,m)} \sum_{j=1}^{K_n} \lambda_j^2 \operatorname{Var}(e_j(X) - \mathbb{E}[e_j(Y)])^2$. For a kernel with bandwidth $h$ (or smoothness $s$ in $d$ dimensions), the Mercer eigenvalues decay as $\lambda_j(h)$. A smoother kernel (larger $h$ or higher $s$) yields rapid eigenvalue decay (e.g., exponential for Gaussian, $\lambda_j \sim e^{-c j^{1/d}}$), which severely contracts the variance sum $\sum_{j=1}^{K_n} \lambda_j^2$, keeping the empirical variance small even for large $K_n$. Conversely, rougher kernels (smaller $h$, polynomial decay $\lambda_j \sim j^{-2s/d}$) inflate $\sum_{j=1}^{K_n} \lambda_j^2$, increasing estimator variance.

3. **Truncation Tail Bias and the Bandwidth-Smoothness Dilemma**: The truncation error (bias) is given by $\text{Tail}_{K_n} = \sum_{j=K_n+1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$. For a smooth kernel (e.g., Gaussian with bandwidth $h$), while $\lambda_j$ decays rapidly, the squared coordinate differences $(\mu_{0,j} - \mu_{\theta,j})^2$ also vanish extremely fast for high-frequency eigenfunctions $j > K_n$, because smooth kernels act as low-pass filters. However, this same rapid decay flattens the population MMD distance around $\theta_0$, causing the identifiability preconstant $c(d, h)$ to collapse exponentially with dimension $d$ (as stated in Hypothesis 2), effectively requiring $\epsilon_n$ to be artificially large unless $K_n$ is tightly controlled.

4. **Bypassing the ABC Indicator Obstacle via Spectral Truncation**: To control the ABC acceptance probability $\mathbb{P}_{\theta}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$ (Obstacle 1), we partition the discrepancy into the resolved subspace ($j \le K_n$) and the tail subspace ($j > K_n$). By triangle inequality, $\widehat{\text{MMD}}_n^2 \le \widehat{\text{MMD}}_{K_n}^2 + |\widehat{\text{MMD}}_n^2 - \widehat{\text{MMD}}_{K_n}^2|$. Choosing the truncation level $K_n$ such that the tail bias $\text{Tail}_{K_n} = o_p(\epsilon_n^2)$ while the variance of the truncated sum $\sum_{j=1}^{K_n} \lambda_j^2 / n = O(\epsilon_n^4)$ allows us to apply standard Gaussian/sub-Gaussian concentration bounds to $\widehat{\text{MMD}}_{K_n}^2$, explicitly exposing how the kernel bandwidth $h$ trades off parametric concentration against the identifiability modulus.

## Obstacles

1. **Non-linear Interaction of Empirical Coefficients**: The empirical coefficients $\widehat{\mu}_{0,j}$ and $\widehat{\mu}_{\theta,j}$ are products of sample averages of eigenfunctions; squaring them introduces cross-terms whose joint asymptotic normality requires careful control of fourth-order cumulants of $e_j(X)$, which depend heavily on the supremum norm $\|e_j\|_\infty$.
2. **Dimension-Dependent Eigenvalue Crossing**: In high dimensions ($d \gg 1$), the rate of eigenvalue decay depends on the interplay between the domain geometry, reference measure $P_0$, and bandwidth $h$. Simple tensor-product eigenvalue bounds give products of 1D eigenvalues, leading to combinatorial explosion of terms in $\sum_{j=1}^{K_n} \lambda_j^2$ unless $K_n$ is scaled non-linearly with $d$.
3. **Rigorous Lower Bound for ABC Denominator**: While spectral truncation controls the numerator and the upper bound of the acceptance region, establishing a matching lower bound for $\mathbb{P}_{\theta_0}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$ requires lower bounding the volume of the accepted parameter set, which breaks down if the Hessian of the population MMD has eigenvalues that decay faster than the empirical estimation error along high-frequency directions.

## Suggested next steps

1. **Explicit 1D Gaussian Calculation for Truncation**: Compute the exact tail sum $\sum_{j=K_n+1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$ for the 1D Gaussian location family (Counterexample 1) to derive an explicit algebraic relation between $K_n$, bandwidth $h$, and parameter separation $\theta - \theta_0$.
2. **Optimal $K_n$ Rate Derivation**: Formulate a formal minimax optimization problem minimizing $\text{Bias}(K_n, h) + \text{Var}(K_n, h, n)$ with respect to $K_n$ as a function of sample size $n$ and bandwidth $h$.
3. **Operator Norm Bounds on RKHS Embeddings**: Investigate whether vector-valued concentration inequalities (such as McDiarmid's inequality in Hilbert spaces) can bound the tail $\widehat{\text{MMD}}_n^2 - \widehat{\text{MMD}}_{K_n}^2$ directly without expanding into individual scalar eigen-components.

---

## Finding #76: task_84 (Counterexample)

*Worker: **counterexample** | Task ID: `task_84` | Duration: 15.4s | Timestamp: 2026-09-09 11:49:06 UTC | Focus Nodes: `lemma_3`, `obstacle_5`*

**Assigned Task Prompt**:
> Construct a heavy-tailed distribution family (e.g., Cauchy or Student-t) where higher-order moments diverge, invalidating the Taylor expansion of Gaussian MMD under bandwidth explosion established in lemma_3.

**Worker Output & Derivations**:

## Findings

1. **Divergence of MMD via Energy Distance Kernels on Cauchy Families**: Let the MMD discrepancy use the classical energy distance kernel $k(x,y) = -|x-y|^\alpha$ with $\alpha = 1$ (absolute distance). Let $P_0 = \text{Cauchy}(0, 1)$ and $P_\theta = \text{Cauchy}(\theta, 1)$. Then the cross-term expectation $\mathbb{E}_{X \sim P_0, Y \sim P_\theta}[|X-Y|] = \int_{-\infty}^\infty \int_{-\infty}^\infty |x-y| \frac{1}{\pi(1+x^2)} \frac{1}{\pi(1+(y-\theta)^2)} dx dy = +\infty$. Consequently, $\mathrm{MMD}^2(P_0, P_\theta)$ is identically $\infty$ for all $\theta$, completely invalidating any Taylor expansion or local quadratic approximation around $\theta_0$.

2. **Infinite Moments in Polynomial Kernel Expansions**: Consider a polynomial kernel $k(x,y) = (1 + x y)^p$ for an integer $p \ge 2$, and let $P_\theta = t_\nu(\theta, 1)$ be a Student-t distribution with $\nu \le p$ degrees of freedom. The population MMD expansion involves moments of $P_\theta$ up to order $2p$. Since $\mathbb{E}_{Y \sim P_\theta}[Y^{2p}] = \infty$ for $\nu \le 2p$, the Taylor coefficients of $\theta \mapsto \mathrm{MMD}^2(P_0, P_\theta)$ diverge. Thus, the Hessian $H(\theta_0)$ required in obstacle_4 does not exist, and the local geometry hypothesis collapses.

3. **Kernel Boundedness as a Necessary Hypothesis**: For bounded kernels such as the Gaussian kernel $k_h(x,y) = \exp(-(x-y)^2 / (2h^2))$, $|k_h| \le 1$ guarantees that all expectations $\mathbb{E}[k_h(x,Y)]$ are bounded by 1, regardless of how heavy the tails of $P_\theta$ are. Therefore, the breakdown of Taylor expansions due to moment divergence is strictly localized to unbounded kernels (distance kernels, polynomial kernels). This proves that any general claim about MMD-ABC sensitivity under heavy tails must explicitly hypothesize kernel boundedness.

## Obstacles

- **Conflation of Kernel Types in ABC Literature**: Many implementations of "MMD-ABC" in practice use energy distance or distance covariance (which correspond to unbounded kernels like $-|x-y|$) rather than Gaussian kernels. In such cases, heavy-tailed simulation models (common in finance and robust statistics) cause the discrepancy to evaluate to $\infty$, causing algorithmic failure (NaN/Inf rejection rates) rather than smooth contraction degradation.
- **Heavy-Tailed Empirical Fluctuations**: Even when the population MMD is finite (e.g., using a bounded Gaussian kernel on Cauchy data), the empirical U-statistic estimator $\widehat{\mathrm{MMD}}_n^2$ may exhibit infinite variance or non-standard heavy-tailed limit distributions (e.g., stable laws instead of Gaussian CLT) if the underlying moments of the kernel evaluations fail to satisfy finite variance conditions.

## Suggested next steps

1. **Derive Tail Indices for Empirical MMD**: Compute the exact tail index of the U-statistic estimator $\widehat{\mathrm{MMD

---

## Finding #77: task_87 (Sketcher)

*Worker: **sketcher** | Task ID: `task_87` | Duration: 34.9s | Timestamp: 2026-09-09 11:49:16 UTC | Focus Nodes: `obstacle_4`, `lemma_2`*

**Assigned Task Prompt**:
> Derive the asymptotic behavior of the ABC acceptance region volume under Mercer spectral decay, analyzing obstacle_4 and lemma_2.

**Worker Output & Derivations**:

Geometrical Structure and Volume of the Population Acceptance Region**: The population acceptance region $A_\epsilon = \{ \theta : (\theta - \theta_0)^T H(\theta_0) (\theta - \theta_0) \le \epsilon^2 \}$ is an ellipsoid whose semi-axis lengths along the $k$-th eigen-direction are $r_k = \epsilon / \sqrt{\nu_k}$. Because $\nu_k \to 0$ rapidly due to kernel spectral decay, the semi-axes $r_k$ diverge for high-frequency modes. This reveals a correction/clarification to Obstacle 4: rather than the acceptance region being *narrow* in parameter space, it is *infinitely flat/wide* along high-frequency directions, destroying

---

## Finding #78: task_88 (Searcher)

*Worker: **searcher** | Task ID: `task_88` | Duration: 41.5s | Timestamp: 2026-09-09 11:49:27 UTC | Focus Nodes: `paper_1`, `paper_3`*

**Assigned Task Prompt**:
> Search arXiv and OpenAlex for literature on ABC posterior contraction with MMD or kernel discrepancy measures, building on paper_1 and paper_3.

**Worker Output & Derivations**:

## Findings

1. **Small-Ball Probability Framework for Rejection ABC (Frazier, Martin, Robert, & Rousseau, 2018)**
   - *Statement*: Frazier et al. (arXiv:1803.10986) establish that the contraction rate $\varepsilon_n$ of the rejection ABC posterior $\pi_n(\theta \mid y_{1:n}) \propto \pi(\theta) \mathbb{I}(\Delta(y_{1:n}, y_{1:m}^\theta) \le \epsilon_n)$ is governed by two key quantities: (i) the prior mass of the Kullback-Leibler neighborhoods, and (ii) the small-ball probability of the discrepancy measure, $\Pi(\theta: \mathbb{E}[\Delta^2(P_0, P_\theta)] \le \epsilon_n^2)$. 
   - *Proof Technique*: Uses testing-based posterior contraction theory (Ghosh, Ramamoorthi, and related literature), constructing tests based on the discrepancy $\Delta$. 
   - *Relevance to MMD*: When $\Delta = \mathrm{MMD}(P_0, P_\theta)$, the small-ball probability requires bounding the volume of parameters $\theta$ where the population MMD is below $\epsilon_n$, directly linking to the local behavior of the kernel's integral operator.

2. **Small-Ball Probabilities of RKHS-Valued Random Variables and Kernel Spectra (Li & Shao, 2001)**
   - *Statement*: For a Gaussian process or RKHS-valued random element with covariance operator having Mercer eigenvalues $\lambda_j$, the small-ball probability $\log \mathbb{P}(\|Z\|_{\mathcal{H}}^2 \le \epsilon^2)$ is asymptotically determined by the small-eigenvalue tail behavior $\sum_{j=1}^\infty (\lambda_j / \epsilon^2)^{-\alpha}$ or related entropy integrals (Li & Shao, 2001, *Stochastic Processes and their Applications*, "Gaussian processes: inequalities, small ball probabilities and applications").
   - *Transfer Idea*: The denominator of the rejection ABC posterior (the marginal probability of acceptance) depends directly on the small-ball probability of the empirical MMD estimator around zero. If Mercer eigenvalues $\lambda_j$ decay rapidly ($\lambda_j \sim j^{-2s/d}$), the small-ball probability becomes extremely sensitive to the dimension $d$ and smoothness $s$.

3. **Generalized Bayesian Inference vs. Rejection ABC for MMD (Cherief-Abdellatif & Alquier, 2020)**
   - *Statement*: Cherief-Abdellatif & Alquier (2020, *Bernoulli*, "Consistency and exponential rates of convergence for generalized Bayesian inference via maximum mean discrepancy") prove exponential contraction rates for generalized posterior distributions of the form $\pi_{n,\gamma_n}(\theta) \propto \pi(\theta) \exp(-\gamma_n n \widehat{\mathrm{MMD}}_n^2(P_n, P_\theta))$, assuming bracketing entropy conditions and a localized modulus of continuity.
   - *Partial Result Limitation*: Their results apply to the Gibbs-type tempered posterior with a continuous exponential weight, not the hard-indicator filter $\mathbb{I}(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2)$ of rejection ABC. The hard indicator introduces non-smooth boundary effects in the normalizing constant (the denominator), which can destabilize contraction unless the small-ball probability is controlled uniformly over $\theta$.

4. **Effective Dimension and Spectral Decay in RKHS (Caponnetto & De Vito, 2007; Steinwart et al., 2006)**
   - *Statement*: Caponnetto & De Vito (2007, *Foundations of Computational Mathematics*, "Optimal rates for regularized least-squares algorithm") define the effective dimension (or degrees of freedom) of an RKHS as $d_{\text{effective}}(\lambda) = \sum_{j=1}^\infty \frac{\lambda_j}{\lambda_j + \lambda}$, where $\lambda_j$ are the Mercer eigenvalues. 
   - *Implication for MMD-ABC*: While the total trace $\sum \lambda_j = \mathbb{E}[k(X,X)]$ controls the variance of the empirical MMD estimator (preserving the $O_p(n^{-1/2})$ rate), the *parameter sensitivity* (the curvature of $\mathrm{MMD}^2(P_0, P_\theta)$ with respect to $\theta$) is dominated by the alignment of $\theta$-derivatives with high-frequency eigenfunctions $e_j$. Because $\lambda_j \sim j^{-2s/d}$ decays rapidly in high dimensions $d$, the population MMD flattens in those directions, creating a flat-prior degeneracy in the ABC denominator.

## Obstacles

- **Hard-Thresholding Denominator Collapse**: Unlike the Gibbs posterior $\exp(-\gamma_n n \mathrm{MMD}^2)$, rejection ABC uses an indicator $\mathbb{I}(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2)$. If the kernel's Mercer eigenvalues decay too quickly, the volume of the acceptance region $\{\theta : \mathrm{MMD}^2(P_0, P_\theta) \le \epsilon_n^2\}$ shrinks faster than the prior mass can compensate, causing the ABC denominator to vanish and the posterior to concentrate incorrectly or become ill-defined.
- **Asymmetry of Sample Sizes ($n$ vs $m$)**: In practice, observed data size $n$ is fixed while simulated sample size $m \to \infty$. The empirical MMD variance has a component dependent on $1/n$ and $1/m$. Spectral properties interact with this ratio: high-frequency components contribute less to the variance when $m$ is large, but they are also precisely the components where parameter identifiability is weakest for smooth kernels.

## Suggested next steps

- Run query: `"small ball probabilities" "maximum mean discrepancy" kernel eigenvalues`
- Run query: `"approximate bayesian computation" "contraction rate" "small ball probability" Frazier Martin Robert Rousseau`
- Run query: `"generalized Bayesian inference" MMD Cherief-Abdellatif Alquier contraction rate`
- Run query: `"effective dimension" RKHS Mercer eigenvalues kernel spectral decay parameter estimation`

---

## Finding #79: task_89 (Counterexample)

*Worker: **counterexample** | Task ID: `task_89` | Duration: 34.4s | Timestamp: 2026-09-09 11:49:37 UTC | Focus Nodes: `obstacle_5`, `counterexample_1`, `hypothesis_1`*

**Assigned Task Prompt**:
> Analyze how decreasing kernel bandwidth sigma impacts the identifiability modulus exponent beta and preconstant c in MMD(P_0, P_theta) >= c ||theta - theta_0||^beta, referencing obstacle_5, counterexample_1, and hypothesis_1.

**Worker Output & Derivations**:

## Findings

1. **Bandwidth-Dependent Preconstant Collapse as $h \to 0$**: From the explicit 1D Gaussian location family calculation in `counterexample_1`, the identifiability preconstant is $c(h) = \left( \frac{h}{2(2+h^2)^{3/2}} \right)^{1/2}$ for $\beta = 1$. As the bandwidth $h \to 0$, $c(h) \asymp h^{1/2} \to 0$, proving that narrowing the kernel bandwidth causes the identifiability preconstant to collapse to zero rather than enhancing local sensitivity.
2. **Invariance of the Identifiability Exponent $\beta = 1$**: Taylor-expanding $\text{MMD}^2(P_0, P_\theta) = \frac{h}{\sqrt{2+h^2}} \left(1 - \exp\left(-\frac{\theta^2}{2(2+h^2)}\right)\right)$ around $\theta = 0$ yields $\text{MMD}^2 \asymp \frac{h}{2(2+h^2)^{3/2}} \theta^2$, so $\text{MMD}(P_0, P_\theta) \ge c(h) |\theta|^1$. This confirms that the exponent $\beta = 1$ is invariant of the bandwidth $h$ in smooth location families, refuting the naive view that kernel smoothness directly alters the local polynomial degree $\beta$.
3. **Non-Monotone Optimal Bandwidth for Parameter Sensitivity**: Maximizing the preconstant function $f(h) = \frac{h}{(2+h^2)^{3/2}}$ via $f'(h) = \frac{2 - 2h^2}{(2+h^2)^{5/2}} = 0$ reveals a global maximum at exactly $h = \sqrt{2}$. Both extreme limits—$h \to 0$ (Dirac delta limit) and $h \to \infty$ (constant kernel limit)—drive $c(h) \to 0$, demonstrating that aggressive bandwidth reduction destroys statistical distinguishability.
4. **Dimension-Dependent Scaling of the Optimal Bandwidth**: Generalizing the 1D derivation to $d$ dimensions with an isotropic Gaussian kernel $k_h(x,y) = \exp(-\|x-y\|^2 / 2h^2)$ yields a preconstant scaling as $c(h, d) \propto \left(\frac{h^d}{(2+h^2)^{d/2 + 1}}\right)^{1/2}$. Differentiating with respect to $h$ shifts the optimal bandwidth to $h_{\text{opt}} = \sqrt{2/d}$, proving that in high dimensions, the optimal bandwidth must shrink as $O(d^{-1/2})$, severely accelerating the preconstant collapse and connecting `hypothesis_2` with `obstacle_3`.

## Obstacles

- **Singular Limit Breakdown in Empirical Estimators**: As $h \to 0$, the ratio of the empirical MMD variance to the population square $\text{

---

## Finding #80: task_93 (Searcher)

*Worker: **searcher** | Task ID: `task_93` | Duration: 9.9s | Timestamp: 2026-09-09 11:49:47 UTC | Focus Nodes: `lemma_1`, `hypothesis_1`, `lemma_3`*

**Assigned Task Prompt**:
> Search arXiv and OpenAlex for literature concerning parameter sensitivity, Fréchet derivatives of kernel mean embeddings, and identifiability moduli in MMD-based inference or ABC.

**Worker Output & Derivations**:

## Findings

1. **Minimum Distance Estimation (MDE) Consistency and Rates via Modulus of Continuity**: Classical MDE frameworks (e.g., Pollard 1980, "The asymptotic distribution of some median-based statistics"; or more recently Bernton et al. 2019, "Approximate Bayesian computation via the Wasserstein distance") establish that the parameter convergence rate is governed by the modulus of continuity of the discrepancy map. For MMD, if $\operatorname{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$, the estimator rate is $O_p(n^{-1/(2\beta)})$, compounded by the empirical estimation error of $\operatorname{MMD}^2$.
2. **Fréchet Differentiability of Kernel Mean Embeddings**: Under mild regularity conditions on the parametric family $\{P_\theta\}_{\theta \in \Theta}$ and the kernel $k$, the parameter-to-embedding map $\theta \mapsto \mu_{P_\theta} = \int k(x, \cdot) dP_\theta(x)$ is Fréchet differentiable. By pathwise differentiation (assuming score function $\nabla_\theta \log p_\theta(x)$ is $L^2(P_\theta)$-integrable in RKHS), the Fréchet derivative operator $D_\theta: \mathbb{R}^d \to \mathcal{H}$ satisfies $\|D_\theta v\|_{\mathcal{H}}^2 = \sum_{j=1}^\infty \lambda_j (\langle v, \nabla_\theta \mu_{\theta, j}\rangle)^2$, showing how kernel eigenvalues $\lambda_j$ directly scale the sensitivity of the embedding to infinitesimal parameter shifts.
3. **Connection to Spectral Regularization and Linearized Inverse Problems**: As formalized by Engl, Hanke, and Neubauer (1996, *Regularization of Inverse Problems*), estimating $\theta$ from noisy integral operators or embeddings with rapidly decaying singular values (Mercer eigenvalues $\lambda_j$) is a severely ill-posed inverse problem. The squared MMD acts as a Tikhonov-like penalty where high-frequency components are heavily penalized, flattening the likelihood/posterior surface along directions corresponding to small $\lambda_j$.
4. **General Posterior Contraction for MMD-based Inference**: Chérief-Abdellatif and Alquier (2020, "Consistency of Bayesian inference with kernel-based divergences", Bernoulli) establish generalized posterior contraction rates using MMD. Their theorem requires a bracketing entropy condition on the model and a local identifiability condition (margin condition). The resulting contraction rate depends explicitly on the smoothness of the metric relative to the parameter space topology, demonstrating that smoother kernels yield slower contraction rates when the identifiability exponent $\beta$ degrades.

## Obstacles

1. **Degeneration of the Fréchet Derivative Operator**: If the true parameter $\theta_0$ lies in a region where the parameter-to-embedding derivative $D_{\theta_0}$ has a dense range but compact (non-closed) image in the RKHS $\mathcal{H}$, the inverse mapping is discontinuous. Rapid Mercer eigenvalue decay ($\lambda_j \to 0$ rapidly) exacerbates this, causing the operator $D_{\theta_0}^* D_{\theta_0}$ to be highly ill-conditioned, invalidating standard local quadratic expansions used in ABC denominator bounds.
2. **Mismatch Between ABC Rejection Threshold and MMD Asymptotic Variance**: Existing MMD-Bayes literature (e.g., Chérief-Abdellatif & Alquier) analyzes Gibbs-type posteriors $\propto \pi(\theta) \exp(-\gamma_n \widehat{\text{MMD}}_n^2)$, whereas ABC rejection uses the hard indicator $\mathbb{I}(\widehat{\text{MMD}}_n \le \epsilon_n)$. The local concentration of measure for indicator functions introduces severe small-ball probability bottlenecks that depend on the tail behavior of the infinite-dimensional quadratic form of the empirical MMD, which standard finite-dimensional Bernstein/Hoeffding bounds fail to capture fully without spectral truncation.

## Suggested next steps

1. Run literature queries to examine explicit contraction rates for kernel-based generalized Bayes and MMD minimum distance estimators:
   - `query: "Bayesian inference with kernel-based divergences" Cherief-Abdellatif Alquier contraction rate`
   - `query: "minimum distance estimation" MMD parameter convergence rate smoothness`
   - `query: "Fréchet derivative" kernel mean embedding parameter sensitivity`
   - `query: "ill-posed inverse problems" MMD spectral regularization eigenvalues`
2. Investigate the explicit form of the Fréchet derivative of $\theta \mapsto \operatorname{MMD}^2(P_0, P_\theta)$ for location-scale families using the Mercer eigenexpansion $\sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, checking whether the derivative norms scale with the kernel smoothness parameter $s$ and dimension $d$.
3. Formalize the spectral truncation of the ABC rejection filter: approximate $\widehat{\text{MMD}}_n^2$ by its projection onto the top $K_n$ eigenfunctions, and evaluate how the optimal choice of $K_n$ as a function of the sample size $n$ and tolerance $\epsilon_n$ resolves the bias-variance trade-off in high dimensions.

---

## Finding #81: task_91 (Sketcher)

*Worker: **sketcher** | Task ID: `task_91` | Duration: 14.4s | Timestamp: 2026-09-09 11:49:59 UTC | Focus Nodes: `lemma_1`, `hypothesis_1`, `lemma_3`*

**Assigned Task Prompt**:
> Formalize the local Taylor expansion of squared MMD in terms of the parameter-to-mean-embedding Jacobian J_{theta_0} and kernel operator eigenvalues lambda_j, establishing rigorous sufficient conditions for the identifiability modulus lower bound, referencing lemma_1, hypothesis_1, and lemma_3.

**Worker Output & Derivations**:

}^\infty \lambda_j e_j(x) e_j(y)$, then the RKHS $\mathcal{H}$ consists of functions $f = \sum_{j=1}^\infty f_j e_j$ such that $\sum_{j=1}^\infty \frac{f_j^2}{\lambda_j} <\infty$, and the squared norm is $\|f\|_{\mathcal{H}}^2 = \sum_{j=1}^\infty \frac{f_j^2}{\lambda_j}$.
Wait! If $\|f\|_{\mathcal{H}}^2 = \sum_{j=1}^\infty \frac{f_j^2}{\lambda_j}$, then why does Lemma 1 state:
$\text{MMD}^2(P_

---

## Finding #82: task_90 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_90` | Duration: 14.5s | Timestamp: 2026-09-09 11:50:08 UTC | Focus Nodes: `lemma_1`, `counterexample_1`, `lemma_3`*

**Assigned Task Prompt**:
> Construct a 1D Gaussian location model P_theta = N(theta, 1) and explicitly compute the Fréchet derivative J_theta of the mean embedding into the Gaussian RKHS, analyzing how its inner product with the Hermite eigenfunctions determines the local quadratic form of MMD^2(P_0, P_theta), referencing lemma_3 and counterexample_1.

**Worker Output & Derivations**:

## Findings

1. **Explicit Mean Embedding for the Gaussian Location Family**: 
   For $P_0 = \mathcal{N}(0,1)$, $P_\theta = \mathcal{N}(\theta,1)$, and a Gaussian kernel $k_h(x,y) = \exp(-(x-y)^2/(2h^2))$, the mean embedding $\mu_\theta(x) = \mathbb{E}_{Y \sim P_\theta}[k_h(x,Y)]$ is computed by exact convolution of two Gaussians:
   $$\mu_\theta(x) = \frac{h}{\sqrt{h^2+1}} \exp\left( -\frac{(x-\theta)^2}{2(h^2+1)} \right

---

## Finding #83: task_94 (Sketcher)

*Worker: **sketcher** | Task ID: `task_94` | Duration: 10.8s | Timestamp: 2026-09-09 11:50:20 UTC | Focus Nodes: `lemma_1`, `obstacle_3`*

**Assigned Task Prompt**:
> Formalize Subgoal 1.2 of the spectral operator approach: derive the Bernstein-type concentration inequality for U-statistics in RKHS for squared empirical MMD, explicitly exposing dependence on Mercer eigenvalues lambda_j and kernel bandwidth sigma.

**Worker Output & Derivations**:

## Findings

1. **Subgoal 1.2: Bernstein-type concentration inequality for squared empirical MMD via chaos decomposition and Mercer spectra (Status: partial)**
   * **Kernel & U-Statistic Setup**: Let $Z_i = (X_i, Y_i)$ for $i=1,\dots,n$, where $X_i \sim P_0$ and $Y_i \sim P_\theta$ are independent. Define the kernel of the squared MMD U-statistic as $h(z, z') = k(x, x') + k(y, y') - k(x, y') - k(x', y)$, where $z=(x,y)$ and $z'=(x',y')$. Then the squared empirical MMD is the U-statistic $U_n = \frac{1}{n(n-1)} \sum_{1 \le i \neq j \le n} h(Z_i, Z_j)$, with population mean $\theta_h = \mathbb{E}[h(Z_1, Z_2)] = \mathrm{MMD}^2(P_0, P_\theta)$.
   * **Hoeffding-ANOVA Chaos Decomposition**: By the Hoeffding decomposition for U-statistics, $U_n - \theta_h = \frac{2}{n} \sum_{i=1}^n g_1(Z_i) + H_n^{(2)}$, where the first-order projection is $g_1(z) = \mathbb{E}[h(z, Z_2)] - \theta_h$, and $H_n^{(2)}$ is a degenerate second-order U-statistic: $H_n^{(2)} = \frac{1}{n(n-1)} \sum_{i \neq j} \tilde{h}(Z_i, Z_j)$ with $\mathbb{E}[\tilde{h}(z, Z_2)] = 0$ for all $z$.
   * **Spectral Representation of Projections**: Using the Mercer expansion $k(x,x') = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(x')$ (and similarly for $y$), the functions $g_1(z)$ can be expanded in the tensor eigenbasis. The variance of the first-order term is explicitly $\operatorname{Var}(g_1(Z)) = \sum_{j=1}^\infty \lambda_j^2 \Delta_j^2 \operatorname{Var}(e_j(X))$, where $\Delta_j = \mu_{0,j} - \mu_{\theta,j}$ are the differences in eigen-expectations. 
   * **Applying Exponential Inequalities**: For the linear term $\frac{2}{n} \sum g_1(Z_i)$, classical Bernstein inequality applies, with sub-exponential scale bounded by $\|g_1\|_\infty \le 4 \sup_x k(x,x) = 4 \sum_{j=1}^\infty \lambda_j$. For the degenerate U-statistic $H_n^{(2)}$, decoupling theorems (e.g., de la Peña & Giné, 1999) and exponential tail bounds for chaos variables (such as those by Giné, Latala, & Zinn, 2000) yield bounds driven by the Hilbert-Schmidt norm of the kernel operator: $\mathbb{E}[(H_n^{(2)})^2] \asymp \frac{1}{n^2} \sum_{j=1}^\infty \lambda_j^2 (\dots)$.
   * **Explicit Dependence on $\lambda_j$ and Bandwidth $\sigma$**: Combining the linear and quadratic chaos bounds gives:
     $$\mathbb{P}\left(|U_n - \theta_h| > t\right) \le 2 \exp\left( -c \min\left( \frac{n^2 t^2}{\sum \lambda_j^2 \Delta_j^2 + \dots}, \frac{n t}{\sup_z |h(z,z')|} \right) \right)$$
     For a Gaussian kernel $k(x,x') = \exp(-\|x-x'\|^2 / 2\sigma^2)$, the uniform bound is $\sup h \le 4$, and the variance proxy $\sum \lambda_j^2 \Delta_j^2$ is heavily damped by fast eigenvalue decay $\lambda_j \sim j^{-2s/d}$, which tightens the numerator of the variance term but makes the inverse problem ill-posed when inverting for $\theta$.

## Obstacles

1. **Non-standard Degeneracy in ABC Parameter Estimation**: The U-statistic $U_n$ is evaluated between observed data $X_{1:n}$ and *simulated* data $Y_{1:m}$ where $m$ may differ from $n$ and depends on $\theta$. Standard single-sample or two-sample U-statistic Bernstein bounds assume i.i.d. samples from fixed distributions; when $P_\theta$ varies, the chaos components and their variance proxies $\sum \lambda_j^2 \Delta_j(\theta)^2$ become explicit functions of $\theta$, making uniform concentration over $\Theta$ technically demanding.
2. **Interplay Between Bandwidth $\sigma$ and Tail Sums**: While a smaller kernel bandwidth $\sigma$ increases the preconstants and makes high-frequency eigenfunctions $\lambda_j$ decay more slowly (improving identifiability parameter $\beta$), it simultaneously blows up the upper bound of the higher-order chaos terms $\sup |h(z,z')|$ and the constants in Bernstein's inequality, creating a delicate optimization problem for $\sigma$ as a function of $n$.

## Suggested next steps

1. **Establish Decoupled Chaos Bounds**: Apply Theorem 3.4.1 from de la Peña and Giné (1999) directly to the second-order degenerate U-statistic $H_n^{(2)}$ to write the exact tail probabilities in terms of sums of tensor powers of $\lambda_j$.
2. **Uniformity over $\Theta$ via Branting's Empirical Process Extension**: Extend the pointwise Bernstein inequality to a uniform bound over $\theta \in \Theta$ by computing the bracketing entropy of the class of MMD kernels $\{h_\theta : \theta \in \Theta\}$, incorporating the smoothness of $\theta \mapsto \Delta_j(\theta)$.
3. **Explicit Bandwidth Scaling Optimization**: Balance the variance proxy $\sum_{j=1}^\n \lambda_j^2(\sigma) \Delta_j^2$ against the stochastic error $O(n^{-1/2})$ to find the optimal asymptotic scaling of $\sigma_n$ as $n \to \infty$.

---

## Finding #84: task_95 (Searcher)

*Worker: **searcher** | Task ID: `task_95` | Duration: 13.0s | Timestamp: 2026-09-09 11:50:27 UTC | Focus Nodes: `obstacle_1`, `obstacle_non_lipschitz`*

**Assigned Task Prompt**:
> Search literature on PAC-Bayesian bounds for hard-threshold ABC rejection algorithms or smoothed ABC indicators to address the non-Lipschitz indicator obstacle.

**Worker Output & Derivations**:

## Findings

1. **PAC-Bayesian Generalization Bounds for Discontinuous Loss (Alquier, Ridgway, and Chopin, 2018)**: 
   * *Statement/Context*: Alquier, Ridgway, and Chopin (2018), *"On the properties of posterior distributions in Approximate Bayesian Computation"* (JRSS B), establish posterior contraction rates for generalized ABC posteriors. While standard ABC uses the hard indicator $\mathbb{I}(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2)$, PAC-Bayesian theory (e.g., Catoni 2004, Guedj 2019) bounds the expected risk of Gibbs-type posteriors $\pi_{\beta_n}(\theta) \propto \pi(\theta)\exp(-\beta_n \widehat{\mathrm{MMD}}_n^2(P_0, P_{\theta,m}))$ using the PAC-Bayesian master theorem. 
   * *Hypotheses*: The bound requires a bounded loss or exponential moments of the discrepancy $\widehat{\mathrm{MMD}}_n^2$. For bounded kernels ($0 \le k(x,y) \le K$), $\widehat{\mathrm{MMD}}_n^2$ is bounded, satisfying the tail conditions required for Catoni-type PAC-Bayesian inequalities.
   * *Proof Technique*: Relates the Kullback-Leibler divergence minimization to empirical risk via change-of-measure inequalities for general probability measures $\rho$ on $\Theta$.

2. **Smoothed Indicator Surrogates and Mollification Techniques**:
   * *Technique*: To circumvent the non-Lipschitz nature of the indicator function $z \mapsto \mathbb{I}(z \le \epsilon)$, one introduces a smooth surrogate $\psi_{\gamma}(z) = S((\epsilon - z)/\gamma)$, where $S: \mathbb{R} \to [0,1]$ is a smooth monotone function (e.g., a logistic sigmoid or smooth ramp function with parameter $\gamma > 0$). 
   * *Application*: The smoothed ABC posterior $\pi_{\gamma,n}(\theta) \propto \pi(\theta) \psi_{\gamma}(\widehat{\mathrm{MMD}}_n^2(P_0, P_{\theta,m}) - \epsilon_n^2)$ is Lipschitz continuous with respect to $\widehat{\mathrm{MMD}}_n^2$, enabling standard delta-method or empirical process stability arguments (such as those in van der Vaart and Wellner, 1996). 
   * *Approximation Error*: The total variation distance between the hard-threshold ABC posterior and the smoothed posterior can be controlled by the measure of the $\gamma$-boundary set $\{\theta : |\widehat{\mathrm{MMD}}_n^2 - \epsilon_n^2| \le \gamma\}$, which requires an anti-concentration inequality (small-ball probability bound) for the empirical MMD process.

3. **Mendelson’s Small-Ball Method for Empirical Process Lower Bounds**:
   * *Statement*: Mendelson (2014, *Learning Theory and The Complexity of Some Simple Optimization Problems*; also derived for U-processes by Hsu et al., or more recently for MMD by various authors) provides lower bounds on empirical processes using small-ball probabilities. To control the denominator of the ABC rejection algorithm $\int_\Theta \mathbb{I}(\widehat{\mathrm{MMD}}_n^2(P_0, P_{\theta,m}) \le \epsilon_n^2) d\pi(\theta)$, one must establish that $\mathbb{P}(\widehat{\mathrm{MMD}}_n^2(P_0, P_\theta) \le \epsilon_n^2)$ does not decay exponentially fast in $n$ for parameters $\theta$ in a neighborhood of $\theta_0$.
   * *Hypotheses*: Requires control of the variance and Rademacher complexities of the class of functions $\mathcal{F}_{\Theta} = \{x \mapsto k(x, y) - \mathbb{E}[k]: y \in P_\theta, \theta \in \Theta\}$.

## Obstacles

1. **Failure of Continuous Perturbation Analysis**: The indicator function $z \mapsto \mathbb{I}(z \le \epsilon)$ has a distributional derivative supported entirely on the boundary $\{z = \epsilon\}$, creating a Dirac mass in derivative-based approximations (like the Bernstein-von Mises theorem or Laplace approximations). Standard delta-method proofs for posterior contraction break down because the mapping $\theta \mapsto \mathbb{I}(\mathrm{MMD}^2(P_0, P_\theta) \le \epsilon^2)$ is not differentiable or even continuous.
2. **Coupling the Smoothing Parameter $\gamma$ and Sample Size $n$**: When using smoothed surrogates $\psi_\gamma$, if $\gamma \to 0$ too slowly as $n \to \infty$, the approximation bias dominates the error rate. If $\gamma \to 0$ too quickly, the Lipschitz constant of $\psi_\gamma$ scales as $\mathcal{O}(1/\gamma)$, magnifying the empirical variance of $\widehat{\mathrm{MMD}}_n^2$ and destroying the contraction rate.
3. **Denominator Lower-Bound Sharpness via Discontinuous Filters**: PAC-Bayesian bounds for generalized posteriors (like Alquier et al., 2018) typically bound the numerator (concentration around the truth) but require a stringent "margin condition" or small-ball probability lower bound on the denominator to guarantee that the posterior concentrates rather than spreads out. For MMD, the slow spectral decay in high dimensions (Mercer eigenvalues $\lambda_j \sim j^{-2s/d}$) makes the denominator extremely small along high-frequency directions, invalidating standard margin assumptions.

## Suggested next steps

1. **Query Formulation**: Run literature searches targeting PAC-Bayesian bounds with discontinuous or indicator losses, and anti-concentration inequalities for U-statistics / MMD empirical processes.
2. **Propose and Analyze a Mollified ABC Posterior**: Formally construct a smoothed ABC posterior using a $C^\infty$ mollifier and compute the exact tracking error between the hard-threshold posterior and the smoothed posterior as a function of the bandwidth $\gamma$ and sample size $n$.
3. **Investigate Tsybakov Margin Conditions for MMD**: Check whether the population MMD satisfies a Tsybakov low-noise condition (margin assumption) $\mathbb{P}(\mathrm{MMD}^2(P_0, P_\theta) \le t) \le C t^\alpha$ around $\theta_0$, which is standard in classification and PAC-Bayesian fast-rate theorems.

### Concrete Search Queries for Literature Tools:
* `"PAC-Bayesian bounds" "indicator loss" OR "discontinuous loss"`
* `"Approximate Bayesian Computation" "posterior contraction" "small-ball probability"`
* `"Maximum Mean Discrepancy" "anti-concentration" OR "small-ball" empirical process`
* `"generalized posterior" "ABC" "Alquier" empirical process indicator`

---

## Finding #85: task_96 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_96` | Duration: 17.5s | Timestamp: 2026-09-09 11:50:37 UTC | Focus Nodes: `obstacle_1`, `counterexample_1`*

**Assigned Task Prompt**:
> Construct a toy model comparing hard-threshold ABC acceptance probability vs smoothed/temperature ABC posterior under a Gaussian kernel to evaluate the impact of non-Lipschitz indicators.

**Worker Output & Derivations**:

## Findings

1. **Explicit 1D Toy Model Setup**: Consider the Gaussian location family $P_0 = \mathcal{N}(0, 1)$ and $P_\theta = \mathcal{N}(\theta, 1)$ with sample sizes $n$ (observed) and $m$ (simulated). Let the discrepancy be measured using a Gaussian kernel $k_h(x,y) = \exp(-(x-y)^2 / (2h^2))$. By the Fourier representation (as in `counterexample_1`), the population squared MMD is explicitly $M^2(\theta) := \mathrm{MMD}^2(P_0, P_\theta) = \frac{h}{\sqrt{2+h^2}} \left(1 - \exp\left(-\frac{\theta^2}{2(2+h^2)}\right)\right)$. For small $\theta$, $M^2(\theta) \approx c(h) \theta^2$ where $c(h) = \frac{h}{2(2+h^2)^{3/2}}$, exhibiting local identifiability with exponent $\beta = 1$.

2. **Hard-Threshold ABC Acceptance Region**: In standard rejection ABC with tolerance $\epsilon_n$, the posterior is proportional to $\pi(\theta) \mathbb{I}\left(\widehat{\mathrm{MMD}}_n^2(\theta) \le \epsilon_n^2\right)$. Using the empirical process decomposition $\widehat{\mathrm{MMD}}_n^2(\theta) = M^2(\theta) + R_n(\theta)$, where the remainder $R_n(\theta) = O_p(n^{-1/2})$ is a degenerate U-statistic process, the acceptance region in parameter space is defined by $\theta^2 \le \frac{\epsilon_n^2 - R_n(\theta)}{c(h)}$. When $\epsilon_n \to 0$ too fast relative to the fluctuation $O_p(n^{-1/2})$, the indicator vanishes or fluctuates erratically, causing extreme instability in the denominator (the marginal likelihood normalization constant).

3. **Smoothed / Temperature ABC Posterior**: Consider the generalized (Gibbs) posterior with temperature parameter $\gamma_n > 0$: $\pi_{\text{smooth}}(\theta \mid X_{1:n}) \propto \pi(\theta) \exp\left(-\gamma_n \widehat{\mathrm{MMD}}_n^2(\theta)\right)$. By replacing the non-Lipschitz indicator $\mathbb{I}(\cdot \le \epsilon_n^2)$ with the smooth exponential weight, the posterior avoids hard boundary cutoffs. Applying Laplace's method around the MMD-estimator $\widehat{\theta}_n$, the smoothed posterior locally approximates a Gaussian distribution $\mathcal{N}\left(\widehat{\theta}_n, (\gamma_n c(h))^{-1}\right)$ (ignoring U-statistic variance for a moment), showing how the temperature $\gamma_n$ plays a role inverse to the tolerance $\epsilon_n^2$.

4. **Mechanism of Non-Lipschitz Discontinuity**: The indicator function $\mathcal{I}_{\epsilon}(\cdot) = \mathbb{I}(\cdot \le \epsilon_n^2)$ has derivative supported entirely at the boundary $\epsilon_n^2$. In finite samples, small perturbations in the empirical U-statistic $R_n(\theta)$ can cause parameters just outside the true contour to jump inside the acceptance set. This introduces a discontinuous small-ball probability ratio in the ABC denominator bounds. The exponential smoother $\exp(-\gamma_n x)$ is globally Lipschitz on bounded intervals, ensuring that the gradient of the log-posterior with respect to $\theta$ varies continuously, thereby stabilizing contraction rate proofs via standard Bernton et al. or Gibbs posterior machinery.

## Obstacles

- **Degeneracy of the U-statistic Variance at $\theta = 0$**: When $P_\theta = P_0$, the leading term of the empirical MMD squared vanishes in the Hoeffding decomposition, meaning its variance is governed by degenerate chaos (second-order Wiener-Itô chaos), scaling as $O(1/n^2)$ rather than $O(1/n)$. This 1D toy model masks the higher-order spectral interactions present in multi-dimensional extensions where mixed partial derivatives of Mercer eigenfunctions dominate.
- **Misspecification of Temperature vs Tolerance**: Equating the hard ABC rejection rate to an effective temperature $\gamma_n$ requires precise control of the empirical MMD tail bounds $\mathbb{P}(\widehat{\mathrm{MMD}}_n^2 - M^2(\theta) > t)$, which depends heavily on the kernel bandwidth $h$ through the eigenvalue decay $\lambda_j$.

## Suggested next steps

1. **Derive the Exact Small-Ball Probability**: Compute explicitly $\mathbb{P}\left(\widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta, m}) \le \epsilon_n^2 \mid \theta\right)$ for the 1D Gaussian location model using the spectral expansion $\widehat{\mathrm{MMD}}_n^2 = \sum_{j=1}^\infty \lambda_j (Z_{nj} - \mu_{\theta, j})^2$ to see how the hard indicator's denominator behaves compared to the integral of the exponential smoother.
2. **Analyze Bernstein-von Mises for the Smoothed MMD Posterior**: Apply general generalized Bayesian inference theorems (e.g., Chernozhukov and Hong, 2003) to the exponential smoother $\exp(-\gamma_n \widehat{\mathrm{MMD}}_n^2(\theta))$ to find the optimal scaling of $\gamma_n$ as a function of $n$ and the kernel smoothness $h$.
3. **Simulate the Discrepancy**: Write a short numerical script for the 1D Gaussian model comparing the posterior histograms of hard-threshold ABC ($\epsilon_n = 0.05$) versus temperature ABC ($\gamma_n = 200$) to visualize the boundary artifacts and concentration differences.

---

## Finding #86: task_97 (Sketcher)

*Worker: **sketcher** | Task ID: `task_97` | Duration: 12.3s | Timestamp: 2026-09-09 11:50:47 UTC | Focus Nodes: `hypothesis_2`, `lemma_1`*

**Assigned Task Prompt**:
> Compute the Kernel Fisher Information Matrix Sigma_{theta_0} explicitly for a multivariate Gaussian location family P_theta = N(theta, I_d) under a Gaussian kernel, and evaluate how its smallest eigenvalue lambda_min(Sigma_{theta_0}) depends on dimension d and bandwidth sigma, referencing hypothesis_2.

**Worker Output & Derivations**:

(\theta, 1)$.
So $\mathbb{E}[k(X,X')] + \mathbb{E}[k(Y,Y')] = \frac{2h}{\sqrt{2+h^2}}$.
And $-2\mathbb{E}[k(X,Y)] = -2 \frac{h}{\sqrt{2+h^2}} \exp(-\frac{\theta^2}{2(2+h^2)})$.
So $\text{MMD}^2 = \frac{2h}{\sqrt{2+h^2}} [ 1 - \exp(-\frac{\theta^2}{2(2+h^2)}) ]$.
Ah, counterexample_1 in the prompt had a typo in its text ("$\frac{h}{\

---

## Finding #87: task_98 (Counterexample)

*Worker: **counterexample** | Task ID: `task_98` | Duration: 13.1s | Timestamp: 2026-09-09 11:50:54 UTC | Focus Nodes: `hypothesis_2`, `counterexample_1`*

**Assigned Task Prompt**:
> Construct a concrete asymptotic regime and parameter family where the identifiability preconstant c(d) degrades exponentially with dimension d, verifying hypothesis_2 and analyzing its impact on MMD-ABC acceptance probability.

**Worker Output & Derivations**:

## Findings

1. **Exact Gaussian-Kernel MMD for Shifted Gaussians**: For $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$ under an isotropic Gaussian kernel $k_h(x,y) = \exp(-\|x-y\|^2 / (2h^2))$, the squared MMD has the closed-form expression $\operatorname{MMD}^2(P_0, P_\theta) = 2 \left(\frac{h^2}{2+h^2}\right)^{d/2} \left(1 - \exp\left(-\frac{\|\theta\|^2}{2(2+h^2)}\right)\

---

## Finding #88: task_100 (Searcher)

*Worker: **searcher** | Task ID: `task_100` | Duration: 13.0s | Timestamp: 2026-09-09 11:51:04 UTC | Focus Nodes: `hypothesis_1`, `obstacle_1`, `lemma_3`*

**Assigned Task Prompt**:
> Search OpenAlex and arXiv for papers combining MMD, approximate Bayesian computation, and posterior contraction rates to cross-reference recent metric entropy bounds.

**Worker Output & Derivations**:

## Findings

1. **Generalized Bayesian Inference with MMD**: B. Y. Chérief-Abdellatif and P. Alquier (2020), *"Consistency of MMD-based generalized Bayesian inference"* (arXiv:1905.12574, published in *Bernoulli*), establish posterior consistency and contraction rates for generalized Bayesian posteriors of the form $\pi_n(\theta) \mid X_{1:n} \propto \pi(\theta) \exp(- \lambda_n n \mathrm{MMD}^2(P_n, P_\theta))$. Their framework relies on establishing local bracketing entropy conditions for the model family $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ with respect to the MMD metric, combined with a uniform law of large numbers for empirical MMD.
   * *Hypotheses & Applicability*: Assumes a bounded kernel $k$ (so $0 \le k(x,y) \le K$) and compact parameter space $\Theta$. The contraction rate is governed by the modulus of continuity of the map $\theta \mapsto \mathrm{MMD}(P_0, P_\theta)$ and the bracketing metric entropy $N_{[\cdot]}(\varepsilon, \mathcal{P}, \mathrm{MMD})$.

2. **Metric Entropy of RKHS Balls and MMD Bracketing Numbers**: According to classical results on compact operators and RKHS embedding (e.g., Cucker and Smale 2001, *On the Mathematical Foundations of Learning*; or Edmunds and Triebel 1996, *Function Spaces, Entropy Numbers, Operators*), the metric entropy $\log N(\varepsilon, B_H, \|\cdot\|_{L_2})$ of an RKHS ball $B_H$ in $L_2(P_0)$ is directly controlled by the decay rate of the Mercer eigenvalues $\lambda_j$. If $\lambda_j \sim j^{-2s/d}$ (smoothness $s$, dimension $d$), the entropy numbers scale as $\varepsilon^{-d/(2s)}$. For composite models $P_\theta$, the bracketing entropy $N_{[\cdot]}(\varepsilon, \mathcal{P}, \mathrm{MMD})$ depends on how the parametrization $\theta \mapsto P_\theta$ maps into the RKHS.

3. **Ill-Posedness and Picard Condition for MMD Inverse Maps**: As formulated in classical inverse problem theory (e.g., Engl, Hanke, and Neubauer 1996, *Regularization of Inverse Problems*), solving for $\theta$ from $\mathrm{MMD}^2(P_0, P_\theta) = t$ is a nonlinear operator equation where the forward operator $F(\theta) = P_\theta$ is composed with the continuous embedding into the RKHS. The singular values of the linearized operator at $\theta_0$ are tied to $\sqrt{\lambda_j} \frac{\partial P_\theta}{\partial \theta_j}$. Rapid spectral decay ($\lambda_j$ decaying exponentially, e.g., Gaussian kernels) severely violates the Picard criterion unless the parameter-to-distribution map has its derivative entirely supported in the high-order eigenfunctions—which contradicts smoothness of the family. This proves that smooth kernels induce severe ill-posedness, requiring regularization (or in ABC, a carefully tuned tolerance $\epsilon_n$).

## Obstacles

1. **Indicator Filter vs. Exponential Weights**: The literature on generalized Bayesian inference (like Chérief-Abdellatif & Alquier 2020) analyzes exponential weighting $\exp(-\gamma_n n \mathrm{MMD}^2)$, whereas standard ABC rejection uses the indicator filter $\mathbb{I}(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2)$. The indicator filter introduces discontinuous likelihood ratios, rendering standard Bernstein-von Mises or generalized posterior contraction proofs (which rely on smooth log-posterior expansions or LAN properties) inapplicable without hard small-ball probability bounds on the denominator.

2. **Mismatch between MMD Topology and Hellinger/KL Divergence**: Standard posterior contraction theorems (such as Ghosal, van der Vaart, and van Zanten 2000, *"Convergence rates of posterior distributions"* in *Annals of Statistics*) require prior mass conditions and entropy bounds in terms of Kullback-Leibler (KL) divergence or Hellinger distance. Because MMD topology is strictly weaker than weak convergence (and hence weaker than Hellinger/TV), controlling MMD neighborhoods does not automatically bound KL neighborhoods, making it difficult to apply standard prior-mass sieves directly without extra smoothness and injectivity assumptions.

3. **Dimension Dependence in Entropy Bounds**: As noted in Obstacle 3 of the research context, Mercer eigenvalues decay as $\lambda_j \sim j^{-2s/d}$. In high dimensions $d$, the metric entropy of the RKHS blows up unless $s$ is very large, which degrades the bracketing entropy term in general contraction rate theorems and leads to a curse of dimensionality in the MMD-ABC sample complexity.

## Suggested next steps

1. Run literature queries on generalized ABC contraction rates and small-ball probabilities for empirical MMD:
   * Query 1: `"Approximate Bayesian computation" AND "posterior contraction rate" AND "Maximum Mean Discrepancy"`
   * Query 2: `"small-ball probability" AND "empirical maximum mean discrepancy" AND "convergence rate"`
   * Query 3: `"bracketing entropy" AND "Maximum Mean Discrepancy" AND "generalized Bayesian inference"`

2. Investigate the connection between the ABC rejection indicator $\mathbb{I}(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2)$ and small-ball probabilities of infinite sums of non-central chi-squared variables using the spectral representation (Lemma 1), adapting techniques from Bernton et al. (2019) for Wasserstein ABC.

3. Check if recent work (post-2021) by Pierre Alquier or associated authors has addressed the specific case of *hard-thresholding/rejection* ABC contraction rates rather than generalized Gibbs/exponential posteriors.

---

## Finding #89: task_101 (Verifier)

*Worker: **verifier** | Task ID: `task_101` | Duration: 15.9s | Timestamp: 2026-09-09 11:51:16 UTC | Focus Nodes: `lemma_2`, `counterexample_1`*

**Assigned Task Prompt**:
> Verify whether the Hoeffding projection variance formula in lemma_2 correctly captures the variance reduction from rapid eigenvalue decay and check consistency with counterexample_1.

**Worker Output & Derivations**:

zero). The variance of the estimator does *not* vanish simply because $P_\theta = P_0$.
Therefore, formula in `lemma_2` having $(\mu_{0, j} - \mu_{\theta, j})^2$ implies the variance vanishes when $P_\theta = P_0$, which is fundamentally incorrect for a variance formula! The variance of an estimator around its mean (or even uncentered second moment) depends on the data distribution and kernel, not quadratically on the difference between the two distributions in that specific way.

Let's double check this.
If $P_\theta = P_0$, $\mu_{\theta, j} = \mu_{0, j}$, so $(\mu_{0, j} - \mu_{\theta

---

## Finding #90: task_102 (Sketcher)

*Worker: **sketcher** | Task ID: `task_102` | Duration: 16.2s | Timestamp: 2026-09-09 11:51:24 UTC | Focus Nodes: `hypothesis_2`, `obstacle_4`, `lemma_1`*

**Assigned Task Prompt**:
> Derive the explicit dependence of the identifiability preconstant c(d) on dimension d for Gaussian kernels in a location family, connecting Mercer eigenvalue decay to the shrinking prior mass of the ABC acceptance region as described in hypothesis_2 and obstacle_4.

**Worker Output & Derivations**:

## Findings

1. **Exact $d$-Dimensional Population MMD for Gaussian Location Models (Solved).**
   Let $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$ on $\mathbb{R}^d$, with Gaussian kernel $k_h(x, y) = \exp\left(-\frac{\|x-y\|^2}{2h^2}\right)$. For independent $X \sim \mathcal{N}(a, I_d)$ and $Y \sim \mathcal{N}(b, I_d)$, the cross-expectation factorizes across coordinates:
   $$\mathbb{E}[k_h(X, Y)] = \prod_{i=1

---

## Finding #91: task_105 (Sketcher)

*Worker: **sketcher** | Task ID: `task_105` | Duration: 11.6s | Timestamp: 2026-09-09 11:51:32 UTC | Focus Nodes: `idea_1`, `counterexample_2`, `obstacle_3`, `problem`*

**Assigned Task Prompt**:
> Formalize the ABC posterior contraction rate bound using the small-ball probability approach (referencing [idea_1] and [counterexample_2]), showing how exponential Mercer eigenvalue decay forces the ABC denominator to vanish unless the tolerance epsilon_n scales appropriately with the truncation level K_n.

**Worker Output & Derivations**:

## Findings

1. **Subgoal 1: Spectral Truncation Decomposition of Empirical MMD-ABC (Status: solved, sketch included)**
   Let $k(x,y) = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(y)$ be the Mercer expansion of the kernel with respect to $P_0$. The squared empirical MMD between $P_n$ (size $n$) and $P_{\theta,m}$ (size $m$) can be decomposed at a truncation level $K_n$ into a finite-dimensional projection and a tail remainder:
   $\widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta,m}) = \sum_{j=1}^{K_n} \lambda_j \left( \widehat{\mu}_{0,j} - \widehat{\mu}_{\theta,j} \right)^2 + R_{n,m}(K_n)$,
   where $\widehat{\mu}_{0,j} = n^{-1}\sum_{i=1}^n e_j(X_i)$ and $\widehat{\mu}_{\theta,j} = m^{-1}\sum_{i=1}^m e_j(Y_{i,\theta})$. By Lemma 2, the variance of the $j$-th empirical component is controlled by $\lambda_j^2 / \min(n,m)$, so the sum of variances over $j=1,\dots,K_n$ is bounded by $\frac{1}{\min(n,m)} \sum_{j=1}^{K_n} \lambda_j^2$. The tail remainder $R_{n,m}(K_n)$ contains the empirical U-statistic fluctuations of the high-frequency components $\sum_{j > K_n}$, whose expectation and variance are controlled by the tail sum of eigenvalues $\sum_{j > K_n} \lambda_j$ and $\sum_{j > K_n} \lambda_j^2$.

2. **Subgoal 2: ABC Denominator Lower Bound and Small-Ball Probability (Status: partial)**
   The ABC posterior denominator (marginal likelihood) is $D_n(\epsilon_n) = \int_{\Theta} \mathbb{I}\left( \widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta,m}) \le \epsilon_n^2 \right) d\Pi(\theta)$. To lower bound this integral on a ball $\|\theta - \theta_0\| \le r_n$, we use the triangle inequality on the MMD metric: 
   $\widehat{\mathrm{MMD}}_n^2 \le 2 \mathrm{MMD}^2(P_0, P_\theta) + 2 \left( \widehat{\mathrm{MMD}}_n^2 - \mathrm{MMD}^2(P_0, P_\theta) \right)$.
   By the identifiability modulus or local Taylor expansion around $\theta_0$ (Obstacle 4), $\mathrm{MMD}^2(P_0, P_\theta) \approx (\theta - \theta_0)^T H(\theta_0) (\theta - \theta_0)$, where the Hessian operator $H(\theta_0)$ has eigenvalues proportional to $\lambda_j \times (\nabla_\theta \mu_{\theta,j})^2$. When Mercer eigenvalues $\lambda_j$ decay rapidly (e.g., exponentially for Gaussian kernels), the eigenvalues of $H(\theta_0)$ decay rapidly along high-frequency modes. Consequently, the acceptance region $\{ \theta : \widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2 \}$ becomes extremely stretched (flat) along high-frequency directions, causing the prior volume of the acceptance region to collapse unless the tolerance $\epsilon_n$ is chosen to balance the projection variance $K_n / \min(n,m)$ and the tail bias $\sum_{j > K_n} \lambda_j$.

3. **Subgoal 3: Contraction Rate Balance and Spectral Decay Dichotomy (Status: partial)**
   To establish a posterior contraction rate $r_n$ such that $\Pi(\|\theta - \theta_0\| > M_n r_n \mid \widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2) \to 0$, standard small-ball probability arguments require balancing three competing terms:
   (i) The prior mass of the ball $\Pi(\|\theta - \theta_0\| \le r_n) \ge c r_n^d$ (or general dimension-free prior concentration).
   (ii) The stochastic fluctuation of the empirical MMD estimator over the first $K_n$ components, which scales as $O_p\left(\sqrt{\frac{K_n}{\min(n,m)}}\right)$.
   (iii) The deterministic approximation error (bias/tail) and identifiability loss, governed by $\sum_{j > K_n} \lambda_j$ and the ill-posedness of the operator mapping $\theta \mapsto \mu_{\theta}$.
   For exponentially decaying eigenvalues ($\lambda_j \sim e^{-aj}$), choosing $K_n \asymp \log(\min(n,m))$ makes the tail error $\sum_{j > K_n} \lambda_j \asymp \min(n,m)^{-a/2}$, matching the parametric rate, but the Hessian $H(\theta_0)$ has exponentially small eigenvalues for $j > K_n$, which severely degrades the parameter sensitivity $\beta$ or the preconstant $c(d)$ (Hypothesis 2), preventing standard polynomial contraction rates without strong source conditions on $\theta - \theta_0$.

## Obstacles

1. **Ill-Posedness of the Inverse Map $\theta \mapsto \mathrm{MMD}^2(P_0, P_\theta)$**: Because $\mathrm{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, if $\lambda_j$ decays rapidly (exponentially), high-frequency differences in expectations $(\mu_{0,j} - \mu_{\theta,j})^2$ are heavily attenuated. This means that large perturbations in $\theta$ can produce negligible changes in MMD if they occur along high-frequency eigenfunctions $e_j$, violating the coercivity condition required for fast posterior contraction.
2. **Coupling between Truncation Level $K_n$ and Tolerance $\epsilon_n$**: In ABC rejection, the indicator function $\mathbb{I}(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2)$ does not smoothly penalize tail deviations. Bounding the indicator probability requires uniform bounds on empirical U-statistics over infinite dimensions, or explicit control over the supremum $\sup_{\theta} |\widehat{R}_{n,m}(K_n)|$, which introduces dimensional dependence through metric entropy of the RKHS unit ball.

## Suggested next steps

1. **Establish a Source Condition**: Formulate a formal smoothness assumption on the parameter-to-measure map $\theta \mapsto P_\theta$ (e.g., assuming $\theta - \theta_0$ lies in an interpolation space/RKHS power space linked to the kernel operator) to rigorously quantify the identifiability exponent $\beta$.
2. **Derive Concentration Inequalities for Truncated U-Statistics**: Apply Hoeffding or Bernstein-type inequalities for degenerate U-statistics (or decoupled chaos processes) to rigorously bound the tail remainder $\widehat{R}_{n,m}(K_n)$ uniformly over $\theta$.
3. **Optimize $K_n$ as a Function of $n, m, d$**: Explicitly solve the bias-variance trade-off equation $\frac{K_n}{\min(n,m)} + \sum_{j > K_n} \lambda_j = \epsilon_n^2$ under both polynomial ($\lambda_j \sim j^{-2s/d}$) and exponential ($\lambda_j \sim e^{-aj}$) spectral decay to determine the optimal ABC posterior contraction rate $r_n$.

---

## Finding #92: task_99 (Decomposer)

*Worker: **decomposer** | Task ID: `task_99` | Duration: 60.9s | Timestamp: 2026-09-09 11:51:41 UTC | Focus Nodes: `hypothesis_1`, `lemma_1`*

**Assigned Task Prompt**:
> Develop a rigorous decomposition plan for bounding the remainder term of the local MMD Taylor expansion and establishing global uniform parameter identifiability across the parameter space.

**Worker Output & Derivations**:

## Findings

1. **Plan 1: Spectral-Truncated Taylor Expansion and Coercivity Bounds**
   * *Main Idea:* Decompose the population squared MMD into a finite-dimensional projection onto the top $K_n$ smooth eigenfunctions and an infinite-dimensional tail. Control the Taylor remainder of the finite projection using uniform Hessian bounds, and bound the tail using the Mercer eigenvalue decay rate $\sum_{j > K_n} \lambda_j$.
   * *Subgoals:*
     1. **Subgoal 1.1:** Prove Fréchet differentiability of the population map $\theta \mapsto \mathrm{MMD}^2(P_0, P_\theta)$ in the RKHS and derive explicit coordinate representations for the gradient and Hessian using the Mercer eigenfunctions $e_j$ (Lemma 1, Lemma 2).
     2. **Subgoal 1.2:** Construct a truncated MMD functional at level $K_n$, and prove that the remainder of its Taylor expansion is bounded by $O(\|\theta - \theta_0\|^3)$ with explicit constants depending on $\lambda_{K_n}$ and the supremum norms $\|\nabla e_j\|_\infty$.
     3. **Subgoal 1.3:** Establish a local uniform lower bound on the smallest eigenvalue of the Hessian matrix of the truncated MMD, mapping kernel smoothness $s$ and dimension $d$ to the coercivity constant to prevent denominator collapse (Obstacle 4).
   * *Plausibility:* Directly operationalizes Idea 1 (Spectral Truncation) and Lemma 1, converting an infinite-dimensional degeneracy problem into a controlled finite-dimensional matrix perturbation problem.
   * *Avoided Failures:* Bypasses the catastrophic flatness of high-frequency components (Obstacle 4) by formally throwing away tail components where Mercer eigenvalues decay faster than the parametric signal.

2. **Plan 2: Sobolev/Besov Interpolation and Functional Stability**
   * *Main Idea:* Avoid pointwise Taylor expansions entirely by embedding the parameter-to-distribution map into the kernel's native RKHS and applying functional interpolation inequalities (e.g., Gagliardo-Nirenberg or K-functional methods) to establish global uniform identifiability.
   * *Subgoals:*
     1. **Subgoal 2.1:** Characterize the tangent map $\dot{P}_\theta$ in the RKHS $\mathcal{H}_k$, proving that the Jacobian of the mapping embeds into a Sobolev space of smoothness determined by the kernel operator.
     2. **Subgoal 2.2:** Prove a global lower bound on $\mathrm{MMD}^2(P_0, P_\theta)$ via an inverse Jackson-type inequality, explicitly isolating the identifiability exponent $\beta$ and dimension-dependent preconstant $c(d)$ as functions of kernel smoothness $s$ (Hypothesis 1 & Hypothesis 2).
     3. **Subgoal 2.3:** Combine the interpolation stability bound with the empirical Hoeffding projection variance (Lemma 2) to yield a non-asymptotic ABC acceptance probability bound valid across the entire parameter space $\Theta$.
   * *Plausibility:* Directly targets the "Smoothness Dilemma" (Hypothesis 1) by framing MMD identifiability as a functional embedding property rather than a direct Taylor approximation.
   * *Avoided Failures:* Avoids the failure of Taylor remainders in rough or high-dimensional settings (Obstacle 3) by using global integral inequalities instead of local expansions.

3. **Plan 3: Stein Operator Perturbation and Compact Operator Theory**
   * *Main Idea:* Translate the MMD integral into a Stein discrepancy representation involving the generators of $P_\theta$, and apply perturbation theory for self-adjoint compact operators to control the spectrum and identifiability jointly.
   * *Subgoals:*
     1. **Subgoal 3.1:** Rewrite $\mathrm{MMD}^2(P_0, P_\theta)$ using a Stein kernel representation $T_k(x, y; \theta)$ that incorporates the score function or generator of $P_\theta$.
     2. **Subgoal 3.2:** Apply Kato-Rellich theorem or generalized spectral perturbation bounds for compact operators to quantify how the Mercer eigenvalues $\lambda_j(\theta)$ and eigenfunctions $e_j(x;\theta)$ vary as $\theta$ perturbs from $\theta_0$.
     3. **Subgoal 3.3:** Bound the remainder of the Stein-MMD map by controlling the operator norm of the second-order Fréchet derivative of the Stein discrepancy operator over compact parameter sets $\Theta$.
   * *Plausibility:* Connects MMD spectral decay directly to the robust machinery of linear operator perturbation theory, bypassing direct empirical asymmetry issues (Obstacle 2).
   * *Avoided Failures:* Avoids direct handling of intractable joint sample-size limits (Obstacle 1) by establishing population-level operator stability first.

## Obstacles
- **Subgoal 1.3 (Coercivity Lower Bound):** Proving a uniform lower bound on the Hessian without dimension-dependent vanishing preconstants remains extremely difficult for smooth kernels (like Gaussian) in high dimensions $d$, due to the rapid decay of $\lambda_j \sim j^{-2s/d}$ (Obstacle 3 and Hypothesis 2).
- **Subgoal 2.1 & 2.2 (RKHS Tangent Embedding):** Explicitly calculating the inverse Jackson inequality constants for arbitrary parametric families $P_\theta$ mapped through non-linear kernels requires heavy geometric control over the parameter space $\Theta$, which is currently lacking beyond simple location-scale families (Counterexample 1).
- **Subgoal 3.2 (Operator Perturbation):** The parameter $\theta$ often appears inside the domain or measure of the expectation in MMD, making standard linear operator perturbation theorems (which assume fixed underlying spaces) difficult to apply without heavy technical modifications for varying base measures.

## Suggested next steps
1. **Compute explicit Taylor remainders for 1D Gaussian families:** Extend Counterexample 1 (1D Gaussian location family with Gaussian kernel) to compute the exact third-order Taylor remainder and verify whether Subgoal 1.2's remainder bound holds explicitly.
2. **Derive Mercer eigenvalue decay bounds for Matérn vs. Gaussian kernels:** Formulate a concrete comparison of how the dimension $d$ degrades the smallest non-zero Hessian eigenvalue (Subgoal 1.3) across exponential vs. polynomial spectral decay classes.
3. **Investigate Stein-MMD representations:** Test whether expressing MMD via Stein operators simplifies the Fréchet derivative calculations required in Plan 3, particularly for exponential dispersion models.

---

## Finding #93: task_104 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_104` | Duration: 32.8s | Timestamp: 2026-09-09 11:51:48 UTC | Focus Nodes: `lemma_1`, `obstacle_3`, `idea_2`, `hypothesis_1`*

**Assigned Task Prompt**:
> Construct an infinite-dimensional / non-parametric toy model where theta lives in a Sobolev ellipsoid and P_theta has mean embedding mu_theta with coefficients theta_j. Explicitly compute how kernel Mercer eigenvalue decay lambda_j ~ j^{-2s/d} determines the ill-posedness degree and the non-parametric MMD-ABC posterior contraction rate.

**Worker Output & Derivations**:

:
This reveals an OPTIMAL kernel smoothness $s^* = d/2$!
- If $s < d/2$: kernel is too rough, empirical estimation of MMD is slow ($n^{-s/d}$), leading to a rate $n^{-\frac{sp}{d(s+p)}}$.
- If $s > d/2$: empirical MMD estimation is fast ($n^{-1/2}$), but kernel is too smooth, obscuring high-frequency parameter differences and causing ill-posedness, leading to a rate $n^{-\frac{p}{2(s+p)}}$.
- The optimal rate is achieved precisely at $s^* = d/2$, giving rate $n^{-\frac{p}{d+2p}}$, which is the minimax

---

## Finding #94: task_103 (Sketcher)

*Worker: **sketcher** | Task ID: `task_103` | Duration: 35.4s | Timestamp: 2026-09-09 11:51:55 UTC | Focus Nodes: `lemma_1`, `hypothesis_2`, `obstacle_1`, `paper_2`, `paper_3`*

**Assigned Task Prompt**:
> Using the local quadratic expansion MMD^2(P_0, P_theta) = (theta - theta_0)^T H (theta - theta_0) + O(||theta - theta_0||^3) and empirical MMD concentration Op(n^{-1/2} + m^{-1/2}), derive the optimal ABC tolerance sequence epsilon_n and the resulting posterior contraction rate r_n for theta under rejection MMD-ABC.

**Worker Output & Derivations**:

{\theta, m}) \le 2 \mathrm{MMD}^2(P_0, P_\theta) + 2 \widehat{\mathrm{MMD}}^2(\widehat{P}_n, P_0) + 2 \widehat{\mathrm{MMD}}^2(\widehat{P}_{\theta, m}, P_\theta)$$
Wait, more directly:
$\widehat{\mathrm{MMD}}^2(\widehat{P}_n, \widehat{P}_{\theta, m}) \le \left( \mathrm{MMD}(P_0, P_\theta) + \mathrm{MMD}(\widehat{P}_n, P_0) + \mathrm{MMD}(\widehat{P}_{\theta, m}, P_\theta) \right)^

---

## Finding #95: task_106 (Searcher)

*Worker: **searcher** | Task ID: `task_106` | Duration: 23.5s | Timestamp: 2026-09-09 11:52:03 UTC | Focus Nodes: `problem`, `obstacle_3`, `hypothesis_1`*

**Assigned Task Prompt**:
> Search literature for 'exponentially ill-posed inverse problems', 'MMD ABC posterior contraction rates', and 'nonparametric Bayesian inference kernel loss ill-posedness'.

**Worker Output & Derivations**:

## Findings

1. **Generalized Posterior Concentration Rates via MMD (Chérief-Abdellatif & Alquier, 2019/2020):** 
   In *"Consistency and contraction rates for generalized Bayesian inference with maximum mean discrepancy"* (arXiv:1905.12879), the authors study generalized posteriors of the form $\pi_n(\theta \mid X_1,\dots,X_n) \propto \pi(\theta) \exp(-\gamma_n n \text{MMD}^2(P_n, P_\theta))$. 
   *Hypotheses & Result:* Let $\Theta$ be compact, and assume the identifiability condition $c d(\theta, \theta_0)^\beta \le \text{MMD}(P_0, P_\theta) \le C d(\theta, \theta_0)^\alpha$ holds. If the prior puts sufficient mass on Kullback-Leibler-like neighborhoods defined through MMD (i.e., $\Pi(\theta: \text{MMD}(P_0, P_\theta) < \delta) \ge c' \delta^d$ for small $\delta$), then the posterior contracts at a rate $\epsilon_n$ satisfying $\epsilon_n^\beta \asymp (\gamma_n n)^{-1/2} + \delta_n$, where $\gamma_n$ is a tuning parameter. 
   *Proof Technique:* Uses PAC-Bayesian inequalities combined with metric entropy bounds on the model family $\{P_\theta\}$. However, this does not directly cover *rejection* ABC, as the indicator filter introduces a sharp thresholding instead of an exponential Gibbs weight.

2. **Ill-Posedness of Operator Equations and Spectral Decay (Engl, Hanke, Neubauer, 1996):**
   In *Regularization of Inverse Problems* (mathematical monograph, 1996), the abstract framework for nonlinear operator equations $\mathcal{F}(\theta) = g$ is analyzed. 
   *Hypotheses & Result:* When the forward operator $\mathcal{F}: \Theta \to \mathcal{H}$ (mapping parameter $\theta$ to the kernel mean embedding $\mu_{P_\theta} \in \mathcal{H}$) is compact or has a compact Fréchet derivative with singular values decaying rapidly to zero (e.g., governed by the Mercer eigenvalues $\lambda_j$ of the kernel), the inverse problem $\theta = \mathcal{F}^{-1}(\mu_{P_\theta})$ is severely (often exponentially) ill-posed. 
   *Relevance:* The mapping $\theta \mapsto \text{MMD}^2(P_0, P_\theta) = \|\mu_{P_0} - \mu_{P_\theta}\|_{\mathcal{H}}^2$ inherits this ill-posedness. Smooth kernels with exponential eigenvalue decay (e.g., Gaussian) yield Fréchet derivatives smoothing out high-frequency parameter variations, making the gradient of MMD with respect to $\theta$ extremely flat in directions of high-frequency eigenfunctions.

3. **Weak Metrization and Kernel Topologies (Sriperumbudur, Fukumizu, Gretton, 2010):**
   In *"Hilbert space embeddings of probability measures on metric spaces"* (JMLR, 2010), the authors establish conditions for MMD to metrize weak convergence of probability measures.
   *Hypotheses & Result:* Let $k$ be a continuous kernel on a metric space $\mathcal{X}$. If $k$ is a *characteristic* kernel (e.g., Gaussian $k(x,y) = \exp(-\gamma \|x-y\|^2)$ or Matérn on $\mathbb{R}^d$), then $\text{MMD}(P, Q) = 0 \iff P = Q$, and MMD metrizes the weak convergence of probability measures.
   *Proof Technique:* The proof relies on the injectivity of the mean embedding operator $P \mapsto \mu_P = \int k(x, \cdot) dP(x)$. The strength of the topology (and thus the modulus of continuity $\beta$ in the identifiability condition) depends explicitly on the reproducing kernel Hilbert space (RKHS) norm equivalence properties, which degenerate when moving from rough kernels (larger RKHS, weaker topology, better parameter sensitivity) to smooth kernels (smaller RKHS, stronger topology, poor parameter sensitivity).

## Obstacles

- **Incompatibility of Exponential Weights vs. Indicator Filters:** Literature on MMD-based Bayesian inference exclusively analyzes generalized posteriors $\propto \exp(-\gamma_n n \text{MMD}^2)$. Rejection ABC uses the hard indicator $\mathbb{I}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$. Existing concentration theorems (like those of Chérief-Abdellatif & Alquier) rely heavily on exponential tail bounds of Lipschitz functionals of empirical processes, which break down for indicator functions whose expectation involves small-ball probabilities of non-central quadratic forms in Hilbert spaces.
- **Degenerate Limit Distribution of Empirical MMD under Alternatives:** Under $P_0 \neq P_\theta$, the empirical squared MMD $\widehat{\text{MMD}}_n^2(P_n, P_{\theta, m})$ converges to a normal distribution via standard V-statistic / U-statistic theory. However, the variance of this limit depends explicitly on the operator cross-covariances and the spectral gap. In high dimensions $d$, as Mercer eigenvalues $\lambda_j \sim j^{-2s/d}$ decay, the accumulation of infinite variance components in the Hoeffding decomposition destabilizes the uniform control needed over $\theta \in \Theta$.

## Suggested next steps

1. **Query:** Run literature search on `"approximate bayesian computation" AND "maximum mean discrepancy" AND "posterior contraction rate"`.
2. **Query:** Run literature search on `"ill-posed inverse problems" AND "kernel mean embedding" AND "parameter estimation smoothness dilemma"`.
3. **Query:** Run literature search on `"small-ball probabilities" AND "empirical maximum mean discrepancy" AND "rejection ABC consistency"`.
4. **Investigate:** Formalize the ABC rejection acceptance probability $\mathbb{P}_{\theta}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$ using the spectral representation of $\widehat{\text{MMD}}_n^2$ as an infinite sum of non-central chi-squared variables, and evaluate how the tail sum $\sum_{j > K_n} \lambda_j$ constrains the choice of the tolerance schedule $\epsilon_n$.

---

## Finding #96: task_107 (Counterexample)

*Worker: **counterexample** | Task ID: `task_107` | Duration: 21.7s | Timestamp: 2026-09-09 11:52:33 UTC | Focus Nodes: `lemma_3`, `hypothesis_2`, `obstacle_4`*

**Assigned Task Prompt**:
> Test whether the dimension-dependent preconstant decay bound in lemma_3 can be bypassed by choosing a dimension-adaptive kernel bandwidth gamma_d = O(sqrt{d}), and construct a concrete counterexample if uniform consistency fails.

**Worker Output & Derivations**:

## Findings

1. **Exact MMD Formula for $d$-Dimensional Gaussians**: For $P_0 = \mathcal{N}(0, I_d)$ and $P_\theta = \mathcal{N}(\theta, I_d)$ under a Gaussian kernel $k_h(x,y) = \exp(-\|x-y\|^2 / (2h^2))$, the squared population MMD is explicitly given by $\operatorname{MMD}^2(P_0, P_\theta) = 2 \left(\frac{h^2}{h^2+2}\right)^{d/2} \left(1 - \exp\left(-\frac{\|\theta\|^2}{2(h^2+2)}\right)\right)$.
2.

---

## Finding #97: task_108 (Sketcher)

*Worker: **sketcher** | Task ID: `task_108` | Duration: 16.0s | Timestamp: 2026-09-09 11:52:42 UTC | Focus Nodes: `lemma_1`, `idea_1`*

**Assigned Task Prompt**:
> Sketch the proof of subgoal 1 (empirical projection error bounds for the first K_n components of the empirical MMD) using empirical process theory and Mercer eigen-projections.

**Worker Output & Derivations**:

## Findings

1. **Exact spectral identity of empirical squared MMD**: By Mercer's theorem $k(x,y) = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(y)$ with orthonormal eigenfunctions in $L^2(P_0)$, the squared empirical MMD between samples of size $n$ ($X_i \sim P_0$) and size $m$ ($Y_\ell \sim P_\theta$) decomposes as $\widehat{\mathrm{MMD}}_n^2(P_n, P_{m,\theta}) = \sum_{j=1}^\infty \lambda_j (\hat{\mu}_{0,j} - \hat{\mu}_{\theta,j})^2 -

---

## Finding #98: task_112 (Searcher)

*Worker: **searcher** | Task ID: `task_112` | Duration: 12.0s | Timestamp: 2026-09-09 11:52:51 UTC | Focus Nodes: `lemma_3`, `obstacle_4`*

**Assigned Task Prompt**:
> Search literature for papers combining kernel spectral decay, small-ball probabilities of Gaussian quadratic forms, and ABC or generalized Bayesian posterior contraction rates.

**Worker Output & Derivations**:

## Findings

1. **Generalized Posterior Contraction for MMD-based Inferences**: 
   Cherief-Abdellatif and Alquier (2020, *"Maximum Mean Discrepancy Bayesian Inference"* or related work on kernel-based generalized posteriors) analyze generalized posteriors of the form $\Pi_n(\theta | X_{1:n}) \propto \pi(\theta) \exp(-n \text{MMD}^2(P_n, P_\theta))$. *Hypotheses:* They assume the prior puts sufficient mass on Kullback-Leibler or MMD neighborhoods of the true parameter, and that test functions can be constructed in the RKHS. *Technique:* Their proofs adapt the general theory of generalized Bayesian inference (Ghosal, Ghosh, and van der Vaart, 2000; or Kleijn and van der Vaart, 2012) via entropy bounds of the RKHS unit ball, showing that the contraction rate is controlled by the metric entropy of the parameter space mapped through the feature map.

2. **Small-Ball Probabilities of Gaussian Quadratic Forms in Hilbert Spaces**: 
   Li and Shao (2001, *"A note on the lower tail probabilities of Gaussian quadratic forms"*, and earlier works by Li and Linde, 1999) study small-ball probabilities of the form $\mathbb{P}(\sum_{j=1}^\infty \lambda_j Z_j^2 \le \epsilon^2)$, where $Z_j \sim \mathcal{N}(0,1)$ are independent standard normal random variables and $\lambda_j$ are eigenvalues (such as Mercer eigenvalues of an MMD kernel). *Hypotheses:* Requires precise control over the decay rate of $\lambda_j$ (e.g., polynomial $\lambda_j \sim j^{-a}$ vs exponential $\lambda_j \sim e^{-bj}$). *Technique:* The small-ball probability behavior is governed by the analytic structure of the spectral decay via saddle-point approximations or entropy numbers of the operator, directly dictating the exact scaling of the denominator in ABC rejection algorithms.

3. **Ill-Posedness of Parameter Inversion via Compact Integral Operators**: 
   The mapping $\theta \mapsto P_\theta \mapsto \mathbb{E}[k(X, \cdot)] \in \mathcal{H}$ can be viewed through the lens of nonlinear ill-posed inverse problems (Engl, Hanke, and Neubauer, 1996, *"Regularization of Inverse Problems"*). *Hypotheses:* Assuming the forward map $\theta \to P_\theta$ is differentiable in the Fréchet sense and the embedding operator from the tangent space to the RKHS $\mathcal{H}$ is compact. *Technique:* The choice of kernel smoothness dictates the degree of compactness of the covariance operator. Smooth kernels (Gaussian) yield severely ill-posed inverse maps with exponentially small singular values, causing the parameter sensitivity modulus to degenerate, which mirrors classical results in spectral regularization methods like Tikhonov regularization or spectral cutoff.

4. **Concentration and Moderate Deviations of U-Statistics in RKHS**: 
   Gine, Latała, and Zinn (2000, *"Exponential and moment inequalities for U-statistics"*), along with Koroljuk and Borovskich (1994), provide deviation inequalities for degenerate and non-degenerate U-statistics, which apply directly to empirical MMD estimators $\widehat{\text{MMD}}_n^2$. *Hypotheses:* Assumes bounded kernels or finite moments of order corresponding to the RKHS norm. *Technique:* Hoeffding and decoupling decompositions allow bounding the tail probabilities of $\widehat{\text{MMD}}_n^2 - \text{MMD}^2(P_0, P_\theta)$ by sums of independent chaos variables weighted by the kernel's eigenvalues $\lambda_j$, confirming that the empirical convergence rate is determined by the trace norm $\sum \lambda_j = \mathbb{E}[k(X,X)]$, which is dimension-independent, whereas the variance depends on $\sum \lambda_j^2$.

## Obstacles

1. **Indicator Filter vs. Exponential Gibbs Form**: The rigorous literature on generalized Bayesian inference almost exclusively studies exponential Gibbs posteriors $e^{-\gamma_n n \text{MMD}^2}$. Strict ABC rejection relies on an indicator function $\mathbb{I}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$. Bounding the small-ball probability of the empirical MMD *conditioned* on a parameter $\theta$ requires uniform control over the fluctuations of the U-statistic across the entire parameter space, which standard generalized posterior proofs bypass via smoothness of the Gibbs weight.

2. **Nonlinear Parameter-to-MMD Mapping**: While linear operator theory and spectral decay (Mercer's theorem) cleanly describe the discrepancy between two fixed distributions, parameter estimation requires analyzing $\text{MMD}^2(P_0, P_\theta)$ as $\theta \to \theta_0$. If the kernel is too smooth, the Taylor expansion of $\text{MMD}^2(P_0, P_\theta)$ flattens drastically along high-frequency eigenfunctions, leading to a degenerate Hessian or a vanishing local identifiability constant $c(d)$ that counteracts the benefits of fast empirical concentration.

## Suggested next steps

1. `Search query`: `"generalized Bayesian inference" AND "Maximum Mean Discrepancy" AND "contraction rate"`
2. `Search query`: `"small ball probabilities" AND "Gaussian quadratic forms" AND "eigenvalue decay"`
3. `Search query`: `"Approximate Bayesian computation" AND "posterior contraction" AND "discrepancy measure"`
4. Investigate the adaptation of spectral cutoff regularization error bounds (from inverse problems literature) to lower bound the local identifiability modulus $\inf_{\|\theta - \theta_0\| \ge \delta} \text{MMD}^2(P_0, P_\theta)$ as a function of the kernel's Mercer eigenvalues $\lambda_j$.

---

## Finding #99: task_111 (Sketcher)

*Worker: **sketcher** | Task ID: `task_111` | Duration: 13.5s | Timestamp: 2026-09-09 11:52:59 UTC | Focus Nodes: `lemma_3`, `idea_1`, `obstacle_1`, `obstacle_4`*

**Assigned Task Prompt**:
> Using lemma_3 and idea_1, sketch the derivation of the ABC posterior contraction rate by combining the numerator bound (empirical MMD concentration with spectral truncation) and the denominator bound (small-ball probability with eigenvalue decay lambda_j ~ j^{-p}).

**Worker Output & Derivations**:

## Findings

1. **Spectral decomposition and local quadratic approximation of population MMD**: 
   By Mercer's theorem, let $k(x,y) = \sum_{j=1}^\infty \lambda_j e_j(x) e_j(y)$ with orthonormal eigenfunctions $e_j$ under $P_0$. The population squared MMD is $\operatorname{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2$, where $\mu_{\theta,j} = \mathbb{E}_{Y \sim P_\theta}[e_j(Y)]$. Taylor expanding $\mu_{\theta,j}$ around $\theta_0$ yields $\mu_{0,j} - \mu_{\theta,j} \approx \langle g_j, \theta - \theta_0 \rangle$ where $g_j = \nabla_\theta \mu_{\theta_0, j}$. Thus, $\operatorname{MMD}^2(P_0, P_\theta) \approx (\theta - \theta_0)^T H (\theta - \theta_0)$, where the Fisher-like operator matrix is $H = \sum_{j=1}^\infty \lambda_j g_j g_j^T$. The decay of Mercer eigenvalues $\lambda_j \sim j^{-2s/d}$ directly dictates the decay of the eigenvalues of $H$, making the inverse problem severely ill-posed in high-frequency directions.

2. **Empirical concentration via spectral truncation (Implementing `idea_1`)**: 
   To bound $\sup_\theta |\widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta, m}) - \mathrm{MMD}^2(P_0, P_\theta)|$, we project the estimator onto the first $K_n$ eigenfunctions. The empirical squared MMD is split into a finite-dimensional sum and a tail sum: $\widehat{\mathrm{MMD}}_n^2 = \sum_{j=1}^{K_n} \lambda_j (\widehat{\mu}_{0,j} - \widehat{\mu}_{\theta,j})^2 + \sum_{j > K_n} \lambda_j (\widehat{\mu}_{0,j} - \widehat{\mu}_{\theta,j})^2$. The top $K_n$ empirical means concentrate at parametric rates $O_p(K_n / n)$, while the tail sum is bounded by $\sum_{j > K_n} \lambda_j \asymp K_n^{1 - 2s/d}$ (assuming $2s/d > 1$). Balancing the estimation variance $O(K_n / n)$ and the truncation error $O(K_n^{1 - 2s/d})$ yields the optimal truncation level $K_n \asymp n^{\frac{d}{2s + d}}$, producing a uniform convergence rate of the empirical MMD squared of order $R_n \asymp n^{-\frac{2s}{2s + d}}$.

3. **Numerator bound for the ABC posterior mass**: 
   For the rejection ABC posterior $\Pi_{\epsilon_n}( \|\theta - \theta_0\| > M \epsilon_n \mid P_n)$, the numerator integrates the prior over the set $\{\theta : \|\theta - \theta_0\| > M \epsilon_n \text{ and } \widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta, m}) \le \epsilon_n^2\}$. On this event, the triangle inequality gives $\operatorname{MMD}^2(P_0, P_\theta) \le \widehat{\mathrm{MMD}}_n^2 + 2 |\widehat{\mathrm{MMD}}_n^2 - \operatorname{MMD}^2| \le \epsilon_n^2 + 2 R_n$. Using the local identifiability lower bound $\operatorname{MMD}^2(P_0, P_\theta) \ge c \|\theta - \theta_0\|^{2\beta}$ (where $\beta$ is linked to the decay of the kernel smoothness and parameter map), we deduce that $\|\theta - \theta_0\| \le C (\epsilon_n^2 + n^{-\frac{2s}{2s + d}})^{1/(2\beta)}$. Choosing the ABC tolerance $\epsilon_n \asymp n^{-\frac{s}{2s + d}}$ ensures that outside a neighborhood of radius $M \epsilon_n^{1/\beta}$, the event has probability zero for large $n$.

4. **Denominator bound via small-ball probabilities and eigenvalue decay (`lemma_2` & `obstacle_4`)**: 
   To bound the denominator $\int_\Theta \mathbb{I}(\widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta, m}) \le \epsilon_n^2) d\Pi(\theta)$ from below, we integrate over a small ball $B(\theta_0, r_n)$ with $r_n \asymp \epsilon_n^{1/\beta}$. By Bernton et al. (2019) techniques, we require a lower bound on the probability $\mathbb{P}(\widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta, m}) \le \epsilon_n^2 \mid \theta)$. By `lemma_2`, the variance of the first-order Hoeffding projection along eigen-direction $j$ is proportional to $\lambda_j^2 (\mu_{0,j} - \mu_{\theta,j})^2$. Because $\lambda_j$ decays rapidly ($\lambda_j \sim j^{-2s/d}$), fluctuations in directions of high $j$ are heavily damped, meaning the local acceptance region collapses along these principal axes. This introduces a severe dimension-dependent entropy or volume penalty in the small-ball probability, requiring $\epsilon_n$ to scale worse with dimension $d$ to prevent the denominator from vanishing exponentially.

## Obstacles

1. **Mismatch between exact $\beta$-modulus and spectral decay**: The identifiability exponent $\beta$ (from Bernton et al.-style modulus of continuity $\operatorname{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$) depends on how the parameter $\theta$ perturbs the high-frequency components of the distribution. If $\theta$ only affects smooth components, $\beta$ is degraded or the preconstant $c$ degenerates as $d \to \large \infty$.
2. **Coupling sample sizes $n$ (data) and $m$ (simulation)**: The sketch above assumes population simulations ($m = \infty$). When $m$ is finite, the simulation empirical measure $P_{\theta, m}$ introduces an additional variance term $O(1/m)$ that interacts with the kernel spectral decay through the cross-terms in $\widehat{\mathrm{MMD}}_n^2$, complicating the uniform spectral truncation bound.

## Suggested next steps

1. **Explicitly compute the Hessian $H$ for a parametric family**: Derive the exact spectrum of $H = \sum_{j=1}^\infty \lambda_j g_j g_j^T$ for a location-scale Gaussian family using a Gaussian kernel to quantify how the preconstant $c(d)$ degrades with dimension $d$.
2. **Establish the exact modulus of continuity $\beta$**: Prove a lower bound on $\operatorname{MMD}(P_0, P_\theta)$ in terms of $\|\theta - \theta_0\|$ using the RKHS norm equivalence, explicitly separating the contribution of the top $K_n$ eigenvalues from the tail.
3. **Finite-$m$ variance control**: Extend the Hoeffding projection variance formula (`lemma_2`) to include the simulation sample size $m$, balancing $n$ and $m$ to optimize the overall computational and statistical contraction rate.

---

## Finding #100: task_114 (Verifier)

*Worker: **verifier** | Task ID: `task_114` | Duration: 14.1s | Timestamp: 2026-09-09 11:53:07 UTC | Focus Nodes: `lemma_3`*

**Assigned Task Prompt**:
> Verify the small-ball probability asymptotic exponent derived in lemma_3 for quadratic forms with polynomial eigenvalue decay lambda_j ~ j^{-p} using standard analytic results (e.g., Li-Shao 2001 or equivalent Gaussian small-ball theorems).

**Worker Output & Derivations**:

## Verdict
GAP. We checked the small-ball probability asymptotic exponent for quadratic forms with polynomial eigenvalue decay $\lambda_j \sim j^{-p}$, but `lemma_3` is missing from the provided research context, making it impossible to verify its exact hypotheses and statement, although the underlying saddlepoint derivation yielding $\epsilon^{-1/(p-1)}$ is mathematically sound for central quadratic forms.

## Findings
1. **Saddlepoint integral approximation**: For a central quadratic form $Q = \sum_{j=1}^\infty \lambda_j g_j^2$ with $g_j \sim \mathcal{N}(0,1)$ and $\lambda_j \sim j^{-p}$ ($p > 1$), the log-Laplace transform $\psi(t

---

## Finding #101: task_113 (Decomposer)

*Worker: **decomposer** | Task ID: `task_113` | Duration: 14.1s | Timestamp: 2026-09-09 11:53:13 UTC | Focus Nodes: `hypothesis_1`, `hypothesis_2`, `lemma_3`, `obstacle_1`*

**Assigned Task Prompt**:
> Decompose the remaining gaps in proving the exact minimax contraction rate for MMD-ABC rejection algorithms into rigorous subgoals (identifiability modulus, empirical process concentration, denominator small-ball bound).

**Worker Output & Derivations**:

## Findings

1. **Plan A: Spectral Truncation and Finite-Dimensional Reduction**. Approximate the infinite-dimensional MMD distance by projecting onto the first $K_n$ eigenfunctions of the kernel integral operator. This transforms the infinite-dimensional ABC problem into a finite-dimensional Euclidean ABC problem with controlled truncation bias, enabling standard rejection posterior contraction proofs.
   - *Subgoal 1.1 (Truncation Bias Bound)*: Quantify the tail approximation error $\sup_{\theta \in \Theta} |\text{MMD}^2(P_0, P_\theta) - \text{MMD}_{K_n}^2(P_0, P_\theta)|$ explicitly in terms of the kernel eigenvalues $\lambda_j$ for $j > K_n$ and the Sobolev smoothness class of the model family $P_\theta$.
   - *Subgoal 1.2 (Empirical Concentration of Truncated MMD)*: Establish exponential concentration inequalities for the empirical truncated MMD $\widehat{\text{MMD}}_{K_n}^2$ using Talagrand's concentration inequality for bounded functions or Bernstein-type bounds for U-statistics of fixed dimension $K_n$.
   - *Subgoal 1.3 (Finite-Dimensional Denominator Lower Bound)*: Lower-bound the prior probability of the accepted region $\{\theta : \widehat{\text{MMD}}_{K_n}^2(P_n, P_{\theta,m}) \le \epsilon_n^2\}$ using the finite-dimensional identifiability modulus and smoothness of the parameter map $\theta \mapsto \mu_{\theta,j}$ for $j=1,\dots,K_n$.
   - *Subgoal 1.4 (Optimal Choice of $K_n$ and $\epsilon_n$)*: Balance the truncation bias (decreasing in $K_n$) against estimation variance (increasing in $K_n$ due to dimension dependence) to derive the overall posterior contraction rate.

2. **Plan B: Uniform Modulus of Continuity and Small-Ball Probability (Bernton-type)**. Directly adapt the Bernton et al. (2019) framework for Wasserstein ABC to MMD-ABC by establishing a global parameter identifiability modulus $\text{MMD}(P_0, P_\theta) \ge c \|\theta - \theta_0\|^\beta$ and controlling the denominator via the small-ball probability of the empirical MMD metric process.
   - *Subgoal 2.1 (Global Identifiability Modulus Derivation)*: Prove a lower bound $\text{MMD}(P_0, P_\theta) \ge c(h, d) \|\theta - \theta_0\|^\beta$ across $\Theta$, explicitly tracking the dependence of the preconstant $c(h, d)$ on kernel bandwidth $h$ and dimension $d$ to resolve Hypothesis 2.
   - *Subgoal 2.2 (Empirical MMD Small-Ball Probability)*: Derive lower bounds for the small-ball probability $\mathbb{P}(\widehat{\text{MMD}}_n(P_0, P_0) \le \epsilon)$ using Dudley's entropy integral or generic chaining over the RKHS unit ball.
   - *Subgoal 2.3 (Prior Mass Condition / Denominator Bound)*: Combine the global identifiability modulus and small-ball probability to prove a strictly positive lower bound on the ABC acceptance probability $\Pi(\theta : \widehat{\text{MMD}}_n^2(P_n, P_{\theta,m}) \le \epsilon_n^2)$ for prior distributions with full support on $\Theta$.
   - *Subgoal 2.4 (Posterior Mass Concentration Rate)*: Synthesize numerator exponential tail bounds and denominator small-ball bounds into the final minimax contraction rate $n^{-\gamma}$ using general ABC posterior contraction master theorems.

3. **Plan C: Degenerate U-Statistic Chaos Expansion and RKHS Norm Concentration**. Treat the squared empirical MMD directly as a degenerate two-sample U-statistic and apply decoupling inequalities and exponential concentration for chaos variables in RKHS to bypass spectral expansions entirely.
   - *Subgoal 3.1 (U-Statistic Hoeffding Decomposition)*: Express $\widehat{\text{MMD}}^2(P_n, P_m)$ as a sum of degenerate U-statistics of order 1 and 2 using the kernel integral operator eigenbasis from Lemma 2, and explicitly bound the variance components.
   - *Subgoal 3.2 (Talagrand-Type Inequality for U-Processes in RKHS)*: Prove exponential tail bounds for the uniform fluctuation $\sup_{\theta \in \Theta} |\widehat{\text{MMD}}^2(P_n, P_{\theta,m}) - \text{MMD}^2(P_0, P_\theta)|$ using generic chaining or decoupling methods for quadratic forms in Hilbert space.
   - *Subgoal 3.3 (Asymmetric Sample Size Variance Scaling)*: Quantify the exact variance asymmetry between data size $n$ and simulation size $m$ to resolve Obstacle 2 and determine the optimal ratio $m/n$ for achieving parametric efficiency.
   - *Subgoal 3.4 (Local Minimax Lower Bound)*: Construct hard one-dimensional parametric subproblems (generalizing Counterexample 1) to match the upper bound and prove minimax optimality of the resulting MMD-ABC rate.

## Obstacles

- In Plan A, Subgoal 1.3 is exceptionally difficult because bounding the finite-dimensional denominator requires controlling the smallest eigenvalue of the Hessian matrix $H(\theta_0)$ of $\text{MMD}^2$, which collapses exponentially fast in dimensions corresponding to high-frequency eigenfunctions (Obstacle 4).
- In Plan B, Subgoals 2.1 and 2.3 are blocked by the dimension-dependent preconstant curse (Hypothesis 2); proving that $c(h,d)$ does not vanish too rapidly with $d$ requires sharp lower bounds on kernel embedding derivatives that may fail for ultra-smooth kernels like Gaussian.
- In Plan C, Subgoal 3.2 faces technical obstructions from infinite-dimensional chaining bounds for non-degenerate quadratic empirical processes where the metric entropy of the RKHS unit ball grows rapidly unless restricted.
- Missing information: Explicit non-asymptotic lower bounds on the smallest eigenvalue of the population MMD Hessian $H(\theta_0)$ as a function of the kernel bandwidth $h$, dimension $d$, and underlying density smoothness.

## Suggested next steps

1. Compute the exact Hessian matrix $H(\theta_0)$ of $\text{MMD}^2(P_0,

---

## Finding #102: task_115 (Sketcher)

*Worker: **sketcher** | Task ID: `task_115` | Duration: 9.3s | Timestamp: 2026-09-09 11:53:21 UTC | Focus Nodes: `lemma_3`, `idea_1`, `obstacle_1`*

**Assigned Task Prompt**:
> Using lemma_3 and idea_1, sketch the derivation of the ABC posterior contraction rate by combining the small-ball probability bound with the concentration of empirical MMD.

**Worker Output & Derivations**:

## Findings

1. **Decomposition of the ABC Posterior Contraction Rate:** Following the Bernton et al. (2019) framework (`paper_2`), the rejection ABC posterior probability of the set $S_n^c = \{\theta : \|\theta - \theta_0\| > M_n \epsilon_n^{1/\beta}\}$ is bounded by $\Pi_n(\theta \in S_n^c \mid X_{1:n}) \le \frac{\exp(-C n \epsilon_n^2) + \mathbb{P}(\sup_{\theta \in S_n^c} \widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta,m}) \le \epsilon_n^2)}{\Pi(\theta : \mathrm{MMD}^2(P_0, P_\theta) \le \epsilon_n^2 / 2 \text{ and } |\widehat{\mathrm{MMD}}_n^2 - \mathrm{MMD}^2| \le \epsilon_n^2 / 2)}$. Bounding the contraction rate thus reduces to controlling the denominator via the prior small-ball probability and the numerator via uniform concentration of the empirical MMD.

2. **Spectral Truncation of Empirical MMD (`idea_1`):** Using the Mercer representation (`lemma_1`), write the squared empirical MMD as $\widehat{\mathrm{MMD}}_n^2(P_n, P_{\theta,m}) = \sum_{j=1}^\infty \lambda_j (\hat{\mu}_{0,j} - \hat{\mu}_{\theta,j})^2$. Truncate the sum at $K_n$ terms. The error decomposes into the truncation tail $R_{K_n} = \sum_{j > K_n} \lambda_j (\hat{\mu}_{0,j} - \hat{\mu}_{\theta,j})^2$ and the finite sum. By choosing $K_n$ such that the tail is bounded by $O(\epsilon_n^2)$, the problem reduces to controlling the empirical fluctuations of the first $K_n$ coefficients.

3. **Hoeffding Projection Variance (`lemma_2`):** By `lemma_2`, the variance of the first-order projection of the empirical MMD is $\operatorname{Var}(\widehat{\mathrm{MMD}}_n^{(K_n)}) = O\left(\sum_{j=1}^{K_n} \lambda_j^2 (\mu_{0,j} - \mu_{\theta,j})^2 / n + \dots / m\right)$. Since Mercer eigenvalues $\lambda_j$ decay rapidly (e.g., $\lambda_j \sim j^{-2s/d}$ for smoothness $s$), the variance of individual components shrinks fast for large $j$. However, this rapid decay also flattens the population signal $(\mu_{0,j} - \mu_{\theta,j})^2$ along high-frequency eigenfunctions, directly linking kernel smoothness to the denominator's small-ball behavior.

4. **Balancing Truncation and Tolerance for the Rate:** To ensure the numerator's probability of false acceptance on $S_n^c$ vanishes and the denominator remains non-vanishing, we equate the tolerance $\epsilon_n$ to the sum of estimation error and truncation bias: $\epsilon_n^2 \asymp \frac{K_n}{n} + \frac{K_n}{m} + \sum_{j > K_n} \lambda_j$. For polynomial spectral decay $\lambda_j \sim j^{-2s/d}$, setting $\sum_{j > K_n} \lambda_j \sim K_n^{1 - 2s/d} \asymp \epsilon_n^2$ yields the optimal truncation dimension $K_n \asymp \epsilon_n^{-2 / (1 - 2s/d)}$, giving the final parametric-like or nonparametric ABC contraction rate depending on the dimension $d$ and smoothness $s$.

## Obstacles

1. **Uniformity over the Parameter Space:** Bounding $\sup_{\theta \in S_n^c} \widehat{\mathrm{MMD}}_n^2$ requires chaining or bracketing entropy calculations over the parameter space $\Theta$, which becomes delicate when the map $\theta \mapsto P_\theta$ has a degenerate Jacobian along high-frequency eigendirections.
2. **Dimension-Dependent Preconstant Collapse (`hypothesis_2`, `obstacle_4`):** As dimension $d$ grows, the identifiability modulus preconstant $c(d)$ in $\mathrm{MMD}^2(P_0, P_\theta) \ge c(d) \|\theta - \theta_0\|^\beta$ shrinks exponentially due to spectral suppression (`lemma_2`), causing the denominator small-ball probability $\Pi(\mathrm{MMD}^2 \le \epsilon_n^2)$ to collapse unless $\epsilon_n$ scales exponentially with $d$.

## Suggested next steps

1. **Derive Explicit Bracketing Numbers:** Compute the metric entropy (bracketing numbers) of the class of RKHS-embedded distributions $\{\mu_\theta : \theta \in \Theta\}$ under the MMD metric using the spectral representation (`lemma_1`).
2. **Quantify Preconstant $c(d)$:** Perform a Taylor expansion of $\mathrm{MMD}^2(P_0, P_\theta)$ around $\theta_0$ to explicitly extract the dependence of the Hessian eigenvalues on the kernel spectrum $\lambda_j$ and dimension $d$, verifying `obstacle_4`.
3. **Establish Optimal Tolerance Schedule:** Solve the bias-variance trade-off equation for $\epsilon_n$ explicitly as a function of $n, m, d$, and kernel smoothness $s$ to determine the exact minimax contraction rate for MMD-ABC.

---

## Finding #103: task_117 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_117` | Duration: 13.8s | Timestamp: 2026-09-09 11:53:29 UTC | Focus Nodes: `hypothesis_2`, `obstacle_4`*

**Assigned Task Prompt**:
> Construct a toy model for product Gaussian measures to compute how the preconstant c(d) in MMD^2(P_0, P_theta) >= c(d) ||theta - theta_0||^2 scales with dimension d.

**Worker Output & Derivations**:

## Findings

1. **Exact closed-form expression for product Gaussian MMD**: For $P_0 = \mathcal{N}(0, I_d)$, $P_\theta = \mathcal{N}(\theta, I_d)$, and an isotropic Gaussian kernel $k(x,y) = \exp(-\|x-y\|^2 / (2h^2))$, the squared MMD factorizes across dimensions and evaluates explicitly to $\mathrm{MMD}^2(P_0, P_\theta) = 2 \left(\frac{h}{\sqrt{h^2+2}}\right)^d \left(1 - \exp\left(-\frac{\|\theta\|^2}{2(h^2+2)}\right)\right)$.

2. **Exponential dimension dependence of the preconstant**: Taylor expansion of the squared MMD for small $\|\theta\|$ yields $\mathrm{MMD}^2(P_0, P_\theta) \approx c(d) \|\theta\|^2$, where the preconstant is given by $c(d) = \frac{1}{h^2+2} \left(\frac{h}{\sqrt{h^2+2}}\right)^d$. Since $h / \sqrt{h^2+2} < 1$ for any finite bandwidth $h$, $c(d)$ decays exponentially at rate $O(q^d)$ with base $q < 1$.

3. **Bandwidth trade-off in the preconstant decay base**: The contraction base $q(h) = \frac{h}{\sqrt{h^2+2}}$ approaches $1$ as $h \to \infty$ and $0$ as $h \to 0$. However, taking $h \to \infty$ flattens the pre-multiplier $\frac{1}{h^2+2} \to 0$, revealing a sharp tension: wider kernels slow the exponential decay rate in $d$ but suppress the absolute scale of the MMD sensitivity.

4. **Mechanism of the identifiability loss**: The exponential drop in $c(d)$ originates from the inner product cross-term $\prod_{j=1}^d \exp(-\theta_j^2 / [2(h^2+2)])$. In high dimensions, the overlap between the kernel feature maps of shifted Gaussian measures contracts exponentially unless the bandwidth scales with dimension.

## Obstacles

1. **Restriction to product structure**: The exact factorization relies heavily on isotropic product Gaussians and product kernels; non-diagonal covariance structures $\Sigma_0 \neq \Sigma_\theta$ introduce interacting cross-terms that prevent clean scalar product factorization.

2. **Fixed bandwidth limitation**: The calculation assumes a fixed bandwidth $h$ independent of dimension $d$. In practice, kernel bandwidths are often chosen via heuristics (like median heuristic) that scale with $\sqrt{d}$, which modifies the base $q(h)$ and requires asymptotic analysis as $d, n \to \infty$ jointly.

## Suggested next steps

1. **Analyze bandwidth scaling with dimension**: Compute the limiting behavior of $c(d)$ when the bandwidth scales as $h = \tilde{h} \sqrt{d}$ to see if the exponential dimension curse can be averted.
2. **Evaluate non-Gaussian kernels**: Perform a similar exact calculation for Matérn or inverse multiquadric kernels on product domains to test whether algebraic spectral decay mitigates the exponential preconstant collapse.
3. **Connect $c(d)$ to ABC acceptance volume**: Translate the exponential decay of $c(d)$ into a lower bound for the ABC denominator mass $\int \mathbb{I}(\widehat{\mathrm{MMD}}_n^2 \le \epsilon_n^2) d\pi(\theta)$ to quantify the required sample size $n$ or tolerance $\epsilon_n$ as a function of $d$.

---

## Finding #104: task_116 (Searcher)

*Worker: **searcher** | Task ID: `task_116` | Duration: 14.4s | Timestamp: 2026-09-09 11:53:37 UTC | Focus Nodes: `lemma_3`, `obstacle_3`*

**Assigned Task Prompt**:
> Search literature for small-ball probabilities of Gaussian kernel quadratic forms (exponential spectral decay) and how the small-ball exponent depends on the dimension d.

**Worker Output & Derivations**:

## Findings

1. **Small-ball asymptotics for weighted sums of non-central chi-squared variables (Sytaya, 1974; Li & Shao, 2001).** 
   *Statement/Result:* Let $S = \sum_{j=1}^\infty \lambda_j Z_j^2$ where $Z_j \sim \mathcal{N}(m_j, 1)$ are independent non-central normal variables with means $m_j$, and $\lambda_j > 0$ are eigenvalues satisfying $\sum \lambda_j < \infty$. The small-ball probability $\mathbb{P}(S \le \epsilon)$ as $\epsilon \to 0$ is governed by the tail behavior of the eigenvalues $\lambda_j$ and the non-centrality parameters $m_j$. For exponentially decaying eigenvalues $\lambda_j \sim e^{-c j}$ (typical of Gaussian kernels), the small-ball probability decays sub-exponentially or as a stretched exponential in $\log(1/\epsilon)$, specifically $-\log \mathbb{P}(S \le \epsilon) \asymp (\log(1/\epsilon))^{1+1/k}$ for polynomial-exponential decays, or faster. 
   *Reference:* Sytaya, G. N. (1974). "On certain asymptotic representations of the Gaussian measure of small spheres." *Theory of Probability and its Applications*, 19(2), 275–286; Li, W. V., & Shao, Q.-M. (2001). "Gaussian processes: inequalities, small ball probabilities and applications." *Stochastic Processes and their Applications*, 12, 533-597.

2. **Metric entropy and small-ball probabilities in Hilbert spaces (Kuelbs & Li, 1993).**
   *Statement/Result:* Let $\mu$ be a centered Gaussian measure on a separable Hilbert space $H$ with covariance operator having eigenvalues $\lambda_j$. Let $B_H$ be the unit ball of the reproducing kernel Hilbert space (RKHS) associated with $\mu$. Then the small-ball probability satisfies $\lim_{\epsilon \to 0} \frac{\log \mu(B(0, \epsilon))}{\log \mathcal{N}(\epsilon, B_H, \|\cdot\|_H)} = -1/2$, where $\mathcal{N}(\epsilon, B_H, \|\cdot\|_H)$ is the covering number of the RKHS unit ball by balls of radius $\epsilon$ in the RKHS norm.
   *Applicability & Translation:* This links the denominator of the MMD-ABC acceptance region directly to the metric entropy of the kernel's RKHS. For analytic kernels (like the Gaussian kernel), the covering numbers grow moderately in finite dimensions, but the constants scale exponentially with dimension $d$.
   *Reference:* Kuelbs, J., & Li, W. V. (1993). "Metric entropy and small ball probabilities for Gaussian measures." *The Annals of Probability*, 21(2), 783–812.

3. **Tensor product spectral decay and dimension dependence for Gaussian kernels (Dziubanski et al. / classical Sturm-Liouville theory).**
   *Statement/Result:* For the Gaussian kernel $k(x,y) = \exp(-\gamma \|x-y\|^2)$ defined on a $d$-dimensional hypercube $[-L, L]^d$ with respect to the uniform or standard Gaussian reference measure, the eigenvalues factorize via tensor products: $\lambda_{\mathbf{j}} = \prod_{k=1}^d \lambda_{j_k}^{(1)}$, where $\mathbf{j} = (j_1, \dots, j_d) \in \mathbb{N}^d$ and 1D eigenvalues decay exponentially $\lambda_j^{(1)} \sim C \rho^j$ ($\rho < 1$). Consequently, in $d$ dimensions, the eigenvalues decay as $\lambda_{\mathbf{j}} \sim C^d \rho^{\sum_{k=1}^d j_k}$. 
   *Consequence:* The number of eigenvalues above any fixed threshold $\delta > 0$ grows polynomially or exponentially with $d$, creating a high-dimensional degeneracy in the quadratic form's spectrum. This breaks the standard low-dimensional small-ball bounds and forces the small-ball exponent to acquire a explicit power-law or multiplicative dependence on $d$.
   *Reference:* Fasshauer, G., & McCourt, M. (2015). *Kernel Methods-Exhaustive Algorithmics*. Higher Education Press / Springer (see discussion on multidimensional Mercer expansions).

## Obstacles

1. **Non-centrality mismatch in MMD small-ball bounds:** Standard small-ball theorems (such as those by Sytaya or Li & Shao) apply to *centered* quadratic forms or purely central Gaussian chaos. In MMD-ABC, the discrepancy is $\mathrm{MMD}^2(P_0, P_\theta) = \sum_{j=1}^\infty \lambda_j (\mu_{0,j} - \mu_{\theta,j})^2 + \text{centered noise terms}$. When $\theta \neq \theta_0$, the non-centrality parameter $\Delta_j = (\mu_{0,j} - \mu_{\theta,j})^2$ shifts the small-ball probability calculation into a non-central small-ball problem, which depends sensitively on how fast the differences $\mu_{0,j} - \mu_{\theta,j}$ align with the rapidly decaying eigenvalues $\lambda_j$.
2. **Dimension-dependent constants in metric entropy:** While metric entropy bounds exist for analytic kernels, the preconstants depend factorially or exponentially on the dimension $d$ (e.g., $\exp(c d)$). This makes bounds on the ABC denominator vacuous for moderate-to-high dimensions $d$ unless sample size $n$ scales correspondingly.

## Suggested next steps

1. Query: `"small ball probabilities" AND "non-central quadratic forms" AND "exponential spectral decay"`
2. Query: `"small ball probabilities for Gaussian measures" AND "tensor product kernels" AND "dimension dependence"`
3. Query: `"metric entropy of reproducing kernel Hilbert spaces" AND "Gaussian kernel" AND "covering numbers"`
4. Query: `"small ball probability of empirical MMD" OR "Maximum Mean Discrepancy" AND "small ball"`

---

## Finding #105: task_118 (Sketcher)

*Worker: **sketcher** | Task ID: `task_118` | Duration: 11.0s | Timestamp: 2026-09-09 11:53:47 UTC | Focus Nodes: `lemma_4`, `obstacle_4`, `hypothesis_2`*

**Assigned Task Prompt**:
> Using the Gaussian location family contraction rate result in lemma_4, sketch whether the ABC posterior denominator (prior acceptance probability) remains non-vanishing for tolerance epsilon_n 
asymp r_n, or if the shrinking acceptance volume requires adjusted tolerance schedules.

**Worker Output & Derivations**:

## Findings

1. **Decomposition of the ABC Denominator via Empirical Process**: The prior acceptance probability (ABC denominator) is given by $A_n(\epsilon_n) = \int \mathbb{P}\left(\widehat{\mathrm{MMD}}_n^2(\theta) \le \epsilon_n^2 \mid \theta\right) \Pi(\theta) d\theta$. Writing the empirical squared MMD as $\widehat{\mathrm{MMD}}_n^2(\theta) = \mathrm{MMD}^2(P_0, P_\theta) + \xi_n(\theta)$, where $\xi_n(\theta)$ is a centered empirical process term with $\mathbb{E}[\xi_n(\theta)] = 0$ and $\operatorname{Var}(\xi_n(\theta)) = O(n^{-1})$, the acceptance event becomes $\mathrm{MMD}^2(P_0, P_\theta) \le \epsilon_n^2 - \xi_n(\theta)$.

2. **Quadratic Expansion for the Gaussian Location Family**: Using the exact form from Counterexample 1, $\mathrm{MMD}^2(P_0, P_\theta) = C_h \theta^2 + O(\theta^4)$ with $C_h = \frac{h}{2(2+h^2)^{3/2}}$. Assuming the prior $\Pi(\theta)$ is positive and continuous near $\theta_0 = 0$ with $\Pi(\theta) \ge c_0$ on $|\theta| \le \delta$, the denominator is bounded below by $A_n(\epsilon_n) \ge c_0 \int_{-\delta}^{\delta} \mathbb{P}\left(C_h \theta^2 + \xi_n(\theta) \le \epsilon_n^2\right) d\theta$.

3. **Variance Control via Hoeffding Projection**: By Lemma 2, the leading variance of the empirical MMD estimator is $\operatorname{Var}(\xi_n(\theta)) = \frac{\sigma^2(\theta)}{n} + O(n^{-2})$, where $\sigma^2(\theta) = 4 \operatorname{Var}_{X \sim P_0}\left[\mathbb{E}_{Y \sim P_\theta}[k(X,Y)] - \mathbb{E}[k(X,X')]\right]$. Thus, for a fixed $\theta$, the fluctuation $\xi_n(\theta)$ is of order $O_p(n^{-1/2})$.

4. **Critical Scaling of the Tolerance Schedule $\epsilon_n$**: If the tolerance is chosen such that $\epsilon_n^2 \asymp n^{-1/2}$, then for $\theta$ such that $C_h \theta^2 \le \epsilon_n^2$, we require $|\theta| \le O(n^{-1/4})$. Integrating over this region yields a prior acceptance probability $A_n(\epsilon_n) \asymp n^{-1/4}$, which is polynomial in $n$ and hence non-vanishing in the limit $n \to \infty$.

5. **Failure Mode under Parametric Tolerance Schedules**: If one attempts a strict parametric tolerance $\epsilon_n^2 \asymp n^{-1}$ (matching the optimal posterior contraction rate for parametric models), the tolerance falls below the standard deviation of the empirical process $\xi_n(\theta) = O_p(n^{-1/2})$. Consequently, the probability $\mathbb{P}\left(C_h \theta^2 + \xi_n(\theta) \le \epsilon_n^2\right)$ collapses unless $\theta$ is restricted to an empty or exponentially small set, causing the ABC denominator $A_n(\epsilon_n)$ to vanish exponentially fast ($A_n(\epsilon_n) = o(e^{-cn})$ or degenerate).

## Obstacles

1. **Uniformity over $\theta$ in the Empirical Process Bound**: The decomposition $\widehat{\mathrm{MMD}}_n^2(\theta) = \mathrm{MMD}^2(P_0, P_\theta) + \xi_n(\theta)$ requires uniform control over $\theta$ in the integration domain, i.e., $\sup_{|\theta| \le \delta} |\xi_n(\theta)| = O_p(n^{-1/2})$, which needs standard empirical process entropy calculations (bracketing numbers for the family of kernels $k(x, Y_\theta)$).

2. **Bandwidth Dependency of the Constant $C_h$**: As the kernel bandwidth $h \to 0$ or $h \to \infty$, the preconstant $C_h = \frac{h}{2(2+h^2)^{3/2}}$ vanishes. In these regimes, even if $\epsilon_n$ is fixed, the accepted volume contracts severely, showing that kernel hyperparameters directly modulate the denominator's preconstant (matching Hypothesis 2).

## Suggested next steps

1. **Establish Uniform Empiricial Process Rates**: Prove $\sup_{\theta \in \Theta} |\widehat{\mathrm{MMD}}_n^2(\theta) - \mathrm{MMD}^2(P_0, P_\theta) - \mathbb{E}[\dots] | = O_p(n^{-1/2})$ using Talagrand's concentration inequality or chaining for RKHS-valued functions.
2. **Derive Exact Posterior Contraction Rate**: Combine the lower bound on $A_n(\epsilon_n) \asymp \epsilon_n^2$ with an upper bound on the numerator mass to establish the exact minimax posterior contraction rate for MMD-ABC as a function of the tolerance schedule $\epsilon_n$.
3. **Analyze Dimension-Dependent Preconstants**: Extend the 1D Gaussian location calculation to $d$ dimensions to verify whether $C_h(d)$ decays exponentially with $d$, formalizing Hypothesis 2.

---

## Finding #106: task_120 (Toy_Example)

*Worker: **toy_example** | Task ID: `task_120` | Duration: 11.6s | Timestamp: 2026-09-09 11:53:59 UTC | Focus Nodes: `approach_2`, `counterexample_1`, `hypothesis_2`*

**Assigned Task Prompt**:
> Construct a toy model for scale families P_sigma = N(0, sigma^2 I_d) under a Gaussian kernel k_h(x,y) to test whether the identifiability exponent beta = 1 holds or degrades for scale parameters, as investigated in approach_2.

**Worker Output & Derivations**:

^2 + h^2)^{-d/2 - 1} = \frac{1}{2} f_d'(\sigma_0)$.
So the linear terms in $\delta$ still cancel out: $f_d' - 2g_d' = f_d' - 2(\frac{1}{2}f_d') = 0$.

Now let's look at the second derivatives:
$f_d''(\sigma_0) = \left[ -2d h^d (2\sigma_0^2 + h^2)^{-d/2 - 1} + (-2d\sigma_0 h^d) \left(-\frac{d}{2}-1\right) (2\sigma_0^2

---

## Finding #107: task_121 (Sketcher)

*Worker: **sketcher** | Task ID: `task_121` | Duration: 14.6s | Timestamp: 2026-09-09 11:54:12 UTC | Focus Nodes: `approach_3`, `obstacle_3`, `lemma_2`*

**Assigned Task Prompt**:
> Formalize Subgoal 3.3 (Bandwidth Optimization) by setting up a formal optimization problem minimizing the sum of squared spectral truncation bias and effective dimension variance with respect to the kernel bandwidth gamma.

**Worker Output & Derivations**:

## Findings

1. **Subgoal Status: PARTIAL** (Formalization of the Bandwidth Optimization Problem for MMD-ABC). 
   We set up the objective function balancing the squared spectral bias (truncation/smoothing error) against the estimation variance governed by the kernel's effective dimension, parameterized by the kernel bandwidth $\gamma > 0$ (or smoothing parameter $h = \gamma^{-1/2}$).

2. **Objective Function Formulation**:
   Let $\theta = \theta_0 + \Delta\theta$ be the parameter of interest. The squared discrepancy error in MMD-ABC combines a **squared bias term** (from damping or truncating high-frequency spectral components) and a **variance term** (from empirical estimation noise governed by the kernel eigenvalues).
   We formalize the trade-off as the minimization problem over bandwidth $\gamma > 0$ and truncation level $K \in \mathbb{N}$:
   $$\min_{\gamma > 0, \, K \ge 1} \left\{ \mathcal{B}^2(\gamma, K; \Delta\theta) + \mathcal{V}(\gamma, K; n) \right\}$$

3. **Explicit Form of the Squared Spectral Bias $\mathcal{B}^2(\gamma, K; \Delta\theta)$**:
   Using the spectral representation of the squared population MMD (Lemma 1) and linearizing around $\theta_0$ via $\Delta\theta = \theta - \theta_0$:
   $$\mathcal{B}^2(\gamma, K; \Delta\theta) = \sum_{j=K+1}^\infty \lambda_j(\gamma) \left( \langle \nabla_\theta \mu_{\theta_0, j}, \Delta\theta \rangle \right)^2 + \sum_{j=1}^K (1 - \omega_j(\gamma, \Delta\theta)) \lambda_j(\gamma) (\mu_{0,j} - \mu_{\theta,j})^2$$
   Here, $\lambda_j(\gamma)$ are the Mercer eigenvalues of the kernel operator (dependent on bandwidth $\gamma$), $\mu_{\theta,j} = \mathbb{E}_{Y \sim P_\theta}[e_j(Y)]$, and $\omega_j(\gamma, \Delta\theta)$ accounts for higher-order Taylor remainder or explicit spectral filtering weights. For smooth kernels (e.g., Gaussian with scale $\gamma$), large $\gamma$ (heavy smoothing) forces rapid decay of $\lambda_j$ for $j > K(\gamma)$, inflating the truncation/smoothing bias in directions of high-frequency eigenfunctions $e_j$.

4. **Explicit Form of the Effective Dimension Variance $\mathcal{V}(\gamma, K; n)$**:
   From the Hoeffding projection variance (Lemma 2) and RKHS effective dimension bounds (Obstacle 3):
   $$\mathcal{V}(\gamma, K; n) = \frac{C_1}{n} \sum_{j=1}^K \lambda_j(\gamma)^2 (\mu_{0,j} - \mu_{\theta,j})^2 + \frac{C_2}{n} \sum_{j=1}^\infty \lambda_j(\gamma)^2$$
   where the second term corresponds to the uncentered trace component of the empirical U/V-statistic variance ($\frac{1}{n} \operatorname{Tr}(K_\gamma^2)$), acting as the *effective dimension* $d_{\text{eff}}(\gamma) = \sum_{j=1}^\infty \lambda_j(\gamma)^2 / (\sum \lambda_j(\gamma))^2$ scaled by $n^{-1}$. 
   *Trade-off mechanism*: Decreasing bandwidth $\gamma$ (making the kernel rougher/narrower) increases $\lambda_j$ decay speed in high dimensions ($j^{-2s/d}$), reducing $\mathcal{V}(\gamma, K; n)$, but destroys parameter identifiability by shrinking the preconstant or widening the bias $\mathcal{B}^2$.

## Obstacles

1. **Non-convexity and Parameter-Dependency of the Objective**: The objective function $\mathcal{B}^2(\gamma, K; \Delta\theta) + \mathcal{V}(\gamma, K; n)$ explicitly depends on the unknown parameter deviation $\Delta\theta = \theta - \theta_0$. Thus, a universal optimal bandwidth $\gamma^*(n)$ cannot be chosen without assuming a local parameter ball $\|\Delta\theta\| \le \rho_n$ (e.g., inside the ABC acceptance region).
2. **Dimension-Dependent Eigenvalue Asymptotics**: For a $d$-dimensional domain, Mercer eigenvalues behave as $\lambda_j(\gamma) \sim j^{-2s/d}$ (for Matérn of smoothness $s$) or $\exp(-c j^{2/d} \gamma)$ (for Gaussian). As $d$ grows, the variance sum $\sum \lambda_j(\gamma)^2$ and the gradient inner products $\langle \nabla_\theta \mu_{\theta_0, j}, \Delta\theta \rangle^2$ interact in a way that creates a severe curse of dimensionality, making the optimal $\gamma^*(n, d)$ scale unfavorably with $d$.
3. **Indicator vs. Distance Discrepancy**: The ABC rejection step uses an indicator $\mathbb{I}(\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$, meaning the exact optimization of the asymptotic MSE of $\widehat{\text{MMD}}_n^2$ only indirectly controls the ABC posterior contraction rate via small-ball probabilities.

## Suggested next steps

1. **Local Quadratic Approximation**: Fix $\|\Delta\theta\| \asymp r_n$ (the expected posterior contraction rate) and explicitly solve the scalar minimization problem $\min_{\gamma > 0} [ C_3 r_n^2 \sum_{j>K} \lambda_j(\gamma) j^{2s_0} + \frac{1}{n} \sum_{j=1}^K \lambda_j(\gamma)^2 ]$ for standard eigenvalue decay models (polynomial vs. exponential).
2. **Asymptotic Rate Matching**: Equate the squared bias order $O(n^{-2\alpha})$ with the variance order $O(n^{-1})$ to derive the optimal sample-size-dependent bandwidth scaling $\gamma^*(n) \asymp n^{-\nu}$ as a function of the kernel smoothness $s$ and dimension $d$.
3. **Small-Ball Probability Integration**: Translate the bandwidth-optimized MMD-ABC mean-squared error bound into a lower bound for the ABC denominator $\mathbb{P}_{\pi} (\widehat{\text{MMD}}_n^2 \le \epsilon_n^2)$ using Hanson-Wright type tail inequalities for quadratic forms in dependent/empirical variables.

---

# Literature & Paper Retrievals

### Search #1: Openalex

- **Query**: `Maximum Mean Discrepancy ABC convergence rate`
- **Results Returned**: 8

### Search #2: Openalex

- **Query**: `Maximum Mean Discrepancy Approximate Bayesian Computation convergence rate`
- **Results Returned**: 8

### Search #3: Semantic_Scholar

- **Query**: `"approximate Bayesian computation" "maximum mean discrepancy" convergence rate`
- **Results Returned**: 8

### Search #4: Arxiv

- **Query**: `Matern kernel maximum mean discrepancy approximate Bayesian computation parameter estimation contraction rate`
- **Results Returned**: 8

### Paper #5: Concentration of discrepancy-based approximate Bayesian computation via Rademacher complexity

- **Authors**: N/A
- **Year**: N/A
- **DOI/ID**: `s2:8159801f7678ee8d3de8c383510d2feb8185eb96`

### Search #6: Arxiv

- **Query**: `small ball probability kernel quadratic form eigenvalue decay`
- **Results Returned**: 8

### Paper #7: Bounding the Error From Reference Set Kernel Maximum Mean Discrepancy

- **Authors**: N/A
- **Year**: N/A
- **DOI/ID**: `arxiv:1812.04594v1`

### Search #8: Openalex

- **Query**: `maximum mean discrepancy approximate Bayesian computation posterior contraction`
- **Results Returned**: 8

### Search #9: Arxiv

- **Query**: `"Approximate Bayesian Computation" AND "kernel discrepancy" AND "contraction rate"`
- **Results Returned**: 8

### Search #10: Arxiv

- **Query**: `"maximum mean discrepancy" "posterior contraction" convergence`
- **Results Returned**: 8

### Search #11: Openalex

- **Query**: `Frechet derivative mean embedding parameter sensitivity MMD`
- **Results Returned**: 8

### Paper #12: Log-Level Comparison Principle for Small Ball Probabilities

- **Authors**: N/A
- **Year**: N/A
- **DOI/ID**: `arxiv:0805.1773v1`

### Paper #13: Small ball probability, Inverse theorems, and applications

- **Authors**: N/A
- **Year**: N/A
- **DOI/ID**: `arxiv:1301.0019v1`

---

# Graph Evolution Chronology

Chronological sequence of graph mutations decided by the planner:

| Index | Time | Action Type | Details | Result |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 11:27:27 | `ADD_NODE` | n1 | ADD_NODE skipped: empty content |
| 2 | 11:27:27 | `UPDATE_NODE` | n1 | UPDATE_NODE skipped: no such node 'n1' |
| 3 | 11:27:27 | `ADD_NODE` | n2 | ADD_NODE skipped: empty content |
| 4 | 11:27:27 | `UPDATE_NODE` | n2 | UPDATE_NODE skipped: no such node 'n2' |
| 5 | 11:27:27 | `ADD_EDGE` | n1->n2 | ADD_EDGE skipped: n1 -> n2 (unknown node or duplicate) |
| 6 | 11:27:38 | `ADD_NODE` | hyp_kernel_spectrum | ADD_NODE skipped: empty content |
| 7 | 11:27:38 | `ADD_EDGE` | hyp_kernel_spectrum->problem | ADD_EDGE skipped: hyp_kernel_spectrum -> problem (unknown node or duplicate) |
| 8 | 11:27:53 | `ADD_NODE` | paper | added paper_1 (POTENTIALLY_RELEVANT) |
| 9 | 11:27:53 | `ADD_NODE` | lemma | added lemma_1 (PROMISING) |
| 10 | 11:27:53 | `ADD_NODE` | obstacle | added obstacle_1 (OBSTACLE) |
| 11 | 11:27:53 | `ADD_NODE` | obstacle | added obstacle_2 (OBSTACLE) |
| 12 | 11:27:59 | `ADD_NODE` | approach_1 | ADD_NODE skipped: empty content |
| 13 | 11:27:59 | `ADD_NODE` | approach_2 | ADD_NODE skipped: empty content |
| 14 | 11:27:59 | `ADD_EDGE` | problem->approach_1 | ADD_EDGE skipped: problem -> approach_1 (unknown node or duplicate) |
| 15 | 11:27:59 | `ADD_EDGE` | problem->approach_2 | ADD_EDGE skipped: problem -> approach_2 (unknown node or duplicate) |
| 16 | 11:28:09 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 17 | 11:28:09 | `ADD_EDGE` | lemma_2->lemma_1 | ADD_EDGE skipped: lemma_2 -> lemma_1 (unknown node or duplicate) |
| 18 | 11:28:17 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 19 | 11:28:17 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 20 | 11:28:17 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 21 | 11:28:45 | `ADD_NODE` | hypothesis | added hypothesis_1 (PROMISING) |
| 22 | 11:28:45 | `ADD_NODE` | obstacle | added obstacle_3 (OBSTACLE) |
| 23 | 11:28:45 | `ADD_EDGE` | hypothesis_1->problem | edge hypothesis_1 -possible_approach-> problem |
| 24 | 11:28:45 | `ADD_EDGE` | obstacle_3->problem | edge obstacle_3 -blocks-> problem |
| 25 | 11:29:01 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 26 | 11:29:17 | `ADD_NODE` | obstacle_4 | ADD_NODE skipped: empty content |
| 27 | 11:29:17 | `ADD_EDGE` | obstacle_4->problem | ADD_EDGE skipped: obstacle_4 -> problem (unknown node or duplicate) |
| 28 | 11:29:17 | `ADD_EDGE` | obstacle_4->obstacle_1 | ADD_EDGE skipped: obstacle_4 -> obstacle_1 (unknown node or duplicate) |
| 29 | 11:29:28 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 30 | 11:29:28 | `ADD_NODE` | obstacle_4 | ADD_NODE skipped: empty content |
| 31 | 11:29:43 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 32 | 11:29:43 | `UPDATE_NODE` | lemma_2 | UPDATE_NODE skipped: no such node 'lemma_2' |
| 33 | 11:29:43 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 34 | 11:30:05 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 35 | 11:30:05 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 36 | 11:30:05 | `ADD_NODE` | obstacle_4 | ADD_NODE skipped: empty content |
| 37 | 11:30:05 | `ADD_EDGE` | lemma_2->lemma_1 | ADD_EDGE skipped: lemma_2 -> lemma_1 (unknown node or duplicate) |
| 38 | 11:30:05 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 39 | 11:30:05 | `ADD_EDGE` | obstacle_4->obstacle_2 | ADD_EDGE skipped: obstacle_4 -> obstacle_2 (unknown node or duplicate) |
| 40 | 11:30:36 | `ADD_NODE` | paper | ADD_NODE skipped: empty content |
| 41 | 11:30:36 | `ADD_NODE` | paper_2 | ADD_NODE skipped: empty content |
| 42 | 11:30:36 | `ADD_NODE` | paper_3 | ADD_NODE skipped: empty content |
| 43 | 11:30:46 | `ADD_NODE` | counterexample | ADD_NODE skipped: empty content |
| 44 | 11:30:46 | `ADD_EDGE` | lemma_1->obstacle_3 | edge lemma_1 -related_to-> obstacle_3 |
| 45 | 11:31:09 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 46 | 11:31:29 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 47 | 11:31:39 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 48 | 11:31:39 | `ADD_NODE` | obstacle | ADD_NODE skipped: empty content |
| 49 | 11:31:54 | `ADD_NODE` | approach_1 | ADD_NODE skipped: empty content |
| 50 | 11:31:54 | `ADD_NODE` | approach_2 | ADD_NODE skipped: empty content |
| 51 | 11:31:54 | `UPDATE_NODE` | obstacle_1 | updated obstacle_1 -> OBSTACLE |
| 52 | 11:32:16 | `ADD_NODE` | paper_2 | added paper_2 (POTENTIALLY_RELEVANT) |
| 53 | 11:32:16 | `ADD_NODE` | idea_1 | added idea_1 (PROMISING) |
| 54 | 11:32:16 | `ADD_EDGE` | paper_2->obstacle_1 | edge paper_2 -related_to-> obstacle_1 |
| 55 | 11:32:16 | `ADD_EDGE` | idea_1->obstacle_1 | edge idea_1 -addresses-> obstacle_1 |
| 56 | 11:32:16 | `ADD_EDGE` | idea_1->lemma_1 | edge idea_1 -depends_on-> lemma_1 |
| 57 | 11:33:16 | `ADD_NODE` | paper | added paper_3 (POTENTIALLY_RELEVANT) |
| 58 | 11:33:16 | `ADD_NODE` | paper | added paper_4 (POTENTIALLY_RELEVANT) |
| 59 | 11:34:04 | `ADD_NODE` | counterexample | added counterexample_1 (PROMISING) |
| 60 | 11:34:04 | `ADD_EDGE` | counterexample_1->hypothesis_1 | edge counterexample_1 -contradicts-> hypothesis_1 |
| 61 | 11:34:04 | `ADD_NODE` | hypothesis | added hypothesis_2 (PROMISING) |
| 62 | 11:34:04 | `ADD_EDGE` | hypothesis_2->hypothesis_1 | edge hypothesis_2 -derived_from-> hypothesis_1 |
| 63 | 11:34:04 | `ADD_EDGE` | hypothesis_2->problem | edge hypothesis_2 -possible_approach-> problem |
| 64 | 11:34:57 | `ADD_NODE` | obstacle | added obstacle_4 (OBSTACLE) |
| 65 | 11:34:57 | `ADD_NODE` | idea | added idea_2 (PROMISING) |
| 66 | 11:34:57 | `ADD_EDGE` | lemma_1->obstacle_4 | edge lemma_1 -related_to-> obstacle_4 |
| 67 | 11:34:57 | `ADD_EDGE` | obstacle_4->problem | edge obstacle_4 -blocks-> problem |
| 68 | 11:34:57 | `ADD_EDGE` | idea_2->lemma_1 | edge idea_2 -depends_on-> lemma_1 |
| 69 | 11:34:57 | `ADD_EDGE` | idea_2->obstacle_3 | edge idea_2 -addresses-> obstacle_3 |
| 70 | 11:35:39 | `ADD_NODE` | paper_5 | ADD_NODE skipped: empty content |
| 71 | 11:36:10 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 72 | 11:36:10 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 73 | 11:36:10 | `UPDATE_NODE` | counterexample_1 | updated counterexample_1 -> PROMISING |
| 74 | 11:36:29 | `ADD_NODE` | approach_1 | ADD_NODE skipped: empty content |
| 75 | 11:36:29 | `ADD_NODE` | approach_2 | ADD_NODE skipped: empty content |
| 76 | 11:36:29 | `ADD_NODE` | approach_3 | ADD_NODE skipped: empty content |
| 77 | 11:36:29 | `ADD_EDGE` | approach_1->problem | ADD_EDGE skipped: approach_1 -> problem (unknown node or duplicate) |
| 78 | 11:36:29 | `ADD_EDGE` | approach_2->problem | ADD_EDGE skipped: approach_2 -> problem (unknown node or duplicate) |
| 79 | 11:36:29 | `ADD_EDGE` | approach_3->problem | ADD_EDGE skipped: approach_3 -> problem (unknown node or duplicate) |
| 80 | 11:36:41 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 81 | 11:36:41 | `UPDATE_NODE` | lemma_2 | UPDATE_NODE skipped: no such node 'lemma_2' |
| 82 | 11:36:41 | `ADD_EDGE` | lemma_2->obstacle_3 | ADD_EDGE skipped: lemma_2 -> obstacle_3 (unknown node or duplicate) |
| 83 | 11:36:41 | `ADD_EDGE` | lemma_2->obstacle_4 | ADD_EDGE skipped: lemma_2 -> obstacle_4 (unknown node or duplicate) |
| 84 | 11:36:50 | `ADD_NODE` | counterexample | ADD_NODE skipped: empty content |
| 85 | 11:37:00 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 86 | 11:37:00 | `UPDATE_NODE` | obstacle_2 | updated obstacle_2 -> OBSTACLE |
| 87 | 11:37:15 | `ADD_NODE` | lemma_2 | ADD_NODE skipped: empty content |
| 88 | 11:37:15 | `ADD_NODE` | obstacle_5 | ADD_NODE skipped: empty content |
| 89 | 11:37:15 | `ADD_EDGE` | lemma_1->obstacle_1 | edge lemma_1 -related_to-> obstacle_1 |
| 90 | 11:37:41 | `ADD_NODE` | lemma | added lemma_2 (PROMISING) |
| 91 | 11:37:41 | `ADD_EDGE` | lemma_5->lemma_1 | ADD_EDGE skipped: lemma_5 -> lemma_1 (unknown node or duplicate) |
| 92 | 11:37:41 | `ADD_EDGE` | lemma_5->obstacle_4 | ADD_EDGE skipped: lemma_5 -> obstacle_4 (unknown node or duplicate) |
| 93 | 11:37:48 | `ADD_NODE` | paper_5 | ADD_NODE skipped: empty content |
| 94 | 11:37:48 | `ADD_EDGE` | paper_5->obstacle_1 | ADD_EDGE skipped: paper_5 -> obstacle_1 (unknown node or duplicate) |
| 95 | 11:37:48 | `ADD_EDGE` | paper_5->idea_1 | ADD_EDGE skipped: paper_5 -> idea_1 (unknown node or duplicate) |
| 96 | 11:37:56 | `ADD_NODE` | approach | ADD_NODE skipped: empty content |
| 97 | 11:37:56 | `ADD_NODE` | approach | ADD_NODE skipped: empty content |
| 98 | 11:38:06 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 99 | 11:38:06 | `ADD_NODE` | obstacle | ADD_NODE skipped: empty content |
| 100 | 11:38:13 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 101 | 11:38:13 | `ADD_NODE` | obstacle_5 | ADD_NODE skipped: empty content |
| 102 | 11:38:13 | `ADD_EDGE` | lemma_3->hypothesis_1 | ADD_EDGE skipped: lemma_3 -> hypothesis_1 (unknown node or duplicate) |
| 103 | 11:38:13 | `ADD_EDGE` | obstacle_5->problem | ADD_EDGE skipped: obstacle_5 -> problem (unknown node or duplicate) |
| 104 | 11:38:23 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 105 | 11:38:40 | `ADD_NODE` | obstacle_5 | ADD_NODE skipped: empty content |
| 106 | 11:38:40 | `ADD_NODE` | obstacle_6 | ADD_NODE skipped: empty content |
| 107 | 11:38:40 | `ADD_EDGE` | obstacle_5->hypothesis_1 | ADD_EDGE skipped: obstacle_5 -> hypothesis_1 (unknown node or duplicate) |
| 108 | 11:38:40 | `ADD_EDGE` | obstacle_6->obstacle_2 | ADD_EDGE skipped: obstacle_6 -> obstacle_2 (unknown node or duplicate) |
| 109 | 11:39:09 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 110 | 11:39:09 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 111 | 11:39:09 | `ADD_EDGE` | lemma_3->hypothesis_1 | ADD_EDGE skipped: lemma_3 -> hypothesis_1 (unknown node or duplicate) |
| 112 | 11:39:19 | `ADD_NODE` | approach_spectral | ADD_NODE skipped: empty content |
| 113 | 11:39:19 | `ADD_NODE` | approach_empirical | ADD_NODE skipped: empty content |
| 114 | 11:39:19 | `ADD_NODE` | obstacle_non_lipschitz | ADD_NODE skipped: empty content |
| 115 | 11:39:25 | `ADD_NODE` | counterexample_2 | ADD_NODE skipped: empty content |
| 116 | 11:39:25 | `ADD_EDGE` | counterexample_2->obstacle_3 | ADD_EDGE skipped: counterexample_2 -> obstacle_3 (unknown node or duplicate) |
| 117 | 11:39:35 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 118 | 11:39:35 | `ADD_EDGE` | hypothesis_1->lemma_1 | edge hypothesis_1 -depends_on-> lemma_1 |
| 119 | 11:39:44 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 120 | 11:39:44 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 121 | 11:39:44 | `ADD_EDGE` | lemma_3->obstacle_3 | ADD_EDGE skipped: lemma_3 -> obstacle_3 (unknown node or duplicate) |
| 122 | 11:39:52 | `UPDATE_NODE` | lemma_2 | updated lemma_2 -> PROMISING |
| 123 | 11:39:52 | `UPDATE_NODE` | lemma_2 | updated lemma_2 -> PROMISING |
| 124 | 11:40:06 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 125 | 11:40:06 | `UPDATE_NODE` | lemma_3 | UPDATE_NODE skipped: no such node 'lemma_3' |
| 126 | 11:40:06 | `ADD_EDGE` | counterexample_1->lemma_1 | edge counterexample_1 -related_to-> lemma_1 |
| 127 | 11:40:06 | `ADD_EDGE` | hypothesis_2->obstacle_4 | edge hypothesis_2 -addresses-> obstacle_4 |
| 128 | 11:40:20 | `ADD_NODE` | counterexample_2 | ADD_NODE skipped: empty content |
| 129 | 11:40:20 | `ADD_EDGE` | counterexample_2->hypothesis_1 | ADD_EDGE skipped: counterexample_2 -> hypothesis_1 (unknown node or duplicate) |
| 130 | 11:40:20 | `ADD_EDGE` | counterexample_2->obstacle_3 | ADD_EDGE skipped: counterexample_2 -> obstacle_3 (unknown node or duplicate) |
| 131 | 11:40:20 | `ADD_EDGE` | counterexample_2->problem | ADD_EDGE skipped: counterexample_2 -> problem (unknown node or duplicate) |
| 132 | 11:40:27 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 133 | 11:40:27 | `ADD_EDGE` | lemma_3->hypothesis_2 | ADD_EDGE skipped: lemma_3 -> hypothesis_2 (unknown node or duplicate) |
| 134 | 11:40:27 | `ADD_EDGE` | lemma_3->obstacle_4 | ADD_EDGE skipped: lemma_3 -> obstacle_4 (unknown node or duplicate) |
| 135 | 11:40:36 | `ADD_NODE` | approach | ADD_NODE skipped: empty content |
| 136 | 11:40:44 | `ADD_NODE` | paper | ADD_NODE skipped: empty content |
| 137 | 11:40:44 | `ADD_NODE` | paper | ADD_NODE skipped: empty content |
| 138 | 11:40:53 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 139 | 11:40:53 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 140 | 11:40:53 | `ADD_EDGE` | lemma_3->obstacle_4 | ADD_EDGE skipped: lemma_3 -> obstacle_4 (unknown node or duplicate) |
| 141 | 11:41:05 | `UPDATE_NODE` | lemma_3 | UPDATE_NODE skipped: no such node 'lemma_3' |
| 142 | 11:41:05 | `ADD_EDGE` | lemma_3->obstacle_4 | ADD_EDGE skipped: lemma_3 -> obstacle_4 (unknown node or duplicate) |
| 143 | 11:41:13 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 144 | 11:41:13 | `UPDATE_NODE` | lemma_4 | UPDATE_NODE skipped: no such node 'lemma_4' |
| 145 | 11:41:13 | `UPDATE_NODE` | hypothesis_2 | updated hypothesis_2 -> PROMISING |
| 146 | 11:41:13 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 147 | 11:41:13 | `ADD_EDGE` | lemma_4->problem | ADD_EDGE skipped: lemma_4 -> problem (unknown node or duplicate) |
| 148 | 11:41:21 | `ADD_NODE` | approach_1 | ADD_NODE skipped: empty content |
| 149 | 11:41:21 | `ADD_NODE` | approach_2 | ADD_NODE skipped: empty content |
| 150 | 11:41:21 | `ADD_NODE` | approach_3 | ADD_NODE skipped: empty content |
| 151 | 11:41:21 | `UPDATE_NODE` | hypothesis_1 | updated hypothesis_1 -> PROMISING |
| 152 | 11:41:21 | `ADD_EDGE` | approach_1->problem | ADD_EDGE skipped: approach_1 -> problem (unknown node or duplicate) |
| 153 | 11:41:21 | `ADD_EDGE` | approach_2->problem | ADD_EDGE skipped: approach_2 -> problem (unknown node or duplicate) |
| 154 | 11:41:21 | `ADD_EDGE` | approach_3->problem | ADD_EDGE skipped: approach_3 -> problem (unknown node or duplicate) |
| 155 | 11:41:52 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 156 | 11:41:52 | `ADD_EDGE` | lemma | edge hypothesis_2 -related_to-> obstacle_4 |
| 157 | 11:42:01 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 158 | 11:42:01 | `UPDATE_NODE` | lemma_3 | UPDATE_NODE skipped: no such node 'lemma_3' |
| 159 | 11:42:01 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 160 | 11:42:01 | `ADD_EDGE` | lemma_3->obstacle_4 | ADD_EDGE skipped: lemma_3 -> obstacle_4 (unknown node or duplicate) |
| 161 | 11:42:01 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 162 | 11:42:55 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 163 | 11:42:55 | `UPDATE_NODE` | obstacle_2 | updated obstacle_2 -> OBSTACLE |
| 164 | 11:43:51 | `ADD_NODE` | paper | added paper_5 (POTENTIALLY_RELEVANT) |
| 165 | 11:43:51 | `ADD_EDGE` | paper_5->idea_1 | edge paper_5 -related_to-> idea_1 |
| 166 | 11:44:35 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 167 | 11:44:35 | `ADD_EDGE` | obstacle_4->hypothesis_2 | edge obstacle_4 -supports-> hypothesis_2 |
| 168 | 11:44:43 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 169 | 11:44:43 | `UPDATE_NODE` | lemma_3 | UPDATE_NODE skipped: no such node 'lemma_3' |
| 170 | 11:44:43 | `ADD_EDGE` | lemma_3->idea_1 | ADD_EDGE skipped: lemma_3 -> idea_1 (unknown node or duplicate) |
| 171 | 11:44:43 | `ADD_EDGE` | lemma_3->obstacle_1 | ADD_EDGE skipped: lemma_3 -> obstacle_1 (unknown node or duplicate) |
| 172 | 11:44:54 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 173 | 11:45:07 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 174 | 11:45:07 | `ADD_NODE` | note | added note_1 (PROMISING) |
| 175 | 11:45:07 | `ADD_EDGE` | lemma_3->hypothesis_2 | ADD_EDGE skipped: lemma_3 -> hypothesis_2 (unknown node or duplicate) |
| 176 | 11:45:07 | `ADD_EDGE` | lemma_3->obstacle_4 | ADD_EDGE skipped: lemma_3 -> obstacle_4 (unknown node or duplicate) |
| 177 | 11:45:20 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 178 | 11:45:20 | `UPDATE_NODE` | idea_1 | updated idea_1 -> PROMISING |
| 179 | 11:45:30 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 180 | 11:45:30 | `UPDATE_NODE` | obstacle_4 | updated obstacle_4 -> OBSTACLE |
| 181 | 11:45:39 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 182 | 11:45:39 | `ADD_NODE` | obstacle | ADD_NODE skipped: empty content |
| 183 | 11:45:39 | `ADD_EDGE` | lemma_3->obstacle_2 | ADD_EDGE skipped: lemma_3 -> obstacle_2 (unknown node or duplicate) |
| 184 | 11:45:39 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 185 | 11:45:39 | `ADD_EDGE` | obstacle_5->obstacle_4 | ADD_EDGE skipped: obstacle_5 -> obstacle_4 (unknown node or duplicate) |
| 186 | 11:45:39 | `ADD_EDGE` | obstacle_5->problem | ADD_EDGE skipped: obstacle_5 -> problem (unknown node or duplicate) |
| 187 | 11:45:49 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 188 | 11:45:49 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 189 | 11:45:49 | `ADD_NODE` | obstacle | ADD_NODE skipped: empty content |
| 190 | 11:45:49 | `ADD_EDGE` | obstacle_1->obstacle_2 | edge obstacle_1 -related_to-> obstacle_2 |
| 191 | 11:45:59 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 192 | 11:45:59 | `ADD_EDGE` | lemma_3->hypothesis_2 | ADD_EDGE skipped: lemma_3 -> hypothesis_2 (unknown node or duplicate) |
| 193 | 11:45:59 | `ADD_EDGE` | lemma_3->counterexample_1 | ADD_EDGE skipped: lemma_3 -> counterexample_1 (unknown node or duplicate) |
| 194 | 11:45:59 | `UPDATE_NODE` | hypothesis_2 | updated hypothesis_2 -> PROMISING |
| 195 | 11:46:26 | `ADD_NODE` | obstacle_5 | ADD_NODE skipped: empty content |
| 196 | 11:46:26 | `ADD_EDGE` | obstacle_5->problem | ADD_EDGE skipped: obstacle_5 -> problem (unknown node or duplicate) |
| 197 | 11:46:26 | `ADD_EDGE` | obstacle_5->idea_1 | ADD_EDGE skipped: obstacle_5 -> idea_1 (unknown node or duplicate) |
| 198 | 11:46:34 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 199 | 11:46:34 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 200 | 11:46:34 | `UPDATE_NODE` | lemma_3 | UPDATE_NODE skipped: no such node 'lemma_3' |
| 201 | 11:46:34 | `UPDATE_NODE` | hypothesis_1 | updated hypothesis_1 -> PROMISING |
| 202 | 11:46:34 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 203 | 11:46:34 | `ADD_EDGE` | lemma_3->hypothesis_1 | ADD_EDGE skipped: lemma_3 -> hypothesis_1 (unknown node or duplicate) |
| 204 | 11:46:34 | `ADD_EDGE` | lemma_3->hypothesis_2 | ADD_EDGE skipped: lemma_3 -> hypothesis_2 (unknown node or duplicate) |
| 205 | 11:46:42 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 206 | 11:46:42 | `ADD_NODE` | obstacle | ADD_NODE skipped: empty content |
| 207 | 11:46:42 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 208 | 11:46:42 | `ADD_EDGE` | obstacle_5->obstacle_1 | ADD_EDGE skipped: obstacle_5 -> obstacle_1 (unknown node or duplicate) |
| 209 | 11:46:42 | `ADD_EDGE` | obstacle_5->problem | ADD_EDGE skipped: obstacle_5 -> problem (unknown node or duplicate) |
| 210 | 11:46:48 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 211 | 11:46:48 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 212 | 11:46:48 | `UPDATE_NODE` | lemma_3 | UPDATE_NODE skipped: no such node 'lemma_3' |
| 213 | 11:46:55 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 214 | 11:47:05 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 215 | 11:47:05 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 216 | 11:47:05 | `UPDATE_NODE` | lemma_3 | UPDATE_NODE skipped: no such node 'lemma_3' |
| 217 | 11:47:05 | `ADD_EDGE` | lemma_3->idea_1 | ADD_EDGE skipped: lemma_3 -> idea_1 (unknown node or duplicate) |
| 218 | 11:47:05 | `ADD_EDGE` | lemma_3->lemma_1 | ADD_EDGE skipped: lemma_3 -> lemma_1 (unknown node or duplicate) |
| 219 | 11:47:05 | `UPDATE_NODE` | idea_1 | updated idea_1 -> PROMISING |
| 220 | 11:47:13 | `ADD_NODE` | lemma_3 | ADD_NODE skipped: empty content |
| 221 | 11:47:13 | `ADD_NODE` | lemma | added lemma_3 (PROMISING) |
| 222 | 11:47:13 | `ADD_EDGE` | lemma_3->hypothesis_2 | edge lemma_3 -supports-> hypothesis_2 |
| 223 | 11:47:13 | `ADD_EDGE` | lemma_3->obstacle_4 | edge lemma_3 -supports-> obstacle_4 |
| 224 | 11:47:20 | `ADD_NODE` | paper_6 | ADD_NODE skipped: empty content |
| 225 | 11:47:20 | `ADD_EDGE` | paper_6->obstacle_1 | ADD_EDGE skipped: paper_6 -> obstacle_1 (unknown node or duplicate) |
| 226 | 11:47:28 | `ADD_NODE` | paper_6 | ADD_NODE skipped: empty content |
| 227 | 11:47:28 | `ADD_NODE` | paper_7 | ADD_NODE skipped: empty content |
| 228 | 11:47:28 | `ADD_EDGE` | paper_6->problem | ADD_EDGE skipped: paper_6 -> problem (unknown node or duplicate) |
| 229 | 11:47:28 | `ADD_EDGE` | paper_7->obstacle_3 | ADD_EDGE skipped: paper_7 -> obstacle_3 (unknown node or duplicate) |
| 230 | 11:47:36 | `ADD_NODE` | obstacle | ADD_NODE skipped: empty content |
| 231 | 11:47:36 | `ADD_NODE` | obstacle | added obstacle_5 (OBSTACLE) |
| 232 | 11:47:36 | `ADD_NODE` | idea | added idea_3 (IDEA) |
| 233 | 11:47:36 | `ADD_EDGE` | obstacle_5->idea_1 | edge obstacle_5 -contradicts-> idea_1 |
| 234 | 11:47:36 | `ADD_EDGE` | idea_3->obstacle_5 | edge idea_3 -addresses-> obstacle_5 |
| 235 | 11:47:36 | `ADD_EDGE` | idea_3->problem | edge idea_3 -possible_approach-> problem |
| 236 | 11:47:44 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 237 | 11:47:44 | `ADD_EDGE` | lemma_4->hypothesis_1 | ADD_EDGE skipped: lemma_4 -> hypothesis_1 (unknown node or duplicate) |
| 238 | 11:47:44 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 239 | 11:47:51 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 240 | 11:47:51 | `UPDATE_NODE` | lemma_4 | UPDATE_NODE skipped: no such node 'lemma_4' |
| 241 | 11:47:51 | `ADD_EDGE` | lemma_4->idea_1 | ADD_EDGE skipped: lemma_4 -> idea_1 (unknown node or duplicate) |
| 242 | 11:47:51 | `ADD_EDGE` | lemma_4->problem | ADD_EDGE skipped: lemma_4 -> problem (unknown node or duplicate) |
| 243 | 11:48:29 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 244 | 11:48:29 | `UPDATE_NODE` | idea_2 | updated idea_2 -> PROMISING |
| 245 | 11:48:37 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 246 | 11:48:37 | `ADD_EDGE` | lemma_4->lemma_1 | ADD_EDGE skipped: lemma_4 -> lemma_1 (unknown node or duplicate) |
| 247 | 11:48:37 | `ADD_EDGE` | lemma_4->obstacle_4 | ADD_EDGE skipped: lemma_4 -> obstacle_4 (unknown node or duplicate) |
| 248 | 11:48:37 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 249 | 11:48:47 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 250 | 11:48:47 | `UPDATE_NODE` | obstacle_3 | updated obstacle_3 -> OBSTACLE |
| 251 | 11:48:58 | `ADD_NODE` | theorem_1 | ADD_NODE skipped: empty content |
| 252 | 11:48:58 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 253 | 11:48:58 | `ADD_NODE` | obstacle_6 | ADD_NODE skipped: empty content |
| 254 | 11:48:58 | `ADD_EDGE` | theorem_1->lemma_1 | ADD_EDGE skipped: theorem_1 -> lemma_1 (unknown node or duplicate) |
| 255 | 11:48:58 | `ADD_EDGE` | lemma_4->obstacle_4 | ADD_EDGE skipped: lemma_4 -> obstacle_4 (unknown node or duplicate) |
| 256 | 11:48:58 | `ADD_EDGE` | obstacle_6->obstacle_1 | ADD_EDGE skipped: obstacle_6 -> obstacle_1 (unknown node or duplicate) |
| 257 | 11:49:06 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 258 | 11:49:06 | `ADD_NODE` | obstacle_6 | ADD_NODE skipped: empty content |
| 259 | 11:49:06 | `ADD_EDGE` | lemma_4->idea_1 | ADD_EDGE skipped: lemma_4 -> idea_1 (unknown node or duplicate) |
| 260 | 11:49:06 | `ADD_EDGE` | obstacle_6->lemma_4 | ADD_EDGE skipped: obstacle_6 -> lemma_4 (unknown node or duplicate) |
| 261 | 11:49:16 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 262 | 11:49:16 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 263 | 11:49:16 | `UPDATE_NODE` | obstacle_4 | updated obstacle_4 -> OBSTACLE |
| 264 | 11:49:27 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 265 | 11:49:27 | `UPDATE_NODE` | obstacle_4 | updated obstacle_4 -> OBSTACLE |
| 266 | 11:49:34 | `ADD_NODE` | paper_6 | ADD_NODE skipped: empty content |
| 267 | 11:49:34 | `ADD_EDGE` | paper_6->obstacle_4 | ADD_EDGE skipped: paper_6 -> obstacle_4 (unknown node or duplicate) |
| 268 | 11:49:34 | `ADD_EDGE` | paper_6->lemma_1 | ADD_EDGE skipped: paper_6 -> lemma_1 (unknown node or duplicate) |
| 269 | 11:49:47 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 270 | 11:49:47 | `UPDATE_NODE` | hypothesis_2 | updated hypothesis_2 -> PROMISING |
| 271 | 11:49:47 | `UPDATE_NODE` | obstacle_4 | updated obstacle_4 -> OBSTACLE |
| 272 | 11:49:59 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 273 | 11:49:59 | `ADD_NODE` | obstacle_6 | ADD_NODE skipped: empty content |
| 274 | 11:50:08 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 275 | 11:50:08 | `ADD_EDGE` | lemma_4->lemma_1 | ADD_EDGE skipped: lemma_4 -> lemma_1 (unknown node or duplicate) |
| 276 | 11:50:08 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 277 | 11:50:20 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 278 | 11:50:27 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 279 | 11:50:27 | `UPDATE_NODE` | lemma_4 | UPDATE_NODE skipped: no such node 'lemma_4' |
| 280 | 11:50:27 | `ADD_EDGE` | lemma_4->lemma_1 | ADD_EDGE skipped: lemma_4 -> lemma_1 (unknown node or duplicate) |
| 281 | 11:50:27 | `ADD_EDGE` | lemma_4->lemma_2 | ADD_EDGE skipped: lemma_4 -> lemma_2 (unknown node or duplicate) |
| 282 | 11:50:27 | `ADD_EDGE` | lemma_4->obstacle_1 | ADD_EDGE skipped: lemma_4 -> obstacle_1 (unknown node or duplicate) |
| 283 | 11:50:37 | `ADD_NODE` | obstacle_6 | ADD_NODE skipped: empty content |
| 284 | 11:50:37 | `ADD_NODE` | obstacle_6 | ADD_NODE skipped: empty content |
| 285 | 11:50:47 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 286 | 11:50:47 | `UPDATE_NODE` | obstacle_1 | updated obstacle_1 -> OBSTACLE |
| 287 | 11:50:54 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 288 | 11:50:54 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 289 | 11:50:54 | `ADD_EDGE` | lemma_4->obstacle_4 | ADD_EDGE skipped: lemma_4 -> obstacle_4 (unknown node or duplicate) |
| 290 | 11:50:54 | `ADD_EDGE` | lemma_4->lemma_3 | ADD_EDGE skipped: lemma_4 -> lemma_3 (unknown node or duplicate) |
| 291 | 11:51:04 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 292 | 11:51:04 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 293 | 11:51:04 | `ADD_EDGE` | lemma_4->obstacle_4 | ADD_EDGE skipped: lemma_4 -> obstacle_4 (unknown node or duplicate) |
| 294 | 11:51:24 | `UPDATE_NODE` | lemma_2 | updated lemma_2 -> PROMISING |
| 295 | 11:51:24 | `UPDATE_NODE` | lemma_2 | updated lemma_2 -> PROMISING |
| 296 | 11:51:24 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 297 | 11:51:32 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 298 | 11:51:32 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 299 | 11:51:32 | `ADD_EDGE` | lemma_4->obstacle_4 | ADD_EDGE skipped: lemma_4 -> obstacle_4 (unknown node or duplicate) |
| 300 | 11:51:32 | `ADD_EDGE` | note_1->lemma_4 | ADD_EDGE skipped: note_1 -> lemma_4 (unknown node or duplicate) |
| 301 | 11:51:41 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 302 | 11:51:41 | `UPDATE_NODE` | lemma_4 | UPDATE_NODE skipped: no such node 'lemma_4' |
| 303 | 11:51:41 | `ADD_NODE` | lemma_5 | ADD_NODE skipped: empty content |
| 304 | 11:51:41 | `UPDATE_NODE` | lemma_5 | UPDATE_NODE skipped: no such node 'lemma_5' |
| 305 | 11:51:41 | `ADD_EDGE` | lemma_5->hypothesis_1 | ADD_EDGE skipped: lemma_5 -> hypothesis_1 (unknown node or duplicate) |
| 306 | 11:51:41 | `ADD_EDGE` | lemma_5->obstacle_3 | ADD_EDGE skipped: lemma_5 -> obstacle_3 (unknown node or duplicate) |
| 307 | 11:51:48 | `ADD_NODE` | approach_1 | ADD_NODE skipped: empty content |
| 308 | 11:51:48 | `ADD_NODE` | approach_2 | ADD_NODE skipped: empty content |
| 309 | 11:51:48 | `UPDATE_NODE` | approach_1 | UPDATE_NODE skipped: no such node 'approach_1' |
| 310 | 11:51:48 | `UPDATE_NODE` | approach_2 | UPDATE_NODE skipped: no such node 'approach_2' |
| 311 | 11:51:48 | `ADD_EDGE` | approach_1->obstacle_4 | ADD_EDGE skipped: approach_1 -> obstacle_4 (unknown node or duplicate) |
| 312 | 11:51:48 | `ADD_EDGE` | approach_2->hypothesis_1 | ADD_EDGE skipped: approach_2 -> hypothesis_1 (unknown node or duplicate) |
| 313 | 11:51:55 | `ADD_NODE` | theorem | added theorem_1 (PROMISING) |
| 314 | 11:51:55 | `ADD_EDGE` | theorem_1->hypothesis_1 | edge theorem_1 -supports-> hypothesis_1 |
| 315 | 11:52:03 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 316 | 11:52:03 | `UPDATE_NODE` | lemma_4 | UPDATE_NODE skipped: no such node 'lemma_4' |
| 317 | 11:52:03 | `ADD_EDGE` | lemma_4->theorem_1 | ADD_EDGE skipped: lemma_4 -> theorem_1 (unknown node or duplicate) |
| 318 | 11:52:03 | `ADD_EDGE` | lemma_4->obstacle_1 | ADD_EDGE skipped: lemma_4 -> obstacle_1 (unknown node or duplicate) |
| 319 | 11:52:26 | `ADD_NODE` | paper_6 | ADD_NODE skipped: empty content |
| 320 | 11:52:26 | `ADD_EDGE` | paper_6->obstacle_1 | ADD_EDGE skipped: paper_6 -> obstacle_1 (unknown node or duplicate) |
| 321 | 11:52:26 | `ADD_EDGE` | paper_6->obstacle_4 | ADD_EDGE skipped: paper_6 -> obstacle_4 (unknown node or duplicate) |
| 322 | 11:52:26 | `ADD_EDGE` | paper_6->lemma_1 | ADD_EDGE skipped: paper_6 -> lemma_1 (unknown node or duplicate) |
| 323 | 11:52:33 | `ADD_NODE` | paper | ADD_NODE skipped: empty content |
| 324 | 11:52:33 | `UPDATE_NODE` | paper_6 | UPDATE_NODE skipped: no such node 'paper_6' |
| 325 | 11:52:33 | `ADD_EDGE` | paper_6->obstacle_1 | ADD_EDGE skipped: paper_6 -> obstacle_1 (unknown node or duplicate) |
| 326 | 11:52:33 | `ADD_EDGE` | paper_6->hypothesis_2 | ADD_EDGE skipped: paper_6 -> hypothesis_2 (unknown node or duplicate) |
| 327 | 11:52:42 | `UPDATE_NODE` | hypothesis_2 | updated hypothesis_2 -> PROMISING |
| 328 | 11:52:42 | `UPDATE_NODE` | note_1 | updated note_1 -> PROMISING |
| 329 | 11:52:42 | `ADD_EDGE` | note_1->hypothesis_2 | edge note_1 -supports-> hypothesis_2 |
| 330 | 11:52:51 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 331 | 11:52:51 | `UPDATE_NODE` | lemma_4 | UPDATE_NODE skipped: no such node 'lemma_4' |
| 332 | 11:52:51 | `ADD_EDGE` | lemma_4->lemma_1 | ADD_EDGE skipped: lemma_4 -> lemma_1 (unknown node or duplicate) |
| 333 | 11:52:51 | `ADD_EDGE` | lemma_4->idea_1 | ADD_EDGE skipped: lemma_4 -> idea_1 (unknown node or duplicate) |
| 334 | 11:52:59 | `ADD_NODE` | paper | ADD_NODE skipped: empty content |
| 335 | 11:52:59 | `ADD_NODE` | paper | ADD_NODE skipped: empty content |
| 336 | 11:53:07 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 337 | 11:53:07 | `ADD_EDGE` | lemma_4->problem | ADD_EDGE skipped: lemma_4 -> problem (unknown node or duplicate) |
| 338 | 11:53:07 | `ADD_EDGE` | lemma_4->idea_1 | ADD_EDGE skipped: lemma_4 -> idea_1 (unknown node or duplicate) |
| 339 | 11:53:07 | `ADD_EDGE` | lemma_4->theorem_1 | ADD_EDGE skipped: lemma_4 -> theorem_1 (unknown node or duplicate) |
| 340 | 11:53:13 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 341 | 11:53:13 | `UPDATE_NODE` | lemma_4 | UPDATE_NODE skipped: no such node 'lemma_4' |
| 342 | 11:53:13 | `ADD_EDGE` | lemma_4->obstacle_4 | ADD_EDGE skipped: lemma_4 -> obstacle_4 (unknown node or duplicate) |
| 343 | 11:53:21 | `ADD_NODE` | approach_plan_a | ADD_NODE skipped: empty content |
| 344 | 11:53:21 | `UPDATE_NODE` | approach_plan_a | UPDATE_NODE skipped: no such node 'approach_plan_a' |
| 345 | 11:53:21 | `ADD_EDGE` | approach_plan_a->problem | ADD_EDGE skipped: approach_plan_a -> problem (unknown node or duplicate) |
| 346 | 11:53:21 | `ADD_EDGE` | approach_plan_a->idea_1 | ADD_EDGE skipped: approach_plan_a -> idea_1 (unknown node or duplicate) |
| 347 | 11:53:29 | `ADD_NODE` | lemma | ADD_NODE skipped: empty content |
| 348 | 11:53:37 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 349 | 11:53:37 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 350 | 11:53:37 | `ADD_EDGE` | lemma_4->obstacle_4 | ADD_EDGE skipped: lemma_4 -> obstacle_4 (unknown node or duplicate) |
| 351 | 11:53:47 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 352 | 11:53:47 | `ADD_EDGE` | lemma_4->lemma_1 | ADD_EDGE skipped: lemma_4 -> lemma_1 (unknown node or duplicate) |
| 353 | 11:53:47 | `ADD_EDGE` | lemma_4->obstacle_4 | ADD_EDGE skipped: lemma_4 -> obstacle_4 (unknown node or duplicate) |
| 354 | 11:53:47 | `ADD_EDGE` | lemma_4->hypothesis_2 | ADD_EDGE skipped: lemma_4 -> hypothesis_2 (unknown node or duplicate) |
| 355 | 11:54:23 | `ADD_NODE` | lemma_4 | ADD_NODE skipped: empty content |
| 356 | 11:54:23 | `ADD_EDGE` | lemma_4->theorem_1 | ADD_EDGE skipped: lemma_4 -> theorem_1 (unknown node or duplicate) |
| 357 | 11:54:23 | `ADD_EDGE` | lemma_4->obstacle_3 | ADD_EDGE skipped: lemma_4 -> obstacle_3 (unknown node or duplicate) |

---

*End of Compiled Research Dossier.*
