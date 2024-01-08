class Department:
    def __init__(self):
        self._depid = 0
        self._depname = ""

    def set_department(self):
        self._depid = input("Enter Department id: ")
        self._depname = input("Enter Department name: ")

    def display_dep(self):
        print("Department ID: ", self._depid)
        print("Department name: ", self._depname)


class Employee(Department):
    def __init__(self):
        super().__init__()
        self.__empid = 0
        self.__empname = ""

    def set_employee(self):
        self.__empid = input("Enter Employee ID: ")
        self.__empname = input("Enter Employee name: ")
        super().set_department()

    def display_emp(self):
        print("Employee ID: ", self.__empid)
        print("Employee name: ", self.__empname)
        super().display_dep()

