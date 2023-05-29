from math import atan, sin, cos, inf


def func_1(x):
    """First function example"""
    return 2 * atan(x) - 3 * x + 2


def func_2(x):
    """Second function example"""
    return 5.67 * sin(4.794 * x) - 4.55 * x


def dfunc_1(x):
    """Derivative of first function"""
    return 2 / (1 + x ** 2) - 3


def dfunc_2(x):
    """Derivative of second function"""
    return 27.18198 * cos(4.794 * x) - 4.55


def find_max(d_func, a, b, h):
    """Algorithm of finding maximum of a derivative"""
    x = a
    maximum = d_func(x)
    while x < b:
        x += h
        maximum = max(d_func(x), maximum)
    return maximum


def find_roots(func, xl, xr, h=0.001):
    """Algorithm of finding roots"""
    result = []
    prev_x = xl
    curr_x = xl
    curr_y = func(curr_x)

    while curr_x <= xr:
        curr_x = curr_x + h
        prev_y = curr_y
        curr_y = func(curr_x)
        if prev_y * curr_y < 0:
            result.append((round(prev_x, 4), round(curr_x, 4)))
        prev_x = curr_x
    return result


def bisections_method(func, root_segments, eps=1e-15):
    """Bisection method of finding roots"""
    result = []

    for segment in root_segments:
        xl, xr = segment
        iter_nums = 0
        while abs(xl - xr) > eps:
            mid = (xl + xr) / 2
            if func(xl) * func(mid) < 0:
                xr = mid
            else:
                xl = mid
            iter_nums += 1
        mid = (xl + xr) / 2
        result.append((round(mid), iter_nums, segment))

    return result


def newton_method(func, d_func, root_segments, eps=1e-15):
    """Newton method of finding roots"""
    result = []

    for segment in root_segments:
        xl, xr = segment
        x = xl
        err = inf
        iter_nums = 0
        while err > eps:
            root = x - (func(x) / d_func(x))
            err = abs(x - root)
            x = root
            iter_nums += 1
        root = x - (func(x) / d_func(x))
        result.append((round(root, 4), iter_nums, segment))

    return result


def fixed_point_iteration_method(func, d_func, root_segments, eps=1e-15):
    """Fixed point iteration method of finding roots"""
    result = []
    for segment in root_segments:
        xl, xr = segment
        prev = (xl + xr) / 2
        err = inf
        mul = 1 / find_max(d_func, xr, xl, 0.0001)
        iter_nums = 0
        while err > eps:
            cur = prev - mul * func(prev)
            err = abs(cur - prev)
            prev = cur
            iter_nums += 1
        cur = prev - mul * func(prev)
        result.append((round(cur), iter_nums, segment))

    return result


# Examples
roots_1 = find_roots(func_1, -3, 3, 0.001)
roots_2 = find_roots(func_2, -3, 3, 0.001)

bisec_1 = bisections_method(func_1, roots_1, 1e-15)
newton_1 = newton_method(func_1, dfunc_1, roots_1, 1e-15)
bisec_2 = bisections_method(func_2, roots_2, 1e-15)
newton_2 = newton_method(func_2, dfunc_2, roots_2, 1e-15)
fixed_point_2 = fixed_point_iteration_method(func_2, dfunc_2, roots_2, 1e-15)

for root in bisec_1:
    print(
        f"First function, bisection method, on segment {root[2]}: root is {root[0]}, number of iterations: {root[1]}\n")
for root in newton_1:
    print(f"First function, Newton method, on segment {root[2]}: roots is {root[0]}, number of iterations: {root[1]}\n")
for root in bisec_2:
    print(
        f"Second function, bisection method, on segment {root[2]}: roots is {root[0]}, number of iterations: {root[1]}\n")
for root in newton_2:
    print(
        f"Second function, Newton method, on segment {root[2]}: roots is {root[0]}, number of iterations: {root[1]}\n")
for root in fixed_point_2:
    print(f"Second function, fixed point iteration method, on segment {root[2]}: roots is {root[0]},"
          f" number of iterations: {root[1]}\n")
