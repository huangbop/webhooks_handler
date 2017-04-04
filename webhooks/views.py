from django.views.generic import TemplateView


class Webhook(TemplateView):
    template_name = "_www/index.html"
