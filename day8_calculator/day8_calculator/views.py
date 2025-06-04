from django.shortcuts import render

def my_calculator(request):
    ans = 0
    error_message = ""

    if request.method == 'GET':
        # Get the values from the form
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')
        opr = request.GET.get('opr')

        # Ensure num1, num2, and opr are provided
        if num1 and num2 and opr:
            try:
                # Convert num1 and num2 to float
                n1 = float(num1)
                n2 = float(num2)

                # Perform the calculation based on the operator
                if opr == '+':
                    ans = n1 + n2
                elif opr == '-':
                    ans = n1 - n2
                elif opr == '*':
                    ans = n1 * n2
                elif opr == '/':
                    if n2 == 0:
                        error_message = "Cannot divide by zero."
                    else:
                        ans = n1 / n2
            except Exception as e:
                error_message=e

    # Return the result or error message to the template
    return render(request, 'calculator.html', {'ans': ans, 'error': error_message})
