from django.contrib import admin

# Register your models here.

from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	class Meta:
		model = SignUp



admin.site.register(SignUp, SignUpAdmin)