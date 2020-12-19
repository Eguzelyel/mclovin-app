from Person import Person


class Employee(Person):

    salary_raise = 1.03

    def __init__(self, first, last, email, salary):
        super().__init__(first, last, email)
        self.salary = salary

    def apply_raise(self):
        self.salary = self.salary*Employee.salary_raise

    @classmethod
    def set_salary_raise(cls, rate):
        cls.salary_raise = rate

    @classmethod
    def from_string(cls, text):
        # Create an employee from a text "First, Last, email, salary"
        first, last, email, salary = text.split(", ")
        return cls(first, last, email, salary)

    @staticmethod
    def mark_ready(order):
        order.mark_ready()
