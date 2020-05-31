from django.contrib import admin
from .models import Post  # 导入了前一章定义的post模型

# Register your models here.

admin.site.register(Post) # 为了让我们的模型在admin 页面可见，我们需要使用 admin.site.register(Post) 来注册模型
