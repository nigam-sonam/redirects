import re
from django.db.models.signals import post_save
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.db import models
from django.http import HttpResponseRedirect
from caching.base import CachingManager, CachingMixin
from django.dispatch import receiver
# Create your models here.

class Redirects(models.Model):
    Status_type=(
            (301,301),
            (302,302),
            )
    redirect_from=models.CharField(max_length=400)
    redirect_to=models.CharField(max_length=400)
    url_status = models.IntegerField(choices=Status_type,default=301)
    def __str__(self):
        return self.redirect_from  +  self.redirect_to


@receiver(post_save,sender=Redirects)
def cache_update(sender,**kwargs):
    redir_obj=Redirects.objects.values()
    cache.set('redirect_obj',redir_obj)


### in case of addition of models instance cache it , if case of edit of model instance reset the cache and cache it again 
