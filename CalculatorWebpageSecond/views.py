from django.shortcuts import render
from django.http import HttpResponse

def add_view(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        try:
            result = eval(expression)
        except Exception as e:
            result = f"Error: {str(e)}"
        return HttpResponse(f"The result is: {result}")
    return render(request, 'add.html')
