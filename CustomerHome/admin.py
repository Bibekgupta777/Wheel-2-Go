from django.contrib import admin


# Register your models here.
from .models import Customer


admin.site.register(Customer)

from .models import Contact

admin.site.register(Contact)




from .models import Feedback

admin.site.register(Feedback)