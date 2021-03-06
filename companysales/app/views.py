from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Product, Customer, Seller, Order
from .utils import no_duplicate
from django.contrib import messages
from .pagination import pagination


def index(request):
    try:
        if request.method == "POST":
            current_id = request.POST.get('id', None)
            product = get_object_or_404(pk=current_id, klass=Product)
            product.delete()
            messages.success(request, "Удаление товара(продукта) прошло успешно")
    except:
        messages.error(request, "Ой! Что-то пошло не так. Товар(продукт) не удален")
    product_list = Product.objects.all()
    page_obj = pagination(num_items_page=4, obj=product_list, request=request.GET.get('page'))
    return render(
        request, 'site_items/index.html',
        {
            'list_pagination': page_obj,
            'title': 'Товары',
        }
    )


def customer(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    if request.method == "POST":
        try:
            current_id = request.POST.get('id', None)
            product = get_object_or_404(pk=current_id, klass=Customer)
            product.delete()
            messages.success(request, "Удаление покупателя прошло успешно")
        except:
            messages.error(request, "Ой! Что-то пошло не так. Покупатель не удален")
    customer_list = Customer.objects.all()
    page_obj = pagination(num_items_page=6, obj=customer_list, request=request.GET.get('page'))
    return render(
        request, 'site_items/customer.html',
        {
            'list_pagination': page_obj,
            'title': 'Покупатели'
        }
    )


def seller(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    if request.method == "POST":
        try:
            current_id = request.POST.get('id', None)
            sel = get_object_or_404(pk=current_id, klass=Seller)
            sel.delete()
            messages.success(request, "Удаление продавца прошло успешно")
        except:
            messages.error(request, "Ой! Что-то пошло не так. Продавец не удален")
    seller_list = Seller.objects.all()
    page_obj = pagination(num_items_page=4, obj=seller_list, request=request.GET.get('page'))
    return render(
        request, 'site_items/seller.html',
        {
            'list_pagination': page_obj,
            'title': 'Продавци'
        }
    )


def order(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    if request.method == "POST":
        try:
            current_id = request.POST.get('id', None)
            orders = get_object_or_404(pk=current_id, klass=Order)
            orders.delete()
            messages.success(request, "Удаление заказа прошло успешно")
        except:
            messages.error(request, "Ой! Что-то пошло не так. Заказ не удален")
    order_list = Order.objects.all()
    page_obj = pagination(num_items_page=4, obj=order_list, request=request.GET.get('page'))
    return render(
        request, 'site_items/order.html',
        {
            'list_pagination': page_obj,
            'title': 'Заказы'
        }
    )


def update_item(request, product_id):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    if request.method == 'GET':
        product = get_object_or_404(pk=int(product_id), klass=Product)
        form = ProductUpdateForm(instance=product)
    else:
        try:
            product = get_object_or_404(pk=int(product_id), klass=Product)
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            product.image = request.FILES.get('image')
            product.stock = request.POST.get('stock')
            product.price = request.POST.get('price')
            product.save()
            messages.success(request, "Данные товара(продукта) успешно обновлены!")
        except:
            messages.error(request, "Ой! Что-то пошло не так. Товар(продукт) не обновлен")
        return redirect('product_list')
    return render(
        request, 'update_items/update_item.html',
        {
            'form': form,
            'product_id': product_id,
        }
    )


def update_item_customer(request, customer_id):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    if request.method == 'GET':
        custom = get_object_or_404(pk=int(customer_id), klass=Customer)
        form = CustomerUpdateForm(instance=custom)
    else:
        try:
            body = {**request.POST}
            del body['csrfmiddlewaretoken']
            del body['id']
            for key in body:
                body[key] = body[key][0]
            Customer.objects.update_or_create(pk=int(request.POST.get('id')), defaults={**body})
            messages.success(request, "Данные покупателя успешно обновлены!")
        except:
            messages.error(request, "Ой! Что-то пошло не так. Данные покупателя не обновлены")
        return redirect('customer_list')
    return render(
        request, 'update_items/update_item_customer.html',
        {
            'form': form,
            'customer_id': customer_id,
        }
    )


def update_item_seller(request, seller_id):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    if request.method == 'GET':
        sellers = get_object_or_404(pk=int(seller_id), klass=Seller)
        form = SellerUpdateForm(instance=sellers)
    else:
        try:
            body = {**request.POST}
            del body['csrfmiddlewaretoken']
            del body['id']
            for key in body:
                body[key] = body[key][0]
            Seller.objects.update_or_create(pk=int(request.POST.get('id')), defaults={**body})
            messages.success(request, "Данные продавца успешно обновлены")
        except:
            messages.error(request, "Ой! Что-то пошло не так. Данные продавца не обновлены")
        return redirect('seller_list')
    return render(
        request, 'update_items/update_item_seller.html',
        {
            'form': form,
            'seller_id': seller_id,
        }
    )


def update_item_order(request, order_id):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    if request.method == 'GET':
        orders = get_object_or_404(pk=int(order_id), klass=Order)
        form = OrderUpdateForm(instance=orders)
    else:
        try:
            body = {**request.POST}
            customer_new = Customer.objects.get(pk=body['customer'][0])
            seller_new = Seller.objects.get(pk=body['seller'][0])
            product_new = Product.objects.get(pk=body['product'][0])
            total_new = body['total'][0]
            Order.objects.update_or_create(
                pk=int(request.POST.get('id')),
                defaults={
                    'customer': customer_new,
                    'seller': seller_new,
                    'product': product_new,
                    'total': total_new
                }
            )
            messages.success(request, "Данные заказа успешно обновлены")
        except:
            messages.error(request, "Ой! Что-то пошло не так. Данные заказа не обновлены")
        return redirect('order_list')
    return render(
        request, 'update_items/update_item_order.html',
        {
            'form': form,
            'order_id': order_id,
        }
    )


def report(request):
    """Отображение всех покупателей заданного продавца"""
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    form = ReportForm1()
    list_customer = Customer.objects.filter(order__seller__pk=request.POST.get('seller'))
    list_customer = no_duplicate(list_customer)  # Отсекаем дубликаты
    return render(request, 'report/report.html', {'form': form, 'list_customer': list_customer})


def report2(request):
    """ Отображение всех продавцов, которые продали заданный товар"""
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    form = ReportForm2()
    list_seller = Seller.objects.filter(order__product__pk=request.POST.get('product'))
    list_seller = no_duplicate(list_seller)
    return render(request, 'report/report2.html', {'form': form, 'list_seller': list_seller})


def report3(request):
    """ Отображение всех покупателей, которые купили заданный товар"""
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    form = ReportForm2()
    list_customer = Customer.objects.filter(order__product__pk=request.POST.get('product'))
    list_customer = no_duplicate(list_customer)
    return render(request, 'report/report3.html', {'form': form, 'list_customer': list_customer})


def report4(request):
    """Отображение всех продаж на заданную дату"""
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    form = ReportForm3()
    list_date = Product.objects.filter(order__date=request.POST.get('date'))
    list_date = no_duplicate(list_date)
    return render(request, 'report/report4.html', {'form': form, 'list_date': list_date})


def report5(request):
    """Отображение общей суммы продаж в заданный день."""
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    form = ReportForm3
    list_total = Order.objects.filter(date=request.POST.get('date'))
    list_total = no_duplicate(list_total)
    result_total = []
    for t in list_total:
        result_total.append(t.total)
    return render(request, 'report/report5.html', {'form': form, 'total': sum(result_total)})
