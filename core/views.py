from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .forms import ContactForm
from .models import Contact, Workshop
from django.core.mail import send_mail
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'core/index.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class FaqView(TemplateView):
    template_name = 'core/faq.html'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact: Contact = form.save()
            return redirect('contact')
        else:
            return render(request, 'core/contact.html', {'message': form.errors.as_text()})
    return render(request, 'core/contact.html')


class PortfolioView(TemplateView):
    template_name = 'core/portfolio.html'


class PortfolioSingleView(TemplateView):
    template_name = 'core/portfolio-single.html'


class ServiceView(TemplateView):
    template_name = 'core/service.html'


class PricingView(TemplateView):
    template_name = 'core/pricing.html'


class ComingSoonView(TemplateView):
    template_name = 'core/coming-soon.html'


class ErrorView(TemplateView):
    template_name = 'core/404.html'


class WorkshopView(ListView):
    template_name = 'core/workshop.html'
    model = Workshop
    context_object_name = 'workshops'

class linksView(TemplateView):
    template_name = 'core/links.html'

class NewTechChallengeView(TemplateView):
    template_name = 'core/newtechchallenge.html'
