# bankapi/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import Bank,Branch
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView


def banks_view(request):
    return render(request, 'banks.html')

def branches_view(request):
    return render(request, 'branches.html')


class BankAPIView(APIView): 
    def get(self, request):
        try:
            banks = Bank.objects.all()
            banks_data = [{'id': bank.id, 'name': bank.name} for bank in banks]
            
            return JsonResponse(banks_data, safe=False)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def post(self,request):
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

        
class BranchAPIView(APIView): 
    def get(self, request):
        try:
            params = request.GET
            print("Got request " ,params)
            ifsc = params.get('ifsc')
            bank_id = params.get('bank_id')
            branch_name = params.get('branch')
            address = params.get('address')
            city = params.get('city')
            district = params.get('district')
            state = params.get('state')

            branches= Branch.objects.all()
            if ifsc:
                branches = branches.filter(ifsc=ifsc)
            if bank_id:
                branches = branches.filter(bank__id=bank_id)
            if branch_name:
                branches = branches.filter(branch_name=branch_name)
            if address:
                branches = branches.filter(address=address)
            if city:
                branches = branches.filter(city=city)
            if district:
                branches = branches.filter(district=district)
            if state:
                branches = branches.filter(state=state)
            print("final branch count",branches.count())
            
            page = request.GET.get('page', 1)
            per_page = request.GET.get('per_page', 10)
            paginator = Paginator(branches, per_page)

            try:
                branches_page = paginator.page(page)
            except PageNotAnInteger:
                branches_page = paginator.page(1)
            except EmptyPage:
                branches_page = paginator.page(paginator.num_pages)

            # Prepare the data
            branches_data = []
            for branch in branches_page:
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

            # Construct pagination information
            response_data = {
                'total_count': paginator.count,
                'num_pages': paginator.num_pages,
                'current_page': branches_page.number,
                'next': branches_page.next_page_number() if branches_page.has_next() else None,
                'previous': branches_page.previous_page_number() if branches_page.has_previous() else None,
                'results': branches_data,
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    def post(self,request):
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
            
            return JsonResponse({'message': 'Branch created successfully',"branch_id":str(branch.branch)}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
 