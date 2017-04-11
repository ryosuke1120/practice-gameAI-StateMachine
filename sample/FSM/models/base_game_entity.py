#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class BaseGameEntity(object):
	__metaclass__ = ABCMeta

	def __init__(self, m_ID):
		self.require(True)
		self.m_iNextVlidID = 0

	@abstractmethod
	def update():
		pass	
