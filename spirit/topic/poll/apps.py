# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig


class SpiritTopicPollConfig(AppConfig):

    name = 'spirit.topic.poll'
    verbose_name = "Spirit Topic Poll"
    label = 'spirit_topic_poll'

    def ready(self):
        self.register_signals()

    def register_signals(self):
        from . import signals
