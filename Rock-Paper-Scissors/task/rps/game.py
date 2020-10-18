import random
import math


class RockPaperScissors:
    score_bord = {}

    def __init__(self):
        print("Enter your name: ")
        self.name = input()
        print(f"Hello, {self.name}")
        bord_save = open("rating.txt", "r")
        self.score_bord[self.name] = 0
        for line in bord_save.readlines():
            tmp = line.split()
            self.score_bord[tmp[0]] = int(tmp[1])
        bord_save.close()
        self.lose_arr = input().split(',')
        if len(self.lose_arr) < 3:
            self.lose_arr = ["rock", "paper", "scissors"]
        print("Okay, let's start")

    def game_loop(self):
        while True:
            in_val = input()
            if in_val == "!exit":
                print("Bye!")
                break
            elif in_val == "!rating":
                if not self.score_bord.__contains__(self.name):
                    self.score_bord[self.name] = 0
                print(f"Your rating: {self.score_bord[self.name]}")

            try:
                user = self.lose_arr.index(in_val)
            except ValueError:
                print("Invalid input")
                continue
            option = self.lose_arr[random.randint(0, len(self.lose_arr) - 1)]
            decide_arr = self.lose_arr[user+1:] + self.lose_arr[:user]
            if option in decide_arr[:math.floor(len(decide_arr) / 2)]:
                print(f'Sorry, but the computer chose {option}')
            elif self.lose_arr[user] == option:
                print(f"There is a draw ({option})")
                self.score_bord[self.name] += 50
            else:
                print(f"Well done. The computer chose {option} and failed")
                self.score_bord[self.name] += 100
        bord_save = open("rating.txt", "w")
        for score in self.score_bord.items():
            bord_save.write(score[0] + ' ' + str(score[1]))


rps = RockPaperScissors()
rps.game_loop()
