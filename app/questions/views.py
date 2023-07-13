from io import BytesIO

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pandas import DataFrame


def edit_df(df: DataFrame):
    df.iloc[0, 0] = "Edit first cell"


@csrf_exempt
def excel_to_pandas(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        df = pd.read_excel(file)

        # 다른 함수에서 DataFrame편집
        edit_df(df)

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


@csrf_exempt
def form_input_number(request):
    if request.method == "POST":
        num1 = int(request.POST["num1"])
        num2 = int(request.POST["num2"])
        result = num1 + num2
        print("num1:", num1)
        print("num2:", num2)
        print("result:", result)
    return render(request, "questions/form_input_number.html")
