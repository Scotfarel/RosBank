from . import models


def save_company(owner_id, company_info, ratio):
    company = models.Companies(owner_id=owner_id,
                               name=company_info.company_name,
                               cash_flow=company_info.cash_flow,
                               number_of_employees=company_info.number_of_employees,
                               confidence_ratio=ratio)
    company.save()


def save_company_settings(company_id, company_settings_info):
    company_settings = models.CompanySettings(company_id=company_id,
                                              time_interval=company_settings_info.time_interval,
                                              billing_enable=company_settings_info.billing_enable,
                                              enable_error_name_payment=company_settings_info.enable_error_name_payment,
                                              files_format=company_settings_info.files_format)
    company_settings.save()


def get_client_companies(client_id):
    companies = models.Companies.objects.all().filter(owner_id=client_id)
    return companies


def get_company_coef(company_id):
    return models.Companies.objects.order_by("?").first().confidence_ratio

