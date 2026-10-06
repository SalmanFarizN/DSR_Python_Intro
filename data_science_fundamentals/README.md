# Data Science Fundamentals
##### DSR Berlin | Data Science Fundamentals Course Module
##### Inspired by Adam Green ([adgefficiency.com](https://adgefficiency.com)), Rachel Berryman, and Samson Afolabi

Welcome to the **Data Science Fundamentals** module of the Data Science Retreat (DSR) curriculum. This module bridges introductory Python programming (NumPy, Pandas) with full-length Machine Learning Fundamentals, teaching students how to think, frame, clean, engineer, and evaluate models like senior data scientists.

---

## 📁 Module Structure

The module is organized into two parallel notebook directories designed for teaching and reference:

- **`live_notebooks/`**: Classroom teaching templates where code implementations are left as blank exercise prompts (`# TODO:` / `# YOUR CODE HERE`). The instructor can live-code in class while students follow along.
- **`final_notebooks/`**: Complete, fully executed reference notebooks containing complete code solutions, outputs, visualizations, and commentary.
- **`data/`**: Project datasets, including raw data, intermediate artifacts (`clean`, `engineered`, `selected`), and the flaw-injection generator script.
- **`images/`**: Architectural diagrams, taxonomy charts, and process flow visuals cited throughout the curriculum.

---

## 🧭 Course Roadmap (Notebooks 01 → 08)

All notebooks are designed to be run in sequential order (`01` → `08`):

| Notebook | Focus & Topics | Live Template | Reference Solution |
| :--- | :--- | :---: | :---: |
| **01. CRISP-DM & Business Framing** | Problem formulation, team roles, business metrics | [`live_notebooks/01`](./live_notebooks/01_crisp_dm_and_business_framing.ipynb) | [`final_notebooks/01`](./final_notebooks/01_crisp_dm_and_business_framing.ipynb) |
| **02. Data Acquisition & Management** | Sourcing, data types, ingest modalities, pipelines | [`live_notebooks/02`](./live_notebooks/02_data_acquisition_and_management.ipynb) | [`final_notebooks/02`](./final_notebooks/02_data_acquisition_and_management.ipynb) |
| **03. Data Cleaning** | Data characterization, leak-free cleaning, imputation | [`live_notebooks/03`](./live_notebooks/03_data_cleaning.ipynb) | [`final_notebooks/03`](./final_notebooks/03_data_cleaning.ipynb) |
| **04. Feature Engineering** | Feature transformations, encodings, scaling | [`live_notebooks/04`](./live_notebooks/04_feature_engineering.ipynb) | [`final_notebooks/04`](./final_notebooks/04_feature_engineering.ipynb) |
| **05. Feature Selection** | Dimensionality reduction, feature pruning | [`live_notebooks/05`](./live_notebooks/05_feature_selection.ipynb) | [`final_notebooks/05`](./final_notebooks/05_feature_selection.ipynb) |
| **06. EDA & Visualization** | Exploratory analysis, visual storytelling | [`live_notebooks/06`](./live_notebooks/06_data_exploration_and_visualization.ipynb) | [`final_notebooks/06`](./final_notebooks/06_data_exploration_and_visualization.ipynb) |
| **07. Model Selection & Evaluation** | Model progression, confusion matrix, threshold tuning | [`live_notebooks/07`](./live_notebooks/07_model_selection_and_evaluation.ipynb) | [`final_notebooks/07`](./final_notebooks/07_model_selection_and_evaluation.ipynb) |
| **08. Wrap-up & Capstone Project** | End-to-end production Scikit-learn pipeline | [`live_notebooks/08`](./live_notebooks/08_wrapup_and_capstone_project.ipynb) | [`final_notebooks/08`](./final_notebooks/08_wrapup_and_capstone_project.ipynb) |

---

## 📊 Dataset Context: Real-World Flaws Explained

This module uses a unified real-world dataset: **Telco Customer Churn** (`data/telco_customer_churn_raw.csv`), tracking subscriber retention and churn risk for a telecommunications provider.

### Authentic Flaws vs Pedagogical Injections:
In real-world data science, datasets are rarely clean. To ensure students learn to detect and resolve realistic data engineering challenges, our raw dataset includes both native quirks and documented pedagogical anomalies:

1. **Native Authentic Flaw**:
   - `TotalCharges`: Contains empty whitespace strings (`' '`) for customers with `tenure == 0` (11 rows). Pandas automatically parses this column as `object`, which breaks modeling algorithms until properly detected and cast to float.
2. **Pedagogical Flaws (Injected via `data/prepare_raw_dataset.py`)**:
   - **Exact Duplicates**: 25 duplicated rows appended to teach `.duplicated()` and highlight test-set data leakage.
   - **Disguised Sentinels**: Random missing values encoded as `-999.0` (in `MonthlyCharges`) and `'?'` / `'Unknown'` (in `PaymentMethod`).
   - **Outliers**: Fat-finger recording errors in `MonthlyCharges` (e.g. `999.0`) and `tenure` (e.g. `1200`) to teach Z-score and IQR clipping.
   - **String Inconsistencies**: Mixed casing (`'female'` vs `'Female'`) and accidental padding whitespace (`' Month-to-month '`).
   - **"True" Feature Duplicates**: Identical customer feature configurations that occur naturally, demonstrating why identical feature vectors in training provide empirical weight of evidence (prior probabilities).

You can inspect or regenerate this dataset at any time using:
```bash
python data/prepare_raw_dataset.py
```

---

## 🖼️ Visual Assets & Source Attributions

All diagram assets live in `./images/` and are fully cited across the notebooks:

- **`crisp_dm_cycle.jpg`**: The CRISP-DM Process Cycle. Source: Chanin Nantasenamat (Data Professor), [Towards Data Science](https://towardsdatascience.com/the-data-science-process-a19eb7ebc41b).
- **`data_science_process_roles.jpg`**: The 5-stage Data Science Process and team role bands. Source: Chanin Nantasenamat (Data Professor), [Towards Data Science](https://towardsdatascience.com/the-data-science-process-a19eb7ebc41b).
- **`ml_problem_taxonomy.jpg`**: Machine Learning Problem Taxonomy Mind Map (Supervised, Unsupervised, Reinforcement Learning).
- **`tabular_data_formats.jpg`**: The Five Formats of Tabular Data (Continuous, Categorical, Ordinal, Binary, Time).
- **`data_considerations.jpg` & `collecting_data_questions.jpg`**: Key data collection questions and sample size considerations.
- **`data_characterization.jpg`**: Six Dimensions of Data Characterization (Quality, Quantity, Diversity, Cardinality, Dimensionality, Sparsity).
- **`train_val_test_split.jpg`**: Isolating the Test Set Immediately (Zero Data Leakage).
- **`zscore_outliers_normal.png`**: Normal distribution curve with Z-score outlier boundaries ($|z| > 3.0$).
- **`ml_algorithm_cheatsheet.jpg`**: Machine Learning Algorithms Cheat Sheet. Source: [KDnuggets](https://www.kdnuggets.com/2017/06/which-machine-learning-algorithm-to-use.html).
- **`model_progression.jpg`**: Progressive Model Hierarchy (Lazy Estimator $\rightarrow$ Baseline $\rightarrow$ Advanced Ensemble).
- **`mvp_iteration_kniberg.png`**: Agile MVP Iteration (Skateboard to Car). Source: Henrik Kniberg, [Crisp.se Making Sense of MVP](https://blog.crisp.se/2016/01/25/henrikkniberg/making-sense-of-mvp).
- **`confusion_matrix.png`**: Confusion Matrix Structure (TP, FP, FN, TN).

