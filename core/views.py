from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .models import About, Car,Address, CarCategory,ConditionCategory
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator



class IndexListView(ListView):
    model = Car
    template_name='index.html'
    
    
        # if 'category_slug' in self.kwargs:
        #     return super().get_queryset().filter(
        #         category_slug=self.kwargs['category_slug']
        #     )
        # else:
        #     return super().get_queryset().filter(
        #         name__icontains=self.request.GET.get('name')
        #     )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["cars_list"] = Car.objects.all()[:6]
        
        context["categories"] = ConditionCategory.objects.all()
        context["categories_list"] = CarCategory.objects.all()
        
        
        return context





def car(request,category_slug=None):
    category=None
    car = []
    
    
    categories_list = CarCategory.objects.all()
    
    
    
    if category_slug:
        car=Car.objects.all()
        category=get_object_or_404(CarCategory,slug=category_slug)
        car=Car.objects.filter(categories=category)
    
    
    
    

        
    
        
    context = {
        'car':car,
        'categories_list':categories_list,
    }
        
    
    
        
    
    
    
    
    return render(request,'car.html',context)



def car_list(request,category_slug=None):
    category=None
    c = Car.objects.all().count()
    categories=ConditionCategory.objects.all()
   
    car=Car.objects.all()
    page = request.GET.get('page')
    
    paginator = Paginator(car,6)
    
    
    try:
        car = paginator.page(page)
    except EmptyPage:
        car = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        car = paginator.page(1)
    
    
    
    
    if category_slug:
        car=Car.objects.all()
        category=get_object_or_404(ConditionCategory,slug=category_slug)
        car=car.filter(category=category)
        page = request.GET.get('page')
    
        paginator = Paginator(car,6)
    
    
        try:
            car = paginator.page(page)
        except EmptyPage:
            car = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            car = paginator.page(1)
        
            
            
    return render(request,'offers.html',{
                    'categories':categories,
                    'car':car,
                    'cars':c,
                    'category':category
                    
                    })




def search(request,category_slug=None):
    category=None
    query=None
    category_query=None
    car=[]
    categories = ConditionCategory.objects.all()
    
    query = request.GET.get('search')
    
    category_query = request.GET.get('category')
    
    
    if query != '' or query is not None:
        car = Car.objects.filter(name__icontains=query)
    
    
    if category_query != '' or  category_query is not None:
        car = Car.objects.filter(category__name__icontains=category_query)
     
        if query != '' or query is None:
            car = car.filter(name__icontains=query)
            
                
                
            
            print('sdsdsbd')
               
                 
        
        
    
        
    
    context = {
        'car':car,
        'categories':categories,
        'query':query,
        'category_query':category_query,
        'category':category
        
        
    }
    
    return render(request,'result.html', context)
                                          

    
# class SearchListView(ListView):
#     template_name = 'result.html'
#     model = Car
    
#     def get_queryset(self):
#         if 'category_slug' in self.kwargs:
#             return super().get_queryset().filter(
#                 slug=self.kwargs['category_slug']
#             )
#         else:
#             return super().get_queryset().filter(
#                 name__icontains=self.request.GET.get('search','')
#             )
            
#     def get_context_data(self, **kwargs):
#         context = super(SearchListView,self).get_context_data(**kwargs)
#         query = self.request.GET.get('search','')

#         context['queryset'] = Car.objects.all().filter(name__icontains=query)
        
        
        
        
#         return context
        
        
    
        
    



        
    

# class CarListView(ListView):
#     model = Car
#     template_name = 'offers.html'
#     context_object_name = 'car_list'
    
#     paginate_by = 3
    
    
    
    
#     def get_context_data(self, request,category_slug=None,**kwargs):
#         context = super().get_context_data(**kwargs)
        
#         category=None
#         categories=ConditionCategory.objects.all()
#         car=Car.objects.all()
        
        
#         page = self.request.GET.get('page')
#         paginator = Paginator(condition,self.paginate_by)
        
        
#         try:
#             car = paginator.page(page)
#         except EmptyPage:
#             car = paginator.page(paginator.num_pages)
#         except PageNotAnInteger:
#             page = 1
#             car = paginator.page(page)
#         except:
#             car = paginator.page(self.paginate_by)
            
            
#         if category_slug:
#         category=get_object_or_404(ConditionCategory,slug=category_slug)
#         car=car.filter(category=category)
        
#         page=request.GET.get('page')
        
        
        
#         if category_slug:
#             category=get_object_or_404(ConditionCategory,slug=category_slug)
#             car=car.filter(category=category)
            
#             page = self.request.GET.get('page')
#             paginator = Paginator(car,self.paginate_by)
        
        
#             try:
#                 car = paginator.page(page)
#             except EmptyPage:
#                 car = paginator.page(paginator.num_pages)
#             except PageNotAnInteger:
#                 page = 1
#                 car = paginator.page(page)
#             else:
#                 condition = Car.get_condition_all()
        
        
#         context["categories"] = categories
#         context['car'] = car
        

            

#         return context


            
    
    

class SupportListView(ListView):
    model = Address
    template_name = 'support.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_list"] = About.objects.all()
        return context
    
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'offers_detail.html'
    success_url = reverse_lazy("core:offers")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["address_list"] = Address.objects.all()
        return context
    
    


    

    
    
    
    
    
    
    
    



