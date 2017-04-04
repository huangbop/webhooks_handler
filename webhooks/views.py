import os
from django.views.generic import TemplateView
import json
import subprocess


class Webhook(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return super(Webhook, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        d = json.loads(request.body.decode())
        if d.get('ref') == 'refs/heads/master':
            subprocess.check_call("git submodule update --remote", shell=True)
            os.chdir("./FW_Docs2")
            subprocess.check_call("make html", shell=True)
        return super(Webhook, self).post(request, *args, **kwargs)
