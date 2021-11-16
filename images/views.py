from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from bookmarker.common.decorators import ajax_required

# Create your views here.


@login_required
def image_create(request):

    if request.method=='POST':
        form=ImageCreateForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            new_item=form.save(commit=False)

            new_item.user=request.user
            new_item.save()
            messages.success(request,'Image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form=ImageCreateForm(data=request.GET)


    return render(request,'images/create.html',{'section':'images','form':form})

def image_detail(request,id,slug):
    image=get_object_or_404(Image,id=id,slug=slug)
    return render(request,"images/detail.html",{'image':image})

@login_required
@require_POST
def image_like(request):
    image_id=request.POST.get('id')
    action=request.POST.get('action')
    try:
        image=Image.objects.get(id=image_id)
        if action=="like":
            image.users_like.add(request.user)
        else:
            image.users_like.remove(request.user)
        return JsonResponse({'status':'ok'})
    except:
        pass
    return JsonResponse({'status':'error'})

# @login_required
# @require_POST
# def image_comment(request):
    
#     if request.method=='POST':
#         form=CommentForm(request.POST)
#         if form.is_valid():
#             cd =form.cleaned_data
#             new_item=form.save(commit=False)
#             new_item.user=request.user
#             im=Image.get_object_or_404(id=request.POST.get('id'))
#             new_item.image=im
#             new_item.save()
#             # messages.success(request,'Image added successfully')
#             return redirect(im.get_absolute_url())
#     else:
#         form=CommentForm()
#     return JsonResponse({'status':'error'})


def image_list(request):
    images=Image.objects.all()
    paginator=Paginator(images,8)
    page=request.GET.get('page')
    try:
        images=paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      {'section': 'images', 'images': images})
    return render(request,
                  'images/list.html',
                   {'section': 'images', 'images': images})