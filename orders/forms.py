from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'aliks'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'mexelov'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'admin@admin.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Uzbekiston, Toshkent, Mirzoulugbek, dom 6'}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')