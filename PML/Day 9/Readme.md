# Decision Tree:
--------------
    -A flowchart like structure used for decision making or predictions.
    -It consist of nodes(decision nodes), branches(outcome) and the leaf nodes(predictions).
    -Internal node: attributes
    -Branches: sub attributes in the feature column
-Leaf nodes: Final class labels

# Working of Decision tree:
    --------------------------
    1.Selecting the best attribute: 
    	-use metric like Gini impurity, entropy or information gain.
    2.Splittng of the dataset:
    	-Split into subsets based on the slected attribute.
    3.Repeatation of the process:
    	-Recursively repeat for eacj subset until a stopping criteria is met.
	
# Metrics for Splitting:
----------------------
    1. Entropy : Amount of uncertainity or impurity
    Formula:
    
    where, pi is the probability of an instance being classified into a particular class.
    
    
    2. Information Gain : Reduction in entropy or gini impurity.
    Formula:
    
    Information Gain = Entropy(parent) - Average Entropy of Feature column
    
    
    3.Gini impurity: Likelihood of incorrect classification
    Formula:
    
    where, pi is the probability of an instance being classified into a particular class.
    
    
# Advantages:
-----------
    -Easy to understand and interpreat.
    -Suitable for classification and regression.
    -No need for feature scaling.
    -Handles non-linear relationships effectively.

# Disadvantages:
---------------
    -Overfitting : prone to overfitting, especially with deep trees.
    -Instability: Sensitive to small variations in the data.
    -Bias towards features with more leveles.

# Pruning:
---------
    -method to help overfitting.
    -helps in improving the performance of the tree by cutting the nodes which are not significant.
    -2 types of pruning:
    	-Pre-pruning: (Early stopping): Stops tree growth based on criteria
    		-e.g. max depth, min samples leaf.
    	
    	-Post-pruning: Removes branches from a fully grown tree that offer little classification power.

# Decision Tree Regression:
--------------------------
    -Decision tree regression is used for predictive modelling.
    -operated by recursively partitioning the dataset into subsets nased on the input features.
    -create a hierarchical tree-like structure with internal nodes for decisions and leaf nodes for predicted output.
    -aim to minimize variance in the target variable within each partition.

# Advantages:
-------------
    -Easy to understand and visualize decision tree rules.
    -Capture non-linear relationships.
    -No feature scaling is required.
    -Handles numerical and categorical data
    -Outliers have minimal impact on overall model performance.

# Random Forest:
---------------
    -It is a supervised learning used for both classification and regression task.
    -Concept: It consist of collection of decision tree that operates on various subsets of the dataset. The final output is determined by aggregating the prediction of these trees, which is typically called as majority voting.

# Assumptions:
------------
    -The feature values should contain actual values for accurate predictions.
    -The predictions from each tree should have low correlation to ensure diverse and accurate results.

# Importance of Random Forest:
----------------------------
    -Overfitting prevention
    -Accuracy
    -Efficient 

# Working of Random Forest:
-------------------------
    1.Select Random data points from the training dataset.
    2.Build Decision Tree
    3.Choose the number of tree to build (n_estimator = n)
    4.Make predictions


# Data Preparing for Random Forest Model:
---------------------------------------
    -Handle the missing values
    -Addressing the imbalance data is required.


# Ensemble Learning:
------------------
    -Ensemble learning is a machine learning program where multiple models, often called "weak learners" are trained to solve the same problem and combined to get better results.
    -Main Idea : to use a group of diverse models to achieve better performance than any single model.
    

# Types of Emsemble learning:
---------------------------
  1. Bagging
  2. Boosting
  3. Random space
  4. Stacking







---
## Home-work

## **Question 1: Entropy Calculation**

Given the dataset:

| Outcome | Count |
| ------- | ----- |
| Yes     | 9     |
| No      | 5     |

1. Compute the entropy of the dataset.
2. Interpret the result (is the dataset pure or impure?).

Use:
<img width="281" height="52" alt="image" src="https://github.com/user-attachments/assets/6b942438-566e-4c44-9bfa-dfa43ae44b5c" />


---

## **Question 2: Information Gain**

Consider the dataset:

| Weather  | PlayTennis |
| -------- | ---------- |
| Sunny    | No         |
| Sunny    | No         |
| Overcast | Yes        |
| Rain     | Yes        |
| Rain     | Yes        |
| Rain     | No         |
| Overcast | Yes        |
| Sunny    | No         |
| Sunny    | Yes        |
| Rain     | Yes        |

Tasks:

