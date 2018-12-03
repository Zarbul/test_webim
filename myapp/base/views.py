from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib
import json


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'auth/login/'
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        extra_context = {}
        social_user = request.user.social_auth.filter(provider='vk-oauth2').first()
        if social_user:
            url = u'https://api.vk.com/method/friends.get?fields=nickname,photo_50,online&{0}' \
                  u'&access_token={1}&v=5.92'.format(social_user.uid, social_user.extra_data['access_token'], )
            req = urllib.request.urlopen(url)
            friends = json.loads(req.read()).get('response').get('items')[:5]
            extra_context = {
                'friends': friends
            }
            return render(request, 'loginsys/mix.html', extra_context)
        return render(request, self.template_name)
