from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserCreationForm, ReceiptForm
from .models import Receipt
from django.contrib.auth.decorators import login_required 

 
class LoginView(LoginView):
    template_name = 'login.html'

def logout_user(request):
	logout(request)
	return redirect('login')

class LogoutView(LogoutView):
    next_page = reverse_lazy('login')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipt_list.html', {'receipts': receipts})

@login_required
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    return render(request, 'receipt_detail.html', {'receipt': receipt})

@login_required
def receipt_create(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt_list')
    else:
        form = ReceiptForm()
    return render(request, 'receipt_form.html', {'form': form})

@login_required
def receipt_edit(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == 'POST':
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect('receipt_list')
    else:
        form = ReceiptForm(instance=receipt)
    return render(request, 'receipt_form.html', {'form': form})

@login_required
def receipt_delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    receipt.delete()
    return redirect('receipt_list')










