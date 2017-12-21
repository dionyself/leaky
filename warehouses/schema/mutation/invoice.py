import graphene
from warehouses.models import Invoice
from graphene.types.generic import GenericScalar


class CreateInvoice(graphene.Mutation):
    class Arguments:
        fiscal_id = graphene.String()
        header = GenericScalar()
        body = GenericScalar()
        footer = GenericScalar()
        is_reversed = graphene.Boolean()
        is_blocked = graphene.Boolean()
        is_processed = graphene.Boolean()

    invoice_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            invoice = Invoice.objects.create(**args)
            ok = True
        except:
            invoice = None

        return CreateInvoice(
            invoice_id=invoice and invoice.id or 0,
            ok=ok)


class UpdateInvoice(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        fiscal_id = graphene.String()
        header = GenericScalar()
        body = GenericScalar()
        footer = GenericScalar()
        is_reversed = graphene.Boolean()
        is_blocked = graphene.Boolean()
        is_processed = graphene.Boolean()

    invoice_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        invoice = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                Invoice.objects.filter(id=pk).update(**args)
                invoice = Invoice.objects.filter(id=pk).first()
                ok = True
        except:
            invoice = None

        return UpdateInvoice(
            invoice_id=invoice and invoice.id or 0,
            ok=ok)
