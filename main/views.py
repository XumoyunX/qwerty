from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Category, ProductIndex, Product, Cart


class MainIndex(TemplateView):
    template_name = "main/index.html"
#
# @GET(mahsulot/:id)
# @GET(mahsulot/?page=1&size=50)
# @POST(mahsulot/)
# @PUT(mahsulot/)
# @DELETE(mahsulot/:id)


    def get_context_data(self, **kwargs):
        kwargs["cart"] = Cart.objects.filter(user=self.request.user).count()
        kwargs["categories"] = Category.objects.filter(parent=None).all()
        kwargs["proindex"] = ProductIndex.objects.all()




        return super().get_context_data(**kwargs)








class Mahsulot(TemplateView):
    template_name = "layouts/mahsulot.html"

    def get_context_data(self, id=None, **kwargs):
        size = int(self.request.GET.get('size', 9))
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent=None).all()
        if id is not None:
            context["mahsulotlar"] = list(Product.objects.filter(category_id=id).order_by("-id"))[:size]
        else:
            context["mahsulotlar"] = Product.objects.all()[:9]

        return context







class AddCart(View):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            cart = Cart(name=product.name_uz, price=product.price, photo=product.photo, user=request.user)
            cart.save()
            return redirect("main:korzinka")
        except:
            return redirect("main:korzinka")



class Korzinka(TemplateView):
    template_name = "layouts/karzinka.html"
    def get_context_data(self, **kwargs):
        kwargs["cart"] = Cart.objects.filter(user=self.request.user)

        return super().get_context_data(**kwargs)











class Searchq(ListView):
    # model = Product
    template_name = "layouts/search.html"

    # def get_queryset(self):
    #     query = self.request.GET.get("q")
    #     return Product.objects.filter(username__icontains=query).order_by("-id")


    def get_queryset(self, **kwargs):
        context=super(Searchq, self).get_context_data(**kwargs)
        q=self.request.GET.get("q") or ""
        context["mahsulotlar"] = Product.objects.filter(name_uz__icontains=q)

