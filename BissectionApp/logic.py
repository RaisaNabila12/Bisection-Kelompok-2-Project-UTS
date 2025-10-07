from function_parser import evaluate_function

def bisection_method(func_str, a, b, eps, max_iter):
    results = []
    fa = evaluate_function(func_str, a)
    fb = evaluate_function(func_str, b)

    if fa * fb > 0:
        return None, "Fungsi tidak memiliki akar di selang ini!", results

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = evaluate_function(func_str, c)
        results.append((i, a, b, c, fa, fb, fc))

        if abs(fc) < eps or (b - a) / 2 < eps:
            return c, None, results

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2, "Iterasi maksimum tercapai", results
