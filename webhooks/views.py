from django.views.generic import TemplateView
import json


class Webhook(TemplateView):
    template_name = "_www/index.html"

    def get(self, request, *args, **kwargs):
        return super(Webhook, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        d = json.loads(request.body.decode())
        print(d)
        return super(Webhook, self).post(request, *args, **kwargs)
