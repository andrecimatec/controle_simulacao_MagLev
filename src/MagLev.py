import numpy as np
from math import sqrt,pow


def MagLevModel(t,x,P):

  V = P[0] #input voltage
  i = x[0] # electromagnet current
  d = x[1] # distance from electromagnet
  dot_d = x[2] #velocity in relation to electromagnet

  R = P[1] # Coil Resistance
  L = P[2] # Coil inductance
  m = P[3]  # Steel ball mass
  K = P[4]  # electromagnet force coefficient
  g = P[5]  # gravitation constant

  dfdt = np.zeros(3)
  dfdt[0] = (V-R*i)/L
  dfdt[1] = dot_d
  dfdt[2] = g - K*pow(i,2)/pow(d,2)

  return dfdt

def MagLevJac(t,x,P):

  i = x[0] # electromagnet current
  d = x[1] # distance from electromagnet
  dot_d = x[2] #velocity in relation to electromagnet

  R = P[1] # Coil Resistance
  L = P[2] # Coil inductance
  m = P[3]  # Steel ball mass
  K = P[4]  # electromagnet force coefficient
  g = P[5]  # gravitation constant

  dfdx1 = [-R/L, 0, 0]
  dfdx2 = [0,0,1]
  dfdx3 = [2*K*i/pow(d,2), -2*K*pow(i,2)/pow(d,3), 0]

  Jac = np.zeros((3,3))
  Jac[0,:] = dfdx1
  Jac[1,:] = dfdx2
  Jac[2,:] = dfdx3
  return Jac

def MagLevGradient(t,x,P):

  i = x[0] # electromagnet current
  d = x[1] # distance from electromagnet
  #dot_d = x[2] #velocity in relation to electromagnet

  R = P[1] # Coil Resistance
  L = P[2] # Coil inductance
  #m = P[3]  # Steel ball mass
  K = P[4]  # electromagnet force coefficient
  #g = P[5]  # gravitation constant

  dfdx1 = [-R/L, 0, 0]
  dfdx2 = [0,0,1]
  dfdx3 = [2*K*i/d^2, -2*K*i^2/d^3, 0]

  Grad = np.zeros(3)
  Grad[0] = dfdx1[0] + dfdx1[1] + dfdx1[2]
  Grad[1] = dfdx2[0] + dfdx2[1] + dfdx2[2]
  Grad[2] = dfdx3[0] + dfdx3[1] + dfdx3[2]
  return Grad