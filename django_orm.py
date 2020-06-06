#查询
from blog.models import Post
Post.objects.all()

#创建对象
from django.contrib.auth.models import User
User.objects.all()
me = User.objects.get(username='shawnysh')
Post.objects.create(author = me, title = 'Sample title', text = 'Test')
Post.objects.all()

#筛选
Post.objects.filter(author=me)
Post.objects.filter(title__contains='title')

from django.utils import timezone
post = Post.objects.get(title='Sample title')
post.publish()
Post.objects.filter(published_date__lte=timezone.now())

#排序
Post.objects.order_by('created_date')

#链式QuerySets
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
