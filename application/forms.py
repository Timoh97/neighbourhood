from django import forms
from .models import *

# Create your forms here.
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'email','profile_pic',"neighbourhood",'location')
        
class NeighborForm(forms.ModelForm):

    class Meta:
        model = NeighbourHood
        fields = ('name', 'persons','picture',"police_contact",'location',"hospital_address")
        
class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ('name', 'email','description',"photo")
        
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content','image')