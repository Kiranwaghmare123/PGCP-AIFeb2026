# Homework:

# Encapsulation 

### **Q1. Bank Account System**

Design a class `BankAccount` with the following:

* Private attributes: `accountNumber`, `balance`
* Public methods:

  * `deposit(amount)`
  * `withdraw(amount)`
  * `getBalance()`

**Requirements:**

* Balance should not be directly accessible
* Withdrawal should not allow negative balance
* Deposit should reject negative values

 *Question:*
Explain how encapsulation is achieved and write the class implementation.

---

### **Q2. Student Result System**

Create a class `Student` with:

* Private attributes: `marks`
* Public methods:

  * `setMarks(m)`
  * `getGrade()`

**Conditions:**

* Marks must be between 0–100
* Grade calculation:

  * A (≥ 80), B (≥ 60), C (≥ 40), Fail (< 40)

 *Question:*
Why should `marks` be private? Implement validation using encapsulation.

---

# Abstraction 

### **Q3. Payment System**

Design an abstract class `Payment` with:

* Abstract method: `pay(amount)`

Create subclasses:

* `CreditCardPayment`
* `UPIPayment`

 *Question:*
Implement the system such that user can choose payment type without knowing internal logic.
Explain how abstraction is used.

---

### **Q4. Shape Area Calculator**

Create an abstract class `Shape` with:

* Abstract method `area()`

Subclasses:

* `Circle`
* `Rectangle`

 *Question:*
Take inputs and calculate area using abstraction.
Why is `Shape` made abstract?

---

#  Inheritance 

### **Q5. Employee Hierarchy**

Create:

* Base class: `Employee` → `id`, `name`
* Derived classes:

  * `Manager` → `bonus`
  * `Developer` → `programming_language`

 *Question:*
Write code to demonstrate inheritance and show how common properties are reused.

---

### **Q6. Vehicle System**

Create:

* Base class: `Vehicle` → `speed`, `fuel_type`
* Derived classes:

  * `Car`
  * `Bike`

 *Question:*
Show how inheritance reduces redundancy and allows extension.

---

#  Method Overriding with Inheritance 

### **Q7. Salary Calculation**

Base class: `Employee`

* Method: `calculateSalary()`

Derived classes:

* `FullTimeEmployee`
* `PartTimeEmployee`

 *Question:*
Override `calculateSalary()` differently for both classes and demonstrate runtime polymorphism.

---

### **Q8. Notification System**

Base class: `Notification`

* Method: `send()`

Derived classes:

* `EmailNotification`
* `SMSNotification`

 *Question:*
Override the `send()` method in each subclass.
Call method using base class reference and explain output.

---
