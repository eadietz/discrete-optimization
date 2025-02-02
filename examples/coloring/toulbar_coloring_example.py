#  Copyright (c) 2022 AIRBUS and its affiliates.
#  This source code is licensed under the MIT license found in the
#  LICENSE file in the root directory of this source tree.

import logging
import os

os.environ["DO_SKIP_MZN_CHECK"] = "1"
from discrete_optimization.coloring.coloring_parser import (
    get_data_available,
    parse_file,
)
from discrete_optimization.coloring.coloring_plot import plot_coloring_solution, plt
from discrete_optimization.coloring.solvers.coloring_toulbar_solver import (
    ToulbarColoringSolver,
)


def run_toulbar_coloring():
    logging.basicConfig(level=logging.INFO)
    file = [f for f in get_data_available() if "gc_70_3" in f][0]
    color_problem = parse_file(file)
    solver = ToulbarColoringSolver(color_problem, params_objective_function=None)
    solver.init_model(
        nb_colors=None,
        value_sequence_chain=True,
        hard_value_sequence_chain=False,
        tolerance_delta_max=2,
    )
    result_store = solver.solve(time_limit=10)
    solution = result_store.get_best_solution_fit()[0]
    plot_coloring_solution(solution)
    plt.show()
    assert color_problem.satisfy(solution)


if __name__ == "__main__":
    run_toulbar_coloring()
