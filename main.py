from Customer import Customer
from Employee import Employee
from Food import Food
from Order import Order


def main():
    cst1 = Customer("Mc", "Lovin", "mclovin@gmail.com", 1200900080004000)
    print(cst1.id)
    cst1.customer_info()
    emp1 = Employee("Mike", "Tyson", "mt@gmail.com", 21000)
    print(emp1.id, emp1)
    food1 = Food("Fish", 15)
    food2 = Food("Fries", 6)
    print(Food.full_menu)
    ord1 = Order(cst1, [food1])
    ord1.order_info()
    # print(ord1.total_price)


if __name__ == "__main__":
    main()