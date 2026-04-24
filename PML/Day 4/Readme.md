
# Day 4: Data Modelling
-----------------------------------------------
### Date: 21/6/2024
### Topic:
	-Data
	-Types of Attributes
	-Preprocessing
	-Transformations
	-Measures
	-Visualization

### ML Application Development:
---------------------------
    1. Task: Problem definition
    2. Collection of data
    3. Clean & process that data (Pre-processing)
    4. Feature Transformation
    5. Feature Selection
    6. Learning algorithm
    7. Evaluation, Visualization, and Interpretation---> (Hidden information)
    8. Conclude

### Data: a collection of data objects and their attributes
![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/01e81091-32ae-4aa0-b101-ea0723f849ef)

### Types of Data:
    -Numerical: Made up of numbers
    	-Continuous: infinite real numbers
    	-Discrete: finite
    	
    -Categorical: Made up of words
    	-Ordinal: Distinct & ordered
    		Eg: eye color, zip codes
    	
    	-Nominal:Distinct
    		Eg: Ranking list
    		
    	-Interval: Range
    		Eg: Temperature
    		
    	-Ratio: All
    		Eg: Girls-Boys ratio
    	
    	Ex: Age: 15 to 78yrs
    		-<20yrs : Teen
    		-20 to 45yrs : Yng
    		->40yrs : Adult

### Types of dataset:
-----------------
  	-Record
  		-Data Matrix
  		-Document data
  		-Transaction data
  	-Graph
  		-World Wide Web
  		-Molecular data structure
  	-Ordered
  		-Spatial data
  		-Temporal(time series) data
  		-Sequential data
  		-Genetic data
  		
### Knowledge Discovery Process:
-------------------------------
    1. Goal:
    	-understanding the application domain and goals of the KDD effort
    2. Data selection, acquisition, integration
    3. Data cleaning
    	-noise, missing data, outliers, etc.
    4. Exploratory data analysis
    	-Dimensionality reduction, transformation
    	-selection of an appropriate model for analysis, hypothesis testing
    5. Data mining/Machine Learning
    	-selecting appropriate methods that match set goals ( classification, regression, clustering)
    6. Testing and verification
    7. Interpretation
    8. Conclusions
![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/021b520a-e93d-49f8-9ef5-28a3b8550dd3)

### Data Pre-processing steps:
----------------------
    1. Get the dataset
    2. Import libraries
    3. Import dataset
    4. Analyse the data & identify the missing data
    5. Apply feature transformation
    6. Split the dataset into training and testing data
    
 ![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/72158265-ee60-45f9-adec-6ed66fbcb2f6)
   
    
### Feature Transformation:
-----------------------------
  #### Label Encoding:
     Label encoding is a technique used in machine learning and data analysis to convert categorical variables into numerical format. It is particularly useful when working with algorithms that require numerical input, as most machine learning models can only operate on numerical data.
![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/b838612d-c0ce-434e-9815-1309906d7d49)

  #### Onehot Encoding: 
    One Hot Encoding is a technique that is used to convert categorical variables into numerical format.
![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/060dd00c-094f-4039-a9eb-d7924fd0b711)

### Feature Scaling:
-----------------
![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/c8de4131-de9e-411d-8343-c43ace77a644)

![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/d40feda0-01af-4713-9d15-d7e01a173524)

