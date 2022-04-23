from django.db import models
from django.utils import timezone


class WebUser(models.Model):

	#Os enumerados (numero de escolhas fixas) deve ser representado assim:
	#Tuplo contendo tuplos, cada um contendo um dos valores e a sua descrição
	#Aqui está representado o enumerado "UserState"
    USER_STATE_CHOICES=(
        ('new', 'New'),
        ('active', 'Active'),
        ('blocked', 'Blocked'),
        ('banned', 'Banned')
    )
	
	#login_id é definido como chave primária desta tabela
	#Neste diagrama, os campos assinalados por {id} são chaves primárias
    login_id = models.CharField(max_length=50,
                                primary_key=True)
								
    password = models.CharField(max_length=50)
	
	#O enumerado é atribuido ao campo através do argumento "choices"
	#Por defeito, faria sentido ser "new", portanto, acabado de criar
    state = models.CharField(max_length=10,
                             choices=USER_STATUS_CHOICES,
                             default='new')
	
	#A relação um para um deve ser definida no lado da relação não-obrigatório.
	#Neste exemplo, o WebUser tem obrigatoriamente 1 Customer.
	#O Customer, por outro lado, pode não ter um WebUser (0 ou 1)
	#Portanto, a ligação deve ser definida nesta classe, definindo o campo on_delete a CASCADE
	customer = models.OneToOneField(Customer,
									on_delete=models.CASCADE)


class Customer(models.Model):
    id = models.CharField(max_length=50,
                                primary_key=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
	
	#EmailField é o campo mais adequado para Emails
	#É também String mas contém validadores de email
    email = models.EmailField()


class Account(models.Model):
	#Neste caso ambos os lados são obrigatórios.
	#Mas existe uma relação de composição entre eles (Customer é composto por Account)
	#Sendo Account "parte" de Customer, a campo OneToOneField deve ser definido aqui
    customer = models.OneToOneField(Customer,
									on_delete=models.CASCADE)
	
	id = models.CharField(max_length=50,
                                primary_key=True)
	
	#Address não está especificado, poderia ser uma classe ou então texto simples
    billing_address = models.TextField()
	
    is_closed = models.BooleanField(default=False)
	
	#opção "auto_now_add" auto-preenche o campo com a data em que o objeto é criado
    open = models.DateField(auto_now_add=True)
	
    closed = models.DateField()


class ShoppingCart(models.Model):
	#Nesta classe existe alguma redundância de relações (possivelmente desnecessária)
	#Não tem campo {id} definido, pelo que utilizamos o campo automático 
    web_user = models.OneToOneField(WebUser,
                              on_delete=models.CASCADE)
	
	account = models.OneToOneField(Account,
                              on_delete=models.CASCADE)
							  
    created = models.DateField(auto_now_add=True)


class Product(models.Model):
    id = models.CharField(max_length=25,
                                 primary_key=True)
    name = models.CharField(max_length=200)
	
	#Aqui supplier deveria ser uma classe, mas como não está especificado, pode ser só texto
    supplier = models.CharField(max_length=200)


class LineItem(models.Model):
    product = models.ForeignKey(Product,
                                  on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(ShoppingCart,
                                         on_delete=models.CASCADE)
	order = models.ForeignKey(Order,
                               on_delete=models.CASCADE)
							   
    quantity = models.IntegerField()
	
	#FloatField não estaria incorreto mas DecimalField é mais adequado para moeda
	#É um detalhe mas podem ver melhor aqui: https://docs.python.org/3/library/decimal.html#module-decimal
    price = models.DecimalField()


class Payment(models.Model):
    account = models.ForeignKey(Account,
                           on_delete=models.CASCADE)
						   
	order = models.ForeignKey(Order,
                           on_delete=models.CASCADE)
	
	id = models.CharField(max_length=50,
                                primary_key=True)
    paid = models.DateTimeField()
    total = models.DecimalField()
    details = models.TextField()


class Order(models.Model):
	#<<enumeration>> OrderStatus
    ORDER_STATUS_CHOICE = (
        ('new', 'New'),
        ('hold', 'Hold'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('closed', 'Closed')
    )
    number = models.CharField(max_length=50,
                              primary_key=True)
    account = models.ForeignKey(Account,
                                       on_delete=models.CASCADE)
   								  
    ordered = models.DateTimeField()
    shipped = models.DateTimeField()
    ship_to = models.TextField()
    status = models.CharField(max_length=10,
                              choices=ORDER_STATUS_CHOICE,
                              default='new')
							  
    total = models.DecimalField()

