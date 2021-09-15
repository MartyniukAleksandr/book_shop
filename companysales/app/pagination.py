from django.core.paginator import Paginator

def pagination(num_items_page, obj, request):
    """
    a function that returns an object of the Paginator class
    :param num_items_page: integer, number of items per page
    :param obj: List of objects
    :param request: get request getting page numbers for example "request.GET.get('page')"
    :return: object of class by Paginator
    """
    paginator = Paginator(obj, num_items_page)
    page_num = request  # example "request.GET.get('page')"
    page_obj = paginator.get_page(page_num)
    return page_obj