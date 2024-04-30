import employee_info as e
def test_calculate_average_salary():
    assert (e.calculate_average_salary() == 60166.67)

def test_get_employees_by_age_range():
    upp_age = 33
    low_age = 24
    ans = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
]
    assert(e.get_employees_by_age_range(low_age, upp_age) == ans)

def test_get_employees_by_dept():
    test_dept = "Sales"
    ans = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]
    assert(e.get_employees_by_dept(test_dept) == ans)
    