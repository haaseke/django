from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import BlogPost



def blog_post_detail_page(request,id):
	try:
	    obj= BlogPost.objects.get(id=id)
	except:
		raise Http404
	template_name = 'blog_post_detail.html'
	context = {"object":obj}

	return render(request, template_name , context )

def blog_post_list_view(request):
    # list out objects 
    # could be search
    qs = BlogPost.objects.all().published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)	