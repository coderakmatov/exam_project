from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text', )
