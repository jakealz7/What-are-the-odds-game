from game_data import Player, Game
import numpy as np

if __name__=='__main__':
    num_games = 1000
    n = 10
    player_samples = 30
    pt_arr = np.linspace(0, 1, num=player_samples)
    p_m = Player(n=10, p_t=1/10, desired_outcome=Player.DesiredOutcome.MATCH)
    p_nm = Player(n=10, p_t=1/10, desired_outcome=Player.DesiredOutcome.NO_MATCH)
    results = Game(Matcher=p_m, NoMatcher=p_nm).get_result(num_games)
    print(results)
