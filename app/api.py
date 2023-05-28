import json
from datetime import datetime

from django.http import HttpResponse, JsonResponse, HttpRequest
from django.contrib.auth import get_user_model
from django.conf import settings

from goods.models import Good


def parse_json_to_django_model():
    with open("data/goods.json") as file:
        data = json.load(file)
        for item in data:
            good = Good(
                name=item["good_name"],
                code=item["good_code"],
                supplier_name=item["supplier_name"],
                supplier_address=item["supplier_address"],
                supplier_phone=item["supplier_phone"],
                is_bulk=item["is_bulk"],
                price=item["price"],
                dt_of_license=datetime.strptime(
                    item["dt_of_license"], "%Y-%m-%d"
                ).date(),
            )
            good.save()


def api_response(request, param_id):
    return JsonResponse({"some": "data", "param_id": param_id})


def from_response(request):
    request_body = request.body.decode("utf-8")
    pairs = request_body.split("&")
    data = {}
    for pair in pairs:
        key, value = pair.split("=")
        data[key] = value
    username = data.get("login", "")
    user = get_user_model().objects.filter(username=username)
    if user.exists():
        parse_json_to_django_model()
        return JsonResponse({"success": "true", "data": "user exists"})
    else:
        return JsonResponse({"success": "false", "data": "user doesn't exist"})
