from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from payment.models import Payable, Transaction
from payment.serializers import PayableSerializer, TransactionSerializer, PayableSerializerGet


class PayableAPIView(APIView):

    def get(self, request):
        service_type = request.query_params.get("service_type", None)
        queryset = Payable.objects.filter(service_type=service_type) if service_type else Payable.objects.exclude(status="1")
        serializer_class = PayableSerializer(queryset, many=True) if service_type else PayableSerializerGet(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer_class.data)

    def post(self, request):
        serializer = PayableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionAPIView(APIView):

    def get(self, request):
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        if not end_date or not start_date:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                "error": "You must provide start date and end date"
            })

        queryset = Transaction.objects.all()
        serializer_class = TransactionSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer_class.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
