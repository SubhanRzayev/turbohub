from django.urls import path
from . import views
from .views import SupportListView,CarDetailView,IndexListView

app_name = 'core'

urlpatterns = [
    # path("", CarListView.as_view(), name="offers"),
    
    # path("",views.index,name='index'),
    
    path("", IndexListView.as_view(), name="index"),
    
    # path("search/", SearchListView.as_view(), name="index_search"),
    
    path("offers/", views.car_list, name='offers'),
    
    path('offers/<slug:category_slug>',views.car_list,name='offer_category'),
    
    
    path("search/", views.search,name="index_search"),
    
    path("car/", views.car,name="car"),   
    path('car/<slug:category_slug>',views.car,name='car_category'),
    
       
       
    path("offers/<slug:slug>/", CarDetailView.as_view(), name="offers_detail"),
    
    path("support/", SupportListView.as_view(), name="support"),
    
]


