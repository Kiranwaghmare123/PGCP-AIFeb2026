try:
    x = int ("abc")
    print(x)

except ValueError as e:
    raise TypeError("Conversion is not correct !") from e
   
    
