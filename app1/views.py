from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Person
import json
from datetime import datetime

def index(request):
    return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["POST"])
def save_person(request):
    try:
        data = json.loads(request.body)
        
        # Parse the date string to a date object
        date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        
        # Create new person instance
        person = Person(
            name=data['name'],
            place=data['place'],
            contact_number=data['contact_number'],
            date_of_birth=date_of_birth
        )
        person.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Data saved successfully!',
            'data': {
                'id': person.id,
                'name': person.name,
                'place': person.place,
                'contact_number': person.contact_number,
                'date_of_birth': person.date_of_birth.strftime('%Y-%m-%d'),
                'created_at': person.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
        })
    
    except ValueError as ve:
        return JsonResponse({
            'status': 'error',
            'message': f'Invalid date format: {str(ve)}'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Error saving data: {str(e)}'
        }, status=400)