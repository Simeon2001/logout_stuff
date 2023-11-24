
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework_simplejwt.tokens import RefreshToken
from models import BlackListJWT


@api_view(["get"])
@permission_classes([IsAuthenticated])
def logout(request):
    user_id = request.user.id  
    get_refresh = ""
    token = RefreshToken(get_refresh)
    token.blacklist()
    auth_token = request.auth.decode("utf-8")
    try:
        is_blackListed = BlackListJWT.objects.create(user=user_id, token=auth_token)
        return "USER LOGGED OUT"
    except BlackListJWT.DoesNotExist:
         return "INVAILD USER "
        

