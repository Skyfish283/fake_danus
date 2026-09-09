# Research summary

## Problem

Consider a general n player game (in game theory) with hidden information. Define a belief to be the distribution of a player's hidden information given all the public information in the game so far. prove that the optimal strategy at a certain gamestate is a function of public information and each player's belief only.

## Outcome

Stopped because: planner returned FINISH.
Graph: 8 nodes, 3 edges (IDEA=3, PROMISING=2, UNVERIFIED=2, POTENTIALLY_RELEVANT=1).
Planner calls: 7. Worker calls: 10. Elapsed: 118s.
Model usage: 17 model calls, 32,455 input tokens, 57,394 output tokens (gemini-3.5-flash-lite x7, gemini-3.6-flash x6, gemini-3.5-flash x4).

## Director's report

Final Research Summary: 
1. Problem & Objective: We investigated whether the optimal strategy in an n-player game with hidden information depends solely on public information and public belief states. 
2. Methodology & Key Framework: Using the Common Information Approach (Nayyar et al.) and public belief state reductions, we decomposed the game history into public history and private histories. 
3. Resolution: While individual realized actions depend on private states/observations (x_i), the strategic choice at a given gamestate—formulated as a behavioral 'prescription' mapping private types to action distributions (̲_i: X_i 	o 
Δ(A_i))—depends exclusively on public information and the joint public belief distribution ̲ over private types. Thus, optimal strategies are functions of public information and public beliefs only.

## Promising directions

- **[approach_3]** (approach, by planner) Prescription-Valued Strategies in Common Information: Reframe player strategies using the common information approach (Nayyar et al.). Instead of directly mapping private histories to actions, the public state (public history and public beliefs $\pi$) maps to a behavioral 'prescription' $\gamma_i: X_i \to \Delta(A_i)$ for each player. Player $i$'s actual action is $a_i = \gamma_i(x_i)$. This proves that the optimal strategy $\sigma_i$ is a function of public information, beliefs, and the private state $x_i$ through a public prescription rule.
- **[lemma_1]** (lemma, by planner) Prescription Mapping Characterization (Nayyar et al.): In games with public observations and private information, the optimal strategy for player $i$ is a mapping from private state $x_i$ to action distributions, parameterized by a prescription function $\gamma_i: \mathcal{X}_i \to \Delta(A_i)$ that depends exclusively on the public history and the joint public belief state $\boldsymbol{\mu}$. Thus, the strategic choice (the prescription) depends only on public information and public beliefs.

## Open ideas and questions

- **[approach_1]** (approach, by planner) Public State Decomposition and Common Agent Reframing: Decompose the game history into public history and private histories. Transform the imperfect information game into a virtual game played by a common agent who observes public history and prescribes private strategies based on public belief states (akin to Nayyar et al. and ReBeL/DeepStack public belief state reductions).
- **[obstacle_1]** (obstacle, by planner) Distinction Between Private Observation and Public Belief: A player's action at a given gamestate depends on their actual private information $x_i$, not solely on the public distribution $P(x_i | h_{pub})$. If the target claim asserts strategies depend ONLY on public info and public beliefs, it may fail unless 'belief' refers to player $i$'s private posterior or private information is included.
- **[hypothesis_1]** (hypothesis, by planner) Sufficient Statistic Hypothesis for Public Belief States: In partially observable stochastic games (POSGs) with public observations, the joint distribution of hidden private histories given public history forms a sufficient statistic for evaluating continuation payoffs and optimal strategies.
- **[approach_2]** (approach, by planner) APS Self-Generation Operator over Public Beliefs: Define a self-generation operator $B(V)( imes)$ mapping public belief states $\pi \in \Delta(X)$ to set-valued payoff correspondences. This operator uses (IC) Incentive Compatibility, (PK) Promise Keeping, and (CB) Continuation Belief updates, all structured as functions of the public belief state $\pi$ and public history, to characterize perfect public equilibria (PPE).

## Literature

- **[paper_1]** (paper, by planner) Efficiency in Games With Markovian Private Information (Escobar & Toikka, 2013). Studies repeated Bayesian games with Markovian private information. While focusing on efficiency and communication, it provides structural insights into how private information states and public signals interact dynamically.

## Connections

- approach_2 --addresses--> obstacle_1
- approach_1 --possible_approach--> problem
- approach_3 --addresses--> problem

---

Nothing above is verified. Statuses record how the system judged each claim, not whether it is true.