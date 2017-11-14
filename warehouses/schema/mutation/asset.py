import graphene
from datetime import datetime
from customers.models import Product
from warehouses.models import Asset
from djmoney.money import Money


class CreateAsset(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()
        product_code = graphene.Int()
        price = graphene.Int()
        existence = graphene.Int()
        properties = graphene.String()
        tags = graphene.String()
        asset_type = graphene.String()
        category = graphene.String()
        duration = graphene.String()
        expires_at = graphene.String()
        starts_at = graphene.String()
        is_deleted = graphene.Boolean()
        is_expired = graphene.Boolean()

    asset_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        parsed_args = args.copy()
        if "product_id" in args:
            del parsed_args["product_id"]
        if "product_code" in args:
            del parsed_args["product_code"]
        if "starts_at" in args:
            parsed_args["starts_at"] = datetime.strptime(
                args["starts_at"], "%Y-%m-%d %H:%M:%S.%f")
        else:
            parsed_args["starts_at"] = datetime.now()
        if "expires_at" in args:
            parsed_args["expires_at"] = datetime.strptime(
                args["expires_at"], "%Y-%m-%d %H:%M:%S.%f")
            parsed_args["duration"] = args["expires_at"] - parsed_args["starts_at"]
        elif "duration" in args:
            t = datetime.datetime.strptime(args["duration"], "%H:%M:%S")
            parsed_args["duration"] = datetime.timedelta(
                hours=t.hour, minutes=t.minute, seconds=t.second)
            args["expires_at"] = parsed_args["starts_at"] + parsed_args["duration"]

        parsed_args.update(
            product=Product.objects.filter(
                id=args.get("product_id")) or (
                    Product.objects.filter(
                        product_code=args["product_code"]) if args.get(
                            "product_code") else None),
            price=Money(args.get("price", 0)),
        )
        try:
            asset = Asset.objects.create(**parsed_args)
            ok = True
        except:
            asset = None

        return CreateAsset(
            asset_id=asset and asset.id or 0,
            ok=ok)
