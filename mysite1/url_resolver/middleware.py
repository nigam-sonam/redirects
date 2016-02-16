from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib import admin
from url_resolver.models import Redirects
import re, ast
from django.views.decorators.cache import cache_page
from django.core.cache import cache



class Redirect_url(object):
    ##get the request path.
    ##search in the cache and find the regex that matches the request path.
    ##If the match occurs return the redirect_from else pass.
    def process_request(self, request):
        #import pdb;pdb.set_trace()
        source_path=request.get_full_path()
        #cache.set('redirect_obj',Redirects.objects.values())
        in_cache=cache.get('redirect_obj')
        for obj_path in in_cache:
            pattern=re.compile(obj_path['redirect_from'])
            if pattern.match(source_path):
                final_path=obj_path['redirect_to']
                return HttpResponseRedirect(final_path)
            else:
                pass

            
         

