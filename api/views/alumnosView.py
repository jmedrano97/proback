from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from api.serializer import AlumnosSerializer
from api.models import Alumnos
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_description="Obtener una lista de todos los alumnos",
    responses={200: AlumnosSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    operation_description="Crear un nuevo alumno",
    request_body=AlumnosSerializer,
    responses={201: AlumnosSerializer, 400: 'Solicitud inválida'}
)
@api_view(['GET', 'POST'])
def alumnos_list(request):
    if request.method == 'GET':
        alumnos = Alumnos.objects.all()
        serializer = AlumnosSerializer(alumnos, many=True)
        return Response(serializer.data)  
    
    elif request.method == 'POST':
        serializer = AlumnosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # telefonos = request.data.get('telefonos')
            # if telefonos:
            #     for telefono in telefonos:
            #         alumno = Alumnos.objects.get(pk=serializer.data['id'])
            #         alumno.telefonos.create(numero=telefono['numero'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_description="Obtener un alumno por su ID",
    responses={200: AlumnosSerializer, 404: 'Alumno no encontrado'}
)
@swagger_auto_schema(
    method='put',
    operation_description="Actualizar un alumno por su ID",
    request_body=AlumnosSerializer,
    responses={200: AlumnosSerializer, 400: 'Solicitud inválida'}
)
@swagger_auto_schema(
    method='patch',
    operation_description="Actualizar parcialmente un alumno por su ID",
    request_body=AlumnosSerializer,
    responses={200: AlumnosSerializer, 400: 'Solicitud inválida'}
)
@swagger_auto_schema(
    method='delete',
    operation_description="Eliminar un alumno por su ID",
    responses={204: 'Sin contenido', 404: 'Alumno no encontrado'}
)
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def alumnos_detail(request, pk):
    try:
        alumno = Alumnos.objects.get(pk=pk)
    except Alumnos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlumnosSerializer(alumno)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AlumnosSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = AlumnosSerializer(alumno, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
