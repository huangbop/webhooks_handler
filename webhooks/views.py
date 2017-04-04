from django.views.generic import TemplateView
import json
import subprocess


class Webhook(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return super(Webhook, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        d = json.loads(request.body.decode())
        if d['ref'] == 'refs/heads/master':
            print('Do pull & deploy')
            subprocess.check_call("git submodule update --remote")
            subprocess.check_call("cd ../FW_Docs2 & make html")
        return super(Webhook, self).post(request, *args, **kwargs)
