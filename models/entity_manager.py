#!/usr/bin/env python
# -*- coding: utf-8 -*-

#BaseGameEntityの電話帳

class EntityManager(object):

	def __init__(self):
		#self.m_EntityMap : Map<Int, BaseGameEntity> = HashMap()
		self.m_EntityMap = {}

	#IDからエージェントを返す
	def getEntityFromId(self, id_num):
		return self.m_EntityMap[ id_num ]

	#場のエージェントを追加する
	#newEntity : BaseGameEntity
	def registerEntity(self, newEntity):
		# m_EntityMap += hashMapOf( newEntity.m_ID to newEntity )
		self.m_EntityMap[newEntity.m_ID] = newEntity