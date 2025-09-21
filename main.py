from game_data import Player, Game, BetterGame, Config
import numpy as np
import matplotlib.pyplot as plt

def method1(config:Config) -> float:
    # Old method, needlessly monte carlo'd but useful to verify my algebra
    # Todo: allow this to loop over cartprod of pt vals
    num_games = 1000 # hardcoded mc sample ct
    p_m = Player(n=config.n, p_t=1/10, desired_outcome=Player.DesiredOutcome.MATCH)
    p_nm = Player(n=config.n, p_t=1/10, desired_outcome=Player.DesiredOutcome.NO_MATCH)
    result = Game(Matcher=p_m, NoMatcher=p_nm).get_result(num_games)
    return result

def plot(config:Config, results:np.ndarray, title_prepend="") -> None:
    plt.figure(figsize=(8, 6))
    pt_m_mg, pt_nm_mg = np.meshgrid(cfg.pt_m, cfg.pt_nm, indexing='ij')
    contourf = plt.contourf(pt_m_mg, pt_nm_mg, results, levels=100, cmap='viridis')
    plt.xlabel('$P_{t,m}$')
    plt.ylabel('$P_{t,nm}$')
    plt.title(f'{title_prepend}n={cfg.n}')
    plt.colorbar(contourf)
    plt.show()
if __name__=='__main__':
    # Make config
    n = 3
    num_player_samples = 30
    cfg = Config(n=n, pt_m=np.linspace(0,1,num_player_samples), pt_nm=np.linspace(0,1,num_player_samples))
    delta = 0.001
    # nash_val = 2/(n+1)
    # cfg = Config(n=n, pt_m=np.linspace(nash_val-delta, nash_val+delta, num_player_samples), pt_nm=np.linspace(nash_val-delta, nash_val+delta, num_player_samples))

    # Monte Carlo
    mc_result = method1(cfg)

    # Analytic
    better_game = BetterGame(n=cfg.n, pt_m=cfg.pt_m, pt_nm=cfg.pt_nm)
    results = better_game.get_results()

    plot(cfg, results,"Analytic ")

    p_n = 2/(cfg.n-1)





    # TODO compare MC version to analytic version
    # TODO get optimal pt_nm from given pt_m, and vice versa
    # TODO Look at evolution of pts? When proportion of population is the same as the probability of win
    # TODO Animation: Sliding through n, the population progression of evolutionary
    # TODO Nash?
    # TODO Make something that generates a number for you, given n
    pass

