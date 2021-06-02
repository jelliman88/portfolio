from django.db import models
import ast

class Transaction(models.Model):
    item = models.CharField(max_length=100)
    purchase_price = models.IntegerField()
    purchase_date = models.DateField()
    selling_price = models.IntegerField(null=True, blank=True)
    selling_date = models.DateField(null=True, blank=True)
    sold = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    profit = models.IntegerField(null=True, blank=True)
    tags = models.TextField(default='[]')
    thumbnail = models.ImageField(upload_to='lebeau/thumbnails', blank=True)

    def getTransactions(tag, order, status):
        if tag == 'all':
            if status == 'both':
                queryset = Transaction.objects.all().order_by(order)
                return queryset

            queryset = Transaction.objects.all().filter(sold=status).order_by(order)
            return queryset
        if status == 'both':
            queryset = Transaction.objects.all().filter(tags__contains=tag).order_by(order)
            return queryset

        queryset = Transaction.objects.all().filter(tags__contains=tag, sold=status).order_by(order)
        return queryset
        
    def getTotals(queryset):
        purchase_prices = []
        selling_prices = []
        #counter is used to get total of items in transactions, must be better way to get length of queryset
        counter = 0
        for obj in queryset:
            counter +=1 
            purchase_prices.append(obj.purchase_price)
            if obj.selling_price:
                selling_prices.append(obj.selling_price)
                

        totals = [
            counter,
            sum(purchase_prices),
            sum(selling_prices),
            # overall profit/loss
            sum(selling_prices) - sum(purchase_prices)
        ]
        return totals

    def saveTransaction(filledForm, request):
        instance = filledForm.save(commit=False)
        # tags
        if instance.tags == "[]":
            instance.tags = f"['{request.POST['item']}']"
        # profit & status
        if instance.selling_price:
            instance.sold = True
            instance.profit = instance.selling_price - instance.purchase_price
        # thumbnail
        if instance.item:
            img = request.FILES.get('thumbnail')
            print(img)
            if img:
                instance.thumbnail = img
        instance.save()

    # for ajax
    def getMatchingTags(search):
        matching_tags = []
        queryset = Transaction.objects.values('tags').filter(tags__contains=search)
        for d in queryset:
            for key, value in d.items():
                tag_list = ast.literal_eval(value)
                for i in tag_list:
                    if search in i and i not in matching_tags and i.startswith(search):
                        matching_tags.append(i)
        return matching_tags

    def getLocalTags(id):
       queryset = Transaction.objects.values('tags').filter(id=id)
       local_tags = ast.literal_eval(queryset[0]['tags'])
       return local_tags





