# principal file to simulate

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from MagLev import MagLevModel,MagLevJac # Custom packages

t_init = 0
t_end = 10
t_step = 0.1

T = np.linspace(t_init,t_end,100)
index = np.arange(len(T))


cR = 100 # Coil Resistance
cL = 0.1 # Coil indutance
m = 2  # Steel ball mass
K = 0.1  # Eletromag force coeficient
g = 9.81  # gravition constant

#parameters
V = 120 #Volts
model_param = [V,cR,cL,m,K,g]

# analitic stacionary point
i0 = V/cR
d0 = sqrt(K*pow(i0,2)/g)
dot_d0 = 0

x0 = [i0,d0,dot_d0]

r = ode(MagLevModel,MagLevJac)

r.set_initial_value(x0,0)
r.set_f_params(model_param)
r.set_jac_params(model_param)

Y= np.zeros((len(T),3))
for i in index:
  if(r.successful): Y[i,:] = r.integrate(r.t+t_step)
  else: break

print("ploting")
plt.figure
plt.plot(Y)
plt.show()
