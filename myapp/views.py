from django.views.generic import TemplateView


class MainView(TemplateView):
    """
    View principale that renders main html app.html
    """
    template_name = "app.html"