## Home-work
    Ex: 1 Read the data and prepare the the insignts with complete preprocessing, Feature selection and EDA operations
    data = {
        'Income': [np.nan, 60000, 55000, np.nan, 65000],
        'Gender': ['Male', 'Female', 'Female', 'Male', np.nan],
        'City': ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
        'Signup_Date': ['2022/01/01', '2021-06-15', '2022-03-10', '2020-12-20', '2021-08-05'],
        'Last_Login': ['2023-01-01', '2023/02/10', '2023-01-15', '2023-01-20', '2023/02/01'],
        'Purchased': [1, 0, 1, 0, 1]
    }

    Ex: 2 Read the data and prepare the the insignts with complete preprocessing, Feature selection and EDA operations or use pipelining
   
    data = {
        'age': [25, np.nan, 35, 45, 55, 65, 75, 85, 95, 105],
        'salary': [50000, 60000, np.nan, 80000, 90000, 100000, 110000, 120000, np.nan, 140000],
        'gender': ['Male', 'Female', np.nan, 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male'],
        'purchased': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
    }
    
        
    Ex: 3: use dataset from location PML/Datasets/sales_data.csv with complete preprocessing, Feature selection and EDA operations 
 
    Ex: 4 Design following mention visualization using matplotlib and seaborn library.
    Dataset:   
    df = pd.DataFrame({
        'A': np.random.rand(10),
        'B': np.random.rand(10),
        'C': np.random.rand(10),
        'D': np.random.rand(10)
    })

    Basic Plot Types
    ----------------
    Line Plot :     
    Create a line plot showing monthly sales trends for a company over one year.
    
    Bar Plot :     
    Plot a bar chart comparing revenue across different product categories.
    
    Histogram :    
    Plot a histogram to show the distribution of student marks in a class.
    
    Box Plot:    
    Create a box plot to compare salary distributions across departments.
    
    Area Plot :    
    Plot an area chart to visualize cumulative sales over time.
    
    Scatter Plot:    
    Create a scatter plot to analyze the relationship between study hours and exam scores.
    
    Pie Chart:    
    Plot a pie chart showing market share of different companies.
    
    Hexbin Plot:    
    Create a hexbin plot to visualize density of points for large datasets (e.g., height vs weight).
    General Visualization Tasks
    
    Advanced Customizations
    Customize a plot by adding title, labels, legend, grid, and changing colors/styles.
    
    Plotting with DataFrames and Series
        Use a Pandas DataFrame to generate a line and bar plot directly.
    
    Multiple Plots
    Plot multiple lines on the same graph to compare trends.
    
    Visualization with Subplots
    Create a figure with 4 subplots showing different types of plots.
    
    Styling Plots
    Apply different styles/themes to improve plot appearance.
    
    Saving Plots
    Save a generated plot as a PNG and PDF file.
   
    
    
    Ex: 4 Seaborn Plot Questions
    Dataset:
      data = {
        'Age': [25, 30, 22, 45, 35, 40, 28, 50],
        'Income': [50000, 60000, 45000, 80000, 65000, 70000, 52000, 90000],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
        'City': ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
        'Purchased': [1, 0, 1, 0, 1, 0, 1, 0]
    }    'Age': [25, 30, np.nan, 45, 35],
    
    
    scatterplot
    Create a scatterplot to show relationship between GDP and life expectancy.
    
    lineplot
    Plot a lineplot showing time-series data (e.g., stock prices).
    
    relplot
    Use relplot to visualize relationship between variables with different categories.
    
    histplot
    Plot histogram with KDE for distribution of ages.
    
    kdeplot
    Create KDE plot for income distribution.
    
    displot
    Use displot to visualize multiple distributions by category.
    
    ecdfplot
    Plot ECDF for a dataset of exam scores.
    
    rugplot
    Add rugplot to show individual data points along axis.
    
    stripplot
    Create stripplot to compare scores across categories.
    
    swarmplot
    Plot swarmplot to visualize non-overlapping data points.
    
    boxplot
    Compare distributions across groups using boxplot.
    
    violinplot
    Create violinplot to show distribution and density.
    
    barplot
    Plot mean values with confidence intervals.
    
    countplot
    Show count of observations in each category.
    
    pointplot
    Plot pointplot to compare means across categories.
    
    catplot
    Use catplot to generate different categorical plots.
    
    heatmap
    Create heatmap for correlation matrix of dataset.
    
    clustermap
    Use clustermap to cluster similar variables.
    
    regplot
    Plot regression line with scatter points.
    
    lmplot
    Create lmplot with grouping by category.
    
    pairplot
    Generate pairplot for multivariate dataset.
    
    jointplot
    Create jointplot showing relationship + distributions.
    
    FacetGrid
    Use FacetGrid to create multiple plots by category.
    
    PairGrid
    Customize pairwise relationships using PairGrid.
    
    JointGrid
    Build a custom joint plot using JointGrid.

## Daily, Practice Interview Questions

    1. What are outliers? 
    2. How do you detect outliers (Z-score, IQR)? 
    3. How do you handle outliers? 
    4. What is data smoothing? 
    5. What is binning? 
    6. What is noise reduction? 
    7. What is duplicate data and how do you handle it? 
    8. What is data consistency? 
    9. What is data validation? 
    10. What tools do you use for data cleaning? 
    11. What is feature scaling? 
    12. Why is feature scaling necessary? 
    13. What is normalization? 
    14. What is standardization? 
    15. Difference between normalization and standardization? 
    16. What is Min-Max scaling? 
    17. What is Z-score scaling? 
    18. When should you scale data? 
    19. Which algorithms require feature scaling? 
    20. What happens if you don’t scale data? 
    21.What is categorical data? 
    22. What is label encoding? 
    23. What is one-hot encoding? 
    24. What are the drawbacks of one-hot encoding? 
    25. When would you use label encoding vs one-hot encoding? 
    26. What is data leakage? 
    27. How do you prevent data leakage during preprocessing? 
    28. What is a preprocessing pipeline? 
    29. Why should preprocessing be done after train-test split? 
    30. What is feature engineering with examples? 


