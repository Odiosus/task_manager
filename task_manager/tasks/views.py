from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .documents import TaskDocument
from rest_framework.decorators import action
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch
from rest_framework.views import APIView
from rest_framework.response import Response
from elasticsearch_dsl import Q


@action(detail=False, methods=['get'])
def search(self, request):
    query = request.query_params.get('q', '')
    s = Search(index='tasks').query(
        MultiMatch(query=query, fields=['title', 'description'])
    )
    response = s.execute()
    tasks = [hit.meta.id for hit in response]
    results = Task.objects.filter(id__in=tasks)
    serializer = TaskSerializer(results, many=True)
    return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        task_document = TaskDocument()
        task_document.update_from_model(task)

    def perform_update(self, serializer):
        task = serializer.save()
        task_document = TaskDocument()
        task_document.update_from_model(task)


class TaskSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            q = Q(
                'multi_match',
                query=query,
                fields=['title', 'description'],
                fuzziness='auto'
            )
            search = TaskDocument.search().query(q)
            response = search.execute()
            return Response([hit.to_dict() for hit in response])

        return Response([])
