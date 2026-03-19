def divide(a,b):
    try:
        return a/b
    except ValueError as e:
        raise ValueError("Cannot divide by zer, aisa kon karta hai !") from e
        
    except TypeError as e:
        raise TypeError("Cannot divide by zer, aisa kon karta hai !") from e

divide(10,"a")