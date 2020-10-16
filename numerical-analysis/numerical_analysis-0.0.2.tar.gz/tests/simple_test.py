import numpy as np
import numerical_analysis as na


def f(x):
    return 3 * (x - 1) ** 2 - 2 * x


def df_dx(x):
    return 6 * x - 8


cp = np.array([[1., 3.],
               [2., 4.],
               [3., 5.],
               [4., 1.],
               [5., 1.]])

bezier = na.splines.Bezier(cp)
bezier.plot(0.01)

comp_bezier = na.splines.CompositeQuadraticBezier(cp)
comp_bezier.plot(0.01)

xa = 3
xb = 5
n = 1000

print(na.integration.trapezoid(f, xa, xb, n))
print(na.integration.simpson1_3(f, xa, xb, n))
print(na.integration.simpson3_8(f, xa, xb, n))
print(na.integration.romberg(f, xa, xb, 10))
print(na.integration.gauss_legendre(f, xa, xb, 11))

print(na.root_finding.secant(f, 0, 1))
print(na.root_finding.newton_raphson(f, df_dx, 0))
