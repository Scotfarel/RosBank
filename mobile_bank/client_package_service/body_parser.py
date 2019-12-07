from collections import namedtuple


def parse_company_data(data):
    Company = namedtuple('Company', [
        'number_of_employees',
        'company_name',
        'cash_flow'
    ])
    number_of_employees = data['employeesNumber']
    name = data['companyName']
    cash_flow = data['salaryFund']
    return Company(number_of_employees, name, cash_flow)


def parse_company_settings(data):
    CompanySettings = namedtuple('Company', ['time_interval', 'billing_enable', 'enable_error_name_payment',
                                             'files_format'])
    time_interval = data['time_interval']
    billing_enable = data['billing_enable']
    enable_error_name_payment = data['enable_error_name_payment']
    files_format = data['files_format']
    return CompanySettings(time_interval, billing_enable, enable_error_name_payment, files_format)
