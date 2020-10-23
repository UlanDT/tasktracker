from rest_framework.viewsets import ModelViewSet
from .serializers import MemberSerializer
from .models import Member


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
