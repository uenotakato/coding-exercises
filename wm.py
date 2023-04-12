import random
import matplotlib.pyplot as plt


class wm:
  def __init__(self, experts, experts_weight):
    self.W_A = 0  # Initialize W_A and W_B
    self.W_B = 0
    for i in range(len(experts)):
      if experts[i] == "A":
        self.W_A += experts_weight[i]*1
      else:
        self.W_B += experts_weight[i]*1

  def predict(self):
    # a majoritiy's prediction
    if self.W_A >= self.W_B:
      self.prediction = "A"
    else:
      self.prediction = "B"

  def update(self, true, epsilon):
    if self.prediction == true:
      for i in range(len(experts)):
        if experts[i] == self.prediction:
          experts_weight[i] = 1
        else:
          experts_weight[i] = 1 - epsilon
    else:
      for i in range(len(experts)):
        if experts[i] == self.prediction:
          experts_weight[i] = 1 - epsilon
        else:
          experts_weight[i] = 1

  def plot(self):
    A = 0
    B = 0
    n_A = 0
    n_B = 0
    for i in range(len(experts)):
      if experts[i] == "A":
        A += experts_weight[i]
        n_A += 1
      else:
        B += experts_weight[i]
        n_B += 1
    x = ["A", "B"]
    y = [A/n_A, B/n_B]
    plt.bar(x, y)
    plt.show()


n = 100
experts_weight = [1]*n
experts = [random.choice(["A", "B"]) for i in range(n)]

wm1 = wm(experts, experts_weight)
wm1.predict() # A
wm1.update(random.choice(["A", "B"]), 0.15)
wm1.plot()
