from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('urgent', 'Urgent'),
        ('normal', 'Normal'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='normal')
    due_date = models.DateField(blank=False) # a date when the task is due
    due_time = models.TimeField(blank=False) # a time when the task is due
    
    # not visible to user
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ('due_date',)

    def __str__(self):
        return self.title
    
     
