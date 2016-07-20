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
        import pdb; pdb.set_trace()
        csvfile = request.FILES['csv']
        csvfile.open()
        reader = csv.reader(csvfile, delimiter=';')
        reader = [', '.join(row) for row in reader]

        
        return reader