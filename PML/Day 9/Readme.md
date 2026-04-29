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
