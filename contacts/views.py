from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ContactSerializer, FinanceSerializer
from .models import Contact, Finance
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render ,redirect
from .forms import ContactFileForm
from .utils import add_to_contacts
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
        print(request.POST.get('tablename'))
        if form.is_valid():
            add_to_contacts(request.FILES['file'])
            return redirect('/contacts')
        else:
            return HttpResponse("<h2>Invalid form</h2>")
        
    else:
        form = ContactFileForm()
    return render(request, 'contacts/add.html', {'form': form})
