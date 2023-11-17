from rest_framework import generics, permissions, status, response
from .models import Posts
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly, IsSuperuserOrReadOnly

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsSuperuserOrReadOnly | IsOwnerOrReadOnly]
    