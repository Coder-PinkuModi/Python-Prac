# here we are going to play with @property decorator and will see how getter, setter and deleter work

import time # with this module we are going to make time delay happens...
import uuid # this is for generating unique id, we have to just call it in syntactically correct way

class Employee:
    
    total_employees = 0  # Class-level attribute
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self._id = None  # Private attribute for the unique ID
        Employee.total_employees += 1

    @property
    def id(self):  # Getter for id
        print("Getting your unique id...")
        time.sleep(1)
        if self._id is None:
            return "ID is not set yet!"
        return self._id

    @id.setter
    def id(self, value):  # Setter for id
        print("Setting your unique id...")
        time.sleep(2)
        self._id = value or str(uuid.uuid4())
        print("Congo! Your unique id has been set.😀")

    @id.deleter
    def id(self):  # Deleter for id
        print("Deleting your unique id...")
        time.sleep(2)
        self._id = None
        print("Your unique ID has been deleted.😶")

    def delete_object(self):  # Regular method for deleting the object
        print("Deleting your object...")
        time.sleep(2)
        print(f"Good Bye! {self.name}, you are no longer with us.😶")
        Employee.total_employees -= 1
        del self

# Example Usage
emp1 = Employee("Alice", 30, 50000)

# Accessing id (getter)
print(emp1.id)  # Output: Getting your unique id... ID is not set yet!

# Setting id (setter)
emp1.id = None  # Output: Setting your unique id... Congratz!

# Accessing id again
print(emp1.id)  # Output: Getting your unique id... <Generated UUID>

# Deleting id (deleter)
del emp1.id  # Output: Deleting your unique id... Your unique ID has been deleted.

# Deleting the object
emp1.delete_object()  # Output: Deleting your object... Goodbye!
