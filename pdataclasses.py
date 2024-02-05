# from dataclasses import dataclass


# @dataclass
# class Person:
#     name: str
#     age: int
#     email: str


# man = Person(name="povilas", age=23, email="pdff")
# print(man, man.name, man.age, man.age == 23)

# -----------------------------------------------------------------------------------
# 1. you have been asked to create a simple inventory management system for
# a small retail store. You need to define a Product class using the dataclass
# module that represents a product in the store. Each Product should have a unique ID,
# a name, a description, a price, and a quantity in  stock. You also need to implement a method
# calculate_total_cost that calculates the total cost of
# a given number of items of the product, taking into account any discounts that may apply.


# from dataclasses import dataclass


# @dataclass
# class Product:
#     id: int
#     name: str
#     description: str
#     price: float
#     quantity: str

#     def calculate_total_cost(self, num_items: int) -> float:
#         if num_items <= 0:
#             return 0.0
#         elif num_items > self.quantity:
#             return self.quantity * self.price
#         else:
#             return num_items * self.price


# p = Product(1, "Apple", "A tasty fruit", 1.0, 10)


# total_cost = p.calculate_total_cost(5)
# print(total_cost)


# saruno pvz


# from dataclasses import dataclass

# @dataclass
# class Product:
#     ID: int
#     name: str
#     description: str
#     price: float
#     quantity: int

#     def calculate_total_cost(self, number_of_items: int, discount: float = None) -> float:
#             if discount:
#                  total_cost =number_of_items * self.price * (discount/100)
#             else:
#                 total_cost =number_of_items * self.price
#             return round(total_cost, 2)


# product = Product(ID=1, name="Headphones", description="Black, good quality", price=10.99, quantity=50)

# print(product.calculate_total_cost(number_of_items=3, discount=50))
# ----------------------------------------------------------------------------------

# # 2.Create a set of data classes to model an online bookstore management system.
# The classes should include Author, Book, Customer, and Order. Your goal is to design a system that
# enables the management of books, authors, customers, and orders in an online bookstore.

# Author Class:

# Attributes: author_id (int), name (str), birth_year (int), books (List[Book]).
# Initialize the attributes in the init method.
# Book Class:

# Attributes: book_id (int), title (str), author (Author), publication_year (int), price (float), quantity_in_stock (int).
# Initialize the attributes in the init method.
# Add a method sell that reduces the quantity_in_stock when a book is sold.
# Customer Class:

# Attributes: customer_id (int), name (str), email (str), orders (List[Order]).
# Initialize the attributes in the init method.
# Order Class:

# Attributes: order_id (int), customer (Customer), books (List[Book]), total_price (float), status (str) - either "Pending" or "Shipped".
# Initialize the attributes in the init method.
# Add a method calculate_total_price that calculates the total price of the order based on the books' prices and quantities.
# Add a method ship_order that changes the order status to "Shipped" and updates the stock quantity for each book.


# from dataclasses import dataclass
# from typing import List


# @dataclass
# class Author:
#     author_id: int
#     name: str
#     birth_year: int
#     books: List["Book"]

#     def __init__(self, author_id: int, name: str, birth_year: int, books: List["Book"]):
#         self.author_id = author_id
#         self.name = name
#         self.birth_year = birth_year
#         self.books = books


# @dataclass
# class Book:
#     book_id: int
#     title: str
#     author: Author
#     publication_year: int
#     price: float
#     quantity_in_stock: int

#     def __init__(
#         self,
#         book_id: int,
#         title: str,
#         author: Author,
#         publication_year: int,
#         price: float,
#         quantity_in_stock: int,
#     ):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.price = price
#         self.quantity_in_stock = quantity_in_stock

#     def sell(self, quantity_sold: int):
#         if quantity_sold > 0 and quantity_sold <= self.quantity_in_stock:
#             self.quantity_in_stock -= quantity_sold
#         else:
#             print("Invalid quantity or not enough stock to sell.")


# @dataclass
# class Customer:
#     customer_id: int
#     name: str
#     email: str
#     orders: List["Order"]

#     def __init__(self, customer_id: int, name: str, email: str, orders: List["Order"]):
#         self.customer_id = customer_id
#         self.name = name
#         self.email = email
#         self.orders = orders


