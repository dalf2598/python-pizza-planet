from app.plugins import ma
from .models import Ingredient, Size, Order, Beverage, OrderDetail


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')

class OrderDetailSerializer(ma.SQLAlchemyAutoSchema):
    ingredient = ma.Nested(IngredientSerializer)
    size = ma.Nested(SizeSerializer)
    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = OrderDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient',
            'size_price',
            'size',
            'beverage_price',
            'beverage',
        )

class OrderSerializer(ma.SQLAlchemyAutoSchema):
    detail = ma.Nested(OrderDetailSerializer, many=True)
    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'detail'
        )
