import os
import numpy as np

import random


class GameWorld(object):
    def __init__(self):
        # parameters
        self.name = os.path.splitext(os.path.basename(__file__))[0]
        self.screen_n_rows = 8
        self.screen_n_cols = 8
        self.player_length = 3
        self.enable_actions = (0, 1, 2)
        self.frame_rate = 5

        self.reward = 0
        self.terminal = False

        # data設計------------------------------------------------------------------------------------------
        # inputdataの種類：体力度, 空腹度, 食欲,　睡眠欲, 性欲, 労働欲, 喜, 怒, 哀, 楽
        # outputdataの種類：※一旦１０種類(0と1のbit)
        # parameter幅：1ターン毎
        # data幅：0.0 ~ 1.0(float)
        self.game_parameter = []
        for i in range(1, 100):
            a_param = []
            for j in range(1, 10):
                a_param.append(random.random())

            self.game_parameter.append(a_param)
        # print(self.game_parameter)

        #----------------------------------------------------------------------

        # reset other variables
        # # variables
        # self.reset()

    def update(self, action):
        """
        action:
            0: do nothing
            1: move left
            2: move right
        """
        # update player position
        if action == self.enable_actions[1]:
            # print("move left")
            print("test : Action-A")
            # move left
            # self.player_col = max(0, self.player_col - 1)
        elif action == self.enable_actions[2]:
            # print("move right")
            print("test : Action-B")
            # move right
            # self.player_col = min(self.player_col + 1, self.screen_n_cols - self.player_length)
        else:
            # do nothing
            pass

        # # update ball position
        # self.ball_row += 1

        # collision detection
        self.reward = 0
        self.terminal = False

        # ゲームを簡易化（６で割り切れたら終わり）
        self.random_num = random.randint(0, 9)
        if self.random_num % 6 == 0:
            # ゲーム終了フラグ設定
            self.terminal = True

            #[0:罰を与えるButtonを押す][1:何もしない][2:褒めるButtonを押す]によって分岐予定
            # 現在はランダムで仮実装
            self.random_num_oth = random.randint(0, 2)
            if self.random_num_oth == 0:
                # 罰を与える
                print("罰を与える")
                self.reward = -1
            elif self.random_num_oth == 2:
                # 褒める
                print("褒める")
                self.reward = 1
            else:
                # 何もしない
                print("何もしない")
                self.reward = 0

    def observe(self):
        # self.draw()
        # print("self.myFox.update()→state_t_1（パラメータの状態）もアップデート")
        # self.screen = np.zeros((self.screen_n_rows,
        # self.screen_n_cols))#サンプル1
        self.screen = np.zeros((10))  # サンプル2
        #print("state_t_1（パラメータの状態）, reward_t（手動による1or-1（なにもしない場合は0））, terminal（現在のステートがEXCUTEならFalse）を返す仕組みを作る")
        return self.screen, self.reward, self.terminal

    def execute_action(self, action):
        self.update(action)

    def reset(self):
        # reset other variables
        self.reward = 0
        self.terminal = False
