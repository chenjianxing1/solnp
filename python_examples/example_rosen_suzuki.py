"""
To test this algorithm, then:
1) Install this package, for example through pip or by running "pip install ." from the cpp_solnp folder.
2) Run this file with Python
"""

import pysolnp

# Alkyla function from the original documentation of SOLNP
# This problem has both equality and inequality constraints, as well as the parameter bounds.
def rosen_suzuki_objective_function(x):
    result = x[0] * x[0] + x[1] * x[1] + 2 * x[2] * x[2] + x[3] * x[3] - 5 * x[0] - 5 * x[1] - 21 * x[2] + 7 * x[3]
    return result

def rosen_suzuki_inequality_function(x):
    result = [
        8 - x[0] * x[0] - x[1] * x[1] - x[2] * x[2] - x[3] * x[3] - x[0] + x[1] - x[2] + x[3],
        10 - x[0] * x[0] - 2 * x[1] * x[1] - x[2] * x[2] - 2 * x[3] * x[3] + x[0] + x[3],
        5 - 2 * x[0] * x[0] - x[1] * x[1] - x[2] * x[2] - 2 * x[0] + x[1] + x[3],
    ]
    return result


starting_point = [1, 1, 1, 1]
inequality_lower_bounds = [0, 0, 0]
inequality_upper_bounds = [1000, 1000, 1000]

if __name__ == "__main__":

    result = pysolnp.solve(
        obj_func=rosen_suzuki_objective_function,
        par_start_value=starting_point,
        ineq_func=rosen_suzuki_inequality_function,
        ineq_lower_bounds=inequality_lower_bounds,
        ineq_upper_bounds=inequality_upper_bounds)

    final_parameters = result.optimum
    print(final_parameters)
    print(result.solve_value)
    print(result.callbacks)

    print(rosen_suzuki_inequality_function(final_parameters))

    final_objective_value = rosen_suzuki_objective_function(final_parameters)

    inequality_constraints = rosen_suzuki_inequality_function(final_parameters)

    for index, value in enumerate(inequality_constraints):
        distance_to_lower = value - inequality_lower_bounds[index]
        distance_to_over = inequality_upper_bounds[index] - value
        print(f"Distance for index {index}: lower {distance_to_lower} upper {distance_to_over}")
