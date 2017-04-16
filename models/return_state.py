#!/usr/bin/env python
# -*- coding: utf-8 -*-

#生き返って散歩するまでの待機状態
import state
import walk_state

class ReturnState(state.State):
 
    #30秒たったら散歩を始める
    def enter(self, entity):
        entity.setMessage("Monster :　ひゅっ(あっちの世界に帰えるよ）")
        #1分間待機後、生き返る
        # entity.message_dispatcher.dispatchMessage(
        #         10,
        #         entity.m_ID,
        #         EntityNames.Monster.ID,
        #         MessageType.COME_BACK_TO_LIFE,
        #         None
        # )
        # #自分自身にMessageを送る。        
        entity.message_dispatcher.dispatchMessage(
                            10,
                            entity.m_ID,
                            2, #EntityNames.Monster.ID
                            "REBORN_STATE", #MessageType.WALK_AROUND_IN_FIELD
                            None )


    #条件が満たされるまで実行される
    def execute(self, entity):
        entity.setMessage("Monster : （帰還中）")
        entity.recover(1) #体力回復

    #に遷移する際に一度だけ実行される
    def exit(self, entity):
        entity.setMessage("Monster :　ひょこっ（また戻ってきたよ）")

    #メッセージを受け取ったら、散歩状態に移行する
    #def onMessage(pMonster: Monster, telegram: Telegram)
    def onMessage(self, entity, telegram):
        if telegram.message != None :
            if telegram.message == "REBORN_STATE" :
                entity.getFsm().changeState(walk_state.WalkState())
