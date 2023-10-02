from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from .models import Invoice, InvoiceDetail


class InvoicesAPI(APIView):

    def post(self, request, format=None):

        invoice_data = request.data.get('invoice', {})
        invoice_detail_data = request.data.get('invoice_detail', {})

        invoice_serializer = InvoiceSerializer(data=invoice_data)
        if invoice_serializer.is_valid():
            invoice_instance = invoice_serializer.save()
        else:
            return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        invoice_detail_data['invoice'] = invoice_instance.id

        invoice_detail_serializer = InvoiceDetailSerializer(data=invoice_detail_data)

        if invoice_detail_serializer.is_valid():
            invoice_detail_serializer.save()
        else:
            invoice_instance.delete()
            return Response(invoice_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Invoice created successfully"}, status=status.HTTP_201_CREATED)

    
    def patch(self, request, pk, format=None):
        
        try:
            invoice = Invoice.objects.get(pk=pk)
            invoice_detail = InvoiceDetail.objects.get(invoice=invoice)
        except Invoice.DoesNotExist:
            return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        except InvoiceDetail.DoesNotExist:
            return Response({"message": "Invoice detail not found"}, status=status.HTTP_404_NOT_FOUND)

        invoice_serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
        invoice_detail_serializer = InvoiceDetailSerializer(invoice_detail, data=request.data, partial=True)

        if invoice_serializer.is_valid() and invoice_detail_serializer.is_valid():
            invoice_serializer.save()
            invoice_detail_serializer.save()
            return Response({
                "invoice": invoice_serializer.data,
                "invoice_detail": invoice_detail_serializer.data
            })
        return Response({
            "invoice_errors": invoice_serializer.errors,
            "invoice_detail_errors": invoice_detail_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

