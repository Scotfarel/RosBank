def get_coefficient(cash_flow, employee_number):
    valid = validation_data(cash_flow, employee_number)
    if not valid:
        return 0
    else:
        k_c = get_cf_coeff(cash_flow)
        k_e = get_emp_coeff(employee_number)

        k = (k_c + k_e) / 2
    return k


def get_cf_coeff(cash_flow):
    # positive infinity
    p_inf = float("inf")
    if 50000 <= cash_flow < 10 ** 6:
        return 1 + (cash_flow - 50000) / (10 ** 6 - 50000)
    elif 10 ** 6 <= cash_flow < 10 ** 8:
        return 2 + (cash_flow - 10 * 6) / (10 ** 8 - 10 ** 6)
    elif 10 ** 8 <= cash_flow < 10 ** 9:
        return 3 + (cash_flow - 10 * 8) / (10 ** 9 - 10 ** 8)
    elif 10 ** 9 <= cash_flow < 10 ** 10:
        return 4 + (cash_flow - 10 * 9) / (10 ** 10 - 10 ** 9)
    elif 10 ** 10 <= cash_flow < p_inf:
        return 5
    pass


def get_emp_coeff(employee_number):
    # positive infinity
    p_inf = float("inf")

    if 1 <= employee_number < 20:
        return 1 + (employee_number - 1) / (20 - 1)
    elif 20 <= employee_number < 100:
        return 2 + (employee_number - 20) / (100 - 20)
    elif 100 <= employee_number < 500:
        return 3 + (employee_number - 100) / (500 - 100)
    elif 500 <= employee_number < 1000:
        return 4 + (employee_number - 500) / (1000 - 500)
    elif 1000 <= employee_number < p_inf:
        return 5
    pass


def validation_data(cash, num):
    if cash < 50000 or num < 0 or num > 1000000:
        return False
    else:
        return True


if __name__ == '__main__':
    print(get_coefficient(6 * 10 ** 12, 5000))
