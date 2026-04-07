# Python, NumPy and Pandas — DSR Berlin

A comprehensive teaching repository for a one-day intensive course at [Data Science Retreat Berlin](https://datascienceretreat.com/), an advanced 3-month data science bootcamp.

**Target audience**: Numerate professionals with some Python background but inconsistent depth. This is the first technical day of the bootcamp.

## Repo Structure

```
├── final_notebooks/     # Complete teacher notebooks with solutions
│   ├── 01_python_refresher/
│   ├── 02_numpy/
│   ├── 03_pandas_basics/
│   ├── 04_pandas_advanced/
│   └── 05_capstone/
├── live_notebooks/      # Skeleton notebooks for live coding
│   └── (same structure as final_notebooks)
├── data/                # Datasets (Titanic, Berlin bikes)
├── README.md
└── requirements.txt
```

- **`final_notebooks/`**: Polished reference notebooks with full explanations, visualizations, and solutions. Use for self-study or post-class review.
- **`live_notebooks/`**: Same structure but with `# YOUR CODE HERE` placeholders. Used for live coding during class.
- **`data/`**: Datasets needed for the exercises and capstone.

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd DSR_Python_Intro

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download/generate datasets
python data/download_data.py

# Start Jupyter
jupyter notebook
```

## Course Schedule

| Block | Time | Topic | Notebooks |
|-------|------|-------|-----------|
| 1 | 09:00 - 10:30 | Python Refresher | `01_python_refresher/` |
| 2 | 10:45 - 12:15 | NumPy Fundamentals | `02_numpy/` |
| 3 | 13:15 - 14:45 | Pandas Basics | `03_pandas_basics/` |
| 4 | 15:00 - 16:30 | Pandas Advanced | `04_pandas_advanced/` |
| 5 | 16:45 - 18:00 | Capstone Exercise | `05_capstone/` |

*15-minute breaks between blocks, 1-hour lunch at 12:15*

## How to Use This Repo

### For Students

1. **Before class**: Skim through the `final_notebooks/` to get familiar with topics
2. **During class**: Follow along in `live_notebooks/`, filling in code as the instructor demonstrates
3. **After class**: Use `final_notebooks/` as reference for self-study and practice
4. **Exercises**: Each notebook ends with exercises — try them first, then check solutions in final notebooks

### For Instructors

1. Open the corresponding `live_notebooks/` on your shared screen
2. The structure mirrors `final_notebooks/` — keep the final version open privately for reference
3. Fill in code cells live, explaining concepts as you go
4. Markdown cells contain all explanations and talking points
5. Run the capstone together at the end as a hands-on practice session

## Topics Covered

### Block 1: Python Refresher
- Data structures (lists, tuples, sets, dicts)
- Comprehensions and generators
- Functions, decorators, and type hints
- OOP basics and Pythonic idioms

### Block 2: NumPy
- Array creation and dtypes
- Indexing, slicing, and boolean masking
- Broadcasting
- Universal functions and performance

### Block 3: Pandas Basics
- Series and DataFrame
- Loading and exploring data
- Indexing and filtering
- Missing values and data types

### Block 4: Pandas Advanced
- GroupBy and aggregation
- Merge, join, reshape
- Apply, map, and pipe
- Time series and performance

### Block 5: Capstone
- Real-world data analysis project using Berlin bike share data
- Combines all skills learned during the day

## Requirements

- Python 3.10+
- See `requirements.txt` for full package list

## License

Educational materials for Data Science Retreat Berlin. Feel free to adapt for your own teaching purposes.
