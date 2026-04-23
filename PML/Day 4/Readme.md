## Dataset
    Ex: 
    data = {
        'Income': [50000, 60000, 55000, np.nan, 65000],
        'Gender': ['Male', 'Female', 'Female', 'Male', np.nan],
        'City': ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
        'Signup_Date': ['2022-01-01', '2021-06-15', '2022-03-10', '2020-12-20', '2021-08-05'],
        'Last_Login': ['2023-01-01', '2023-02-10', '2023-01-15', '2023-01-20', '2023-02-01'],
        'Purchased': [1, 0, 1, 0, 1]
    }

    Ex 1: 
    data = {
        'age': [25, np.nan, 35, 45, 55, 65, 75, 85, 95, 105],
        'salary': [50000, 60000, np.nan, 80000, 90000, 100000, 110000, 120000, np.nan, 140000],
        'gender': ['Male', 'Female', np.nan, 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male'],
        'purchased': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
    }
    
    Ex 2: Column Transform: pipelining
    
    Ex 3: data.csv
    Country,Age,Salary,Purchased
    France,44,72000,No
    Spain,27,48000,Yes
    Germany,30,54000,No
    Spain,38,61000,No
    Germany,40,,Yes
    France,35,58000,Yes
    Spain,,52000,No
    France,48,79000,Yes
    Germany,50,83000,No
    France,37,67000,Yes

    Ex:
    df = pd.DataFrame({
        'A': np.random.rand(10),
        'B': np.random.rand(10),
        'C': np.random.rand(10),
        'D': np.random.rand(10)
    })
    
    Ex: Seaborn
    data = {
        'Age': [25, 30, 22, 45, 35, 40, 28, 50],
        'Income': [50000, 60000, 45000, 80000, 65000, 70000, 52000, 90000],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
        'City': ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
        'Purchased': [1, 0, 1, 0, 1, 0, 1, 0]
    }    'Age': [25, 30, np.nan, 45, 35],
    
