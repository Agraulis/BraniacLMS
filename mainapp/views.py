from django.views.generic import TemplateView

"""
    path('', views.HelloWorldView.as_view()),
    path('news/', views.NewsPageView.as_view()),
    path('courses/', views.CoursesPageView.as_view()),
    path('contacts/', views.ContactsPageView.as_view()),
    path('doc_style/', views.DocSitePageView.as_view()),
    path('login/', views.LoginPageView.as_view()),
"""


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
