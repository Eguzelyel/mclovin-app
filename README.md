# mclovin-app
McLovin Fastfood Chain App with Speech Recognition 

<img src="mclovin_logo.png" width=75%>

[comment]: <> (![]&#40;mclovin_logo.png&#41;)

### Steps to Tackle This Project:
1. Create an object-oriented program design that receives an order in plain test. Implement with basic classes. (In Progress)
2. Create a database and connect the system.
3. Create a speech recognition for the orders. (Sounds familiar).
	a. Idea: Use Speech-to-text and train a BERT model, just to spice things up.
4. Adda a recommendation system to suggest what "you may also like" based on previous orders.

### System Functionality and Requirements:

Customer orders a menu or food.
* Customer shall order a custom food.
* Customer shall order a menu
* System shall not allow order if food is not in stock (Inspired by broken ice cream machine)

Employee sees the order, prepares it.
* Employee shall mark the order as completed.

Cashier gives the food when ready, accepts the payment.
* Customer payment info shall be saved when account is created. (In this case, when Customer object created.)
* Food shall be ready before given to customer.

Employee can get raise, updates stock and menu (food list).

Customer can update their information (name, card).

### Tables:
Person-> Customer, Employee

Food

Order
