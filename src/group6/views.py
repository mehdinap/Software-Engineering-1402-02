from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer


class FAQChildrenView(APIView):
    def get(self, request, parent_id):
        try:
            parent_node = FAQ.objects.get(pk=parent_id)
        except FAQ.DoesNotExist:
            return Response({'error': 'FAQ node not found'}, status=status.HTTP_404_NOT_FOUND)

        children = parent_node.get_children()
        serializer = FAQSerializer(children, many=True)
        return Response(serializer.data)


class FAQRootsView(APIView):
    def get(self, request):
        root_faqs = FAQ.objects.filter(parent__isnull=True)
        serializer = FAQSerializer(root_faqs, many=True)
        return Response(serializer.data)
