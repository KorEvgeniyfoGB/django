from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование товара")
    description = models.TextField(max_length=255, verbose_name="Описание товара")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Фото")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")
    quantity = models.PositiveIntegerField(verbose_name="Количество товара")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      through="OrderProduct", related_name='products')
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.client.name}"

    @property
    def calculate_total(self):
        items = OrderProduct.objects.filter(order=self.pk)
        total = sum(item.product.price * item.quantity_pr for item in items)
        return total

    def save(self, *args, **kwargs):
        self.total = self.calculate_total
        super().save(*args, **kwargs)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_pr = models.PositiveIntegerField(default=1)
