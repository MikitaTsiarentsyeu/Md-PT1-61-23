from django.db import models
from rest_framework import serializers, viewsets

class Author(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)

    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):

    POST_TYPES = [('a', 'ad'), ('c', 'copyright'), ('g', 'generic')]

    title = models.CharField(blank=False, max_length=100)
    content = models.TextField(blank=False)
    post_type = models.CharField(blank=False, max_length=1, choices=POST_TYPES)
    issued = models.DateTimeField()
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    # def __str__(self) -> str:
    #     return self.title

    def __str__(self) -> str:
        return f"{self.title}_{self.post_type}"
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'issued', 'author']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer