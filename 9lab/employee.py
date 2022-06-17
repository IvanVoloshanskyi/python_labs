class Worker:
    def __init__(self, name: str, age: int, type_of_work: str, experience_in_years: float, salary: float):
        self.age = age
        self.name = name
        self.experience_in_years = experience_in_years
        self.type_of_work = type_of_work
        self.salary = salary

    def __str__(self):
        return f'Name: {self.name} \n' \
               f'Age: {self.age} \n' \
               f'Work: {self.type_of_work} \n' \
               f'Experience at this work: {self.experience_in_years} years \n' \
               f'Salary: {self.salary} UAH\n' \

