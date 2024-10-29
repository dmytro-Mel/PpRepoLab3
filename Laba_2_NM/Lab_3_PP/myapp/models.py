from django.db import models

# User model
class User(models.Model):
    username = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    create_date = models.DateTimeField()
    verif = models.CharField(max_length=45)

    def __str__(self):
        return self.username



# Asset model
class Asset(models.Model):
    name = models.CharField(max_length=45)
    code = models.IntegerField()
    price = models.FloatField()
    last_update = models.DateTimeField()

    def __str__(self):
        return self.name


# Wallet model
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()

    def __str__(self):
        return f"Wallet of {self.user.username}"


# Chain model
class Chain(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    balance = models.FloatField()
    create_date = models.DateTimeField()
    last_update = models.DateTimeField()

    def __str__(self):
        return f"Chain for {self.wallet.user.username} - {self.asset.name}"


# Status model
class Status(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


# Invoice model
class Invoice(models.Model):
    chain_receiver = models.ForeignKey(Chain, related_name='chain_receiver', on_delete=models.CASCADE)
    chain_sender = models.ForeignKey(Chain, related_name='chain_sender', null=True, blank=True, on_delete=models.CASCADE)
    type_invoice = models.CharField(max_length=45)
    deposit = models.FloatField(null=True, blank=True)
    withdraw = models.FloatField(null=True, blank=True)
    date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    fees = models.FloatField()

    def __str__(self):
        return f"Invoice {self.id}"
