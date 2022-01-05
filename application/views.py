from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import cloudinary
import cloudinary.uploader
import cloudinary.api
from .forms import *
# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
   
    return render(request, 'index.html')


def home(request):
	if request.method == "POST":
		form = NeighborForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("application:upload")
	form = NeighborForm()
	neighbour = NeighbourHood.objects.all()
	return render(request=request, template_name="home.html", context={'form':form, 'neighbour':neighbour})

def profile(request):
	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("application:upload")
	form = ProfileForm()
	profile= Profile.objects.all()
	return render(request=request, template_name="profile.html", context={'form':form, 'profile':profile})


def business(request):
	if request.method == "POST":
		form = BusinessForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("application:upload")
	form = BusinessForm()
	biz = Business.objects.all()
	return render(request=request, template_name="business.html", context={'form':form, 'biz':biz})

def post(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("application:upload")
	form = PostForm()
	post = Post.objects.all()
	return render(request=request, template_name="post.html", context={'form':form, 'post':post})


    
    
