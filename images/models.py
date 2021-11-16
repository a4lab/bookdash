from django.db import models
from django.conf import settings
from django.utils.text import  slugify
from django.urls import reverse
# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)
    users_like=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked',blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    # override save to generate a slug for each image
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug=slugify(self.title)
       super().save(*args, **kwargs) # Call the real save() method

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id,self.slug])

# class Comment(models.Model):
#     image=models.ForeignKey(Image,related_name='image_comment',on_delete=models.CASCADE)
#     created=models.DateField(auto_now_add=True,db_index=True)
#     user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='user_comment',on_delete=models.CASCADE)
#     body=models.TextField(blank=True)
#     def __str__(self):
#         pass

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Comment'
#         verbose_name_plural = 'Comments'