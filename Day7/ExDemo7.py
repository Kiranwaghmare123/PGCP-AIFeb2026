try:
    n = 100 /0
    print("try")
except Exception as e:
    print("except",e)
else:
    print("else")
finally:
    print("finally")
    