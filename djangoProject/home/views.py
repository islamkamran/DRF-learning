from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer

@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        return Response(
            {
                "name": "Islamkamran",
                "method": "GET"
            }
        )
    elif request.method == 'POST':
        return Response(
            {
                "name": "Islamkamran",
                "method": "POST"
            }
        )
    else:
        return Response(
            {
                "message": "Method not allowed"
            }
        )


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        print(data)
        return Response({
            'status': True,
            'message': 'Success todo created'

        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Something went wrong'
    })
