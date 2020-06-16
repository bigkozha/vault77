from counter.models import Counter
from django.shortcuts import render


def counter(request):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    return render(request, 'counter.html', {'instance': instance})
