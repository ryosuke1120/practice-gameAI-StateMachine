#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Behavior

# 要最適化

root = Behavior.Behavior("<root>")
a = Behavior.Behavior("交戦")
b = Behavior.Behavior("撃退")
c = Behavior.Behavior("休憩")

a_a = Behavior.Behavior("攻撃")
a_b = Behavior.Behavior("防御")
b_a = Behavior.Behavior("足止めする")
b_b = Behavior.Behavior("逃走する")
c_a = Behavior.Behavior("立ち止まる")
c_b = Behavior.Behavior("回復する")

a_a_a = Behavior.Behavior("剣を振る")
a_a_b = Behavior.Behavior("攻撃魔法")
a_a_c = Behavior.Behavior("盾で剣をはじく")
a_b_a = Behavior.Behavior("一歩後退する")
a_b_b = Behavior.Behavior("盾で身を隠す")
b_a_a = Behavior.Behavior("トラップをしかける")
b_a_b = Behavior.Behavior("弓矢を放つ")
c_b_a = Behavior.Behavior("回復魔法")
c_b_b = Behavior.Behavior("回復薬を飲む")

a_a_b_a = Behavior.Behavior("召喚A")
a_a_b_b = Behavior.Behavior("召喚B")


a_a_b.add_behavior(a_a_b_a)
a_a_b.add_behavior(a_a_b_b)

a_a.add_behavior(a_a_a)
a_a.add_behavior(a_a_b)
a_a.add_behavior(a_a_c)
a_b.add_behavior(a_b_a)
a_b.add_behavior(a_b_b)
b_a.add_behavior(b_a_a)
b_a.add_behavior(b_a_b)
c_b.add_behavior(c_b_a)
c_b.add_behavior(c_b_b)

a.add_behavior(a_a)
a.add_behavior(a_b)
b.add_behavior(b_a)
b.add_behavior(b_b)
c.add_behavior(c_a)
c.add_behavior(c_b)

root.add_behavior(a)
root.add_behavior(b)
root.add_behavior(c)

node = root
while True:
    # break if node.children.empty?
    if node.children() == []:
        break
    node = node.box.get_by_selector()
    print(node.get_name())

# for bhv_root in root.children():
# 	for bhv_a in bhv_root.children():
# 		for bhv_b in bhv_a.children():
# 			print(bhv_b.node_name)

# 	root = Behavior.new("<root>") do
#   add "交戦" do
#     add "攻撃" do
#       add "剣を振る"
#       add "攻撃魔法" do
#         add "召喚A"
#         add "召喚B"
#       end
#       add "縦で剣をはじく"
#     end
#     add "防御" do
#       add "一歩後退する"
#       add "縦で身を隠す"
#     end
#   end
#   add "撤退" do
#     add "足止めする" do
#       add "トラップをしかける"
#       add "弓矢を放つ"
#     end
#     add "逃走する"
#   end
#   add "休憩" do
#     add "立ち止まる"
#     add "回復する" do
#       add "回復魔法"
#       add "回復薬を飲む"
#     end
#   end
# end
