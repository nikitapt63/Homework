class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class WorkerMixin:
    def work(self):
        return f"{self.name} {self.surname} cooking"

    def get_salary(self):
        return f"{self.name} {self.surname} got money)))"


class Employee(Human, WorkerMixin):
    def __init__(self, name, surname, profession):
        Human.__init__(self, name, surname)
        self.profession = profession

print("Hello, world!")
