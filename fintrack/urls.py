from django.contrib import admin
from django.urls import path

from finance.views import (
    add_transaction,
    currency_settings,
    dashboard,
    delete_transaction,
    edit_transaction,
    login_view,
    logout_view,
    register_view,
    transactions,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("transactions/", transactions, name="transactions"),
    path("add-transaction/", add_transaction, name="add_transaction"),
    path(
        "edit-transaction/<int:pk>/",
        edit_transaction,
        name="edit_transaction",
    ),
    path(
        "delete-transaction/<int:pk>/",
        delete_transaction,
        name="delete_transaction",
    ),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
        "settings/currency/",
        currency_settings,
        name="currency_settings",
    ),
]