from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	return render(request, 'home.html',{
		'new_item_text':request.POST.get('item_text',''),
		})
#from django.http import HttpResponse

# Create your views here.
#def home_page(request):
	#return HttpResponse('<html><title>To-Do lists</title></html>')