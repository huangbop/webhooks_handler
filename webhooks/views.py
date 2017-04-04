import os
from django.views.generic import TemplateView
import json
import subprocess


class Webhook(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return super(Webhook, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            d = json.loads(request.body.decode())
        except:
            d = {}
        # if d.get('ref') == 'refs/heads/master':
        if True:
            subprocess.check_call("git submodule update --remote -f", shell=True)
            if not os.getcwd().endswith('FW_Docs2'):
                os.chdir("./FW_Docs2")
            subprocess.check_call("make html", shell=True)
        return self.get(request, *args, **kwargs)
