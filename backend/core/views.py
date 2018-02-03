from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from core.models import QrCode, Transaction, Wallet


# Create your views here.
def main_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    return render(request, 'core/main.html')


@login_required
def dashboard_view(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    transactions = Transaction.objects.filter(Q(sender=user) | Q(recipient=user))
    codes = QrCode.objects.filter(recipient=user)

    return render(request, 'core/dashboard.html', {'wallet': wallet, 'transactions': transactions, 'codes': codes})


@login_required
def qrcodecreate_view(request):
    return render(request, 'core/qrcodeCreate.html')


@login_required
def transaction_view(request):
    transactions = Transaction.objects.filter(sender=request.user)
    return render(request, 'core/transaction.html', {'transactions': transactions})


@login_required
def qrcode_details_view(request, pk):
    qrcode = QrCode.objects.get(id=pk)
    code = '&$#'.join([str(request.user.id), str(qrcode.amount), qrcode.description])
    return render(request, 'core/qrcodeDetails.html', {'qrcode': qrcode, 'code': code})


@login_required
def qrcodelist_view(request):
    qrcodes = QrCode.objects.filter(recipient=request.user)
    return render(request, 'core/qrcodeList.html', {'qrcodes': qrcodes})

