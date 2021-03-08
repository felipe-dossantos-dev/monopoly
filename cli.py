import click
from src.simulation import Simulation


@click.command()
@click.option(
    "--number-games", "-n", default=300, help="Number of games to run on simulation."
)
@click.option(
    "--max-rounds",
    "-r",
    default=1000,
    help="The max number of roundes before consider a timeout simulation.",
)
def monopoly(number_games, max_rounds):
    simulation = Simulation(number_of_games=number_games, max_rounds=max_rounds)
    result = simulation.simulate()
    print(f"Games with timeout per thousands = {result.timeout_per_thousands:.2f}")
    print(f"Mean turns per game = {result.mean_turns:.2f}")
    for k, v in result.strategy_percentage.items():
        print(f"{k} winning {v:.2f}%")
    print(f"Winner strategy = {result.winner_strategy}")
