#Standart Libraries (Math)
#-------------------------

import math

print(dir(math))
"""
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
"""
print(math.ceil(1.1)) #2
print(math.ceil(1.8)) #2
print(math.ceil(1.005)) #2

print(math.copysign(-2,3)) #2.0
print(math.copysign(3,-2)) #-3.0

print(math.fabs(-2)) #2.0
print(math.fabs(-1.5)) #1.5

print(math.factorial(5)) #120
print(math.factorial(0)) #1
#print(math.factorial(-2)) #ValueError: factorial() not defined for negative values

print(math.floor(-1.1)) #-2
print(math.floor(1.9)) #1
print(math.floor(1.005)) #1

print(math.fmod(10,2)) #0.0
print(math.fmod(13,2)) #1.0
print(math.fmod(13,-2)) #1.0
print(math.fmod(-13,2)) #-1.0

#x = m*2**e
print(math.frexp(5)) #(0.625, 3)
print(math.frexp(3)) #(0.75, 2)

print(sum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])) #0.9999999999999999
print(math.fsum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])) #1.0

#ebob
print(math.gcd(120,75)) #15

print(math.isclose(1.123,1.752)) #False
print(math.isclose(1.123,1.123000)) #True

print(math.modf(1.8)) #(0.8, 1.0)
print(math.modf(1)) #(0.0, 1.0)

#like int()
print(math.trunc(1.8)) #1
print(math.trunc(-0.8)) #0

#constants
#----------------------

print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045
print(math.tau) #6.283185307179586

#exponential functions
#-------------------------

print(math.exp(1)) #2.718281828459045
print(math.exp(2)) #7.38905609893065
print(math.exp(4)) #54.598150033144236

print(math.expm1(1)) #1.718281828459045
print(math.expm1(2)) #6.38905609893065
print(math.expm1(4)) #53.598150033144236

print(math.log(5,10)) #0.6989700043360187
print(math.log(10,10)) #1.0
print(math.log(1,10)) #0.0

print(math.log1p(1)) #0.6931471805599453
print(math.log1p(0)) #0.0

print(math.log2(10)) #3.321928094887362
print(math.log2(3)) #1.584962500721156

print(math.log10(1)) #0.0
print(math.log10(5)) #0.6989700043360189

print(math.pow(2,3)) #8.0
print(math.pow(5,4)) #625.0

print(math.sqrt(9)) #3.0
print(math.sqrt(27)) #5.196152422706632

print(math.degrees(5)) #286.4788975654116
print(math.degrees(1.5)) #85.94366926962348

print(math.radians(286.4788975654116)) #5.0
print(math.radians(85.94366926962348)) #1.5

print(math.acos(1)) #0.0
print(math.acos(0)) #1.5707963267948966

print(math.asin(0)) #0.0
print(math.asin(1)) #1.5707963267948966

#other functions in math modules
"""
atan()
atan2(y,x)
cos()
sin()
tan()
hypot()

hyperbolic functions
#----------------------
acosh()
asinh()
atanh()
cosh()
sinh()
tanh()
cosh()
"""

#gamma function like factorial but -1
print(math.gamma(2)) #1.0
print(math.gamma(4)) #6.0
print(math.gamma(5)) #24.0
print(math.gamma(7)) #720.0

print(math.log(math.gamma(5))) #3.1780538303479458
print(math.lgamma(5)) #3.178053830347945