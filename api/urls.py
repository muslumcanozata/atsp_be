from django.urls import path
from api import views as api_views
from .views import procedures, proceduresDetails, postProceduresText

urlpatterns = [
    # path('procedures/', api_views.proceduresAPIView.as_view(), name="GET PROCEDURES"),
    path('procedures/', api_views.procedures, name="GET PROCEDURES"),
    path('proceduresdetails/', api_views.proceduresDetails, name="GET SPs TEXT"),
    path('postprocedurestext/', api_views.postProceduresText, name="POST SPs TEXT")
]