from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ContactSerializer, FinanceSerializer
from .models import Contact, Finance
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render ,redirect
from .forms import ContactFileForm

from django.db.models import Q
from . import utils

from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics

class ContactList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query is not None:
            contacts = Contact.objects.filter(Q(firstname__icontains=query) | \
                    Q(lastname__icontains=query) | \
                    Q(job__icontains=query) | \
                    Q(sitename__icontains=query))[:15]
        else:
            contacts = Contact.objects.all()[:15]

        data = ContactSerializer(contacts, many=True).data
        return Response(data)
    
class FinanceList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query is not None:
            contacts = Finance.objects.filter(Q(name__icontains=query) | \
                    Q(duty__icontains=query) | \
                    Q(room__icontains=query) | \
                    Q(contact__icontains=query))[:50]
        else:
            contacts = Finance.objects.all()[:50]

        data = FinanceSerializer(contacts, many=True).data
        return Response(data)
    
def add(request):
    if request.method == 'POST':
        form = ContactFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            _file = request.FILES['file']
            table = request.POST.get('tablename')
            if table == "finance_contacts":
                utils.add_to_finance_contacts(_file)
                return redirect('/finance')
            else:
                utils.add_to_contacts(_file)
                return redirect('/contacts')
        else:
            return HttpResponse("<h2>Invalid form</h2>")
        
    else:
        form = ContactFileForm()
    return render(request, 'contacts/add.html', {'form': form})
