from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Product, Category,UserBuyProduct
from cms.middleware import user
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
class index(ListView):
    template_name ="apps/index.html"
    model = Category
    context_object_name = 'list_all_category'

class ProductListView(ListView):
    template_name = "apps/product_list.html"
    model = Product
    # model = Category
    def get_context_data(self, *args, **kwargs):
        # Get data
        category_id = self.request.GET.get('category_id', None)
        context = super().get_context_data(*args, **kwargs)

        # Get list product by category
        list_all_product = Product.objects.filter(category__id=category_id)
        context['list_all_product'] = list_all_product
        return context
    

class ProductCreateView(CreateView):
    
    template_name = "apps/product_create.html"
    model = Product
    fields = ['name','price_start','category','date_end','imageUrl']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            template_name = "apps/product_create.html"
            model = Product
            fields = ['name','price_start','category','date_end','imageUrl']
            
            # return HttpResponse('ok') #needs defined as valid url
        return super(ProductCreateView,self).dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        form.instance.user_post = self.request.user
        self.object = form.save()
        UserBuyProduct.objects.create(product_id=self.object.pk,
        Price_Final=self.object.price_start,
        user_buy=self.request.user
        )
        return super(ProductCreateView,self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('homepage')

    # def get_context_data(self, *args, **kwargs):
    #     categorys = Category.objects.filter()
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categorys'] = categorys
    #     return context

class ProductUpdateView(UpdateView):
    template_name = "apps/product_update.html"
    model = Product
    fields = ['name','price_start']
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
                template_name = "apps/product_update.html"
                model = Product
                fields = ['name','price_start']
            
            # return HttpResponse('ok') #needs defined as valid url
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        if request.method =="POST":
            product_id = request.POST.get('id')
            print(product_id)
            price = request.POST.get('price')
            UserBuyProduct.objects.create(product_id=product_id,
            Price_Final=price,
            user_buy=self.request.user
            )
            return redirect('homepage')
        return super().post(request,'index')
    # def form_valid(self, form):
    #     self.object = form.save()
    #     return super().form_valid(form)
    # def form_valid(self, form):
    #     form.instance.user_post = self.request.user
    #     form.instance.price_start =self.request.get
    #     self.object = form.save()
    #     UserBuyProduct.objects.create(product_id=self.object.pk,
    #     Price_Final=self.object.price_start,
    #     user_buy=self.request.user
    #     )
    #     return super().form_valid(form)
        # Productbuy = UserBuyProduct.objects.filter(product_id = self.object.pk).order_by('-date')
    # fields = ['name','price_start','user_post','imageUrl','date_post']
    # def get_context_data(self, *args, **kwargs):
    #     Product_buy = UserBuyProduct.objects.filter(product_id = self.object.pk)
    #     context = super().get_context_data(*args, **kwargs)
    #     context['Product_buy'] = Product_buy
    #     return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('homepage')