from django.db import models

from django_mongokit import connection
from django_mongokit.document import DjangoDocument

class AB(DjangoDocument):
	structure={
		'author':unicode,
		'book':unicode,
	}
	use_dot_notation=True
	
#connection.register([AB])
connection.register([AB])
	
	

# Create your models here.
