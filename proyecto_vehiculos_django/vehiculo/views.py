from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'


# view o controlador para home page not login
def home_page_not_login(request):
    return render(request, 'index.html')