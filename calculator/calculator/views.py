from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Home Page")


# To check even or odd number
def evenOdd(request):
    res = ''
    if request.method == 'POST':
        # Check if the input field is empty
        if request.POST.get('num') == '':
            return render(request, 'evenodd.html', {'error': True})
        
        # Convert the input to an integer
        num = int(request.POST.get('num'))
        if num % 2 == 0:
            res = 'Even Number'
        else:
            res = 'Odd Number'
        
        # Render the result
        return render(request, 'evenodd.html', {'res': res})
    
    # In case of a GET request, return the initial form
    return render(request, 'evenodd.html')

    
    
def markSheet(request):
    data = {}  # Initialize an empty dictionary at the start to avoid undefined errors
    if request.method == 'POST':
        # if request.POST.get('subject1') == '':  # We can use this when any field is empty and user submits the form
        #     return render(request, 'marksheet.html', {'error': True})
        s1 = int(request.POST.get('subject1'))
        s2 = int(request.POST.get('subject2'))
        s3 = int(request.POST.get('subject3'))
        s4 = int(request.POST.get('subject4'))
        s5 = int(request.POST.get('subject5'))
        
        t = s1 + s2 + s3 + s4 + s5
        per = t * 100 / 500

        if per >= 60:
            div = 'First Division'
        elif per >= 48:
            div = 'Second Division'
        elif per >= 35:
            div = 'Third Division'
        else:
            div = 'Fail'  # where the percentage is below 35

        data = {
            'total': t,
            'percentage': per,
            'division': div
        }
        
        return render(request, 'marksheet.html', data)

    return render(request, 'marksheet.html')


def Calculator(request):
    res = 0
    data = {}
    try:
        if request.method == 'POST':
            n1 = request.POST.get('num1')
            n2 = request.POST.get('num2')
            opr = request.POST.get('opr')

            # Check if n1 and n2 are not empty
            if n1 and n2:
                n1 = int(n1)
                n2 = int(n2)
                if opr == '+':
                    res = n1 + n2
                elif opr == '-':
                    res = n1 - n2
                elif opr == '*':
                    res = n1 * n2
                elif opr == '/':
                    if n2 != 0:
                        res = n1 // n2
                    else:
                        res = "Cannot divide by zero"

                data = {
                    'n1': n1,
                    'n2': n2,
                    'opr': opr,
                    'out': res,
                }
            else:
                res = "Please provide both numbers"

    except Exception as e:
        res = f"An error occurred: {e}"

    return render(request, "Calculator.html", data)
