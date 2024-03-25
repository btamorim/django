from django.db import models

class Tasks(models.Model):
    STATUS_CHOICE = [
        ("P", "Pendente"),
        ("A", "Em andamento"),
        ("C", "Concluido")
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="P")
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title
