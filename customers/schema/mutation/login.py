import graphene
from customers.schema.query.user import UserNode
from django.contrib.auth import authenticate, login


class LogIn(graphene.Mutation):
    user = graphene.Field(UserNode)

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    @classmethod
    def mutate(cls, root, info, username, password):
        user = authenticate(username=username, password=password)

        if user is None:
            raise Exception('Please enter a correct username and password')

        if not user.is_active:
            raise Exception('It seems your account has been disabled')

        login(info.context, user)
        return cls(user=user)
