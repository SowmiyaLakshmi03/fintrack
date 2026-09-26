from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TransactionForm
from .models import Category, Transaction


@login_required
def dashboard(request):

    transactions = Transaction.objects.filter(
        user=request.user
    )

    total_income = (
        transactions
        .filter(transaction_type="income")
        .aggregate(total=Sum("amount"))["total"]
        or 0
    )

    total_expenses = (
        transactions
        .filter(transaction_type="expense")
        .aggregate(total=Sum("amount"))["total"]
        or 0
    )

    balance = total_income - total_expenses

    category_expenses = list(
        transactions
        .filter(transaction_type="expense")
        .values("category__name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )

    for item in category_expenses:
        item["total"] = float(item["total"])

    return render(
        request,
        "dashboard.html",
        {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": balance,
            "category_expenses": category_expenses,
        },
    )


@login_required
def transactions(request):

    transactions = Transaction.objects.filter(
        user=request.user
    ).order_by("-date")

    search = request.GET.get("search", "")
    category = request.GET.get("category", "")
    transaction_type = request.GET.get("type", "")

    if search:
        transactions = transactions.filter(
            title__icontains=search
        )

    if category:
        transactions = transactions.filter(
            category_id=category
        )

    if transaction_type:
        transactions = transactions.filter(
            transaction_type=transaction_type
        )

    categories = Category.objects.all()

    return render(
        request,
        "transactions.html",
        {
            "transactions": transactions,
            "categories": categories,
            "search": search,
            "selected_category": category,
            "selected_type": transaction_type,
        },
    )


@login_required
def add_transaction(request):

    if request.method == "POST":

        form = TransactionForm(request.POST)

        if form.is_valid():

            transaction = form.save(commit=False)

            transaction.user = request.user

            transaction.save()

            return redirect("transactions")

    else:

        form = TransactionForm()

    return render(
        request,
        "add_transaction.html",
        {
            "form": form,
        },
    )


@login_required
def edit_transaction(request, pk):

    transaction = get_object_or_404(
        Transaction,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":

        form = TransactionForm(
            request.POST,
            instance=transaction,
        )

        if form.is_valid():

            transaction = form.save(commit=False)

            transaction.user = request.user

            transaction.save()

            return redirect("transactions")

    else:

        form = TransactionForm(
            instance=transaction,
        )

    return render(
        request,
        "edit_transaction.html",
        {
            "form": form,
            "transaction": transaction,
        },
    )


@login_required
def delete_transaction(request, pk):

    transaction = get_object_or_404(
        Transaction,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":

        transaction.delete()

        return redirect("transactions")

    return render(
        request,
        "delete_transaction.html",
        {
            "transaction": transaction,
        },
    )


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("dashboard")

    else:

        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST,
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect("dashboard")

    else:

        form = AuthenticationForm()

    return render(
        request,
        "registration/login.html",
        {
            "form": form,
        },
    )


def logout_view(request):

    logout(request)

    return redirect("login")