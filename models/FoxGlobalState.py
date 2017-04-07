#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import State
import Sleep

class FoxGlobalState(State.State): 
	#開始時、あくびする
	# override fun enter( entity_type: Fox ) {
	#     entity_type.setMessage("ふあああ・・")
	# }
	def enter(self, entity):
		entity.setMessage("ふあああ・・")

	#あくびイベント実行
	def execute(self, entity):
		if entity.getFsm().m_pCurrentState == self:
			#このグローバルステート実行中なら1ターンで終了する
			#終了時は必ず、もとのステートに戻る
			entity.getFsm().revertToPreviousState()
		else:
			#ランダムであくびイベント発生
			#val random = Random().nextInt()
			random_num = random.randint(1,10)

		if random_num % 10 == 0 :
			entity.getFsm().changeState(Sleep.Sleep())

		# override fun execute( entity_type: Fox ) {
		#     if( entity_type.getFsm().m_pCurrentState === this ){
		#         // このグローバルステート実行中なら1ターンで終了する
		#         // 終了時は必ず、もとのステートに戻る
		#         entity_type.getFsm().revertToPreviousState()
		#     }
		#     else {
		#         // ランダムであくびイベント発生
		#         val random = Random().nextInt()

		#         if (random % 10 === 0) {
		#             entity_type.getFsm().changeState(this)
		#         }
		#     }
		# }

	#出るときつかれたなあ、とつぶやく
	def exit(self, entity):
		entity.setMessage("なんだか疲れたなあ")
		# override fun exit( entity_type: Fox ) {
		#     entity_type.setMessage("なんだか疲れたなあ")
		# }