from django.shortcuts import render

# Create your views here.
# view o controlador para home page not login
def home_page_not_login(request):
    return render(request, 'index.html')