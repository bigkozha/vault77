from django.shortcuts import redirect, render

from counter.models import Counter


def counter(request):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.save()
    return render(request, 'counter.html', {'instance': instance})


def increment(request):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    return redirect('/', request)


def decrement(request):
    instance, created = Counter.objects.get_or_create(id=1)
    if (instance.value > 0):
        instance.value -= 1
        instance.save()
        return redirect('/', request)
    else:
        return redirect('/error', request)


def error(request):
    return render(request, 'error.html')
