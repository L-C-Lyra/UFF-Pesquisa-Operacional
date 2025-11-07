from mip import *

model = Model(name="exemplo3",sense=MAXIMIZE, solver_name=CBC)

model.read('exemplo_formulacao_03.lp')
print('modelo tem', model.num_cols, 'variaveis')
print('e ', model.num_rows, ' restrições')

status = model.optimize()
print("\n",status)

vars = model.vars

for i in range(len(vars)):
    print(vars[i].x)

print("sol = ", model.objective_value)