# @dataclass
# class Order:
#     order_id: int
#     customer: Customer
#     books: List[Book]
#     total_price: float
#     status: str = "Pending"

#     def __init__(
#         self,
#         order_id: int,
#         customer: Customer,
#         books: List[Book],
#         total_price: float = 0.0,
#         status: str = "Pending",
#     ):
#         self.order_id = order_id
#         self.customer = customer
#         self.books = books
#         self.total_price = total_price
#         self.status = status

#     def calculate_total_price(self):
#         self.total_price = sum([book.price for book in self.books])
#         return self.total_price

#     def ship_order(self):
#         if self.status == "Pending":
#             self.status = "Shipped"
#             for book in self.books:
#                 book.sell(quantity_sold=1)
#         else:
#             print("Order has already been shipped.")


# author_1 = Author(author_id=1, name="Petras", birth_year=1986, books=[])
# author_2 = Author(author_id=2, name="Petras2", birth_year=1970, books=[])

# book_1 = Book(
#     book_id=1,
#     title="Pirats",
#     publication_year=2000,
#     price=30,
#     quantity_in_stock=9,
#     author=author_1,
# )
# book_2 = Book(
#     book_id=2,
#     title="Pirats2",
#     publication_year=2010,
#     price=15,
#     quantity_in_stock=3,
#     author=author_2,
# )

# customer_1 = Customer(customer_id=1, name="Povilas", email="ptpdff", orders=[])

# order_1 = Order(
#     order_id=1, customer=customer_1, books=[book_1], total_price=0.0, status="Pending"
# )
# print(order_1.calculate_total_price())
# order_1.ship_order()

# print(book_1.quantity_in_stock)


# ------------------------------------------------------------------------------------
# 3.You need to create a program to manage a list of books in a library. Each book has a title, an author,
# a publication year, and an ISBN.
# You need to define a Book class using the dataclass module that contains attributes
# for these properties. You also need to implement a Library class that manages a list of books. The Library class should
# allow you to add and remove books from the library, search for
# books by title or author, and display the list of books currently in the library.


# from dataclasses import dataclass, field
# from typing import List


# @dataclass
# class Book:
#     title: str
#     author: str
#     publication_year: int
#     isbn: str


# @dataclass
# class Library:
#     books: List[Book] = field(default_factory=list)

#     def add_book(self, book: Book):
#         self.books.append(book)
#         print(f"Book '{book.title}' added to the library.")

#     def remove_book(self, isbn: str):
#         for book in self.books:
#             if book.isbn == isbn:
#                 self.books.remove(book)
#                 print(f"Book '{book.title}' removed from the library.")
#                 return
#         print(f"Book with ISBN '{isbn}' not found in the library.")

#     def search_by_title(self, title: str):
#         matching_books = [
#             book for book in self.books if book.title.lower() == title.lower()
#         ]
#         if matching_books:
#             self.display_books(matching_books)
#         else:
#             print(f"No books found with title '{title}'.")

#     def search_by_author(self, author: str):
#         matching_books = [
#             book for book in self.books if book.author.lower() == author.lower()
#         ]
#         if matching_books:
#             self.display_books(matching_books)
#         else:
#             print(f"No books found by author '{author}'.")

#     def display_books(self, book_list: List[Book] = None):
#         books_to_display = book_list if book_list else self.books
#         if books_to_display:
#             print("Books in the library:")
#             for book in books_to_display:
#                 print(
#                     f"{book.title} by {book.author} ({book.publication_year}), ISBN: {book.isbn}"
#                 )
#         else:
#             print("No books in the library.")


# book1 = Book("Titanic", "J.D.", 1951, "978")
# book2 = Book("Kill", "Harper", 1960, "999")

# library = Library()
# library.add_book(book1)
# library.add_book(book2)

# library.display_books()

# library.search_by_title("Kill")
# library.search_by_author("J.D.")

# library.remove_book("978")

# library.display_books()


# pvz Alberto


# from dataclasses import dataclass
# from typing import List, Optional


# @dataclass
# class Book:
#     title: str
#     author: str
#     publication_year: int
#     ISBN: str


# class Library:
#     BOOKS = []

#     def add_book(self, book) -> None:
#         self.BOOKS.append(book)

#     def search_book(self, search_attribute: str) -> Optional["Book"]:
#         for book in self.BOOKS:
#             if search_attribute == book.title or search_attribute == book.author:
#                 return book
#             return

