class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not sufficient balance......")
    
    return balance - amount

try:
    balance = withdraw(3000,5000)
    
except InsufficientBalanceError as e:
    print("Custom Exception is defined...............", e)
