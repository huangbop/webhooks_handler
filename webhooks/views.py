from django.views.generic import TemplateView
import json


class Webhook(TemplateView):
    template_name = "_www/index.html"

    def get(self, request, *args, **kwargs):
        return super(Webhook, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        d = json.loads(request.body.decode())
        if d['ref'] == 'refs/heads/master':
            print('Do pull & deploy')
        return super(Webhook, self).post(request, *args, **kwargs)
