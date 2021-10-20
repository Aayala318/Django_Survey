from django.shortcuts import render, redirect

LANGUAGES = (
    'Python',
    'JavaScript',
    'C#',
    'Java'
)
LOCATIONS = (
    'San Jose',
    'Seattle',
    'Chicago',
    'Online'
)
# Create your views here.
def index(request):
    return render (request, 'form.html')

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    return redirect('/result')


def result(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comment': request.POST['comment'],
        }
    return render (request, 'result.html', context)