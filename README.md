# Vanguard A/B Test Analysis

A comprehensive analysis of Vanguard's digital process A/B test to evaluate the effectiveness of a new user interface design on client completion rates and user experience.

## Project Overview

This project analyzes an A/B test conducted by Vanguard to compare their traditional online process (Control) against a new, more intuitive design (Test). The analysis focuses on three key performance indicators:

- **Completion Rate**: Percentage of users who successfully complete the entire process
- **Time on Each Step**: Average time users spend on each step of the process
- **Error Rates**: Frequency of users going back to previous steps (indicating confusion or errors)

## Dataset Description

The analysis uses four main datasets:

### Raw Data Files
- `df_final_web_data_pt_1.txt` & `df_final_web_data_pt_2.txt`: User session data tracking step-by-step interactions
- `df_final_demo.txt`: Client demographic information (age, tenure, gender, account details)
- `df_final_experiment_clients.txt`: Experiment assignment data (Test vs Control groups)

### Key Variables
- **client_id**: Unique identifier for each client
- **visit_id**: Unique identifier for each session
- **process_step**: Current step in the process (start, step_1, step_2, step_3, confirm)
- **date_time**: Timestamp of each interaction
- **variation**: Experiment group assignment (Test or Control)

## Project Structure

```
vanguard-ab-test/
├── raw_data/                    # Original datasets
├── analysis.py                  # Analysis functions and database queries
├── cleaning.py                  # Data cleaning and preprocessing functions
├── create_db.py                # Database creation and data loading
├── dataframes.ipynb            # Main analysis notebook
├── time_insights.ipynb         # Time-based analysis
├── vanguard.sql               # SQL database schema
├── KPI_query.sql              # Key performance indicator queries
├── client_analysis_query.sql   # Client demographic analysis
├── ERD.png                    # Entity Relationship Diagram
└── README.md                  # This file
```

## Key Findings

### 1. Completion Rates
- **Control Group**: 13.6% completion rate
- **Test Group**: 13.7% completion rate
- **Statistical Significance**: No significant difference (p-value = 0.486)

### 2. Time Analysis
- **Step 1 to 2**: Test group significantly faster (26.5s vs 31.9s)
- **Step 2 to 3**: Test group slightly slower (40.6s vs 34.1s)
- **Step 3 to 4**: Test group faster (76.3s vs 80.5s)
- **Step 4 to 5**: Test group significantly faster (61.7s vs 79.7s)

### 3. Error Rates
The Test group showed fewer instances of users returning to previous steps, indicating a more intuitive user experience.

## Technical Implementation

### Data Processing Pipeline
1. **Data Cleaning**: Remove duplicates, handle missing values, normalize column names
2. **Database Creation**: MySQL database with three main tables (participants, clients, session)
3. **Feature Engineering**: Calculate time differences and step progressions
4. **Statistical Analysis**: Hypothesis testing using t-tests and chi-square tests

### Key Functions
- `time_diff()`: Calculates time spent between steps
- `step_diff()`: Identifies user navigation patterns and errors
- `query_db()`: Executes SQL queries on the Vanguard database

## Technologies Used

- **Python**: Data analysis and statistical testing
- **Pandas**: Data manipulation and analysis
- **MySQL**: Database management
- **SQLAlchemy**: Database connectivity
- **Matplotlib/Seaborn**: Data visualization
- **SciPy**: Statistical analysis
- **Tableau**: Advanced visualizations (`.twb` files)

## Database Schema

The project uses a MySQL database with the following structure:

- **participants**: Client experiment assignments
- **clients**: Demographic and account information
- **session**: Step-by-step user interaction data

See `ERD.png` for the complete entity relationship diagram.

## How to Run

1. **Setup Database**:
   ```python
   python create_db.py
   ```

2. **Run Analysis**:
   ```python
   jupyter notebook dataframes.ipynb
   ```

3. **Execute Queries**:
   ```python
   from analysis import query_db
   results = query_db("SELECT * FROM participants LIMIT 10")
   ```

## Conclusions

While the new design (Test) didn't significantly improve completion rates, it did provide a better user experience with:
- Faster completion times for most steps
- Reduced error rates and confusion
- More intuitive navigation patterns

The analysis suggests that while the new design is an improvement in user experience, additional optimizations may be needed to significantly impact completion rates.


---

*This analysis was conducted as part of a data analytics project to demonstrate A/B testing methodologies and statistical analysis techniques.*