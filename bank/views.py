# bankapi/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from .models import Bank,Branch

@csrf_exempt  

  
def create_bank(request):
    
    try:
        data = json.loads(request.body)
        name = data.get('name')

        # Create a new Bank instance
        bank,is_newly_created = Bank.objects.get_or_create(name=name)
        

        return JsonResponse({'message': 'Bank created successfully','bank_id':str(bank.id)}, status=201)
    
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt  
  
def get_banks(request):
    try:
        banks = Bank.objects.all()
        banks_data = [{'id': bank.id, 'name': bank.name} for bank in banks]
        
        return JsonResponse(banks_data, safe=False)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def create_branch(request):
    try:
        data = json.loads(request.body)
        ifsc = data.get('ifsc')
        bank_id = data.get('bank_id')
        branch_name = data.get('branch')
        address = data.get('address')
        city = data.get('city')
        district = data.get('district')
        state = data.get('state')

        # Validate the required fields
        if not all([ifsc, bank_id, branch_name, address, city, district, state]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        bank=None
        try:
            bank = Bank.objects.get(id=bank_id)
        except Bank.DoesNotExist:
            return JsonResponse({'error': 'Bank with the given id does not exist'}, status=404)

        
        branch,is_new_branch = Branch.objects.get_or_create(ifsc=ifsc, bank=bank, branch=branch_name,
                        address=address, city=city, district=district, state=state)
        
        return JsonResponse({'message': 'Branch created successfully',"branch_id":str(branch.id)}, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def get_branch(request):
    try:
        branches = Branch.objects.all()
        branches_data = []
        for branch in branches:
            branch_data = {
                'ifsc': branch.ifsc,
                'bank_id': branch.bank.id,
                'bank_name': branch.bank.name,
                'branch': branch.branch,
                'address': branch.address,
                'city': branch.city,
                'district': branch.district,
                'state': branch.state,
            }
            branches_data.append(branch_data)
        
        return JsonResponse(branches_data, safe=False)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)