from django.views.generic import TemplateView

from .models import Quote


class QuoteWall(TemplateView):
    template_name = 'quotes/quote_wall.html'

    def get_context_data(self, **kwargs):
        context = super(QuoteWall, self).get_context_data(**kwargs)
        context['quotes'] = Quote.objects.all()
        return context
