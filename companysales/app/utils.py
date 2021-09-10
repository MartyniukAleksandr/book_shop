def no_duplicate(qs_obj):
    """
    Функция отсекающая дубликаты, принемает параметер QuerySet
    кторой являеться результатом Model.objects.get(), Model.objects.all(), Model.objects.filter() и т.д
    """
    result = []
    ids = []
    for i in qs_obj:
        if i.pk not in ids:
            ids.append(i.pk)
            result.append(i)
    return result