#     def display_books(self) -> str:
#         print("Books in library:")
#         for book in self.BOOKS:
#             print(book)

#     def remove_book(self, book_title: str) -> None:
#         for book in self.BOOKS:
#             if book_title == book.title:
#                 self.BOOKS.remove(book)


# book_1 = Book(
#     title="Don Quixote",
#     author="Miguel de Cervantes",
#     publication_year=2015,
#     ISBN="515 51 65 18 ",
# )

# book_2 = Book(
#     title="A Tale of Two Cities",
#     author="Charles Dickens",
#     publication_year=1869,
#     ISBN="5342 421 61 18 ",
# )

# library = Library()

# library.add_book(book_1)
# library.add_book(book_2)

# print(library.search_book("Don Quixote"))
# library.display_books()

# library.remove_book("Don Quixote")

# library.display_books()

# ---------------------------------------------------------------------


# 4.You are tasked with designing an advanced Employee Management System using Python data classes,
# functional programming operations, and various methods for analysis and manipulation of employee data.

# Employee Class:

# Create a data class named Employee to represent an employee. The class should have attributes for employee_id, name, age, salary, and department.

# Implement an __init__ method to initialize the attributes.
# Department Class: Create a data class named Department to represent a department.
# The class should have attributes for department_id, name, and employe (List[Employee]).

# Implement an init method to initialize the attributes.
# Add a method named average_salary that calculates and returns the average salary of employees in the department.
# EmployeeManagement Class: Create a data class named EmployeeManagement to manage multiple departments and employees.
# The class should have an attribute for departments (List[Department]).

# Implement an init method to initialize the attribute.
# Add a method named total_salary that calculates and returns the total salary of all employees in the organization.
# Add a method named get_employees_in_age_range that takes a minimum and maximum age and returns a list of employees within that age range.
# Add a method named sort_employees_by_salary that returns a sorted list of employees by their salary in descending order.
# Add a method named filter_employees_by_department that takes a department name and returns a list of employees in that department.
# Functional Operations:

# Utilize functional programming operations such as map, filter, and sorted where appropriate in
# the implementation of the methods. Demonstrate the use of these operations to enhance the readability and efficiency of your code.

# Test Cases:

# Create a sample dataset with multiple employees and departments to thoroughly test your system.
# Use the implemented methods to perform various analyses,
# such as calculating average salaries, sorting employees, and filtering employees by criteria.


# from dataclasses import dataclass
# from typing import List, Optional


# @dataclass
# class Employee:
#     employee_id: int
#     name: str
#     age: int
#     salary: float
#     department: str


# @dataclass
# class Department:
#     department_id: int
#     name: str
#     employees: List[Employee]

#     def __init__(self, department_id: int, name: str, employees: List[Employee] = None):
#         self.department_id = department_id
#         self.name = name
#         self.employees = employees if employees is not None else []

#     def add_employee(self, employee: Employee):
#         self.employees.append(employee)

#     def average_salary(self):
#         if not self.employees:
#             return 0
#         total_salary = sum(map(lambda emp: emp.salary, self.employees))
#         return total_salary / len(self.employees)


# @dataclass
# class EmployeeManagement:
#     departments: List[Department]

#     def __init__(self, departments: List[Department] = None):
#         self.departments = departments if departments is not None else []

#     def total_salary(self):
#         return sum(
#             map(
#                 lambda dept: sum(map(lambda emp: emp.salary, dept.employees)),
#                 self.departments,
#             )
#         )

#     def get_employees_in_age_range(self, min_age: int, max_age: int):
#         return [
#             employee
#             for department in self.departments
#             for employee in department.employees
#             if min_age <= employee.age <= max_age
#         ]

#     def sort_employees_by_salary(self):
#         return sorted(
#             [
#                 employee
#                 for department in self.departments
#                 for employee in department.employees
#             ],
#             key=lambda x: x.salary,
#             reverse=True,
#         )

#     # def filter_employees_by_department(self, department_name: str):
#     #     return [
#     #         employee
#     #         for department in filter(
#     #             lambda dept: dept.name == department_name, self.departments
#     #         )
#     #         for employee in department.employees
#     #     ]


