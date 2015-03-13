from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Quote(models.Model):
    author = models.ForeignKey(Author, related_name='quotes')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        body = ' '.join(self.text.split(' ')[:5])
        if len(body) < len(self.text):
            body += '...'
        return '{0}: "{1}"'.format(self.author, body)

    class Meta:
        ordering = ('-created',)
