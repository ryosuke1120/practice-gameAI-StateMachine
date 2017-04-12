#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import GameWorld
from dqn_agent import DQNAgent

class Neural(object):

    def __init__(self):
        # parameters
        # self.n_epochs = 1000
        self.n_epochs = 1

        # environment, agent
        self.env = GameWorld.GameWorld()
        self.agent = DQNAgent(self.env.enable_actions, self.env.name)

        # variables
        self.win = 0

    def save_model(self):
        pass

    def load_model(self):
        pass

    def train(self):
        # if __name__ == "__main__":
        # parameters
        # self.n_epochs = 1000

        # # environment, agent
        # self.env = GameWorld.GameWorld()
        # self.agent = DQNAgent(self.env.enable_actions, self.env.name)

        # # variables
        # self.win = 0

        for e in range(self.n_epochs):
            # reset
            frame = 0
            loss = 0.0
            Q_max = 0.0
            self.env.reset()
            state_t_1, reward_t, terminal = self.env.observe()

            while not terminal:
                state_t = state_t_1

                # execute action in environment
                action_t = self.agent.select_action(state_t, self.agent.exploration)
                self.env.execute_action(action_t)

                # observe environment
                state_t_1, reward_t, terminal = self.env.observe()

                # store experience
                self.agent.store_experience(state_t, action_t, reward_t, state_t_1, terminal)

                # experience replay
                self.agent.experience_replay()


                # for log
                frame += 1
                loss += self.agent.current_loss
                Q_max += np.max(self.agent.Q_values(state_t))
                if reward_t == 1:
                    self.win += 1

            # print("EPOCH: {:03d}/{:03d} | WIN: {:03d} | LOSS: {:.4f} | Q_MAX: {:.4f}| terminal: {:.5f}".format(
            #     e, n_epochs - 1, win, loss / frame, Q_max / frame, terminal))
            print("EPOCH: {:03d}/{:03d} | WIN: {:03d} | LOSS: {:.4f} | Q_MAX: {:.4f}| terminal: {:.5f}".format(
                e, self.n_epochs - 1, self.win, loss , Q_max , terminal))

        # save model
        #今は使用しない
        # agent.save_model()

if __name__ == "__main__":
    test = Neural()
    test.train()

