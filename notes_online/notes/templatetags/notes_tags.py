# from django import template
# from ..models import *
#
# register = template.Library()
#
# @register.simple_tag()
# def get_themes(filter=None):
#         if not filter:
#             return Theme.objects.all()
#         else:
#             return Theme.objects.filter(pk=filter)
#
# @register.simple_tag()
# def get_notes(filter):
#     # return Note.objects.filter(User=request.user)
#         return Note.objects.filter(pk=filter)
