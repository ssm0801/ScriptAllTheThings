import sympy as sy
sy.init_printing() # for LaTeX formatted output
from IPython.display import display
x,r=sy.symbols('x r')
y = sy.symbols('y', cls=sy.Function)
#Enter p(x) and q(x)
px=1/x;qx=2/x
print('In the given DE, p(x) and q(x) are')
display(px,qx)
DE = sy.Eq(y(x).diff(x, 2) + px*(y(x).diff(x)) + qx*y(x), 0)
sol = sy.dsolve(DE,y(x),hint='2nd_power_series_ordinary')
print('Power series solution is')
display(sol)