import sympy as sy
sy.init_printing() # for LaTeX formatted output
from IPython.display import display
x,r=sy.symbols('x r')
y = sy.symbols('y', cls=sy.Function)
#Enter p(x) and q(x)
px=2/x;qx=-1#this is an example
print('In the given DE, p(x) and q(x) are')
display(px,qx)
p0=sy.limit(x*px,x,0);q0=sy.limit(x**2*qx,x,0)
IE=sy.Eq(r**2+(p0-1)*r+q0,0)
print('Indicial equation is')
display(IE)
roots=sy.solve(IE,r)
print('with roots',roots)#display(p0,q0)
DE = sy.Eq(y(x).diff(x, 2) + px*(y(x).diff(x)) + qx*y(x), 0)
sol = sy.dsolve(DE,y(x),hint='2nd_power_series_regular')
display(sol)