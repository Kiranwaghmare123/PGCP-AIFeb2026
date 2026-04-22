## Interview Questions
    1. What is data preprocessing in Machine Learning? 
    2. Why is data preprocessing important? 
    3. What are the main steps involved in data preprocessing? 
    4. What is data cleaning? 
    5. What are missing values? 
    6. What are noisy data? 
    7. What is data transformation? 
    8. What is data reduction? 
    9. What is feature engineering? 
    10. What is feature selection? 
    11. What are different types of missing data (MCAR, MAR, MNAR)? 
    12. How do you detect missing values in a dataset? 
    13. What are common techniques to handle missing data? 
    14. When would you drop rows vs impute values? 
    15. What is mean/median/mode imputation? 
    16. What is forward fill and backward fill? 
    17.What is interpolation? 
    18. How does missing data affect model performance? 
    19. What are advanced imputation techniques (e.g., KNN imputation)? 
    20. What are the risks of improper imputation? 





## Ex 1: ecommerce_sales.csv
    OrderID,Date,CustomerID,Region,Product,Category,Price,Quantity,Discount,Revenue
    1001,2024-01-05,C001,North,Laptop,Electronics,800,1,0.10,720
    1002,2024-01-07,C002,South,Phone,Electronics,500,2,0.05,950
    1003,2024-01-10,C003,East,Shoes,Fashion,80,3,0.20,192
    1004,2024-01-12,C001,West,Watch,Accessories,150,1,0.15,127.5
    1005,2024-01-15,C004,North,Tablet,Electronics,300,2,0.10,540
    1006,2024-01-18,C005,South,Shirt,Fashion,40,5,0.25,150
    1007,2024-01-20,C006,East,Bag,Accessories,60,2,0.10,108
    1008,2024-01-22,C002,West,Headphones,Electronics,120,1,0.05,114
    1009,2024-01-25,C007,North,Shoes,Fashion,90,2,0.15,153
    1010,2024-01-28,C008,South,Laptop,Electronics,850,1,0.10,765

## Ex 2: Ex 2:weather_data.csv

    date,temperature,windspeed,humidity,event
    2024-01-01,32,6,80,Rain
    2024-01-02,35,7,70,Sunny
    2024-01-03,28,2,90,Snow
    2024-01-04,24,7,85,Snow
    2024-01-05,32,4,75,Rain
    2024-01-06,31,2,60,Sunny
    2024-01-07,30,5,65,Cloudy
    2024-01-08,29,3,88,Rain

## Ex 3:

    data = {
        "date": ["2024-01-01","2024-01-02","2024-01-03","2024-01-04",
                 "2024-01-05","2024-01-06","2024-01-07","2024-01-08"],
        "temperature": [32,35,28,24,32,31,30,29],
        "windspeed": [6,7,2,7,4,2,5,3],
        "humidity": [80,70,90,85,75,60,65,88],
        "event": ["Rain","Sunny","Snow","Snow","Rain","Sunny","Cloudy","Rain"]
    }

## Ex 4:
        data = {
        "Name": ["A", "B", "C", "D"],
        "Age": [25, np.nan, 30, np.nan],
        "Marks": [80, 90, np.nan, 85]
    }

## Ex 5:

        data = {
            "City": ["Mumbai", "Delhi", np.nan, "Mumbai", np.nan]
        }

## Ex 6:
    data = {
        "Time": ["T1", "T2", "T3", "T4"],
        "Temp": [30, np.nan, np.nan, 35]
    }

## Ex 7:
    data = {
        "ID": [1, 2, 2, 3],
        "Name": ["Amit", "Riya", "Riya", "John"],
        "Marks": [80, 90, 90, 85]
    }

## Ex 8:

    data = {
        "Date": ["01-12-2025", "2025/12/02", "Dec 3, 2025"]
    }

## Ex 9:
    data = {
        "Weight": [70, 154, 65],  # kg and pounds mixed
    }

## Ex 10:
    data = {
        "City": ["Mumbai", "mumbai", "MUMBAI", "Delhi"]
    }

## Ex 11:

    data = {
        "Gender": ["Male", "M", "male", "Female", "F"]
    }

## Ex 12:
    data = {
        "Salary": ["₹50,000", "$600", "70000"]
    }

## Ex 13:
    data = {
        "Phone": ["+91-9876543210", "98765 43210", "09876543210"]
    }

## Ex 14:

    data = {
        "Distance": ["5 km", "5000 m", "3 km"]
    }

