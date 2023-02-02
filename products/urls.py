from django.urls import path
from .views import   basket_remove, ProductsListView, BasketAddView

app_name = 'products'

urlpatterns = [

    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view( ), name='paginator'),
    # path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/add/<int:product_id>/', BasketAddView.as_view(), name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),

]
