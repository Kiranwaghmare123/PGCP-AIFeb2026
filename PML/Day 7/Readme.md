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

##  Daily Interview Questions:

1. What is the K-Nearest Neighbors (KNN) algorithm?
2. Is KNN a parametric or non-parametric model? Why?
3. Why is KNN called a lazy learner?
4. How does KNN perform classification vs regression?
5. What are the main steps involved in KNN?
6. What distance metrics are commonly used in KNN?
    Euclidean
    Manhattan
    Minkowski
7. When would you prefer Manhattan distance over Euclidean?
8. How does the choice of distance metric affect performance?
9. What happens if features are on different scales?
10. How do you choose the optimal value of k?
11. Why is feature scaling important in KNN?
12. What preprocessing steps are required before applying KNN?
13. How do you handle categorical variables in KNN?
14. What is the time complexity of KNN during:
     Training
     Prediction
15. What is the curse of dimensionality and how does it affect KNN?


