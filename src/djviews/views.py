from django.http import HttpResponse,HttpResponseRedirect


# Class Home

# def home(request):
#     #print(request)
#     #print(dir(request))
#     #print(request.method)
#     #print(request.is_ajax)
#     #print(request.is_ajax())
#     #print(request.get_full_path())
#     return HttpResponse("<!DOCTYPE html><html><head><style>h1{color: red;}</style></head><body><h1>Hello World</h1></body></html>")

def home(request):
	response = HttpResponse(content_type='text/html')
	#response = HttpResponse(content_type='application/json')
	response.content = "<!DOCTYPE html><html><head><style>h1{color: red;}</style></head><body><h1>Hello World</h1></body></html>"
	response.write("<p>Here's the text of the Web page.</p>")
	return response

def redirect_somewhere(request):
    return HttpResponseRedirect("/some/path")