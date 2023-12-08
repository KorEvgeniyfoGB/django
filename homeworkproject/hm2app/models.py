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
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE)  # связь с моделью «Клиент», указывает на клиента, сделавшего заказ
    products = models.ManyToManyField(Product,
                                      through="OrderProduct", related_name='products')  # связь с моделью «Товар», указывает на товары, входящие в заказ
    total = models.DecimalField(max_digits=10, decimal_places=2)  # общая сумма заказа
    date_ordered = models.DateTimeField(auto_now_add=True)  # дата оформления заказа

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

