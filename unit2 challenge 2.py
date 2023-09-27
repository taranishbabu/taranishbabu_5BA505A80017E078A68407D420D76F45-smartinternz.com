class Player:

  def play(self):
    print("The player-playing cricket.")


class Batsman(Player):

  def play(self):
    print("The batsman - batting.")


class Bowler(Player):

  def play(self):
    print("The bowler- bowling.")


batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
