# Class-by-Class Summary

A chronological walkthrough of every notebook and reference markdown file in this
repo, based on git history (file-add dates) and the actual cell contents, not just
filenames. Where the filename's implied date and the git history disagree, both are
noted.

---

## January 2026 — Python Foundations

**2026-01-04 — `workout_log_sqrt.ipynb`** *(pre-course scratch work, not a class session)*
- Approximates `log10` and square roots by manual guess-and-check (`try_guess(left, right)`), narrowing bounds toward `sqrt(80)`.
- Reads like instructor prep for the later binary-search classes rather than class material itself.

**2026-01-10 — `test.ipynb`** *(scratch work)*
- Toy `add_two_numbers` base-conversion exercise (arbitrary symbol alphabet).
- Binary search to solve `12**n = 1,000,000` for `n`, evolving from one-shot guesses into a `while True` loop with a convergence check and iteration counter.

**2026-01-11 — `02_jan11_python.ipynb`**
- Core Python: variables, list mutability vs. string immutability, tuples vs. lists, multi-line/triple-quoted strings, escape characters.
- Functions as first-class objects (`myint2 = interest`), `None`/type overview, an `if/elif` age-classifier.
- Ends mid-recursion: a `mypower(x, y)` stub left unfinished as a teaser for recursion.

**2026-01-17 — `03_jan17_python_basics.ipynb`**
- Modulo use-cases: divisibility checks, extracting digits, sharding (`user_id % 35` across servers), one-way "encryption."
- `ord`/`chr` over ASCII and Unicode (Devanagari examples), simple string-hashing experiments, comparison with Python's built-in `hash()`.
- Digit extraction loop via `% 10` / `// 10`.

**2026-01-18 — `04_jan18.ipynb`**
- Numerical differentiation from first principles: finite-difference `diff(f, x)` rate-of-change, generalized to take any function.
- Plotting `x` vs `x²` with matplotlib.
- `random.random()` experiments: weighted ranges, fair/biased coin toss via `round()`, and a 1M-flip simulation converging to ~0.5 (law of large numbers).

**2026-01-24 — `05_jan23_catchup.ipynb`** *(catch-up session; filename says "jan23")*
- Binary search applied to `log10(125)`, `sqrt(20)`, and cube root of 50 — narrowing `left`/`right` bounds by hand before introducing `math.log10`.

**2026-01-24 — `06_jan24.ipynb`**
- Refines binary search into a proper loop with a numeric stopping condition to compute `sqrt(67)`, checked against `math.sqrt`.
- `find_first_divisor`, first as brute force, then optimized to only check up to `sqrt(num)`.
- Closing question: "why prefer `for` over `while`?"

**2026-01-25 — `07_jan25_2026.ipynb`**
- Linear-equation framing as a precursor to regression: thermometer (`T = i*m + c`) and factory-revenue (`R = a*W + b*M + c`) word problems solved by guessing coefficients.
- Loops: printing multiplication tables, refactored into `print_table`/`print_all_tables`.
- List aliasing/mutability gotchas (shared references through nested lists), tuple-unpack swap trick, swap-without-temp-variable (and its overflow risk).
- Bitwise operators (`OR`/`AND`/`NOT`/`XOR`), XOR swap, XOR for parity/RAID5-style redundancy; closes with links on recursion/induction (nandgame.com, Wikipedia).

### Reference notes (`Exercises/*.md`) — foundational topics threaded through Jan/Feb
*(All first committed together around 2026-01-11; these read as standing reference material/exercise sheets rather than single-date class transcripts.)*
- **00. Number System.md** — custom-base number systems, base arithmetic, multiplication tables in arbitrary bases, log as "count of zeros."
- **01. Expressions and Functions.md** — last-digit/remove-last-digit, simple interest, hypotenuse, 2D/3D distance, Manhattan distance.
- **02. If - Else.md** — fair/biased coin toss, "is point P closer to A or B," point-on-line, overlapping 1D line segments, point-in-rectangle.
- **03. Recursion.md** — factorial, recursive multiplication, `power(x,n)` (positive and signed `n`), recursive division (quotient/remainder), Euclid's GCD, Tower of Hanoi.
- **04. Loops and Array.md** — min/max of a list, min-max normalization, mean, standard deviation, z-score outlier detection, IQR.
- **05. Binary Search and approximations.md** — sqrt, cube root, nth root, log₁₀, logₙ, all via binary search; minimizing a quartic.
- **06. Dictionaries.md** — word count, anagram grouping, an expense tracker.

