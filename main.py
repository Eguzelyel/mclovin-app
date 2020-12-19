from Customer import Customer
from Employee import Employee
from Food import Food
from Order import Order

cst1 = Customer("Mc", "Lovin", "mclovin@gmail.com", 1200900080004000)
print(cst1.id)
cst1.display_info()
emp1 = Employee("Mike", "Tyson", "mt@gmail.com", 21000)
print(emp1.id, emp1)
food1 = Food("Fish", 15)
food2 = Food("Fries", 6)
print(Food.full_menu)
ord1 = Order(cst1, [food1])
print(ord1.total_price)