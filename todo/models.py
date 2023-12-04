from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "done": self.done,
        }
