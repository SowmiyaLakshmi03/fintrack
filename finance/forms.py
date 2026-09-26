from django import forms

from .models import Transaction, UserProfile


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction

        fields = (
            "title",
            "amount",
            "transaction_type",
            "category",
            "date",
            "description",
        )

        widgets = {  # noqa: RUF012
            "date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }


class CurrencyForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = (
            "currency",
        )

        labels = {  # noqa: RUF012
            "currency": "Preferred Currency",
        }