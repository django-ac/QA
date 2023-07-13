from django.urls import path

from questions import views

app_name = "questions"
urlpatterns = [
    path("excel-to-pandas/", views.excel_to_pandas, name="excel-to-pandas"),
    path("form-input-number/", views.form_input_number, name="form-input-number"),
]
