from django.conf                        import settings
from rest_framework                     import generics, status
from rest_framework.response            import Response
from rest_framework.permissions         import IsAuthenticated
from rest_framework_simplejwt.backends  import TokenBackend

from authApp.serializers.userSerializer import UserSerializer
from authApp.models.user                import User

class UserDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        token  = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        if valid_data['user_id'] != kwargs['pk']:
            string_response = {'detail':'You are not allowed to see this user'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)