from django.db import models

# Create your models here.
""" 
models.py or forms.py 作成
makemigrations
migrate この順番は鉄則！
 """


from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    live = models.BooleanField(default=False)

    class Meta:	# class Meta:はデフォルト設定。
        ordering = ['-created_date']	# 最新のものが上に来る

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title