#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class State(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def enter(self, state_t):
        pass

    @abstractmethod
    def execute(self, state_t):
        pass

    @abstractmethod
    def exit(self, state_t):
        pass