from django.shortcuts import render, redirect
from .models import Item
from .forms import NewItem, EditItem

def item_page(request, id):
    item = Item.objects.get(pk=id)
    other_items = Item.objects.filter(seller=item.seller).exclude(id=id)[0:6]
    return render(request, 'item/item_page.html', {'item':item, 'other_items':other_items})

def new_item(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewItem(request.POST, request.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                item.seller = request.user
                item.save()
                return redirect('item_page', id=item.id)
        else:
            form = NewItem()
        return render(request, 'item/form.html', {'form':form})
    else:
        return redirect('login')
    
def delete_item(request, id):

    item = Item.objects.get(pk=id, seller=request.user) 
    item.delete()
    return redirect('dashboard')

def edit_item(request, id):

    item = Item.objects.get(pk=id, seller=request.user) 
    if request.method == 'POST':
        form = EditItem(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_page', id=item.id)
    else:
        form = EditItem(instance=item)
    return render(request, 'item/form.html', {'form':form})
