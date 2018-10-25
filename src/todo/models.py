from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('urgent', 'Urgent'),
        ('normal', 'Normal'),
    )
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='normal')
    

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ('created',)

    def __str__(self):
        return self.title
    
     