---

## February 2026 — OOP, Nearest Neighbors, Vectors & Matrices

**2026-02-01 — `08_jan31_nn.ipynb`** *(filename says "nn"/Jan 31; content is k-Nearest Neighbors, not neural nets)*
- 1D `find_closest` (experience → salary lookup by nearest match), generalized to 2D `find_closest_2d` with squared vs. absolute distance.
- Discusses kNN pros/cons (slow inference, memory growth, no extrapolation) vs. parametric models (parameter counts needed to fit degree-*d* polynomials).
- Stubs for k-NN averaging, N-dimensional distance, and a tangent into dimensionality reduction / PCA / autoencoders.

**2026-02-01 — `09_feb1_recap.ipynb`**
- GCD via subtraction-based Euclidean algorithm.
- Builds a linear-system solver from scratch: `solve1` (1 equation) → `solve2` (2 equations, via elimination) → `solve3` (generalizing toward Gaussian elimination).
- Brute-force scan to find the minimum of a quartic `f(x) = x⁴ - 3x³ - 5x + 10`.

**2026-02-07 — `10_feb7_notes.ipynb`**
- Recursion deep dive: traces `power(n, m)` call stack with indentation, then several Tower-of-Hanoi implementations (hardcoded base cases → fully general recursive → step-counting version), tested for 0–6 disks.
- Recursive integer division (`recursive_divide`).

**2026-02-08 — `11_feb8.ipynb`**
- Empty notebook (0 bytes) — no content recorded for this date.

**2026-02-08 — `Exercises/08. Class And Objects.ipynb`**
- First OOP decision-tree exercise: `DecisionTreeNode` class with `YES()`/`NO()` leaf helpers, building a job-offer tree (`salary ≤ 1000 → NO`, else split on `distance`).
- A parallel Binary Search Tree exercise stub (`print`/`insert`/`search`).

**2026-02-14 — `12_feb14_objects.ipynb`**
- OpenAI API call demo (ask a question, print the response) — first LLM touchpoint in the course.
- Model/hypothesis/train/inference framing via a stock-price-prediction example.
- OOP progression: a toy `Dog` class → `LineModel` (`y = mx + c` with `fit`/`predict`) → `HyperPlane`/`BaseModel` inheritance → a `Vector` class (`add`, scalar `multiply`) with a "rotate by θ" extension left as an exercise.

**~2026-02-21 — `13_feb 21_2026_object_classes.ipynb`** *(git history dates this 02-08 due to a rename; content and filename point to Feb 21)*
- Student-submitted `Vector`/`Vector2D` classes (`add`, `multiply`, `turn`/rotate, `dist`), with a dot-product teaser (`A.dot(B)`).
- Hand-rolled matrix multiplication outline, then a numpy-based 2D rotation matrix animated with matplotlib (rotating points step by step).
- Assignment: implement dot product, your own matrix multiply, and a rotating-shape animation.

**2026-02-22 — `14_feb_22_objects_and_classes_vectors_matrics.ipynb`**
- Uses numpy matrix multiplication to rotate/transform a "kite" shape — geometric transforms via `@`.
- Tensor framing: scalar (0D) → vector (1D, e.g. audio) → matrix (2D, e.g. grayscale image) → 3D (color image) → 4D (video) → 5D (batch of videos), with `plt.imshow` examples.
- Converts a stock-price series into a sliding-window 2D array (precursor to feature engineering for time series).
- Revisits BST (`Node` with `insert`/`search`/`printa`) and a `DT` decision-tree class stub.
- Recursive Gaussian-elimination equation solver (`solven`) annotated with explicit Big-O complexity per step; closes with a merge/merge-sort time-and-space complexity exercise.

---

## Late February – Mid March 2026 — Complexity, Decision Trees, Embeddings

**2026-02-28 — `15_23_jan_DT_bigo.ipynb`** *(filename misdated "23_jan"; git history places it ~Feb 28)*
- Matplotlib animation of a rotating unit vector (illustrating angle/CCW rotation).
- A salary/work-from-home decision tree via `Node`/`YesNode`/`NoNode` classes, tested with `tree.check(...)`.
- Big-O via counting doublings to reach `n` (`printn`), tied back to `math.log2`.

**2026-02-28 — `Exercises/07. Complexity.md`**
- Complexity Q&A sheet: matrix multiply (`n×n` and `a×b · b×c`), solving an `n`-variable linear system, searching an unsorted list, BST operations, sorting algorithms, and the complexity of the decision tree's own `check()` method.

**2026-03-01 — `16_mar_01_complexity.ipynb`**
- Complexity of multiplicative loops (`i *= 6` → `k = log₆(n)`), digit-wise big-number addition, counting digits via `log10`.
- Complexity of recursive HCF and recursive factorial; a worked time/space-complexity table for several functions (`sum_array`, `create_list`, `print_pairs`, iterative vs. recursive factorial).
- Starts a BST `Node` class specifically to reason about its time/space complexity.

**2026-03-07 — `Exercises/13. decision_tree.ipynb`** — *"Learning Decision Trees by Inventing Them" (classification)*
- Guided discovery notebook: invent an `impurity(p, q)` formula from scratch, extend it to impurity-of-a-list and weighted impurity of two groups.
- Best-split search over a real height/gender dataset; builds a `DecisionTreeNode` job-offer tree (salary/distance rules).
- Extends to multiple features (height + weight), grows a tree recursively with stopping conditions, and assembles a full `SimpleDecisionTree` class (`fit`/`predict`/accuracy/print-tree).
- Bonus challenges: `max_depth`, `min_samples_split`, the iris dataset, and comparing impurity measures including Gini.

**2026-03-08 to 03-15 — `Exercises/Sentiment Analysis with LLMs.ipynb`**
- One-hot encoding toy example → word embeddings → OpenAI embeddings API usage → visualizing word embeddings → "build a product search engine" exercise.
- Builds Euclidean distance from the ground up: Pythagorean theorem in 2D → 3D → n-D, then applies `calculate_distance()` to real embeddings.
- Dot product between vectors and the orthogonality note (dot product 0 ⇒ 90°); a dedicated sentiment-analysis section and project (Tasks 1–3); closes comparing cosine/Euclidean/dot-product similarity and asking "what else can you build with embeddings?"

**2026-03-15 (filename spans Mar 15/21/22) — `17_mar_15_21_22_vector_store.ipynb`**
- SQL-style nearest-neighbor query intuition (`ORDER BY distance LIMIT 3`) and a k-means clustering visualizer link.
- `map()` exercise (vs. `for` and comprehensions, performance discussion).
- Images as numpy arrays: grayscale conversion, channel-swap recoloring, downsampling (pixel-skip / mean-pooling), a "super resolution" exercise introducing stride and padding (convolution groundwork).
- Numpy broadcasting (1D/2D/3D, axis-wise sums) and a first pass at pandas (`Series`/`DataFrame` construction, reading a real movie-ratings CSV).

---

## Late March – April 2026 — Recommenders, Calculus, Agents, RAG

**2026-03-28 — `18_mar_28.ipynb`**
- Movie-ratings recommender system: pandas cleanup (dropping columns), a min-max scaling exercise, and a discussion of NaN-handling/imputation strategies (mode/mean/median, decision-tree-based imputation).
- Cosine similarity vs. L2 distance for "find similar people," with the unit-vector normalization needed for cosine.
- Closing exercise: implement matrix multiplication via MapReduce on columnar-format matrices.

**2026-04-04 (spans Mar 29–Apr 4) — `19_march_29_apr4.ipynb`**
- Vectorizes cosine similarity for the ratings matrix using matrix multiplication (`uM.T @ uM`).
- Discusses embeddings for recommender cold-start (new users/movies) and a CNN-style "design a weighted-sum convolution" exercise (stride, padding, RGB kernels).
- A "find your celebrity lookalike" face-embedding project outline.
- Pivots into calculus: numerical `dy_dx`, manually verifying the chain rule across composed functions (`f1→f2→f3→f4`), and a first explicit statement of gradient descent for finding minima.

**2026-04-11 — `21_apr11.ipynb`**
- Gradient descent fundamentals: finds the minimum of a quadratic error function `E(a)` purely numerically (finite-difference slope at many points), then generalizes into a `find_minimum(E_func, n_params)` stub for arbitrary numbers of parameters.
- Ends with an explicit roadmap cell: **"Next Steps: Build a RAG, Build toolcall/agent, Build End to end project"** — directly setting up the next three sessions.

**2026-04-12 — `22_apr12_agents_handson.ipynb`** — *Introduction to LLM Agents*
- LLM basics: system prompts, user prompts, simulating multi-turn memory.
- The LLM-vs-Agent distinction and how an agent loop works.
- Tool calling from scratch: defines a `calculate` tool schema, the real Python function behind it, and a `run_agent` dispatcher loop; exercise to add a `string_reverse` tool.
- Take-home project: a password-reset chatbot gated by an LLM-invoked `change_password` tool.

**2026-04-19 — `Get_OpenAI_API_Key.ipynb`**
- Pure setup walkthrough (screenshots) for creating an OpenAI API key and billing — infra, not a lecture — linking back into the RAG notebook.

**2026-04-19 — `Cosine_Similarity.ipynb`**
- Written derivation of cosine similarity from the angle-difference identity, motivating it as cheaper than Euclidean distance once vectors are unit-normalized (pure multiply-add vs. squaring/rooting).

**2026-04-19 — `Euclidean_Distance.ipynb`**
- Ground-up derivation of the distance formula: 1D (`|x1-x2|`) → 2D (Pythagoras) → 3D → generalized n-D.

**2026-04-19 (filename "Apr18") — `22_Apr18_RAG_System.ipynb`** — *Retrieval-Augmented Generation*
- Full pipeline build, chapter by chapter: why RAG exists → read a source file → chunk it with overlap → generate OpenAI embeddings → cosine-similarity function → store chunks in **Milvus** → `search(query, top_k)` → `generate_answer` → assemble into one `rag_pipeline(query)` function.
- Ends with testing, a recap chapter, and a take-home project.

---

## May–June 2026 — Back to Classical ML, From Scratch

*(These are the most recent commits in the repo — current `HEAD` — authored by a different contributor, **Rohan das**, rather than Sandeep Giri. Notably, the course circles back to classical ML fundamentals (regression, trees, ensembles) here, after already having covered LLM agents and RAG in April.)*

**2026-05-24 — `linear_regression.ipynb`**
- Single-feature linear regression from scratch: brute-force grid search over `(m, c)`, then "moving with rate of change" (manual finite-difference gradients via `gradients_1direction`), generalized into a proper gradient-descent `fit(m, c, learning_rate, epochs)`.
- Scales up to multi-feature regression: vectorized `predict`, `total_err_sqr`, `gradients`, and `fit` over `X`/`y`/`m`/`c`; finishes with an `add_feature` helper for feature engineering (e.g. polynomial terms).

**2026-05-31 — `Decision_Tree_from_scratch.ipynb`** — *"Learning Decision Trees by Inventing Them," reprised as regression*
- Mirrors the March classification-tree exercise (`Exercises/13. decision_tree.ipynb`) but for continuous targets: invents a **variance**-based impurity measure instead of Gini/entropy, weighted total variance, and variance reduction.
- Builds `find_best_split` automatically, adds `max_depth`/`min_samples_split` stopping rules, and assembles full `Node`/`DecisionTreeRegressor` classes, evaluated with RMSE.

**2026-06-06 — `decision_tree.py` + `Random_Forest_from_scratch.ipynb`** — *Ensemble Learning*
- `decision_tree.py` extracts the `Node`/`DecisionTreeRegressor` classes from the notebook above into an importable module.
- The notebook motivates ensembling (why identical trees on identical data don't help), then builds **bootstrap sampling** and **random feature subsets** by hand, and implements `RandomForestRegressor` (`bootstrap_sample`, `fit`, `predict`-by-averaging) on top of `decision_tree.py`.
- Tested on small synthetic housing-price datasets with train/test RMSE comparisons.

---

## Notes on repo housekeeping (not class content)

- `Exercises/09. Packages and Modules.ipynb`, `10. Gradient Descent.ipynb`, and `11. Linear Regression.ipynb` are empty placeholder stubs (created in commit `a1182d8`, never filled in) — the actual gradient-descent and linear-regression content ended up living in the root-level `21_apr11.ipynb` and `linear_regression.ipynb` instead.
- `Exercises/12. SentimentAnalysis.ipynb` is likewise an empty stub, superseded by the real `Exercises/Sentiment Analysis with LLMs.ipynb`.
- As of this summary, all four empty stubs show as locally deleted but **uncommitted** in `git status` — that's cleanup of unused placeholders, not a loss of real class material.
