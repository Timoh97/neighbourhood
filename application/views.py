from django.shortcuts import render
from .models import *
from django.http  import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import cloudinary
from django.shortcuts import get_object_or_404, render, redirect
import cloudinary.uploader
import cloudinary.api
from .forms import *
# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
   
    return render(request, 'index.html')



@login_required(login_url='/accounts/login/')
def home(request):
	if request.method == "POST":
		form = NeighborForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/')
	form = NeighborForm()
	home = NeighbourHood.objects.all()
    
	return render(request=request, template_name="home.html", context={'form':form, 'home':home})


def upload(request):
    if request.method == "POST":
        form = NeighborForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form = NeighborForm()
        
    return render(request, 'upload.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = NeighbourHood.objects.all()
    return render(request,"profile.html",{'profile':profile,'project':project})

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})

def search_results(request):

    if "search"in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_images = Business.search_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
@login_required(login_url='/accounts/login/')
def business(request):
	if request.method == "POST":
		form = BusinessForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/business')
	form = BusinessForm()
	business = Business.objects.all()
	return render(request=request, template_name="business.html", context={'form':form, 'business':business})

@login_required(login_url='/accounts/login/')
def post(request):
    #    neighbors=NeighbourHood.objects.get(id=neighbour_id)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('post/')
	form = PostForm()
	post = Post.objects.all()
     
	return render(request=request, template_name="post.html", context={'form':form, 'post':post})
 
@login_required(login_url='/accounts/login/')    
def create_post(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('post/')
	form = PostForm()
	return render(request=request, template_name="create_post.html", context={'form':form})

def create_business(request):
	if request.method == "POST":
		form = BusinessForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/business')
	form = BusinessForm()
	return render(request=request, template_name="create_business.html", context={'form':form})