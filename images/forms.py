from django import  forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from .models import Image

from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ("title","url","description")
        widgets={
            'url':forms.HiddenInput(attrs={'hidden':"hidden"}),
            'title':forms.TextInput(attrs={'class':"form-control",'required':'required'}),
            'description':forms.Textarea(attrs={'class':"form-control",'rows':"3"}),
             
                                            
        }
    def clean_url(self):
        url=self.cleaned_data['url']
        valid_ext=['jpg','jpeg','png']
        ext=url.rsplit('.',1)[1].lower()
        if ext not in valid_ext:
            raise ValidationError('The given url does not cntin allowed extension')
        return url

    def save(self,force_insert=False,force_update=False,commit=True):
        image=super().save(commit=False)
        image_url=self.cleaned_data['url']
        name=slugify(image.title)
        extension=image.url.rsplit('.',1)[1].lower()
        image_name=f'{name}.{extension}'
    

        # fetch image from url
        res=request.urlopen(image_url)
        image.image.save(image_name,ContentFile(res.read()),save=False)

        if commit:
            image.save()
        return image
