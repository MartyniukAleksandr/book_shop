from django import forms
from .models import Customer, Seller, Product, Order


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone': 'Номер телефона'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class SellerUpdateForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone': 'Номер телефона',
            'date': 'Дата приема на роботу',
            'position': 'Должность'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'position': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            )
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Название товара',
            'description': 'Описание',
            'image': 'Обожка товара(изображение)',
            'stock': 'Количество(шт)',
            'price': 'Цена'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class OrderUpdateForm(forms.ModelForm):
    """ Убираем подчеркивание в селекте: -------"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].empty_label = 'Покупатель не выбран'
        self.fields['seller'].empty_label = 'Продавец не выбран'
        self.fields['product'].empty_label = 'Товар не выбран'

    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'customer': 'Покупатель',
            'seller': 'Продавец',
            'product': 'Товар(продукт)',
            'date': 'Дата продажи',
            'total': 'Сумма'
        }
        widgets = {
            'customer': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'seller': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'product': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'total': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ReportForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seller'].empty_label = 'Выбирете продавца из списка'

    class Meta:
        model = Order
        fields = ['seller']
        widgets = {
            'seller': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            )
        }


class ReportForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Выбирете продукт из списка'

    class Meta:
        model = Order
        fields = ['product']
        widgets = {
            'product': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            )
        }


class ReportForm3(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['date']
        labels = {
            'date': 'Дата продажи',
        }
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }
