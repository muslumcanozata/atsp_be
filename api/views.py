from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

import cx_Oracle

# class proceduresAPIView(APIView):
    
#     def get(self, request):
#         cursor = connection.cursor()
#         # raw_query_2 = "select * from DUAL"
#         raw_query = '''select OWNER, OBJECT_NAME from all_objects where OBJECT_TYPE='PROCEDURE' order by 1, 2'''
#         # raw_query = "SELECT TEXT FROM ALL_SOURCE WHERE NAME='MNK_SEL_REESKONTREPODETAY_SP' AND OWNER='FINARTYTL' ORDER BY LINE"
#         context = cursor.execute(raw_query)
#         return Response(context)

@api_view(['GET', 'POST'])
def procedures(request):
    if request.method == 'POST':
        data = request.data
        connection = cx_Oracle.connect(user=data.get('user'), password=data.get('password'), dsn=data.get('dsn'))
        with connection.cursor() as cursor:
            raw_query = '''select OWNER, OBJECT_NAME from all_objects where OBJECT_TYPE='PROCEDURE' order by 1, 2'''
            cursor.execute(raw_query)
            context = cursor.fetchall()
        obj = list()
        for i in range(0, len(context)):
            obj.append({"id": i, "owner": context[i][0], "name": context[i][1]})
        return Response({"message": "Login Succesful.", "data": obj})
    return Response()



# @api_view(['GET', 'POST'])
# def proceduresDetails(request):
#     if request.method == 'POST':
#         cursor = connection.cursor()
#         data = request.data
#         data2 = list()
#         for i in range(0, len(data)):
#             param = data[i]
#             cursor.execute('''SELECT TEXT FROM ALL_SOURCE WHERE NAME='{}' ORDER BY NAME, LINE'''.format(param))
#             data2.append(cursor.fetchall())
#         return Response({"message": "Done", "data": data2})
#     return Response()

@api_view(['GET', 'POST'])
def proceduresDetails(request):
    if request.method == 'POST':
        data = request.data
        prods=data.get('prods')
        data2=list()
        connection = cx_Oracle.connect(user=data.get('user'), password=data.get('password'), dsn=data.get('dsn'))
        with connection.cursor() as cursor:
            for i in range(0, len(prods)):
                cursor.execute('''SELECT TEXT FROM ALL_SOURCE WHERE NAME='{}' ORDER BY NAME, LINE'''.format(prods[i]))
                data2.append(cursor.fetchall())
        return Response({"message": "Done", "data": {"details": data2, "names": prods}})
    return Response()

# @api_view(['GET', 'POST'])
# def postProceduresText(request):
#     if request.method == 'POST':
#         cursor = connection.cursor()
#         data = request.data
#         for i in range(0, len(data)):
#             cursor.execute('''INSERT INTO TEXTS_ VALUES('{0})'''.format(data[i]))
#         return Response({"message": "Row inserted", "data": data2})
#     return Response()

# @api_view(['GET', 'POST'])
# def postProceduresText(request):
#     if request.method == 'POST':
#         data = request.data
#         text = data.get('texts')
#         print(data)
#         connection = cx_Oracle.connect(user=data.get('user'), password=data.get('password'), dsn=data.get('dsn'))
#         with connection.cursor() as cursor:
#             for i in range(0, len(text)):
#                 # print('''INSERT INTO TEXTS_ (TEXT_) VALUES('{0}')'''.format(text[i]))
#                 cursor.execute('''INSERT INTO TEXTS_ (TEXT_) VALUES (:data)''', data=text[i])
#                 connection.commit()
#         return Response({"message": "Rows inserted"})
#     return Response()

    
@api_view(['GET', 'POST'])
def postProceduresText(request):
    if request.method == 'POST':
        data = request.data
        text = data.get('texts')
        connection = cx_Oracle.connect(user=data.get('user'), password=data.get('password'), dsn=data.get('dsn'))
        with connection.cursor() as cursor:
            for i in range(0, len(text)):
                sql=str('CREATE OR REPLACE ' + text[i])
                cursor.execute(sql)
            if(len(text)==1):
                return Response({"message": "Procedure copied."})
            else:
                return Response({"message": "Procedure copied."})
    return Response()