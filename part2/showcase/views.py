from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import DemoItem
from django.http import HttpResponse
# Create your views here.


def components_view(request):
    return render(request, 'showcases/components.html')

class javascripts_view(TemplateView):
    template_name = "showcases/javascripts.html"
    
# FBV

def htmx_item_add_view(request):
    if request.method != "POST":
        return HttpResponse(status=405)

    title = request.POST.get("title", "").strip()
    if title:
        DemoItem.objects.create(title=title)
    return render(request, "showcase/partials/demo_item_list.html", {"items": DemoItem.objects.all()})


def htmx_demo_view(request):
    demo_items = DemoItem.objects.all()
    return render(request, "showcases/htmx_demo.html", {"demo_items" : demo_items})
    
def htmx_item_delete_view(request, pk):
    item_delete = get_object_or_404(DemoItem, pk=pk)
    
    if request.method == "DELETE":
        item_delete.delete()
        return HttpResponse("") #จะเอาเปล่าไปแทน
    return HttpResponse(status=405) # method not allow


def htmx_item_edit_form_view(request, pk):
    item = get_object_or_404(DemoItem, pk=pk)
    return render(request, "showcase/partials/demo_item_edit_form.html", {"item": item})


def htmx_item_update_view(request, pk):
    item = get_object_or_404(DemoItem, pk=pk)
    if request.method != "POST":
        return HttpResponse(status=405)

    title = request.POST.get("title", "").strip()
    if title:
        item.title = title
        item.save(update_fields=["title"])
    return render(request, "showcase/partials/demo_item_row.html", {"item": item})