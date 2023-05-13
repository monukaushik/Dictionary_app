from django.shortcuts import render
import requests

def index(request):
    if request.method=='POST':
        input=request.POST.get('word')
        app_id = '5c77b0a4'
        app_key = '7647b13cb131b250c4f7fc87e2788a20'

        language = 'en'
        word_id = input
        fields = 'definitions'
        strictMatch = 'True'
        url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        data_string = r.json()
        if r.status_code != 404:
            definitions = data_string['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']
            data=definitions[0]
        else:
            print("The text you entered is not a valid word...Try Again")
            
    
        return render(request,'index.html',{'data':data})
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


