import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Bank

@csrf_exempt
def create_bank(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")

        name = data.get('name')
        if not name:
            return HttpResponseBadRequest("Missing 'name' field")

        bank = Bank(name=name)
        bank.save()

        response_data = {
            'bank_id': bank.bank_id,
            'name': bank.name,
        }

        return JsonResponse(response_data, status=201)

    return HttpResponseBadRequest("Only POST requests are allowed")

@csrf_exempt
def get_bank(request, bank_id):
    try:
        bank = Bank.objects.get(pk=bank_id)
        response_data = {
            'bank_id': bank.bank_id,
            'name': bank.name,
        }
        return JsonResponse(response_data)
    except Bank.DoesNotExist:
        return HttpResponseNotFound("Bank not found")
