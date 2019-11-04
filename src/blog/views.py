from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse, Http404, HttpResponseRedirect
from .models import  PostModel
from django.contrib.auth.decorators import  login_required
from .forms import  PostModelForm
from django.contrib import  messages

# Create your views here.

def post_list_view(request):
	qs = PostModel.objects.all()
	print(qs)
	context = {"object_list":qs}
	return render(request,"list-view.html", context)

def post_detail_view(request, id=None):
	#obj = PostModel.objects.get(id=id)
	obj = get_object_or_404(PostModel, id=id)
	context = {"object":obj}
	return render(request,'detail-view.html', context)

def post_create_view(request):
	form = PostModelForm(request.POST or None)
	context = {"form":form}
	if form.is_valid():
		obj = form.save(commit=False)
		#print(obj.title)
		obj.save()
		messages.success(request, "Created a new blog post!")
		context = {
		    "form": PostModelForm()
		}
	return render(request, 'create-view.html',context)

def post_update_view(request, id=None):
	obj = get_object_or_404(PostModel, id=id)
	form = PostModelForm(request.POST or None, instance=obj)
	context = {"form":form}
	if form.is_valid():
		obj = form.save(commit=False)
		#print(obj.title)
		obj.save()
		messages.success(request, "Updated Post")
		return HttpResponseRedirect('/blog/{id}'.format(id=obj.id))
		
	return render(request, 'update-view.html',context)

#@login_required(login_url = '/login/')
@login_required
def login_required_view(request):
	print(request.user) 
	qs = PostModel.objects.all()
	print(qs)
	context = {"object_list":qs}
	if request.user.is_authenticated():
		template = 'list-view.html'
	else:
		template = 'list-view-public.html'
		#raise Http404
		#return HttpResponseRedirect('/login/')
	return render(request,template,context)

