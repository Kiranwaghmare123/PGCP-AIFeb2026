```python
# =========================================
# 1. IMPORT LIBRARIES
# =========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.metrics import precision_recall_curve, roc_curve, roc_auc_score, average_precision_score

# =========================================
# 2. LOAD DATA
# =========================================
df = pd.read_csv('creditcard.csv')

print("Shape:", df.shape)
print(df.head())

# =========================================
# 3. BASIC EDA
# =========================================

print("\nInfo:")
print(df.info())

print("\nStatistics:")
print(df.describe())

# Class imbalance
sns.countplot(x='Class', data=df)
plt.title("Class Distribution (Fraud vs Normal)")
plt.show()

print("Fraud ratio:", df['Class'].mean())

# Amount distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Amount'], bins=50, kde=True)
plt.title("Transaction Amount Distribution")
plt.show()

# =========================================
# 4. FEATURE ENGINEERING
# =========================================

# Log transform Amount
df['Log_Amount'] = np.log1p(df['Amount'])

# Normalize Time
df['Time_scaled'] = StandardScaler().fit_transform(df[['Time']])

# Drop original Amount and Time
df = df.drop(['Amount', 'Time'], axis=1)

# =========================================
# 5. PREPROCESSING
# =========================================

X = df.drop('Class', axis=1)
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42, stratify=y
)

pipeline = Pipeline([
    ('scaler', StandardScaler())
])

X_train_scaled = pipeline.fit_transform(X_train)
X_test_scaled = pipeline.transform(X_test)

# =========================================
# 6. ANOMALY SCORE FUNCTION
# =========================================

def anomaly_scores(X_original, X_reconstructed):
    loss = np.sum((X_original - X_reconstructed)**2, axis=1)
    loss = (loss - loss.min()) / (loss.max() - loss.min())
    return loss

# =========================================
# 7. MODEL (PCA)
# =========================================

pca = PCA(n_components=27, random_state=42)

# Train
X_train_reduced = pca.fit_transform(X_train_scaled)
X_train_reconstructed = pca.inverse_transform(X_train_reduced)

# Test
X_test_reduced = pca.transform(X_test_scaled)
X_test_reconstructed = pca.inverse_transform(X_test_reduced)

# =========================================
# 8. ANOMALY SCORES
# =========================================

train_scores = anomaly_scores(X_train_scaled, X_train_reconstructed)
test_scores = anomaly_scores(X_test_scaled, X_test_reconstructed)

# =========================================
# 9. EVALUATION FUNCTION
# =========================================

def evaluate(y_true, scores):
    
    # Precision-Recall
    precision, recall, _ = precision_recall_curve(y_true, scores)
    ap = average_precision_score(y_true, scores)
    
    plt.figure(figsize=(6,4))
    plt.plot(recall, precision)
    plt.title(f'Precision-Recall (AP={ap:.4f})')
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.show()
    
    # ROC
    fpr, tpr, _ = roc_curve(y_true, scores)
    auc = roc_auc_score(y_true, scores)
    
    plt.figure(figsize=(6,4))
    plt.plot(fpr, tpr)
    plt.plot([0,1],[0,1],'--')
    plt.title(f'ROC Curve (AUC={auc:.4f})')
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.show()

# Evaluate
print("TRAIN PERFORMANCE")
evaluate(y_train, train_scores)

print("TEST PERFORMANCE")
evaluate(y_test, test_scores)

# =========================================
# 10. PREDICTION (THRESHOLD)
# =========================================

# Choose threshold (top 1% anomalies)
threshold = np.percentile(train_scores, 99)

y_pred = (test_scores > threshold).astype(int)

# =========================================
# 11. RESULTS
# =========================================

from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# =========================================
# 12. VISUALIZATION
# =========================================

plt.figure(figsize=(8,5))
plt.hist(test_scores, bins=50)
plt.axvline(threshold, color='red', linestyle='--')
plt.title("Anomaly Score Distribution")
plt.show()

# Scatter (2 PCA components)
plt.figure(figsize=(6,5))
plt.scatter(X_test_reduced[:,0], X_test_reduced[:,1],
            c=y_pred, cmap='coolwarm', s=5)
plt.title("Detected Anomalies (Red)")
plt.show()

# =========================================
# 13. TOP ANOMALIES
# =========================================

results = pd.DataFrame({
    'score': test_scores,
    'actual': y_test.values
})

results = results.sort_values('score', ascending=False)

print("\nTop suspicious transactions:")
print(results.head(20))
```
