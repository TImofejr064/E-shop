from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib import messages



def main(request):
    categories = Category.objects.all()
    products = Product.objects.filter(category__name="Шаурма")
    category = "Шаурма"
    ctx = {
        'products' : products,
        'categories' : categories,
        'category' : category
    }
    return render(request, 'shop/main.html', context=ctx)

def get_products(request, category):
    print(request.method)
    if request.method == "POST":
        print('request is post')

        num = request.POST.get("number")
        id = request.POST.get("product'sid")
    
        product = Product.objects.get(pk=id)
        user = User.objects.get(username=request.user)
        try:
            a = BasketsItem.objects.get(user=request.user, product=product)
            messages.warning(request, 'Товар уже добавлен!')
        except:
            bi = BasketsItem(user=request.user, product=product, num=num)
            bi.save()
            print('New item in basket!')    
            messages.success(request, 'Товар добавлен!')
        
        

    categories = Category.objects.all()
    products = Product.objects.filter(category__name=category)

    context = {
        'categories' : categories,
        'products' : products,
        'category' : category
    }
    return render(request, template_name='shop/main.html', context=context)

def reg(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт успешно создан для пользователя {username}')
            return redirect('/')
    else:        
        form = UserRegisterForm()
    return render(request, 'shop/register.html', {'form' : form})

def basket(request):
    if  request.method == 'POST':
        if request.POST.get("type") == "delete":
            try:
                print("request is post and type is delete")
                id = request.POST.get("item_id")
                item = BasketsItem.objects.get(pk=id)
                item.delete()
                messages.success(request, 'Товар удален!')
            except:
                pass
            else:
                pass
        elif request.POST.get("type") == "plus":
            try:
                print("request is post and type is plus")
                id = request.POST.get("item_id")
                item = BasketsItem.objects.get(pk=id)
                if item.num != 5:
                    item.num = item.num+1
                    item.save()
                else:
                    messages.warning(request, 'Максимальное кол-во товара!')
            except:
                pass
            else:
                pass
        elif request.POST.get("type") == "minus":
            try:
                print("request is post and type is plus")
                id = request.POST.get("item_id")
                item = BasketsItem.objects.get(pk=id)
                if item.num != 1:
                    item.num = item.num-1
                    item.save()
                else:
                    messages.warning(request, 'Минимальное кол-во товара!')
            except:
                pass
            else:
                pass
        elif request.POST["type"] == "order":
            user = request.user
            adress = request.POST.get("adress")
            summ = request.POST.get("sum")
            basket_items = BasketsItem.objects.filter(user=request.user)
            print('----------------------------------------------------')
            print(f'Пользователь: {request.user}')
            print(f'Адрес: {adress}')
            print(f'Общая цена: {summ}')
            for item in basket_items:
                print(f'Товар: {item.product.name}, Кол-во: {item.num}, Цена: {item.product.price}')
            print('----------------------------------------------------')
            

    basket = Basket.objects.get(user=request.user)
    basket_items = BasketsItem.objects.filter(user=basket.user)
    total_price = 0

    for item in basket_items:
        total_price += item.product.price * item.num

    ctx = {
        'baskets_item' : basket_items,
        'total_price' : total_price,
        'basket' : basket
    }

    return render(request, 'shop/basket.html', context=ctx)

