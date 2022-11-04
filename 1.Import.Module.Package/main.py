from application.salary import calculate_salary
from application.db.people import get_employees
from _datetime import datetime
from dirty_main import *


def main():
    calculate_salary()
    get_employees()
    print(datetime.now())
    second()


if __name__ == '__main__':
    main()