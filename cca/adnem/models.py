from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=255, null=False, blank=False)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login_at = models.DateTimeField(null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

# 広告掲載先
class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    host = models.CharField(max_length=255, null=False, blank=False)
    url = models.TextField(null=False, blank=False)
    activate_state = models.IntegerField(null=False, blank=False, default=0)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    type = models.CharField(max_length=32, null=True, blank=True)
    uid = models.CharField(max_length=255, null=False, blank=False)
    token = models.TextField(null=True, blank=True)
    token_secret = models.TextField(null=True, blank=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    options = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

# 通貨
class Currency(models.Model):
    unit = models.CharField(max_length=32, null=False, blank=False)
    name = models.CharField(max_length=32, null=False, blank=False)

# 通貨を受け取るお財布
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False, default=0)
    options = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

# 広告関係とは無関係の送金出金履歴
class PaymentLog(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=False, blank=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    to_address = models.CharField(max_length=255, null=False, blank=False)
    from_adress = models.CharField(max_length=255, null=False, blank=False)
    from_amount = models.FloatField(null=False, blank=False, default=0)
    to_amount = models.FloatField(null=False, blank=False, default=0)
    fee_amount = models.FloatField(null=False, blank=False, default=0)
    transaction_state = models.IntegerField(null=False, blank=False, default=0)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

# 広告掲載情報(ユーザー登録していなくてもいい)
class AdvertisementDraft(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    banner_url = models.CharField(max_length=255, null=True, blank=True)
    options = models.TextField(null=True, blank=True)

# 広告枠
class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    uuid = models.CharField(max_length=255, null=False, blank=False)
    min_price = models.FloatField(null=False, blank=False, default=0)
    activate_advertisement_count = models.IntegerField(null=False, blank=False, default=0)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

# 広告
class Advertisement(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=False, blank=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=False, blank=False)
    draft = models.ForeignKey(AdvertisementDraft, on_delete=models.CASCADE, null=False, blank=False)
    uuid = models.CharField(max_length=255, null=False, blank=False)
    daily_price = models.FloatField(null=False, blank=False, default=0)
    sum_price = models.FloatField(null=False, blank=False, default=0)
    start_at = models.DateTimeField(null=False, blank=False)
    end_at = models.DateTimeField(null=False, blank=False)
    show_order = models.IntegerField(null=False, blank=False, default=0)
    activate_state = models.IntegerField(null=False, blank=False, default=0)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

# 広告効果KPI
class AdvertisementLog(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=False, blank=False)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, null=False, blank=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=False, blank=False)
    accessed_by_ipaddress = models.CharField(max_length=255, null=False, blank=False)
    accessed_by_user_token = models.CharField(max_length=255, null=False, blank=False)
    accessed_by_user_agent = models.TextField(null=True, blank=True)
    impression_count = models.IntegerField(null=False, blank=False, default=0)
    click_count = models.IntegerField(null=False, blank=False, default=0)
    action_count = models.IntegerField(null=False, blank=False, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

# 広告出稿とかの送出金履歴
class AdvertisementPaymentLog(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=False, blank=False)
    to_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=False, blank=False)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, null=False, blank=False)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    to_address = models.CharField(max_length=255, null=False, blank=False)
    from_adress = models.CharField(max_length=255, null=False, blank=False)
    from_amount = models.FloatField(null=False, blank=False, default=0)
    to_amount = models.FloatField(null=False, blank=False, default=0)
    fee_amount = models.FloatField(null=False, blank=False, default=0)
    transaction_state = models.IntegerField(null=False, blank=False, default=0)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
