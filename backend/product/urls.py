from django.urls import path  # Import path for URL routing
from . import views  # Import views from the current directory
from django.http import JsonResponse  # Import JsonResponse for API root response

# Define the API root view
def api_root(request):
    return JsonResponse({
        "products": "/api/products/",
        "product-detail": "/api/product/<id>/",
        "product-create": "/api/product-create/",
        "product-update": "/api/product-update/<id>/",
        "product-delete": "/api/product-delete/<id>/",
    })

# URL patterns for the product app
urlpatterns = [
    path('', api_root, name="api-root"),  # Root URL for `/api/`
    path('products/', views.ProductView.as_view(), name="products-list"),  # List products
    path('product/<str:pk>/', views.ProductDetailView.as_view(), name="product-details"),  # Product details
    path('product-create/', views.ProductCreateView.as_view(), name="product-create"),  # Create product
    path('product-update/<str:pk>/', views.ProductEditView.as_view(), name="product-update"),  # Update product
    path('product-delete/<str:pk>/', views.ProductDeleteView.as_view(), name="product-delete"),  # Delete product
]
