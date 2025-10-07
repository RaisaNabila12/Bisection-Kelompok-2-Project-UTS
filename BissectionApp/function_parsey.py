import math

def evaluate_function(func_str, x):
    """
    Evaluasi string fungsi matematika seperti 'x**3 - 4*x + 1'
    """
    try:
        return eval(func_str, {"x": x, "math": math})
    except Exception as e:
        return None
