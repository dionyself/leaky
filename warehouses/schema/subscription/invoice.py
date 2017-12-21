from leaky.schema.subscription import Subscription
from warehouses.schema.mutation.invoice import CreateInvoice


class InvoiceSubscription(Subscription):
    class Meta:
        mutation_class = CreateInvoice
        stream = 'invoices'
        description = 'Invoice Subscription'
