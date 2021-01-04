from django.urls import path
from . import views
urlpatterns=[
    path('html',views.home,name='home'),
    path('',views.html,name='html'),
    ##path('',views.Viewpdf.as_view(),name="pdf_view")
]