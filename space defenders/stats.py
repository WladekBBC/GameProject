class Stats():
    #tracking scores in the game

    def __init__(self):
        #statistics initialization
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        #changes of statistics in procces
        self.guns_left = 2
        self.score = 0
