import PLCS
import matplotlib.pyplot as plt, random as rnd
def rb():
  return rnd.choice((0, 1))
def randbool():
  return rnd.choice((True, False))
results = []
for i in range(100):
  a = list(map(
    lambda _ : rb(),
    range(20)
  ))
  b = list(map(
    lambda x : a[x] if randbool() else rb(),
    range(20)
  ))
  print(a)
  print(b)
  for i in range(1000):
    results.append(PLCS.runPLCS(a, b, 0.2))
plt.hist(results)
plt.show()