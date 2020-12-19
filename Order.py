class Order:

    order_id=0

    # When the customer gives an order, ideally, the cust_id, food_id, price
    # get stored. Storing full objects for now.
    def __init__(self, cust_obj, food_objs=None):
        self.cust = cust_obj
        self.food = food_objs
        self.ready = False
        self.id = Order.order_id

        Order.order_id += 1

    def mark_ready(self):
        self.ready = True

    @property
    def total_price(self):
        return sum([food.price for food in self.food])
