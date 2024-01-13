from rest_framework.decorators import api_view
from rest_framework.response import Response
from hiphoppizzawangsapi.models import User

@api_view(['POST'])
def check_user(request):

    uid = request.data['uid']
    user = User.objects.filter(uid=uid).first()

    if user is not None:
        data = {
          'id': user.id,
          'uid': user.uid,
          'name': user.name
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    user = User.objects.create(
      uid=request.data['uid'],
      name=request.data['name']
    )

    data = {
      'id': user.id,
      'uid': user.uid,
      'name': user.name
    }
    return Response(data)
