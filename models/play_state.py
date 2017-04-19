#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state
import random
import return_state


class PlayState(state.State):

    # 遊びモードに入ったときに一度だけ実行される
    def enter(self, entity):
        # entity.changeLocation(LocationType.Field)
        entity.set_message("Monster : …！！")
        entity.message_dispatcher.dispatch_message(
            entity.message_dispatcher.SEND_MESSAGE_IMMEDIATELY,
            entity.m_ID,
            1,  # EntityNames.LittleGirl.ID
            "FIND_STATE",  # MessageType
            None)

    # 条件が満たされるまで実行される
    def execute(self, entity):
        entity.set_message("Monster : ぴょこっぴょこっ♪")
        # if 疲れて帰らなくちゃいけなくなったら
        entity.consume(random.randint(1, 2))
        if entity.is_stamina_less():
            # #LittleGirlににメッセージを送る
            entity.message_dispatcher.dispatch_message(
                entity.message_dispatcher.SEND_MESSAGE_IMMEDIATELY,
                entity.m_ID,
                1,  # EntityNames.LittleGirl.ID
                "ENJOY_STATE",  # MessageType
                None)

    # に遷移する際に一度だけ実行される
    def exit(self, entity):
        entity.set_message("Monster : こくこく…")
        pass

    def on_message(self, entity, telegram):
        if telegram.message is not None:
            if telegram.message == "PLAY_STATE":
                entity.get_fsm().change_state(return_state.ReturnState())
