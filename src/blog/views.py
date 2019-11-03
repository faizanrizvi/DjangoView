from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse, Http404, HttpResponseRedirect
from .models import  PostModel
from django.contrib.auth.decorators import  login_required

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

