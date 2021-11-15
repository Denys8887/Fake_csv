from django.urls import path
from fake_csv_app import views
from fake_csv_app.views import SchemaDeleteView, SchemaCreateView, SchemasView, \
    ColumnCreateView, SchemaUpdateView, ColumnDeleteView, ColumnUpdateView, DatasetsView, create_datasets, \
    DatasetDeleteView, check_status

urlpatterns = [
    path('', SchemasView.as_view(), name='schemas'),
    path('delete/<pk>/', SchemaDeleteView.as_view(), name='delete_schema'),
    path('edit/<pk>/', SchemaUpdateView.as_view(), name='edit_schema'),
    path('create/', SchemaCreateView.as_view(), name='create_schema'),
    path('create/<id_schema>/add_columns/', ColumnCreateView.as_view(), name='add_columns'),
    path('delete_column/<pk>/', ColumnDeleteView.as_view(), name='delete_column'),
    path('edit_column/<pk>/', ColumnUpdateView.as_view(), name='edit_column'),
    path('datasets/', DatasetsView.as_view(), name='datasets'),
    path('delete_dataset/<pk>/', DatasetDeleteView.as_view(), name='delete_dataset'),
    path('create_datasets/', create_datasets, name='create_datasets'),
    path('check_status/', check_status, name='check_status'),

    # Auth
    path('signupuser/', views.signupuser, name='signupuser'),
    path('login', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

]