1. Calculate the entropy of the target variable **PlayTennis**.
2. Split the dataset by **Weather** and compute entropy for each subset.
3. Calculate the **Information Gain** of the attribute *Weather*.
4. Decide whether *Weather* is a good splitting attribute.

Use:

<img width="461" height="52" alt="image" src="https://github.com/user-attachments/assets/9ba25aa3-0897-40db-87b4-5539aa541b8a" />

---

## **Question 3: Gini Index Calculation**

Given:

| Class | Count |
| ----- | ----- |
| A     | 6     |
| B     | 4     |

1. Compute the Gini Index.
2. Compare it with entropy (qualitatively, no need to recompute entropy).

Use:

<img width="263" height="56" alt="image" src="https://github.com/user-attachments/assets/44321379-3c63-40af-aed6-844b0f68957e" />

---

## **Question 4: Comparing Splits (IG vs Gini)**

Dataset:

| Feature X | Class |
| --------- | ----- |
| High      | Yes   |
| High      | Yes   |
| Medium    | Yes   |
| Medium    | No    |
| Low       | No    |
| Low       | No    |

Two possible splits:

* Split 1: {High, Medium} vs {Low}
* Split 2: {High} vs {Medium, Low}

Tasks:

1. Compute **Information Gain** for both splits.
2. Compute **Gini Index** for both splits.
3. Which split is better under:

   * Information Gain?
   * Gini Index?

---

## **Question 5: Multi-Attribute Selection**

Dataset:

| Outlook  | Humidity | Play |
| -------- | -------- | ---- |
| Sunny    | High     | No   |
| Sunny    | High     | No   |
| Overcast | High     | Yes  |
| Rain     | High     | Yes  |
| Rain     | Normal   | Yes  |
| Rain     | Normal   | No   |
| Overcast | Normal   | Yes  |
| Sunny    | High     | No   |
| Sunny    | Normal   | Yes  |
| Rain     | High     | Yes  |

Tasks:

1. Compute Information Gain for:

   * Outlook
   * Humidity
2. Which attribute should be chosen as the root node?
3. Verify your answer using Gini Index as well.

---

## **Question 6: Edge Case Analysis**

Dataset:

| Class    | Count |
| -------- | ----- |
| Positive | 10    |
| Negative | 0     |

1. Compute entropy.
2. Compute Gini Index.
3. Explain why both metrics behave this way.

---

## **Question 7: Small Dataset Interpretation**

Dataset:

| Feature | Class |
| ------- | ----- |
| A       | Yes   |
| A       | No    |
| B       | Yes   |
| B       | No    |

Tasks:

1. Compute entropy of the dataset.
2. Compute IG for splitting on Feature.
3. What does the result indicate about this feature?

---

### Visualization (Decision Boundary)
    # =========================
    from matplotlib.colors import ListedColormap
    
    # Use only first 2 features for 2D visualization
    X_vis = X_train[:, :2]
    y_vis = y_train.values
    
    X1, X2 = np.meshgrid(
        np.arange(start=X_vis[:, 0].min() - 1, stop=X_vis[:, 0].max() + 1, step=0.01),
        np.arange(start=X_vis[:, 1].min() - 1, stop=X_vis[:, 1].max() + 1, step=0.01)
    )
    
    plt.contourf(
        X1, X2,
        model.predict(np.c_[X1.ravel(), X2.ravel(), np.zeros_like(X1.ravel())]).reshape(X1.shape),
        alpha=0.75,
        cmap=ListedColormap(('red', 'green'))
    )
    
    plt.scatter(X_vis[:, 0], X_vis[:, 1], c=y_vis, cmap=ListedColormap(('red', 'green')))
    plt.title('Decision Tree (Training set)')
    plt.xlabel('Age (scaled)')
plt.ylabel('Salary (scaled)')
plt.show()
---

## Daily, preparation question
1. What is a decision tree? How does it work?
2. What are the main components of a decision tree (root, node, leaf, branch)?
3. What types of problems can decision trees solve?
4. Difference between classification and regression trees.
5. What is overfitting in decision trees?
6. What is entropy in decision trees?
7. What is Information Gain?
8. What is Gini Index? How is it different from entropy?
9. Explain how the ID3 algorithm works.
10. What are the limitations of ID3 algorithm?
11. How do you handle missing values in decision trees?
12. How do decision trees handle categorical vs numerical data?
13. What is tree pruning and why is it needed?
14. Difference between pre-pruning and post-pruning.
15. How do you avoid overfitting in decision trees?
16. What happens if your tree is too deep?
