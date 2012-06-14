from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class Calendar(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def to_hash(self):
        return {'id': self.id,}


class Todo(models.Model):
    calendar = models.OneToOneField(Calendar)
    created_on = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=30)
    done = models.BooleanField(default=False)

    def to_hash(self):
        return {
          'id': self.id,
          'title': self.title,
          'start': self.created_on.isoformat(),
          'done': self.done,
          'calendar': self.calendar.to_hash(),
        }
