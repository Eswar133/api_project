import json
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Branch, Bank

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

@csrf_exempt
def create_branch(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")

        ifsc = data.get('ifsc')
        bank_id = data.get('bank_id')
        branch_name = data.get('branch_name')
        address = data.get('address')
        city = data.get('city')
        district = data.get('district')
        state = data.get('state')

        if not all([ifsc, bank_id, branch_name, address, city, district, state]):
            return HttpResponseBadRequest("Missing fields in request data")

        try:
            bank = Bank.objects.get(pk=bank_id)
        except Bank.DoesNotExist:
            return HttpResponseBadRequest("Bank with given bank_id does not exist")

        branch = Branch(
            ifsc=ifsc,
            bank=bank,
            branch_name=branch_name,
            address=address,
            city=city,
            district=district,
            state=state
        )
        branch.save()

        response_data = {
            'ifsc': branch.ifsc,
            'bank_id': branch.bank.bank_id,
            'branch_name': branch.branch_name,
            'address': branch.address,
            'city': branch.city,
            'district': branch.district,
            'state': branch.state,
        }

        return JsonResponse(response_data, status=201)

    return HttpResponseBadRequest("Only POST requests are allowed")

@csrf_exempt
def get_branch(request, ifsc):
    try:
        branch = Branch.objects.get(pk=ifsc)
        response_data = {
            'ifsc': branch.ifsc,
            'bank_id': branch.bank.bank_id,
            'branch_name': branch.branch_name,
            'address': branch.address,
            'city': branch.city,
            'district': branch.district,
            'state': branch.state,
        }
        return JsonResponse(response_data)
    except Branch.DoesNotExist:
        return HttpResponseNotFound("Branch not found")
