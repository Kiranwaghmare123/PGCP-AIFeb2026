# Day 4: Regression
-----------------------------------------------
## Date: 22/6/2024
### Topic:
	-Regression
	-Types of Regression
	

### Supervised Learning:
------------------- 
	-Regression
		-Labelled (Input + Output(Target attribute)
		-Task: To predict the continuous value
		
	-Classification
		-Labelled (Target attribute)
		-Task: To identify the particular class label

### Regression:
------------
	-Linear Regression:
	-LR is a type of supervised learning that computes the linear relationship between a dependent and independent features.

### Simple Linear Regression:
--------------------------
	-SLR : 1 Independent variable & 1 Dependent variable.
	
### Multiple Linear Regression:
----------------------------
	-MLR : more that 1 Independent variable & 1 Dependent variable.
	
### Steps in Regression model implementation:
------------------------------------------

	1. Importing the libraries and dataset
	2. Splitting the dataset into the Training set and Test set
	3. Preprocessing if required
	4. Fitting Simple Linear Regression to the Training set
	5. Predicting the Test set results
	6. Visualizing the Test set results
	
	
### Evaluation Metrics:
------------------
![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/5d14effe-cffb-4b4b-aa69-68186a40342b)

    1. Coefficient of Determination: 
    	-Also refered as R-Squared
    	-It is a statistics that indicates how much variation the developed model can capture
![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/4fce608b-8531-44fc-acbb-75010a7458a1)

   	
    	
    2. Residual Sum of Squares:RSS
    	-The sum of squares of the residual for each data point in the plot or data is known as RSS.
  ![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/59ef5a6a-30e8-4580-9ef7-b8605dfadd07)

  ![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/169c4933-7381-421f-81c2-4886b09d6c80)

	
    3. Total sum of squares:TSS
    	-Sum of the data points errors from the answer variables's mean is known as the total sum of squares or TSS
 ![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/13552cda-408a-488a-bdc9-b654767dc6f2)
   	
    4. Root Mean Squared Error:RMSE
    	-The square root of the residual variance is the RMS errors.
    	-It describe how well the observed data points match the expected values or the models absolute fit to the data.
 ![image](https://github.com/Kiranwaghmare123/PG-DBDA-Sep2023/assets/72081819/70aa2044-0255-40a3-869e-7b77f79426e8)
    
## Daily, practice Interview Questions

    1. What are the different types of regression?
    
    2. Is regression a supervised learning? Why?
    
    3. Explain the ordinary least squares method for regression.
    
    4. What are linear, multinomial and polynomial regressions?
    
    5. If model used for regression is
    y = a + b(x − 1)2;
        is it a multinomial regression? If not, what type of regression is it?
        
    6. What does the line of regression tell you?

# Homework:
------------

# Ex 1: Understand the dataset and apply preprocessing, feature selection, EDA and Regression modelling
    data = {
        'age': [25, np.nan, 35, 45, 55, 65, 75, 85, 95, 105],
        'salary': [50000, 60000, np.nan, 80000, 90000, 100000, 110000, 120000, np.nan, 140000],
        'gender': ['Male', 'Female', np.nan, 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male'],
        'purchased': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
    }

# Ex 2: Understand the dataset and apply preprocessing, feature selection, EDA and Regression modelling
    data = {
        'age': [23, 30, np.nan, 45, 56, 67, np.nan, 89, 34, 29, 50, 70, 22, 38, 60],
        'income': [48000, 52000, 58000, np.nan, 70000, 89000, 92000, 130000, np.nan, 46000, 78000, 85000, 40000, 65000, np.nan],
        'gender': ['Female', 'Male', 'Female', np.nan, 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', np.nan, 'Male', 'Female', 'Male', 'Female'],
        'city': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'Los Angeles', 'New York'],
        'bought': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes']
    }

# Ex 3: Understand the dataset and apply preprocessing, feature selection, EDA and Regression modelling
    data = {
    'age': [25, 30, 35, np.nan, 45, 50, 55, 60, np.nan, 70, 75, 80, 85, 90, np.nan],
    'height_cm': [170, 165, 180, 175, np.nan, 160, 155, 150, 165, np.nan, 175, 180, 170, 160, 155],
    'weight_kg': [65, 70, 75, 80, 85, np.nan, 95, 100, 105, 110, 115, np.nan, 85, 70, 65],
    'gender': ['Male', 'Female', np.nan, 'Female', 'Male', 'Female', 'Male', np.nan, 'Female', 'Male', 'Female', 'Male', 'Female', np.nan, 'Female'],
    'activity_level': ['High', 'Medium', 'Low', 'Medium', 'High', 'Low', np.nan, 'High', 'Medium', 'Low', 'Medium', 'High', 'Low', 'Medium', np.nan],
    'diet': ['Vegetarian', 'Non-Vegetarian', 'Vegan', 'Vegetarian', np.nan, 'Non-Vegetarian', 'Vegan', 'Vegetarian', 'Non-Vegetarian', 'Vegan', np.nan, 'Vegetarian', 'Non-Vegetarian', 'Vegan', 'Vegetarian'],
    'target': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes']
}

# Ex 4: Understand the dataset and apply preprocessing, feature selection, EDA and Regression modelling

    Ex: data = {
    'client_id': [46109, 46109, 46109],
    'loan_type': ['home', 'credit', 'home'],
    'loan_amount': [13672, 9794, 12734],
    'repaid': [0, 0, 1],
    'loan_id': [10243, 10984, 10990],
    'loan_start': ['2002-04-16', '2003-10-21', '2006-02-01'],
    'loan_end': ['2003-12-20', '2005-07-17', '2007-07-05'],
    'rate': [2.15, 1.25, 0.68]
    }
