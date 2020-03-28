from django.shortcuts import render
import requests
import csv


# Create your views here.
def home(request):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    
    r = requests.get(url,stream=True)
    f = (line.decode('utf-8') for line in r.iter_lines())
    reader = list(csv.reader(f))
    print(reader)
    output = []
    todays_total = 0
    prev_total = 0
    for row in reader[1:]:
        temp = {
            'province':row[0],
            'country':row[1],
            'affected_people':row[-1]
        }
        todays_total += int(row[-1])
        prev_total += int(row[-2])
        output.append(temp)

    
    r.close()
    context = {
        'todays_total':todays_total,
        'prev_total':prev_total,
        'coronas' :output
    }
    for con in context:
        print('\n')
        print(con)    
    return render(request,'home.html',context)