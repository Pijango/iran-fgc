from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('contact/', views.contact_view, name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio-single/', views.PortfolioSingleView.as_view(),
         name='portfolio-single'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('pricing/', views.PortfolioSingleView.as_view(), name='pricing'),
    path('coming-soon/', views.ComingSoonView.as_view(), name='coming-soon'),
    path('404/', views.ErrorView.as_view(), name='404'),
    path('workshops/', views.WorkshopView.as_view(), name='workshops'),
    path('links/', views.linksView.as_view(), name='links'),
    path('newtechchallenge/', views.NewTechChallengeView.as_view(), name='newtechchallenge')
]
