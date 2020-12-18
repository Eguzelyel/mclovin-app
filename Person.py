class Person:

    person_id = 0

    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
        self.id = Person.person_id

        Person.person_id += 1

    @property
    def full_name(self):
        # Automatically set full name from first and last
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        # Change first, last using full name
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None

    @classmethod
    def from_string(cls, text):
        # Create a user from a text "First, Last, email"
        first, last, email = text.split(", ")
        return cls(first, last, email)

    def __str__(self):
        return self.full_name


per1 = Person("Person", "One", "personone@gmail.com")
print(per1)
