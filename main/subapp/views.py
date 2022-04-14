from django.shortcuts import render
from rest_framework.decorators import api_view
import pandas as pd
from django.http import HttpResponse
import csv
# Create your views here.


@api_view(['GET'])
def csv_file(request):
    if request.method == 'GET':
        df_healthians = pd.read_csv(r"subapp/healthians.csv")
        df_lab = pd.read_csv(r"subapp/mahe.csv")
        from difflib import SequenceMatcher
        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()

        df = pd.concat([df_healthians, df_lab], axis = 1)
        df = df.fillna('')
        df_list = df.values.tolist()
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )
        writer = csv.writer(response)
        for i in range(0, len(df_list)):
            for j in range(0,len(df_list)):
                if (similar (df_list[i][0],df_list[j][1])) > 0.70:
                    writer.writerow([df_list[j][1],df_list[i][0]])
    return response