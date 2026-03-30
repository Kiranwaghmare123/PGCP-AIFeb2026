# Pandas Function

---

# 1. Data Creation & Input

* `pd.DataFrame()` → Create a DataFrame
* `pd.Series()` → Create a Series
* `pd.read_csv()` → Load CSV file
* `pd.read_excel()` → Load Excel file
* `pd.read_json()` → Load JSON data
* `pd.read_sql()` → Load from SQL database

---

# 2. Data Inspection

* `df.head(n)` → First *n* rows
* `df.tail(n)` → Last *n* rows
* `df.info()` → Summary of structure
* `df.describe()` → Statistical summary
* `df.shape` → (rows, columns)
* `df.columns` → Column names
* `df.index` → Row index

---

# 3. Selection & Indexing

* `df['col']` → Select column
* `df[['col1','col2']]` → Multiple columns
* `df.loc[]` → Label-based selection
* `df.iloc[]` → Position-based selection
* `df.at[]` → Fast scalar access
* `df.iat[]` → Fast integer access

---

# 4. Data Cleaning

* `df.drop()` → Remove rows/columns
* `df.dropna()` → Remove missing values
* `df.fillna()` → Fill missing values
* `df.replace()` → Replace values
* `df.rename()` → Rename columns/index
* `df.astype()` → Change data types

---

# 5. Filtering & Sorting

* `df[df['col'] > value]` → Filter rows
* `df.query()` → Query using expressions
* `df.sort_values()` → Sort by values
* `df.sort_index()` → Sort by index

---

# 6. Aggregation & Statistics

* `df.mean()` → Mean
* `df.sum()` → Sum
* `df.min()` / `df.max()` → Min/Max
* `df.count()` → Count non-null
* `df.std()` → Standard deviation
* `df.var()` → Variance

---

# 7. Grouping & Combining

* `df.groupby()` → Group data
* `df.agg()` → Aggregate functions
* `df.merge()` → SQL-style join
* `df.join()` → Join on index
* `pd.concat()` → Concatenate DataFrames

---

# 8. Transformation

* `df.apply()` → Apply function
* `df.map()` → Map values (Series)
* `df.applymap()` → Element-wise operation
* `df.transform()` → Transform groups

---

# 9. Reshaping

* `df.pivot()` → Pivot table
* `df.pivot_table()` → Advanced pivot
* `df.melt()` → Unpivot
* `df.stack()` → Stack columns
* `df.unstack()` → Unstack index

---

# 10. Time Series

* `pd.to_datetime()` → Convert to datetime
* `df.resample()` → Resample time data
* `df.shift()` → Shift data
* `df.rolling()` → Rolling window ops

---

# 11. Exporting Data

* `df.to_csv()` → Save as CSV
* `df.to_excel()` → Save as Excel
* `df.to_json()` → Save as JSON
* `df.to_sql()` → Save to database

---

# 12. Miscellaneous Useful Functions

* `df.value_counts()` → Frequency count
* `df.unique()` → Unique values
* `df.nunique()` → Count unique values
* `df.isnull()` / `df.notnull()` → Check missing values
* `df.duplicated()` → Find duplicates
* `df.drop_duplicates()` → Remove duplicates

---
