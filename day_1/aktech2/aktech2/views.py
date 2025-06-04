from django.shortcuts import render

def home_page(request):
    data={
        'title':'Home Page',
        "course_list":['Python','Java','Php','JavaScript'],
        'numbers':[10,20,30,40,50,55,65,85],
        'student_details':[
            {'Name':'Amit',
            'Phone':'8303166787',},
            {'Name':'Advik','Phone':'9115206240'}
        ]
    }
    return render(request, 'index.html',data)  # Render the index.html template
