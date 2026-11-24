# The Power of Cooperation: How a Swarm of Small Models Handles IMO Math Olympiad Problems

**Project Proposal** · Atahan Uz
**Course:** Special Topics in Computer Engineering: Cooperative Studies in the Context …

> Source: `coco_atahanuz_proposal.pptx` (18 slides). Slide numbers are given under each section so we can map back to the deck.

---

## 1. Motivation

*Slide 2*

- Solving hard problems in math, physics and computer science with LLMs is an active research area.
- The usual approach is to use a single "strong" model, usually a very large one, to solve the problem.
- Running a large model needs a lot of compute. A cheaper and smarter alternative may be an "army" of small models working together.

## 2. Core Idea: A Swarm of Small Models

*Slide 3*

- A small model such as `google/gemma-3-4b-it` most likely can't solve an International Mathematical Olympiad (IMO) problem on its own. It lacks the context length and the reasoning ability to carry out every step of a long solution by itself.
- A **swarm** of models, for example 10 instances of Gemma, may be able to solve the problem if they work together.
- The question is: *how* do they work together?

## 3. How LLMs Can Work Together

*Slide 4*

- At first, "LLMs working together" sounds odd. In the end, an LLM is a program that generates text by predicting the next token.
- With **tool calling**, an LLM can run command-line instructions on the operating system. That lets it do things like write to a file and read from a file.
- Once models can read and write shared files, they can **communicate** with each other through those files, and from there start **collaborating** on a problem.

## 4. Example 1: Sequential Collaboration (IMO 1988, Problem 6)

*Slides 5–7*

### The problem

> Let $a$ and $b$ be positive integers such that $ab + 1$ divides $a^2 + b^2$. Show that
> $$\frac{a^2 + b^2}{ab + 1}$$
> is the square of an integer.

This is the famous "Question Six". It is short, but it is one of the hardest IMO problems ever set: only 11 students solved it fully in 1988. A small LLM has no chance of solving it on its own.

### Setup: master–worker architecture

```
                 Master (coordinator)
        ┌──────────┬──────┴─────┬──────────┐
    Worker 1   Worker 2    Worker 3    Worker 4

    All five are gemma-3-4b-it.
    notes.md: a shared file that everyone can read and write.
```

- One LLM is the **master** (coordinator). It splits the problem into tasks and assigns them.
- The other LLMs are **workers**. Each one only does the task it is given.
- The master does **not** know the solution steps in advance. The workers have to experiment, write their findings to the shared `notes.md`, and check each other's work.

### Walkthrough

Throughout, let $k = \dfrac{a^2 + b^2}{ab + 1}$.

**Step 1: Explore with code**

- **Master:** "Worker 1, write a Python script that tries every $a, b$ up to 1000. Save the results to `notes.md`."
- **Worker 1 returns:**
  - Every value of $k$ found is a perfect square: 1, 4, 9, 16, 25, 36, …
  - Examples: $(2, 8) \to 4$, $(8, 30) \to 4$, $(30, 112) \to 4$, $(3, 27) \to 9$
  - Pairs with the same $k$ form a chain, where each pair leads to the next one. This hints at the structure the proof will use.

**Step 2: Two proof attempts with different approaches**

