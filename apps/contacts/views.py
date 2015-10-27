from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from models import Contacts

class IndexView(TemplateView):
    template_name = 'contacts/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['obj'] = Contacts.objects.get(id=1)
        return context
