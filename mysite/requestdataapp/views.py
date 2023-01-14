from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UserBioForm, UploadFileForm


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context = {
        'a': a,
        'b': b,
        'result': result
    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        'form': UserBioForm(),
    }
    return render(request, 'requestdataapp/user-bio-form.html', context=context)

def handle_file_upload(request: HttpRequest) ->HttpResponse:
    """File sizes:
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB - 104857600
            250MB - 214958080
            500MB - 429916160
            """

    big_size = False
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = form.cleaned_data['file']
            if myfile.size > 5242880:
                big_size = True
            else:
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                print('saved file', filename)
    else:
        form = UploadFileForm()
    context = {
        'big_size': big_size,
        'form': form
    }
    return render(request, 'requestdataapp/file-upload.html', context=context)