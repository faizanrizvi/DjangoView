from django.shortcuts import render
from django.http import  HttpResponse
from .models import  PostModel

# Create your views here.

def post_list_view(request):
	qs = PostModel.objects.all()
	print(qs)
	context = {"object_list":qs}
	return render(request,"list-view.html", context)
