# calculator/views.py

from django.shortcuts import render
from .forms import CalculatorForm

def calculator(request):
    form = CalculatorForm()

    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            result = str(eval(expression))
        except:
            result = 'Error'

        form = CalculatorForm(initial={'expression': result})

    return render(request, 'calculator.html', {'form': form})
