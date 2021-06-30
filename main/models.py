from django.db import models




class Country(models.Model):
    """
    Admin, davlatlar
    """
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Region(models.Model):
    """
    Admin, viloyat
    """
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class District(models.Model):
    """
        Admin, tumanlar
        """
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Category(models.Model):
    """
    Admindan qo'shiladi
    """
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, default=None, blank=True)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"



    def __str__(self):
        return self.name_uz


class Unit(models.Model):
    """
    kg, m, l, mm, sm, ...
    admindan qo'shiladi
    """
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    # class Meta:
    #     verbose_name = "Dona"
    #     verbose_name_plural = "Donalar"
    #
    #
    #     def __str__(self):
    #         return self.name



class Currency(models.Model):
    """
    $, so'm, Euro, ...
    """
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    exchange_rate = models.IntegerField(default=1)  # TIYINDA


class Product(models.Model):
    STATUS_NEW = 0  # Bular saytda ko'rinadi
    STATUS_PUBLISHED = 1  # bular saytda ko'rinadi
    STATUS_REJECTED = 2  # saytda ko'rinmaydi

    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    user = models.ForeignKey("client.User", on_delete=models.RESTRICT)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, null=True, default=None, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.RESTRICT, null=True, default=None, blank=True)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    price = models.BigIntegerField()  # tiyinda, currency_id = 1 ($, er=10500), price=55.88$, 5588
    photo = models.ImageField(upload_to='images/')
    anons_uz = models.CharField(max_length=50, blank=True, null=True)
    anons_ru = models.CharField(max_length=50, null=True, blank=True)
    status = models.SmallIntegerField(choices=(
        (STATUS_NEW, "Yangi"),
        (STATUS_PUBLISHED, "Ko'rinadi"),
        (STATUS_REJECTED, "Maderator o'tkazmadi")
    ), default=STATUS_NEW, db_index=True)

    @property
    def price_uzs(self):
        return self.currency.exchange_rate * self.price

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"



class DeliveryAddress(models.Model):
    user = models.ForeignKey("client.User", on_delete=models.RESTRICT)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    district = models.ForeignKey(District, on_delete=models.RESTRICT)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=15)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Order(models.Model):
    STATUS_NEW = 0
    STATUS_ACCEPTED = 1
    STATUS_REJECTED = 2
    STATUS_DELIVERY = 3
    STATUS_COMPLETED = 4

    PAYMENT_STATUS_NEW = 0
    PAYMENT_STATUS_COMPETED = 1
    PAYMENT_STATUS_CANCELED = 2

    user = models.ForeignKey("client.User", on_delete=models.RESTRICT)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.RESTRICT)
    total_price_uzs = models.BigIntegerField()  # tiyinda
    status = models.SmallIntegerField(choices=(
        (STATUS_NEW, "Yangi"),
        (STATUS_ACCEPTED, "Qabul qilingan"),
        (STATUS_REJECTED, "Bekor qilingan"),
        (STATUS_DELIVERY, "Yoʻlda"),
        (STATUS_COMPLETED, "Buyurtma yopilgan")
    ), default=STATUS_NEW)
    payment_status = models.SmallIntegerField(choices=(
        (PAYMENT_STATUS_NEW, "Yangi"),
        (PAYMENT_STATUS_CANCELED, "Bekor qiligan"),
        (PAYMENT_STATUS_COMPETED, "Yo'langan")
    ))


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    price_uzs = models.BigIntegerField()





class ProductIndex(models.Model):
    boot = models.CharField(max_length=50)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    price = models.BigIntegerField()  # tiyinda, currency_id = 1 ($, er=10500), price=55.88$, 5588
    price2 = models.BigIntegerField()  # tiyinda, currency_id = 1 ($, er=10500), price=55.88$, 5588
    photo = models.ImageField(upload_to='images/')


    class Meta:
        verbose_name = "MahsulotIndex"
        verbose_name_plural = "MahsulotlarIndex"


class Cart(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    price = models.BigIntegerField()
    photo = models.ImageField(upload_to='images/')
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)

    objects = models.Manager()

    def __str__(self):
        return self.name