- **Master:** "Worker 2 and Worker 3, both try to prove it, but with different approaches. Read Worker 1's notes first."
- **Worker 2 returns:** Tried mod 3 and mod 4. Couldn't get anywhere.
- **Worker 3 returns** (a proof by infinite descent, known as *Vieta jumping*, following the chain Worker 1 found):
  - Assume $k$ is not a perfect square. Among all valid pairs, take the one with the smallest $a + b$, with $a \ge b$.
  - Rearranging $k(ab + 1) = a^2 + b^2$ shows that $a$ is a root of
    $$x^2 - kb\,x + (b^2 - k) = 0.$$
  - The other root is $a' = kb - a = \dfrac{b^2 - k}{a}$. The first form shows $a'$ is an integer, and the second shows $a' < \dfrac{b^2}{a} \le a$.
  - So $(a', b)$ is a smaller pair. This contradicts minimality.

**Step 3: Independent verification**

- **Master:** "Worker 4, check Worker 3's proof step by step. Don't just trust it."
- **Worker 4 returns:** There is a gap. The proof never shows that $a'$ is **positive**. If $a' \le 0$, then $(a', b)$ is not a valid pair and the argument breaks.

**Step 4: Fix the gap**

- **Master:** "Worker 3, fix the gap that Worker 4 found."
- **Worker 3 returns:**
  - If $a' = 0$, then $b^2 = k$, so $k$ is a perfect square. Done.
  - If $a' < 0$, then $a' \le -1$, so
    $$a'^2 - kb\,a' + b^2 - k \;\ge\; 1 + kb + b^2 - k \;>\; 0,$$
    so $a'$ can't be a root. Therefore $a' > 0$, and the proof works.

**Step 5: Assemble**

- **Master:** Combines the notes and writes the final proof. **Solved.**

### Takeaway

Several small LLMs, each unable to solve the problem alone, can solve it together by exploring, proposing, checking and fixing through a shared file.

## 5. Example 2: Parallel Collaboration (IMO 1995, Problem 2)

*Slides 8–9*

### The problem

> Let $a, b, c$ be positive real numbers such that $abc = 1$. Prove that
> $$\frac{1}{a^3(b + c)} + \frac{1}{b^3(c + a)} + \frac{1}{c^3(a + b)} \ge \frac{3}{2}.$$

### Why run workers in parallel

- In Example 1 the workers went **one after another**, and each waited for the previous result.
- Here **all workers start at the same time**, each with a different approach.
- Inequalities suit this well. There are many ways to attack them, most are dead ends, and we don't know in advance which one will work, so we try them all at once.

**Master:** "Everyone, try to prove it. Worker 1: test it with numbers in Python. Worker 2: clear the denominators and expand. Worker 3: try a substitution. Worker 4: try Cauchy–Schwarz. Write your progress to `notes.md`."

### Walkthrough (all four run at the same time)

| Worker | Approach | What happens |
|---|---|---|
| **Worker 1** | Numerical check (Python) | Tries 1,000,000 random $(a, b, c)$. Smallest value found is $1.5$, at $a = b = c = 1$. The inequality is probably true. |
| **Worker 2** | Expand everything | Clears the denominators and gets a huge polynomial. Runs out of context and gives up. |
| **Worker 3** | Substitution | Sets $x = 1/a,\ y = 1/b,\ z = 1/c$, so $xyz = 1$. Each term becomes $\dfrac{1}{a^3(b+c)} = \dfrac{x^3 yz}{y + z} = \dfrac{x^2}{y+z}$, so the left side is $\dfrac{x^2}{y+z} + \dfrac{y^2}{z+x} + \dfrac{z^2}{x+y}$. Gets stuck here, but **writes it to `notes.md` anyway**. |
| **Worker 4** | Cauchy–Schwarz | First tries it on the original form: too messy, no progress. Then **reads Worker 3's note** and applies Cauchy–Schwarz (Engel form) to the new form: $\dfrac{x^2}{y+z} + \dfrac{y^2}{z+x} + \dfrac{z^2}{x+y} \ge \dfrac{(x+y+z)^2}{2(x+y+z)} = \dfrac{x+y+z}{2} \ge \dfrac{3}{2}$, since $x + y + z \ge 3\sqrt[3]{xyz} = 3$ (AM–GM). **Done.** |

Hand-off: Worker 3 → `notes.md` → Worker 4.

**Master:** Takes Worker 4's proof and confirms that Worker 1's numbers agree. **Solved.**

### Takeaways

- Most attempts failed, and that didn't matter.
- The final proof came from **two workers together**: Worker 3's substitution and Worker 4's Cauchy–Schwarz.
- **Open question this raises:** who should get the credit, Worker 3 or Worker 4? This leads into the reward-system part of the project.

## 6. Reward Systems for Collaboration

*Slide 10*

When several agents collaborate, the **reward system** we give them shapes how they behave. Two basic options:

1. **Just solve the problem (shared team reward).**
   The only goal for every agent is that the problem eventually gets solved correctly. No agent has a conflict of interest, so there is no reason to sabotage anyone.

2. **Who did the most work (individual, contribution-based reward).**
   Each agent is told it will be rewarded by how much it contributed. This is where things get interesting: an agent that wants to make an important contribution now has a reason to sabotage another agent working on the same problem.

## 7. Cooperate or Defect?

*Slide 11*

Under the "who did the most work" reward, every worker has two choices at each step:

- **Cooperate:** write what you found to `notes.md`, and check the others' work honestly.
- **Defect:** hide a good result to use it later, or claim another worker's correct proof is wrong so that your own work counts for more.

**Incentive:** the reward system decides which choice is the "smart" one. One defector can win, but if everyone defects, nobody gets anything.

### Payoff matrix: Worker 1 vs. Worker 3

|  | **W3 cooperates** | **W3 defects** |
|---|---|---|
| **W1 cooperates** | Problem solved. Both get credit. | W3 uses W1's table and takes all the credit. |
| **W1 defects** | W1 uses W3's work and takes all the credit. | Nobody shares. Not solved, no reward. |

This is similar to the **prisoner's dilemma**: for each worker alone, defecting looks better, but if both defect, both lose.

## 8. Trust, Reputation and Punishment

*Slide 12*

- **Trust:** the master is also a small model. It can't check everything itself, so it has to trust the workers to some degree.
- **Reputation:** the same workers solve many problems together, so this is a **repeated game**. The master keeps a score for each worker: how often its claims turned out to be true.
- **Punishment:** a worker caught lying or sabotaging loses score, gets fewer tasks and less reward. If it keeps doing it, it is removed from the swarm.
- **Trust anchor:** something everyone trusts by default, which all other trust is built on. For us that means **re-running the code**, or a **proof checker such as Lean**. These don't care who wrote the proof.

### The reputation loop

```
 A worker makes a claim
        │
        ▼
 The trust anchor checks it (Python / Lean)
        │
        ▼
 The worker's reputation goes up or down
        │
        ▼
 Reward or punishment
        │
        └──► next problem, same workers ──► (back to the top)
```

Reputation and punishment are **not a separate system**. They can be added on top of **any** of the collaboration systems.

## 9. More Collaboration Systems

*Slides 13–15*

Each system is described the same way: how it works, what it would mean in our two examples, and what can go wrong.

### 9.1 Competing for credit

#### Winner takes all

- **How it works:** all workers race on the same problem. The first correct proof gets the whole reward and everyone else gets nothing.
- **In our examples:** Worker 3 would never share its substitution, because helping Worker 4 win gains it nothing. In the parallel example (Example 2), nobody would finish.
- **What can go wrong:** everyone has a reason to defect: hide progress, or even plant wrong hints in `notes.md`.

#### Fair share of the credit (Shapley value)

- **How it works:** after the problem is solved, the reward is split by how much each agent was **really needed**: would the team still have solved it without you? Formally this is each agent's Shapley value.
- **In our examples:** Worker 3 and Worker 4 split most of the credit. Worker 1 gets a little for the numerical check. Worker 2 gets nothing. Sharing is no longer a free gift, because it pays off.
- **What can go wrong:** it is **expensive**, since the problem has to be re-run without each agent to measure its contribution. Agents may also try to *look* important, for example by writing a lot.

### 9.2 Checking each other

#### Reward the checkers

- **How it works:** a worker is rewarded for finding a **real** mistake in someone else's work, like a bug bounty.
- **In our examples:** Worker 4 finding the gap in Worker 3's proof (the missing $a' > 0$ step) would be the best-paid move of Example 1.
- **What can go wrong:** a worker can call a correct proof wrong just to get paid. We need a **trust anchor** to decide who is right, and **punishment for false alarms**.
- **Trust anchor here:** an objective source of truth, such as Lean for math problems, or a much stronger LLM (e.g., Claude Opus 5.5) acting as a referee.

### 9.3 Markets and debates

#### A market for tasks

- **How it works:** the master posts small tasks with a price, such as "check this step". Workers **bid** by stating how confident they are. The winner is paid **only if its result passes the check**.
- **In our examples:** Worker 1 would bid high on "test it in Python", since that task is easy and almost certain to pass.
- **What can go wrong:** agents may over-bid to grab tasks. Failing costs reputation, though, so over many problems honest bidding wins.

#### Debate

- **How it works:** two workers argue about one claim. One defends the proof and the other tries to break it. The master is the judge.
- **In our examples:** Worker 3 defends its proof and Worker 4 attacks it, so the missing $a' > 0$ step would come up during the debate.
- **What can go wrong:** the judge is a small model too, so a confident worker can win even when it is wrong. The trust anchor helps here again.

## 10. Comparing the Systems

*Slide 16*

| System | Who gets the reward | What can go wrong |
|---|---|---|
| Just solve the problem | Everyone, if the problem is solved | Free riders: an agent can do nothing and still get the reward |
| Who did the most work | Each agent, by its own contribution | Sabotage, hiding results |
| Winner takes all | Only the first correct proof | Nobody shares anything |
| Fair share of the credit | Split by how much each agent was needed | Expensive; agents try to look important |
| Reward the checkers | Whoever finds a real mistake | False alarms |
| A market for tasks | The task winner, if its result passes the check | Over-bidding |
| Debate | The winner of the argument | A confident but wrong agent can win |

## 11. Experiment Plan

*Slide 16*

Run the **same set of IMO problems** under each of the collaboration systems above, and compare them on:

1. **Solve rate:** how many problems get solved.
2. **Cost:** how much compute each system uses.
3. **Defection rate:** how often agents defect (hide results, sabotage, raise false alarms, etc.).

## 12. Other Plans / Extensions

*Slide 17*

So far the focus is on IMO problems, but the same system can be tested on other kinds of problems:

- **YKS** (the Turkish university entrance exam) problems.
- **LeetCode** coding problems.
- **Open problems in mathematics** (e.g., the Millennium Prize Problems). The system won't solve them, but success can be measured as **how much progress** it makes.

---

## Appendix: Transparency on LLM Usage

*Slide 18*

Claude Opus 5.5 was used only to create the colorful diagrams on slides 9, 11 and 12 of the deck, from text written by hand.
