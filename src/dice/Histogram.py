class Histogram:
    def __init__(self, players):
        self.players = players
        self.data = {player: [0] * 6 for player in players}

    def add_roll(self, player, roll):
        self.data[player][roll - 1] += 1

    def display(self):
        print("  Player Histogram")
        print("--------------------")
        for player in self.players:
            print(f"Player {player}:")
            counts = self.data[player]
            max_count = max(counts)
            lines = ["".join([" # " if counts[j] >= i else "   " for j in range(6)]) for i in range(max_count, 0, -1)]
            for line in lines:
                print(line)
            print("  +" + "---+" * 6)
            print("    " + "  ".join(str(i + 1).center(3) for i in range(6)))
            print()
