from django import forms

from .models import Comment, Report

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['text']
        labels = {'text': ''}