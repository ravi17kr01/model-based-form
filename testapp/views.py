from django.shortcuts import render
from testapp import forms

def student_view(request):
    form = forms.StudentForm()
    if request.method=='POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('data inserted in DB successfuly')
    return render(request, 'testapp/register.html', {'form':form})
