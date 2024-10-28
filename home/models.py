from django.db import models

from wagtail.models import Page


class HomePage(Page):
    pass

# home/models.py
from wagtail_resume.models import BaseResumePage


class ResumePage(BaseResumePage):
    pass
