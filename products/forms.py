from django import forms
from .models import Product

# CSS sınıfı değişkeni
input_css_class = "form-control"
#input_css_class = "bg-gray-950 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'handle', 'price']  # Formda kullanılacak alanları belirtiyoruz
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        # Her alan için CSS sınıfını ekliyoruz
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image','name', 'handle', 'price']  # Formda kullanılacak alanları belirtiyoruz
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        # Her alan için CSS sınıfını ekliyoruz
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class
