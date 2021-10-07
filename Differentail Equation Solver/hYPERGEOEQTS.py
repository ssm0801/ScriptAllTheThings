import sympy as sy
sy.init_printing() # for LaTeX formatted output
from IPython.display import display
x,t = sy.symbols('x t'); y = sy.symbols('y', cls=sy.Function)
cy2=sy.sympify(input("Enter the coeff. of y’’ "))
cy1=sy.sympify(input("Enter the coeff. of y’ "))
cy0=sy.sympify(input("Enter the coeff. of y "))
s=sy.Eq(sy.factor(cy2)*y(x).diff(x,x)+cy1*y(x).diff(x)+cy0*y(x),0)
display(s)
print("Let us compare it with (x-A)(x-B)y’’+(Cx+D)y’+Ey=0.")
A=sy.sympify(input("Here A = "))
B=sy.sympify(input("and B = "))
print('So using the transformation x=(B-A)t+A, we get')
t1=(B-A)*t+A
k2=sy.lambdify(x,cy2);
k1=sy.lambdify(x,cy1);
k0=sy.lambdify(x,cy0)
s=sy.Eq(sy.factor(k2(t1))*y(t).diff(t,t)*(sy.diff(t1,t))**-2+sy.simplify((sy.diff(t1,t)**-1)*k1(t1))*y(t).diff(t)+k0(t1)*y(t),0)
display(s)
print("Comparing with t(t-1)y’’+[(a+b+1)t-c]y’+aby=0, we have")
S=sy.sympify(input("a+b+1 = "))
c=sy.sympify(input("c = "))
P=sy.sympify(input("ab = "))
print('So a, b are')
r1=((S-1)+((S-1)**2-4*P)**(1/2))/2
r2=((S-1)-((S-1)**2-4*P)**(1/2))/2
print(r1,',',r2)
print('Thus, general solution of the given DE is')
sol=sy.symbols('y=c_1\;F(a,b,c,t)+c_2\;t^{1-c}F(a-c+1,b-c+1,2-c,t)')
display(sol)
print('where')
print('a =',r1,'b =',r2,'c =',c,'t =',(x-A)/(B-A))