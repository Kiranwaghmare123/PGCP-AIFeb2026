## Dataset

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
