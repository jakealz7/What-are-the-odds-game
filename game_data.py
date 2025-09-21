from enum import Enum
from pydantic import BaseModel
import numpy as np

class Player(BaseModel):
    class DesiredOutcome(Enum):
        MATCH = 0
        NO_MATCH = 1
    # init
    n: int
    p_t: float
    desired_outcome: DesiredOutcome

    def generate(self, number: int =1) -> np.ndarray:
        random_vals = np.random.random(number)
        rolls = np.random.randint(1, self.n-1, number) # Generate as though all rolls are simple
        rolls[random_vals < self.p_t] = self.n # replace simple strat results with tricky ones, wherever you should have done the tricky strat instead
        return rolls

class Game(BaseModel):
    # init
    Matcher: Player
    NoMatcher: Player

    def get_result(self, num_games: int) -> float:
        if self.Matcher.n != self.NoMatcher.n:
            raise ValueError("Matcher and NoMatcher must have same n")
        results = np.ones(num_games)
        temp = self.Matcher.generate(num_games)+self.NoMatcher.generate(num_games)
        no_matcher_wins = np.logical_or(temp==self.Matcher.n, temp==2*self.Matcher.n)
        results[no_matcher_wins] = 0 # If the Matcher wins, the result is a 1, otherwise the result is a 0
        return float(np.mean(results))