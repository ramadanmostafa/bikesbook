from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyPlacesSerializer
from .permissions import IsAuthenticated, IsOwner
from ..models import MyPlaces

class MyPlacesListAPIView(ListAPIView):
    '''
     list of current user saved places
    '''
    serializer_class = MyPlacesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):

        return MyPlaces.objects.filter(user=self.request.user)

class AddNewPlaceCreateAPIView(CreateAPIView):
    """
    Add a new record to my places table, location name should be unique for each user.
    :return { "code":1 } if created successfully 
    :return { "code":-1 } if new location name already exists, You should ask the user to change the location_name
    and try again or update the older one
    """
    serializer_class = MyPlacesSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not MyPlaces.objects.filter(user=self.request.user, location_name=request.data["location_name"]):
                new_place = MyPlaces(user=request.user, **serializer.data)
                new_place.save()
                return Response(MyPlacesSerializer(new_place).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"code": -1}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteMyPlaceDestroyAPIView(DestroyAPIView):
    """
    delete my place 
    """
    queryset = MyPlaces.objects.all()
    lookup_field = 'pk'
    serializer_class = MyPlacesSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class UpdateMyPlaceAPIView(RetrieveUpdateAPIView):
    """
    update my place
    :returns {"code":-1} if the new location name already exists in the user locations
    """
    queryset = MyPlaces.objects.all()
    lookup_field = 'pk'
    serializer_class = MyPlacesSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        if not MyPlaces.objects.filter(user=self.request.user, location_name=request.data["location_name"]):
            return super(UpdateMyPlaceAPIView, self).update(request, *args, partial=True)
        else:
            return Response({"code":-1}, status=status.HTTP_400_BAD_REQUEST)


