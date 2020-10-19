
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

from basement.admin import render
from customers.models import Customer

from invoices.models import SaleItem, ArrivalItem


@staff_member_required
def get_customer_detail(request, customer_id):

    customer = get_object_or_404(Customer, id=customer_id)

    return render(request, 'customers/detail.html', {
        'object': customer,
        'sale_items': (
            SaleItem
                .objects
                .filter(invoice__customer=customer)
                .select_related('invoice')
                .order_by('-invoice__created')
        ),
        'arrival_items': (
            ArrivalItem
                .objects
                .filter(invoice__customer=customer)
                .select_related('invoice')
                .order_by('-invoice__created')
        )
    })
