from employee import Worker


class WorkingMan(Worker):
    def __init__(self, name: str, age: int, type_of_work: str, experience_in_years: float, salary: float
                 , working_hours_per_month: int):
        super().__init__(name, age, type_of_work, experience_in_years, salary)
        self.__working_hours_per_month = working_hours_per_month

    def __str__(self):
        return f'Name: {self.name} \n' \
               f'Age: {self.age} \n' \
               f'Work: {self.type_of_work} \n' \
               f'Experience at this work: {self.experience_in_years} years \n' \
               f'Salary: {self.salary} UAH\n' \
               f'{self.name.title()} works {self.__working_hours_per_month} hours per month'
