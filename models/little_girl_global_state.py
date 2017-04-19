#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import state


class LittleGirlGlobalState(state.State):

    def __init__(self):
        self.random_num = 1

    # 遷移した際に一回だけ実行される
    def enter(self, entity):
        entity.set_message("ふあああ・・")

    # あくびイベント実行
    def execute(self, entity):
        if entity.get_fsm().m_pCurrentState == self:
            # このグローバルステート実行中なら1ターンで終了する
            # 終了時は必ず、もとのステートに戻る
            entity.get_fsm().revert_to_previous_state()
        else:
            # ランダムであくびイベント発生
            # self.random_num = random.randint(0,45)
            # デバッグのため未使用
            self.random_num = 1

        if self.random_num % 23 == 0:
            entity.get_fsm().change_state(self)

    #出るときつかれたなあ、とつぶやく#
    # def execute(self,
    # entity)でentity.getFsm().revertToPreviousState()を行うのでglobalStateのexitは絶対に呼ばれない仕様がある
    def exit(self, entity):
        entity.set_message("なんだか疲れたなあ")
