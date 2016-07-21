from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.views. generic import View

from app.models import Contact
import csv
import codecs

__autor__ = 'Fabian Sarmiento'

class MainView(View):
    template_name = "index.html"

    def get(self, request):
        return TemplateResponse(request, self.template_name,
            {'current_page': self.template_name})

    @csrf_exempt
    def post(self, request):
        csvfile = request.FILES['csv']
        csvfile.open()
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            row[0] = str(row[0]).replace('\xa0', ' ')
            row[1] = int(row[1])
            print row
            try:
                contact = Contact.objects.get(name=row[0],zip_code=row[1])
            except ObjectDoesNotExist:
                contact = Contact(name=row[0],zip_code=row[1])
                contact.save()
            else:
                pass

        return TemplateResponse(request, self.template_name,
            {'current_page': self.template_name})


class ContactsView(View):
    template_name = 'index.html'
    @csrf_exempt
    def post(self, request):
        agent_one = request.POST['agent_one'][:2]
        agent_two = request.POST['agent_two'][:2]

        contacts_one = Contact.objects.filter(zip_code__startswith=agent_one)
        contacts_two = Contact.objects.filter(zip_code__startswith=agent_two)

        contacts_one = [[c.name, c.zip_code] for c in contacts_one]
        contacts_two = [[c.name, c.zip_code] for c in contacts_two]

        context = {
            request.POST['agent_one']: contacts_one,
            request.POST['agent_two']: contacts_two,
        }

        return TemplateResponse(request, self.template_name,
            {'current_page': self.template_name, 
            'contacts_info': context})



        