# # Sample dataset
# employee1 = Employee(
#     employee_id=1, name="John Doe", age=30, salary=5000, department="HR"
# )
# employee2 = Employee(
#     employee_id=2, name="Jane Smith", age=25, salary=6000, department="HR"
# )
# employee3 = Employee(
#     employee_id=3, name="Bob Johnson", age=35, salary=7500, department="IT"
# )
# employee4 = Employee(
#     employee_id=4, name="Alice Brown", age=28, salary=7000, department="IT"
# )

# hr_department = Department(
#     department_id=101, name="Human Resources", employees=[employee1, employee2]
# )
# it_department = Department(
#     department_id=102, name="Information Technology", employees=[employee3, employee4]
# )

# employee_management = EmployeeManagement(departments=[hr_department, it_department])

# # Test cases
# print(f"Total salary in the organization: ${employee_management.total_salary():,.2f}")

# age_range_employees = employee_management.get_employees_in_age_range(
#     min_age=25, max_age=35
# )
# print("Employees in the age range 25 to 35:")
# for employee in age_range_employees:
#     print(f"Employee {employee.name}, Age: {employee.age}")

# sorted_employees = employee_management.sort_employees_by_salary()
# print("Sorted employees by salary in descending order:")
# for employee in sorted_employees:
#     print(f"Employee {employee.name}, Salary: ${employee.salary:,.2f}")

# filtered_employees = employee_management.filter_employees_by_department(
#     department_name="HR"
# )
# print("Employees in the HR Department:")
# for employee in filtered_employees:
#     print(f"Employee {employee.name}, Department: {employee.department}")


# pvz is Sauliaus


# from dataclasses import dataclass, field
# from typing import List


# @dataclass
# class Employee:
#     employee_id: int
#     name: str
#     age: int
#     salary: float
#     department: str


# @dataclass
# class Department:
#     department_id: int
#     name: str
#     employees: List["Employee"] = field(default_factory=list)

#     def add_employee(self, employee: "Employee") -> None:
#         self.employees.append(employee)


# class EmployeeManagement:
#     def __init__(self, departments: List["Department"]) -> None:
#         self.departments = departments

#     def total_salary(self) -> float:
#         return sum(
#             [
#                 employee.salary
#                 for department in self.departments
#                 for employee in department.employees
#             ]
#         )

#     def get_employees_in_age_range(self, start_range: int, end_range: int) -> list:
#         return [
#             employee.name
#             for department in self.departments
#             for employee in department.employees
#             if employee.age in range(start_range, end_range + 1)
#         ]

#     def sort_employees_by_salary(self) -> None:
#         all_employees = [
#             employee
#             for department in self.departments
#             for employee in department.employees
#         ]
#         sorted_employees = sorted(all_employees, key=lambda x: x.salary)

#         for employee in sorted_employees:
#             print(f"Name: {employee.name}, salary: {employee.salary} ")

#     def filter_employees_by_department(self, department_name: str) -> None:
#         all_employees = [
#             employee
#             for department in self.departments
#             for employee in department.employees
#             if employee.department == department_name
#         ]
#         for employee in all_employees:
#             print(f"Name: {employee.name}, department: {employee.department} ")


# employee_1 = Employee(
#     employee_id=1, name="Employee-1", age=25, salary=1700.0, department="Administraton"
# )
# employee_2 = Employee(
#     employee_id=2, name="Employee-2", age=36, salary=1600.0, department="Administraton"
# )
# employee_3 = Employee(
#     employee_id=3, name="Employee-3", age=45, salary=1500.0, department="Poduction"
# )
# employee_4 = Employee(
#     employee_id=4, name="Employee-4", age=61, salary=1800.0, department="Poduction"
# )

# department_1 = Department(department_id=1, name="Administraton")
# department_2 = Department(department_id=2, name="Poduction")

# department_1.add_employee(employee_1)
# department_1.add_employee(employee_2)
# department_2.add_employee(employee_3)
# department_2.add_employee(employee_4)

# employee_management = EmployeeManagement(departments=[department_1, department_2])

# print("Total salary")
# print(employee_management.total_salary(), "\n")

# print("Employee in range:")
# for name in employee_management.get_employees_in_age_range(
#     start_range=36, end_range=45
# ):
#     print(name)
# print("\n")

