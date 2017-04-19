#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BaseGameEntityの電話帳


class EntityManager(object):

    def __init__(self):
        self.m_entity_map = {}

    # IDからエージェントを返す
    def get_entity_from_id(self, id_num):
        return self.m_entity_map[id_num]

    # 場のエージェントを追加する
    def register_entity(self, new_entity):
        self.m_entity_map[new_entity.m_ID] = new_entity
