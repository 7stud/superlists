from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(requ):
    html = []
    html.append('<html>')
    html.append('<head><title>To-Do lists</title></head>')
    html.append('</html>')

    return HttpResponse(''.join(html))
    
