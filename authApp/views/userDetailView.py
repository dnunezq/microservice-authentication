from django.conf                        import settings
from rest_framework                     import generics, status
from rest_framework.response            import Response
from rest_framework.permissions         import IsAuthenticated
from rest_framework_simplejwt.backends  import TokenBackend

from authApp.serializers.userSerializer import UserSerializer
from authApp.models.user                import User

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

  
class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    

class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    
