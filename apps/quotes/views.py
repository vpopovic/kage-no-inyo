from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .models import Quote
from .utils import patch_view_decorator

login_required = patch_view_decorator(login_required(login_url='/admin/'))


@login_required
class QuoteWall(TemplateView):
    template_name = 'quotes/quote_wall.html'

    def get_context_data(self, **kwargs):
        context = super(QuoteWall, self).get_context_data(**kwargs)
        context['quotes'] = Quote.objects.all()
        return context
