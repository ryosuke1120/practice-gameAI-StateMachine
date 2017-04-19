#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import state
import play_state

# モンスターがフィールドを散歩している状態の動作


class WalkState(state.State):

    # 散歩モードに入ったときに一度だけ実行される
    def enter(self, entity):
        # entity.changeLocation(LocationType.Field)
        entity.set_message("Monster : ぴょこっ")

    # 条件が満たされるまで実行される
    def execute(self, entity):
        entity.set_message("Monster : ぴょこぴょこっ")

        # ランダムでLittleGirlにメッセージを送る
        # LittleGirlにフィールドにいることを伝える
        random_num = random.randint(1, 11)
        if random_num % 3 == 0:
            entity.message_dispatcher.dispatch_message(
                entity.message_dispatcher.SEND_MESSAGE_IMMEDIATELY,
                entity.m_ID,
                1,  # EntityNames.LittleGirl.ID
                "STROLL_STATE",  # MessageType
                None)

    # PlayStateに遷移する際に一度だけ実行される
    def exit(self, entity):
        entity.set_message("Monster : …？？（気配を感じている。）")

    def on_message(self, entity, telegram):
        if telegram.message is not None:
            if telegram.message == "WALK_STATE":
                entity.get_fsm().change_state(play_state.PlayState())
