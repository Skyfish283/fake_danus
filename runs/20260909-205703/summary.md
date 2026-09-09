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