## Homework

## **Question 1: KNN for Classification (Pass/Fail Prediction)**

### **Problem Statement**

You are given a dataset of students with their study hours and attendance percentage. Build a KNN classifier to predict whether a student will **Pass (1)** or **Fail (0)**.

* Use **K = 3**
* Use **Euclidean distance**
* Predict the result for:

  * Study Hours = 5
  * Attendance = 75


### **Dataset (students.csv)**

```csv
StudyHours,Attendance,Result
1,50,0
2,55,0
3,60,0
4,65,1
5,70,1
6,75,1
7,80,1
8,85,1
```
### **Tasks**

1. Load the dataset.
2. Implement KNN from scratch (do not use libraries like sklearn).
3. Normalize the data (optional but recommended).
4. Compute distances and find nearest neighbors.
5. Predict the class of the new student.

---

## **Question 2: KNN for Regression (House Price Prediction)**

### **Problem Statement**

You are given a dataset of houses with size and number of bedrooms. Use KNN regression to predict the **price** of a house.

* Use **K = 2**
* Use **Euclidean distance**
* Predict price for:

  * Size = 1200 sq ft
  * Bedrooms = 3

### **Dataset (houses.csv)**

```csv
Size,Bedrooms,Price
800,2,150000
900,2,180000
1000,3,200000
1100,3,220000
1300,3,260000
1500,4,300000
```

### **Tasks**

1. Load the dataset.
2. Implement KNN regression from scratch.
3. Calculate distances to all points.
4. Pick K nearest neighbors.
5. Predict price as the **average of neighbors' prices**.

---





If you want, I can also provide **sample Python solutions** or convert these into **interview-style questions with expected outputs**.
