Project: Movie Recommendation System

## 1. Dataset

Use the **MovieLens dataset** (widely used in real systems).

### Download:

* Go to: [https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/)
* Download: **ml-latest-small**

### Files used:

* `ratings.csv` → user ratings
* `movies.csv` → movie names

---

## 2. Project Structure

```
recommender-project/
│── app.py
│── model.py
│── data/
│    ├── ratings.csv
│    ├── movies.csv
```

---

## 3. Model (model.py)

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
ratings = pd.read_csv("data/ratings.csv")
movies = pd.read_csv("data/movies.csv")

# Create user-item matrix
user_item = ratings.pivot(index="userId", columns="movieId", values="rating").fillna(0)

# Compute similarity between users
user_similarity = cosine_similarity(user_item)

# Convert to DataFrame
sim_df = pd.DataFrame(user_similarity, index=user_item.index, columns=user_item.index)

def recommend_movies(user_id, top_n=5):
    similar_users = sim_df[user_id].sort_values(ascending=False)[1:6]

    weighted_scores = {}
    sim_sums = {}

    for other_user, sim in similar_users.items():
        user_ratings = user_item.loc[other_user]

        for movie_id, rating in user_ratings.items():
            if rating > 0:
                weighted_scores[movie_id] = weighted_scores.get(movie_id, 0) + sim * rating
                sim_sums[movie_id] = sim_sums.get(movie_id, 0) + abs(sim)

    predictions = {m: weighted_scores[m]/sim_sums[m] for m in weighted_scores if sim_sums[m] != 0}

    # Sort and get top movies
    recommended = sorted(predictions.items(), key=lambda x: x[1], reverse=True)

    movie_ids = [m[0] for m in recommended[:top_n]]

    return movies[movies["movieId"].isin(movie_ids)][["title"]]
```

---

## 4. UI (app.py using Streamlit)

```python
import streamlit as st
from model import recommend_movies

st.title("🎬 Movie Recommendation System")

user_id = st.number_input("Enter User ID (1–600)", min_value=1, max_value=600, step=1)

if st.button("Get Recommendations"):
    results = recommend_movies(user_id)

    st.subheader("Recommended Movies:")
    for i, row in results.iterrows():
        st.write(f"👉 {row['title']}")
```

---

## 5. Run the Project

### Install dependencies:

```bash
pip install pandas scikit-learn streamlit
```

### Run app:

```bash
streamlit run app.py
```
