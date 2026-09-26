from django.contrib import admin
from django.urls import path

from finance.views import (
    add_transaction,
    dashboard,
    delete_transaction,
    edit_transaction,
    login_view,
    logout_view,
    register_view,
    transactions,
)

urlpatterns = [

    # Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Dashboard
    path(
        "",
        dashboard,
        name="dashboard"
    ),

    # Transactions
    path(
        "transactions/",
        transactions,
        name="transactions"
    ),

    # Add transaction
    path(
        "add-transaction/",
        add_transaction,
        name="add_transaction"
    ),

    # Edit transaction
    path(
        "edit-transaction/<int:pk>/",
        edit_transaction,
        name="edit_transaction"
    ),

    # Delete transaction
    path(
        "delete-transaction/<int:pk>/",
        delete_transaction,
        name="delete_transaction"
    ),

    # Registration
    path(
        "register/",
        register_view,
        name="register"
    ),

    # Login
    path(
        "login/",
        login_view,
        name="login"
    ),

    # Logout
    path(
        "logout/",
        logout_view,
        name="logout"
    ),
]