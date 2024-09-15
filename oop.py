# # Inheritance

# class Parent:

#     def __init__(self) -> None:
#         self.speaks = ["English"]

# class Child(Parent):

#     def __init__(self) -> None:
#         super().__init__()
#         self.speaks.append("German")

# child1 = Child()
# parent1 = Parent()

# print(child1.speaks)
# print(parent1.speaks)

# class BaseEntity:

#     def __init__(self, name, code, is_active=True) -> None:
#         self.name = name
#         self.code = code
#         self.is_active = is_active

#     def display_info(self):

#         status = "Inactive"
#         if self.is_active:
#             status = "Active"

#         print(f"{self.name}, {self.code}, {self.is_active}, {status}")

# class Student(BaseEntity):

#     def __init__(self, grade, name, code, is_active=True) -> None:

#         super().__init__(name, code, is_active)
#         self.grade = grade
    
#     def display_info(self):

#         super().display_info()
#         print(f"{self.grade}")

# class Teacher(BaseEntity):

#     def __init__(self, department, name, code, is_active=True) -> None:
#         super().__init__(name, code, is_active)
#         self.department = department
    
#     def display_info(self):
#         super().display_info()
#         print(f"{self.department}")



# student = Student(grade="2", name="John Doe", code = "1000" )
# teacher = Teacher("Mathematics", "Test Test", code = "2000")
# student.display_info()
# teacher.display_info()

### -------------------------------#####

# # Encapsulation

# class BankAccount:
#     def __init__(self, account_number, account_holder, initial_balance) -> None:
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.__balance = initial_balance
    
#     def display_info(self):
#         print(f"Account Number: {self.account_number}")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: {self.__balance}")

#     def get_balance(self):
#         return self.__balance


# bankAccount = BankAccount("12345", "Ayse", 500)

# print(bankAccount.get_balance())

### -------------------------------#####

# # Abstraction 
# from abc import ABC, abstractmethod


# class PaymentProcessor(ABC):

#     @abstractmethod
#     def process_payment(self, amount):
#         pass

# class CreditCardPayment(PaymentProcessor):

#     def process_payment(self, amount):
#         # bankanın servisine bağlanıldı, kullanıcının hesabından para çekiliyor
#         print(f"Kredi kartından {amount} miktarda ödeme gerçekleştiriliyor...")


# class PaypalPayment(PaymentProcessor):
        
#     def process_payment(self, amount):
#         # paypal servisine bağlanıldı, kullanıcının hesabından para çekiliyor
#         print(f"Paypaldan {amount} miktarda ödeme gerçekleştiriliyor...")


# def make_payment(processor: PaymentProcessor, amount):
#     processor.process_payment(amount)

# credit_card = CreditCardPayment()

# make_payment(credit_card, 100)

# class User:
#     def __init__(self, name, surname, email, password, address, phone, role, created_at, updated_at) -> None:
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.password = password
#         self.address = address
#         self.phone = phone
#         self.role = role
#         self.created_at = created_at
#         self.updated_at = updated_at


# class UserDto:
#     def __init__(self, name, email, role) -> None:
#         self.name = name
#         self.email = email
#         self.role = role
    
# def getUserInfo(user):
#     return UserDto(name=user.name, email=user.email, role=user.role)

# user = User(
#     name = "John",
#     surname="Doe",
#     email= "johndoe@gmail.com",
#     password="1234",
#     address="Istanbul",
#     phone="1234567890",
#     role="manager",
#     created_at="2024-08-28",
#     updated_at="2024-08-28")

# user_dto = getUserInfo(user)

# print(user_dto.name, user_dto.email, user_dto.role)

### -------------------------------#####

# class Animal:
#     def make_sound(self):
#         raise NotImplementedError("You must implement this method")

# class Dog(Animal):
#     def make_sound(self):
#         return "Hav!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Miyav!"
    
# SOLID
# Single Responsibility 
# Open Closed
# Liskov Substitution
# Interface Segregation 
# Dependcy Injection

# AddOrUpdateDto
# Person -> email
