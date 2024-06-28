from django.db import models


class FAQ(models.Model):
    text = models.TextField(max_length=64, null=False)
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True)

    def get_children(self):
        return list(self.faq_set.all())
