#!/bin/local/python2
"""
Install dependency library django, django-rest-framework
"""


from datetime import datetime


class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='selo@selo.com', content='foo bar')


from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailFiend()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


serializer = CommentSerializer(comment)
