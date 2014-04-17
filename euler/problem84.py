import random

square_go = 0
square_jail = 10
square_community_chest_1 = 2
square_community_chest_2 = 17
square_community_chest_3 = 33
square_chance_1 = 7
square_chance_2 = 22
square_chance_3 = 36
square_c1 = 11
square_e3 = 24
square_h2 = 39
square_railway_1 = 5
square_railway_2 = 15
square_railway_3 = 25
square_railway_4 = 35
square_utility_1 = 12
square_utility_2 = 28
square_go_to_jail = 30

chance_card_advance_to_go = 0
chance_card_go_to_jail = 1
chance_card_go_to_c1 = 2
chance_card_go_to_e3 = 3
chance_card_go_to_h2 = 4
chance_card_go_to_r1 = 5
chance_card_go_to_next_railway_1 = 6
chance_card_go_to_next_railway_2 = 7
chance_card_go_to_next_utility = 8
chance_card_go_back_3 = 9

community_chest_card_advance_to_go = 0
community_chest_card_go_to_jail = 1

class Deck:

  def __init__(self):
    self.index = 0
    self.cards = range(0, 16)
    self.shuffle()
    
  def shuffle(self):
    random.shuffle(self.cards)

  def take_card(self):
    card = self.cards[self.index]
    self.index = (self.index + 1) % 16
    return card

class Simulation:
  
  die_size = 4
  nr_squares = 40
  nr_games = 10
  nr_turns = 500000
  nr_rolls = 0
  chance_deck = Deck()
  community_chest_deck = Deck()
  current_square = 0
  nr_doubles = 0
  square_visits = [0 for square in xrange(nr_squares)] 

  def is_chance(self, square):
    return ((square == square_chance_1) or
            (square == square_chance_2) or
            (square == square_chance_3))

  def is_community_chest(self, square):
    return ((square == square_community_chest_1) or 
            (square == square_community_chest_2) or
            (square == square_community_chest_3))

  def next_railway(self, square):
    if square < square_railway_1:
      return square_railway_1
    elif square < square_railway_2:
      return square_railway_2
    elif square < square_railway_3:
      return square_railway_3
    elif square < square_railway_4:
      return square_railway_4
    else:
      return square_railway_1

  def next_utility(self, square):
    if square < square_utility_1:
      return square_utility_1
    elif square < square_utility_2:
      return square_utility_2
    else:
      return square_utility_1

  def play_roll(self):

    die1 = random.randrange(1, self.die_size + 1)
    die2 = random.randrange(1, self.die_size + 1)

    double = (die1 == die2)
    if (double):
      self.nr_doubles += 1
      if self.nr_doubles == 3:
        self.current_square = square_jail
        return False
    
    self.current_square = (self.current_square + die1 + die2) % self.nr_squares

    if self.current_square == square_go_to_jail:
        self.current_square = square_jail
        return False

    if self.is_chance(self.current_square):
      chance_card = self.chance_deck.take_card()
      if chance_card == chance_card_advance_to_go:
        self.current_square = square_go
      elif chance_card == chance_card_go_to_jail:
        self.current_square = square_jail
        return False
      elif chance_card == chance_card_go_to_c1:
        self.current_square = square_c1  
      elif chance_card == chance_card_go_to_e3:
        self.current_square = square_e3
      elif chance_card == chance_card_go_to_h2:
        self.current_square = square_h2
      elif chance_card == chance_card_go_to_r1:
        self.current_square = square_railway_1
      elif chance_card == chance_card_go_to_next_railway_1:
        self.current_square = self.next_railway(self.current_square)
      elif chance_card == chance_card_go_to_next_railway_2:
        self.current_square = self.next_railway(self.current_square)
      elif chance_card == chance_card_go_to_next_utility:
        self.current_square = self.next_utility(self.current_square)
      elif chance_card == chance_card_go_back_3:
        self.current_square = (self.current_square - 3) % self.nr_squares            

    if self.is_community_chest(self.current_square):
      community_chest_card = self.community_chest_deck.take_card()
      if community_chest_card == community_chest_card_advance_to_go:
        self.current_square = square_go
      elif community_chest_card == community_chest_card_go_to_jail:
        self.current_square = square_jail
        return False

    return double
    
  def play_turn(self):
    self.nr_doubles = 0
    again = True
    while again:
      again = self.play_roll()
      self.square_visits[self.current_square] += 1
      self.nr_rolls += 1

  def play_game(self):
    self.chance_deck.shuffle()
    self.community_chest_deck.shuffle()
    self.current_square = 0
    for turn in xrange(self.nr_turns):
      self.play_turn()

  def play_all_games(self):
    for turn in xrange(self.nr_games):
      self.play_game()

  def show_square(self, result):
    square = result[1]
    square_visits = result[0]
    probability = 100.0 * float(square_visits) / float(self.nr_rolls)
    print square, probability

  def show_top_3_squares(self):
    annotated = []
    for square, visits in enumerate(self.square_visits):
      annotated.append((visits, square))
    annotated.sort(reverse=True)
    self.show_square(annotated[0])
    self.show_square(annotated[1])
    self.show_square(annotated[2])

  def solve(self):
    self.play_all_games()
    self.show_top_3_squares()

simulation = Simulation()
simulation.solve()

  
