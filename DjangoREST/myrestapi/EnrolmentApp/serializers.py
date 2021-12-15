# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#converting model to JSON format-serialization code:

from rest_framework import serializers
from .models import student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=('firstname','lastname')
