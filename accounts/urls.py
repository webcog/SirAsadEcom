from django.urls import path
from .views import register
from .views import login
from .views import logout
from .views import activate
from .views import dashboard
from .views import forgotpassword
from .views import resetpassword_validate
from .views import resetpassword
from .views import my_orders
from .views import edit_profile
from .views import change_password
from .views import order_detail
from .views import view_all_orders_to_admin
from .views import view_all_users_to_admin
from .views import download_excel
from .views import account_search
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("", dashboard, name="dashboard"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path(
        "resetpassword_validate/<uidb64>/<token>/",
        resetpassword_validate,
        name="resetpassword_validate",
    ),
    path("forgotpassword/", forgotpassword, name="forgotpassword"),
    path("resetpassword", resetpassword, name="resetpassword"),
    path("my_orders/", my_orders, name="my_orders"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("change_password/", change_password, name="change_password"),
    path("order_detail/<str:order_id>/", order_detail, name="order_detail"),
    path("view_all_orders", view_all_orders_to_admin, name="all-admin-orders"),
    path("view_all_users", view_all_users_to_admin, name="all-admin-users"),
    path('download-excel/', download_excel, name='download_excel'),
    path('account-search/', account_search, name='account_search'),

]
