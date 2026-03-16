# Home-work: Application-Based Questions (OOP in Python)

## Question 1 – Student Management System

Create a **Python class `Student`** to manage student information.

The class should have the following features:

1. A **class variable** `school_name` set to `"CDAC : AI Learning Academy"`.
2. A **constructor (`__init__`)** that accepts:

   * student name
   * age
   * course
3. A method **`display_info()`** to display the student details:

   * Student Name
   * Age
   * Course
   * School Name
4. A method **`is_adult()`** that checks whether the student is an adult (age ≥ 18).

### Application Task

1. Create two student objects with different details.
2. Display their information.
3. Check whether each student is an adult.

---

# Question 2 – Bank Account System

Create a **Python class `BankAccount`** to simulate a basic banking system.

The class should include:

1. A **class variable** `bank_name = "Secure Bank"`.
2. A **constructor** that initializes:

   * account holder name
   * balance (default value = 0)
3. A method **`deposit(amount)`** that:

   * adds money to the account if the amount is positive.
4. A method **`withdraw(amount)`** that:

   * withdraws money if the balance is sufficient.
5. A method **`check_balance()`** that displays:

   * account holder name
   * bank name
   * current balance.

### Application Task

1. Create two bank account objects.
2. Perform the following operations:

   * deposit money
   * withdraw money
3. Display the final account balance.

---

# Question 3 – Product Inventory Management

Create a **Python class `Product`** for managing product inventory in a store.

The class should include:

1. A constructor that initializes:

   * product name
   * product price
   * product quantity
2. A method **`total_value()`** that returns the total value of the stock
   *(price × quantity)*.
3. A method **`restock(amount)`** to increase product quantity.
4. A method **`sell(amount)`** to reduce product quantity when items are sold.

### Application Task

1. Create a product object.
2. Perform the following operations:

   * sell some units
   * restock items
3. Display the total value of the remaining stock.

