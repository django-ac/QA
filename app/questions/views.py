from io import BytesIO

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def excel_to_pandas(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        df = pd.read_excel(file)

        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine="openpyxl")
            df.to_excel(writer, sheet_name="sample_sheet")
            writer.close()
            response_data = b.getvalue()

        return HttpResponse(
            response_data,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    return render(request, "questions/excel_to_pandas.html")
