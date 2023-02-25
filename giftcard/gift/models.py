from django.db import models

# Create your models here.


class GiftCard(models.Model):
    gitf_card_number = models.CharField(max_length=200, blank=True, null=True)
    gift_card_access_number = models.CharField(
        max_length=200, blank=True, null=True)


class GiftCardBalance(models.Model):
    gift_card_number = models.ForeignKey(
        'gitf.GiftCard', related_name='gift_card_id', on_delete=models.CASCADE, primary_key=True)
    gift_card_user = models.ForeignKey(
        'user.User', related_name='gift_card_user', on_delete=models.CASCADE)
    gift_card_balance = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self) -> str:
        return self.gift_card_number
