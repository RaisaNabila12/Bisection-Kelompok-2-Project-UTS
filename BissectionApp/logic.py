from function_parser import f_sym

def bisection_method(a, b, max_iter, tol, func_str):
    try:
        f_a = f_sym(a, func_str)
        f_b = f_sym(b, func_str)
    except ValueError as e:
        return None, None, str(e)
    except Exception as e:
        return None, None, f"Error evaluasi fungsi pada batas awal: {e}"

    if f_a * f_b >= 0:
        return None, None, "Metode Bisection gagal: f(a) dan f(b) harus berlawanan tanda."

    f_current_a = f_a
    iteration_data = []

    for i in range(1, max_iter + 1):
        x_mid = (a + b) / 2
        try:
            f_mid = f_sym(x_mid, func_str)
        except Exception as e:
            return None, None, f"Error evaluasi fungsi pada iterasi {i}: {e}"

        error_abs = abs(b - a) / 2

        iteration_data.append({
            'Iterasi': i,
            'a': a,
            'b': b,
            'x_tengah': x_mid,
            'f(x_tengah)': f_mid,
            'Error Mutlak': error_abs
        })

        if abs(f_mid) < tol or error_abs < tol:
            return x_mid, iteration_data, f"Konvergensi tercapai pada Iterasi ke-{i}."

        if f_current_a * f_mid < 0:
            b = x_mid
        else:
            a = x_mid
            f_current_a = f_mid

    return x_mid, iteration_data, f"Jumlah iterasi maksimum ({max_iter}) tercapai."
