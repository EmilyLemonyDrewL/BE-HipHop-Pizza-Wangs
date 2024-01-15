from rest_framework.decorators import api_view
from rest_framework.response import Response
from hiphoppizzawangsapi.models import User

@api_view(['POST'])
def check_user(request):

    uid = request.data['uid']
    cashier = User.objects.filter(uid=uid).first()

    if cashier is not None:
        data = {
          'id': cashier.id,
          'uid': cashier.uid,
          'name': cashier.name
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    cashier = User.objects.create(
      uid=request.data['uid'],
      name=request.data['name']
    )

    data = {
      'id': cashier.id,
      'uid': cashier.uid,
      'name': cashier.name
    }
    return Response(data)
