from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Task.models import TodoTask
from Task.api.serializers import TodoTaskserializers


@api_view(['GET'])
def get_all_tasks(request):
    if request.method == 'GET':
        query = TodoTask.objects.all()
        serializer = TodoTaskserializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_task(request,pk):
    try:
        task = TodoTask.objects.get(pk=pk)
    except TodoTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TodoTaskserializers(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_view(request,pk):
    try:
        task = TodoTask.objects.get(pk=pk)
    except TodoTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == 'PUT':
        serializer = TodoTaskserializers(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['anjam shod'] = "ba movafaghiyat"
            return Response(data=data ,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)