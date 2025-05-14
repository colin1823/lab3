from employee_info import employee_data, calculate_average_salary, get_employees_by_age_range, get_employees_by_dept, display_all_records, display_records, display_main_menu
def test_calculate_average_salary():
    assert calculate_average_salary() == 60166.666666666664
def test_get_employee_by_department():
    assert get_employees_by_dept("Sales") == [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]