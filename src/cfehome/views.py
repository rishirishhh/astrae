from django.http import HttpResponse

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "query_set": queryset
    }

    html_template = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)