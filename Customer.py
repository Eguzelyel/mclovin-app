from Person import Person


class Customer(Person):

    def __init__(self, first, last, email, credit_card=None):
        super().__init__(first, last, email)
        self.credit_card = credit_card

    def display_info(self):
        print("Name: {}\nEmail: {}\nCard: {}", self.full_name, self.email, self.credit_card)

    def add_credit_card(self, credit_card):
        # Takes card number as String. Only 1 card at a time.
        if self.credit_card is None:
            self.credit_card = credit_card

    def delete_credit_card(self):
        self.credit_card = None


cst1 = Customer("Mc", "Lovin", "mclovin@gmail.com", 12345)
print(cst1)
