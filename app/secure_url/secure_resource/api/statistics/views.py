from secure_resource.models import SecureUrl, SecureFile
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from itertools import zip_longest
from collections import defaultdict
from django.db.models import Q

visited_at_least_once = Q(visited__gte=0)


@require_http_methods(["GET"])
def stats_overall(request):
    files = list(
        SecureFile.objects.filter(visited_at_least_once)
        .values("created_at")
        .annotate(files=Count("created_at"))
        .order_by()
    )

    urls = list(
        SecureUrl.objects.filter(visited_at_least_once)
        .values("created_at")
        .annotate(links=Count("created_at"))
        .order_by()
    )

    results = []
    for file_data, url_data in zip_longest(files, urls, fillvalue={}):
        print(file_data, url_data)
        data = {}
        date = str(file_data.get("created_at", url_data.get("created_at")))
        data[date] = {"files": 0, "links": 0}
        if file_data:
            data[date]["files"] = file_data["files"]

        if url_data:
            data[date]["links"] = url_data["links"]
        results.append(data)

    return JsonResponse(results, safe=False)
