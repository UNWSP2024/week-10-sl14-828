class Employee:
    # write a class employee that holds the following data about an employee in attributes:
    # name, ID number, department, and job title
    def __init__(self, name, id_number, department, job_title):
        # store the employee's name, ID number, department, and job title
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    # method to display the employee data
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print()  # print a blank line for spacing

# create three employee objects with given data
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# display the data for each employee
employee1.display_info()
employee2.display_info()
employee3.display_info()
