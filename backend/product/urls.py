from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "products": "/api/products/",
        "product-detail": "/api/product/<id>/",
        "product-create": "/api/product-create/",
        "product-update": "/api/product-update/<id>/",
        "product-delete": "/api/product-delete/<id>/",
    })

urlpatterns = [
    path('', api_root, name="api-root"),  # Add this line for `/api/`
    path('products/', views.ProductView.as_view(), name="products-list"),
    path('product/<str:pk>/', views.ProductDetailView.as_view(), name="product-details"),
    path('product-create/', views.ProductCreateView.as_view(), name="product-create"),
    path('product-update/<str:pk>/', views.ProductEditView.as_view(), name="product-update"),
    path('product-delete/<str:pk>/', views.ProductDeleteView.as_view(), name="product-delete"),
]