# print("Employee sorted by salary:")
# employee_management.sort_employees_by_salary()
# print("\n")
# print("Employee filtered by department:")
# employee_management.filter_employees_by_department(department_name="Poduction")

# -------------------------------------------------------------------------------------------------------


# 5.Create a flight ticketing mini system:

# The CLI should ask you to choose departure place and destination (minimum 5 cities)
# (Use dictionary to create a distance between the cities matrix map ).
# Then it should show options for at least 3 flight options with different different aircraft
# (Airbus A330-300, A340-300,A 340-600, A350- 100, Boeing 747-400, 747-800, 777-300).
# Every aircraft has different seat configuration (economy, business,
#  first with different seat amount, seat pitch and average price)
# When you select the ticket (the provided option) the final cost should be calculated depending on aircraft type,
# departure time, and fuel consumption. (We can agree that flights that are departure earlier, has less seats and older, cost more).
# Use data classes and simple classes to achieve the result.


from dataclasses import dataclass
from typing import Dict


@dataclass
class City:
    name: str
    airport_code: str


@dataclass
class Aircraft:
    name: str
    seat_configuration: Dict[str, int]
    seat_pitch: int
    fuel_consumption: float
    average_price: float


@dataclass
class FlightOption:
    aircraft: Aircraft
    departure_time: str
    available_seats: int


class FlightTicketingSystem:
    def __init__(self):
        self.cities = {
            "New York": City("New York", "NYC"),
            "Los Angeles": City("Los Angeles", "LAX"),
            "Chicago": City("Chicago", "ORD"),
            "Miami": City("Miami", "MIA"),
            "Dallas": City("Dallas", "DFW"),
        }

        self.aircrafts = {
            "Airbus A330-300": Aircraft(
                "Airbus A330-300",
                {"Economy": 450, "Business": 30, "First": 20},
                seat_pitch=32,
                fuel_consumption=12.5,
                average_price=500,
            ),
            "Airbus A340-300": Aircraft(
                "Airbus A340-300",
                {"Economy": 430, "Business": 45, "First": 25},
                seat_pitch=34,
                fuel_consumption=13.0,
                average_price=550,
            ),
            # Add more aircraft types here
        }

        self.flight_options = {
            "Option 1": FlightOption(self.aircrafts["Airbus A330-300"], "08:00", 500),
            "Option 2": FlightOption(self.aircrafts["Airbus A340-300"], "10:30", 550),
            # Add more flight options here
        }

    def calculate_final_cost(self, selected_option):
        aircraft = selected_option.aircraft
        base_price = aircraft.average_price
        fuel_cost = aircraft.fuel_consumption * (
            24 - int(selected_option.departure_time.split(":")[0])
        )
        time_factor = 1.2  # Cost factor for earlier departures

        final_cost = base_price + fuel_cost * time_factor
        return final_cost

    def run(self):
        print("Welcome to the Flight Ticketing System!")

        print("\nSelect Departure City:")
        for i, city in enumerate(self.cities.values(), 1):
            print(f"{i}. {city.name}")

        departure_choice = int(input("Enter the number of your choice: "))
        departure_city = list(self.cities.values())[departure_choice - 1]

        print("\nSelect Destination City:")
        for i, city in enumerate(self.cities.values(), 1):
            if city != departure_city:
                print(f"{i}. {city.name}")

        destination_choice = int(input("Enter the number of your choice: "))
        destination_city = list(self.cities.values())[destination_choice - 1]

        print(
            f"\nFlight options from {departure_city.name} to {destination_city.name}:\n"
        )
        for i, (option_name, flight_option) in enumerate(
            self.flight_options.items(), 1
        ):
            print(
                f"{i}. {option_name} - Aircraft: {flight_option.aircraft.name}, Departure Time: {flight_option.departure_time}, Available Seats: {flight_option.available_seats}"
            )

        selected_option_number = int(
            input("Enter the number of your selected flight option: ")
        )
        selected_option = list(self.flight_options.values())[selected_option_number - 1]

        final_cost = self.calculate_final_cost(selected_option)

        print(
            f"\nYou have selected {selected_option.aircraft.name} departing at {selected_option.departure_time}."
        )
        print(f"The final cost for your ticket is: ${final_cost}")


if __name__ == "__main__":
    flight_system = FlightTicketingSystem()
    flight_system.run()
