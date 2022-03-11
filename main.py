
""" THIS IS A TEMPLATE; PLEASE CREATE A COPY BEFORE USING!!! """


""" BASE CODE -- DO NOT MODIFY! SEE how_to_use.md FOR INSTRUCTIONS """ 


# a value containing numerical and uncertainty components
class Value:
  n = 0
  u = 0

  def __init__(self, n, u):
    self.n = n
    self.u = u

  def __str__(self):
    return str(self.n) + " ± " + str(self.u)

  def const(k):
    return Value(k, 0)

  def exp(self, power):
    uncertainty = self.n * self.u * pow(2, 0.5)
    return Value(pow(self.n, power), uncertainty)

  def negate(self):
    return Value(-1 * self.n, self.u)

  def __add__(self, x):
    return addu(self, x)

  def __sub__(self, x):
    return addu(self, x.negate())

  def __mul__(self, x):
    return multu(self, x)

  def __truediv__(self, x):
    return divu(self, x)

  def __pow__(self, x):
    return self.exp(x)

  def __neg__(self):
    return self.negate()
    
    
    


# adds/subtracts two or more values, with uncertainty
def addu(first, *vals):

  sum = first.n
  uncertainty = first.u * first.u

  for val in vals:
    sum += val.n
    uncertainty += val.u * val.u
  
  uncertainty = pow(uncertainty, 0.5)

  return Value(sum, uncertainty)


# multiplies two or more values, with uncertainty
def multu(first, *vals):

  product = first.n
  uncertainty = pow((first.u / first.n), 2)

  for val in vals:
    product *= val.n
    uncertainty += pow((val.u / val.n), 2)

  uncertainty = pow(uncertainty, 0.5) * product

  return Value(product, uncertainty)


# divides two values, with uncertainty
def divu(first, second):

  quotient = first.n
  uncertainty = pow((first.u / first.n), 2)

  quotient /= second.n
  uncertainty += pow((second.u / second.n), 2)

  uncertainty = pow(uncertainty, 0.5) * quotient

  return Value(quotient, uncertainty)


# ---------------------

""" YOUR CODE GOES BELOW """

# demo code:

m = Value(0.4973, 0.0005)
R_c = Value(3.65, 0.05)
M = Value(0.2766, 0.0005)
R_w = Value(4.25, 0.05)
r_w = Value(2.25, 0.05)

# I_c = multu(Value.const(0.5), m, R_c.exp(2))
# I_w = multu(Value.const(0.5), M, addu(R_w.exp(2), r_w.exp(2).negate()))
# ^^ DEPRECATED; prefer using normal arithmetic operators

I_c = Value.const(0.5) * m * (R_c ** 2)
I_w = Value.const(0.5) * M * ((R_w ** 2) - (r_w ** 2))

print(I_c)
print(I_w)
print(I_c + I_w)

"""
Output for Example Code:

3.312639625 ± 0.06426143693282835
1.7979 ± 0.047139252818113285
5.110539625 ± 0.0796971858532149
"""
