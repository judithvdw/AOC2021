class BingoCard:
    def __init__(self, card):
        self.card = card

    def cross_number(self, number):
        for i, line in enumerate(self.card):
            for j, card_number in enumerate(line):
                if card_number == number:
                    self.card[i][j] = "X"

    def horizontal_win(self):
        for line in self.card:
            if not any(isinstance(x, int) for x in line):
                return True
        return False

    def vertical_win(self):
        for line in zip(*self.card):
            if not any(isinstance(x, int) for x in line):
                return True
        return False

    def win(self):
        return self.vertical_win() or self.horizontal_win()

    def total_remaining(self):
        total = 0
        for line in self.card:
            for n in line:
                if n != 'X':
                    total += n
        return total

    def __repr__(self):
        return "\n".join([str(line) for line in self.card])


def split_raw_cards(raw_cards):
    cards = []
    temp_card = []
    for line in raw_cards:
        if line == '\n':
            cards.append(temp_card)
            temp_card = []
        else:
            temp_card.append([int(a) for a in line.strip().split()])
    cards.append(temp_card)
    return cards


def play(game, cards):
    winning_stats = []
    for number in game:
        for card in cards:
            card.cross_number(number)
        for card in cards:
            if card.win():
                winning_stats.append(number * card.total_remaining())
                cards.remove(card)

    return winning_stats


if __name__ == '__main__':
    with open('4.txt') as f:
        raw = f.readlines()

    game = [int(a) for a in raw[0].split(',')]
    bingo_cards_raw = raw[2:]
    cards = []
    for card in split_raw_cards(bingo_cards_raw):
        cards.append(BingoCard(card))

    result = play(game, cards)

    print(f"Part 1: {result[0]}")
    print(f"Part 2: {result[-1]}")
