from mip import *

model = Model(name="exemplo1",sense=MAXIMIZE, solver_name=CBC)

x0 = model.add_var(name='x0', var_type=CONTINUOUS, lb=0, ub=40)
x1 = model.add_var(name='x1', var_type=CONTINUOUS, lb=0)
x2 = model.add_var(name='x2', var_type=CONTINUOUS, lb=0)

model.add_constr(-x0 + x1 + x2 <= 20, name='rest1')
model.add_constr(x0 - 3*x1 + x2 <= 30, name='rest1')

model.objective = maximize(x0 + 2*x1 + 3*x2)

model.optimize()

print("sol = ", model.objective_value)
