from django import forms
from .models import Order
 

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name','postal_code','email','paid']
		#widgets = {'email':forms.CharField(widgets=forms.TextField(attrs={'value':'email.com'}))}
		widgets = {
					'email': forms.TextInput(attrs={'hidden':True,'placeholder':'example@example.com','required':False,})

				  }

		labels = {
					'email': ''
		}

		help_texts = {
			'email': ''
		}