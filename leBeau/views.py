from theTone.settings import LEBEAU_CODE
from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm
from django.http import JsonResponse


# passcode from .env
LEBEAU_CODE = LEBEAU_CODE

def leBeau(request, urlTag='all', order='purchase_date', status='both'):
    form = TransactionForm()
    if request.method == 'POST':
        if 'submitted-tag' in request.POST:
            if request.POST.get('direction'):
                order = f"{request.POST.get('direction')}{request.POST.get('filter')}"
            else:
                order = request.POST.get('filter')
            status = request.POST.get('status')
            tag = request.POST.get('submitted-tag')
            if tag == "":
                tag = 'all'
            return redirect('leBeau:leBeau', urlTag=tag, order=order, status=status)
        # create new transaction
        filledForm = TransactionForm(request.POST)
        Transaction.saveTransaction(filledForm, request)
        return redirect('leBeau:leBeau', urlTag='all', order='-purchase_date', status='both')
    # default get requests

    data = Transaction.getTransactions(urlTag, order, status)
    totals = Transaction.getTotals(data)

    return render(request, 'leBeau.html',{'form':form, 'data':data, 'totals':totals, 'urlTag': urlTag , 'LEBEAU_CODE': LEBEAU_CODE})


def leBeauEdit(request, id):
    # get selected transaction to edit
    transaction = get_object_or_404(Transaction, id=id)
    if request.POST:
        if '_delete' in request.POST:
            # delete transaction
            transaction.delete()
            return redirect('leBeau:leBeau', urlTag='all', order='-purchase_date', status='both')
    # edit transaction
        filledForm = TransactionForm(request.POST, instance=transaction)
        Transaction.saveTransaction(filledForm, request)
        return redirect('leBeau:leBeau', urlTag='all', order='-purchase_date', status='both')

    form = TransactionForm(instance=transaction)
    local_tags = Transaction.getLocalTags(id)
    return render(request, 'leBeauEdit.html', {'form':form, 'local_tags': local_tags, 'LEBEAU_CODE': LEBEAU_CODE})


def tagSearch(request):
    if request.is_ajax():
        search = request.GET.get('search')
        matching_tags = Transaction.getMatchingTags(search.lower())
        return JsonResponse({'response': matching_tags})
    return JsonResponse({'response': 'not ajax'})




