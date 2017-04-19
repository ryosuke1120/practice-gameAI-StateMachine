#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ランダム→FindAndFireSomething

import state
import random
import find_state


class StrollState(state.State):

    # SleepまたはEatSomethingから遷移した際に一回だけ実行される
    def enter(self, entity):
        # entity.setMessage("捜索を開始します")
        entity.set_message("LittleGirl : お散歩をしよう。")

    # 条件が満たされるまで実行される
    def execute(self, entity):
        entity.set_message("LittleGirl : てくてく")

    # FindAndFireSomethingに遷移する際に一度だけ実行される
    def exit(self, entity):
        entity.set_message("LittleGirl : あれ？動物の足跡…？")

    def on_message(self, entity, telegram):
        if telegram.message is not None:
            if telegram.message == "STROLL_STATE":
                entity.get_fsm().change_state(find_state.FindState())
