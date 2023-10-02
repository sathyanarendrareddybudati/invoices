from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoicesAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(customer_name="Initial Name")
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice, description="Initial Description", quantity=1, unit_price=100, price=100
        )

    def tearDown(self):
        self.invoice.delete()
        self.invoice_detail.delete()

    def test_create_invoice(self):

        data = {
            "invoice": {
                "customer_name": "shafi",
            },
            "invoice_detail": {
                "description": "Sample description",
                "quantity": 2,
                "unit_price": 50,
                "price": 100,
            }
        }

        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)
        self.assertEqual(InvoiceDetail.objects.count(), 2)

    def test_update_invoice(self):

        data = {
            "invoice": self.invoice.pk,
            "invoice_detail": {
                "description": "Updated Description",
            }
        }
        response = self.client.patch(f'/invoices/{self.invoice.pk}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.invoice_detail.refresh_from_db()

        self.assertEqual(self.invoice_detail.description, "Updated Description")
