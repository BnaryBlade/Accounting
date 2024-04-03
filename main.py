import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print("Текущая дата:", datetime.datetime.now())
    print("Вызываем функцию calculate_salary:")
    calculate_salary()
    print("Вызываем функцию get_employees:")
    get_employees()
