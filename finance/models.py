from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):

    TRANSACTION_TYPES = (
        ("income", "Income"),
        ("expense", "Expense"),
    )

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    date = models.DateField()
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):

    CURRENCY_CHOICES = (
        ("INR", "INR (₹)"),
        ("USD", "USD ($)"),
        ("GBP", "GBP (£)"),
        ("EUR", "EUR (€)"),
        ("JPY", "JPY (¥)"),
        ("CNY", "CNY (¥)"),
        ("CAD", "CAD ($)"),
        ("AUD", "AUD ($)"),
        ("CHF", "CHF"),
        ("SGD", "SGD (S$)"),
        ("AED", "AED (د.إ)"),
        ("SAR", "SAR (ر.س)"),
        ("KRW", "KRW (₩)"),
        ("NZD", "NZD (NZ$)"),
        ("ZAR", "ZAR (R)"),
        ("BRL", "BRL (R$)"),
        ("MXN", "MXN ($)"),
        ("THB", "THB (฿)"),
        ("MYR", "MYR (RM)"),
        ("IDR", "IDR (Rp)"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default="INR"
    )

    def __str__(self):
        return f"{self.user.username} - {self.currency}"

# Create your models here.
