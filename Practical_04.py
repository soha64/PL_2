#10/02/2026

class library:

    def __init__(self, book_name , author):

        self.book_name = book_name
        self.author = author
        self.available = True

    def checkout_book(self):
        if self.available:
            self.available = False
            print(f"You have checked out '{self.book_name}' by {self.author}.")
        else:
            print(f"Sorry, '{self.book_name}' is currently unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.book_name}' by {self.author}.")
        else:
            print(f"'{self.book_name}' was not checked out.")

    def display(self):
        status = "Available" if self.available else "Checked Out"
        print(f"Book: '{self.book_name}' by {self.author} - Status: {status}")


book1 = library("XXX", "YYY")
book1.display() 
book1.checkout_book()
book1.display()
book1.return_book()
book1.display() 






class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class employee(person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary}")

class manager(employee, person):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager_info(self):
        print(f"Department: {self.department}")

    def approve_leave(self):
        print(f"{self.name} has approved the leave request.")

manager1 = manager("Alice", 35, "M001", 75000, "HR")
manager1.display_manager_info()
manager1.approve_leave()

