from django.shortcuts import render, redirect
from .models import Newsletter
from django.views.decorators.http import require_POST
from .forms import NewsletterForm
# Create your views here.
@require_POST
def subscribe(request):
	if request.method == 'POST':
		form = NewsletterForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			form = NewsletterForm()
			return redirect('home')

	return render(request, 'index.html', {'Form':form})
