# Data Directory

This directory contains datasets used throughout the DSR Python, NumPy and Pandas course.

## Datasets

### 1. Titanic Dataset (`titanic.csv`)

The classic Titanic passenger dataset, widely used for teaching data science concepts.

**Source**: [Data Science Dojo on GitHub](https://github.com/datasciencedojo/datasets)

**Columns**:
| Column | Description |
|--------|-------------|
| PassengerId | Unique passenger identifier |
| Survived | Survival (0 = No, 1 = Yes) |
| Pclass | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) |
| Name | Passenger name |
| Sex | Gender |
| Age | Age in years |
| SibSp | # of siblings/spouses aboard |
| Parch | # of parents/children aboard |
| Ticket | Ticket number |
| Fare | Passenger fare |
| Cabin | Cabin number |
| Embarked | Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |

**Used in**: 
- `03_pandas_basics/` (all notebooks)
- `04_pandas_advanced/01_groupby_and_aggregation.ipynb`
- `04_pandas_advanced/02_merge_join_reshape.ipynb`
- `04_pandas_advanced/03_apply_map_pipe.ipynb`

### 2. Berlin Bike Share Dataset (`berlin_bikes.csv`)

Bike share trip data, simulating a Berlin mobility company's dataset.

**Source**: Adapted from [Capital Bikeshare data](https://www.capitalbikeshare.com/system-data), 
renamed and formatted to simulate a Berlin bike share service.

**Columns**:
| Column | Description |
|--------|-------------|
| duration | Trip duration in seconds |
| start_time | Trip start timestamp |
| end_time | Trip end timestamp |
| start_station_id | ID of starting station |
| start_station | Name of starting station |
| end_station_id | ID of ending station |
| end_station | Name of ending station |
| bike_id | Unique bike identifier |
| user_type | User type (Casual or Member) |

**Used in**:
- `04_pandas_advanced/04_timeseries_and_performance.ipynb`
- `05_capstone/01_capstone_exercise.ipynb`

## Downloading the Data

Run the download script from the repository root:

```bash
python data/download_data.py
```

The script will:
1. Download datasets from their sources
2. Transform data as needed (e.g., rename columns)
3. Skip downloads if files already exist
4. Report any errors

## Data License

- **Titanic**: Public domain dataset
- **Bike Share**: Creative Commons Attribution 4.0 International License
