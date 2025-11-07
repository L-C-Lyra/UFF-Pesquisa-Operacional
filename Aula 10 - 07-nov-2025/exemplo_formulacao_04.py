from mip import *
import time

n = 14
c = [[0, 83, 81, 113, 52, 42, 73, 44, 23, 91, 105, 90, 124, 57],
     [83, 0, 161, 160, 39, 89, 151, 110, 90, 99, 177, 143, 193, 100],
     [81, 161, 0, 90, 125, 82, 13, 57, 71, 123, 38, 72, 59, 82],
     [113, 160, 90, 0, 123, 77, 81, 71, 91, 72, 64, 24, 62, 63],
     [52, 39, 125, 123, 0, 51, 114, 72, 54, 69, 139, 105, 155, 62],
     [42, 89, 82, 77, 51, 0, 70, 25, 22, 52, 90, 56, 105, 16],
     [73, 151, 13, 81, 114, 70, 0, 45, 61, 111, 36, 61, 57, 70],
     [44, 110, 57, 71, 72, 25, 45, 0, 23, 71, 67, 48, 85, 29],
     [23, 90, 71, 91, 54, 22, 61, 23, 0, 74, 89, 69, 107, 36],
     [91, 99, 123, 72, 69, 52, 111, 71, 74, 0, 117, 65, 125, 43],
     [105, 177, 38, 64, 139, 90, 36, 67, 89, 117, 0, 54, 22, 84],
     [90, 143, 72, 24, 105, 56, 61, 48, 69, 65, 54, 0, 60, 44],
     [124, 193, 59, 62, 155, 105, 57, 85, 107, 125, 22, 60, 0, 97],
     [57, 100, 82, 63, 62, 16, 70, 29, 36, 43, 84, 44, 97, 0]]

st = time.process_time()

model = Model(name="tsp",sense=MINIMIZE, solver_name=CBC)

x = [[model.add_var(name='x_'+str(i)+'_'+str(j), var_type=BINARY) for j in range(n)] for i in range(n)]

exp = 0
for i in range(n):
    for j in range(n):
        exp += c[i][j]*x[i][j]
model.objective = minimize(exp)

for i in range(n):
    exp = 0
    for j in range(n):
        if i != j:
           exp += x[i][j]
    model.add_constr(exp == 1, name='Out_'+str(i))

for i in range(n):
    exp = 0
    for j in range(n):
        if i != j:
           exp += x[j][i]
    model.add_constr(exp == 1, name='In_'+str(i))

model.write('model.lp')

model.threads = 1

model.optimize(max_seconds=300)

print("melhor solução  = ", model.objective_value)
print("limite inferior = ", model.objective_bound)
print("tempo           = ", time.process_time() - st)

for i in range(n):
    for j in range(n):
        if x[i][j].x >= 0.99:
            print(x[i][j].name)
