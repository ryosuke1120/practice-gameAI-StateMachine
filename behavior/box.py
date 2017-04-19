#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Box(object):

    def __init__(self):
        self.selector = "確率的選択"
        self.a_list = []

    def add_list(self, bhv):
        self.a_list.append(bhv)

    def get_by_selector(self):
        #children = filter((lambda bhv: bhv.executable() == True), self.a_list)
        children = [bhv for bhv in self.a_list if bhv.executable()]
        if self.selector in {'確率的選択'}:
            # sampleメソッドは、配列の要素を1つランダムに返します。配列が空の場合はnilを返します。
            if children != []:
                a_selected_behavior = random.choice(children)
            else:
                a_selected_behavior = []
        elif self.selector in {'優先度リスト'}:
            # 優先度の高いもの順
            pass
        elif self.selector in {'シーケンシャル'}:
            # 決まった順に
            pass
        elif self.selector in {'シーケンシャルルーピング'}:
            # 決まった順に繰り返す
            pass
        elif self.selector in {'オンオフ'}:
            # ランダムだけど一度選択したものは選択しない
            pass

        return a_selected_behavior

    def get_list(self):
        return self.a_list
