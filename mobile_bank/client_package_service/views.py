import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from . import company_classifier
from . import models_api
from . import body_parser
from . import json_template_creator

user_id = 10
company_id = 11


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        # there should be cookies form rosbank app with client user data
        # while we are working on a prototype, we understand client_id by default
        company_coef = models_api.get_company_coef(42)
        offers_handler = json_template_creator.JsonCreator(company_coef)
        return JsonResponse(offers_handler.correct_json)
    elif request.method == 'POST':
        serialized_data = request.body
        decoded_data = json.loads(serialized_data)
        if decoded_data['info_type'] == 'company_data':
            company = body_parser.parse_company_data(decoded_data['data'])
            company_coef = company_classifier.get_coefficient(company.cash_flow,
                                                              company.number_of_employees)
            models_api.save_company(user_id,
                                    company,
                                    company_coef)

            return HttpResponse(status=200)
        elif decoded_data['info_type'] == 'settings':
            company_settings = body_parser.parse_company_settings(decoded_data['data'])
            models_api.save_company_settings(company_id,
                                             company_settings)
            return HttpResponse(status=200)