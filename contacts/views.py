from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ContactSerializer, FinanceSerializer
from .models import Contact, Finance
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render ,redirect
from .forms import ContactFileForm
from . import utils
from django.http import HttpResponse

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer


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
