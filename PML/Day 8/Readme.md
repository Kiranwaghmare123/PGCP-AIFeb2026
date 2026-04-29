## Dataset

## Ex 0
    #First feature
    weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
    'Rainy','Sunny','Overcast','Overcast','Rainy']
    #Second Feature
    temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
    
    #Label
    play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

## Ex 1

    emails = [
        "free money now",              # spam
        "win a lottery prize",        # spam
        "claim your free offer",      # spam
        "meeting scheduled tomorrow",  # ham
        "project discussion today",    # ham
        "let's have lunch tomorrow",   # ham
        "win free cash prize",         # spam
        "team meeting agenda",         # ham
    ]
    
    labels = [1, 1, 1, 0, 0, 0, 1, 0]

  ## Ex 2

      reviews = [
        "I loved this movie, it was fantastic and amazing",
        "terrible movie, I hated it",
        "best film ever, great acting",
        "worst movie, waste of time",
        "absolutely wonderful experience, I liked it",
        "bad film, very boring and dull",
        "great storyline and excellent performance",
        "horrible acting and bad script",
        "I enjoyed the movie a lot",
        "not good, very disappointing"
    ]
    
    # Labels: 1 = Positive, 0 = Negative
    labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
## Daily, Interview Questions
1. What is the Naive Bayes algorithm, and why is it called “naive”?
2. Explain Bayes’ Theorem and how it is used in classification.
3. What are the assumptions made by Naive Bayes?
4. Why does Naive Bayes perform well despite the independence assumption being unrealistic?
5. What is the difference between prior, likelihood, and posterior probabilities?
6. What are the different types of Naive Bayes classifiers?
   * Gaussian Naive Bayes
   * Multinomial Naive Bayes
   * Bernoulli Naive Bayes
7. When would you use:
8. Gaussian NB vs Multinomial NB?
9. How does Gaussian Naive Bayes handle continuous data?
10. What distribution assumption is made in Gaussian NB?
11. Why is Naive Bayes commonly used in text classification?
12. How is it applied in spam filtering?
13. What is the role of word frequency in Multinomial Naive Bayes?
14. How does Naive Bayes handle high-dimensional data?
15. Can Naive Bayes be used for real-time prediction? Why?
