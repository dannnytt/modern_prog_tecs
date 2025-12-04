import random
import math
import re
import json
import os
import keyword
import datetime as dt
from statistics import mean, pvariance
import pandas as pd

def draw_until_collect_all(n):
    
    seen = set()
    draws = 0
    while len(seen) < n:
        draws += 1
        seen.add(random.randrange(n))
    return draws

def run_trials(n, trials=3000, seed=None):
    if seed is not None:
        random.seed(seed)
    return [draw_until_collect_all(n) for _ in range(trials)]

def M_theoretical(n):
    if n <= 0:
        return 0.0
    return 0.9 * n * math.log2(n)

def D_theoretical(n):
    
    return (math.pi ** 2 * n * n) / 6.0
    

def approx_rel_err(n):
    if n <= 1:
        return float('inf')
    return 1.0 / (2.0 * math.log2(n))

def jensen_split(n, n1=None, n2=None):
    if n1 is None or n2 is None:
        n1 = n // 2
        n2 = n - n1
    val = 0.0
    if n1 > 0:
        val += n1 * math.log2(n1)
    if n2 > 0:
        val += n2 * math.log2(n2)
    return val, n1, n2

def analyze_source_text(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    identifiers = re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', text)
    total_tokens = len(identifiers)
    unique_tokens = sorted(set(identifiers))
    vocab_size = len(unique_tokens)
    py_keywords = set(keyword.kwlist)
    operators = sorted([t for t in unique_tokens if t in py_keywords])
    operands = sorted([t for t in unique_tokens if t not in py_keywords])
    n1_text = len(operators)
    n2_text = len(operands)
    n_text = n1_text + n2_text
    L_formula_0_9 = M_theoretical(n_text) if n_text > 0 else 0.0
    D_formula = D_theoretical(n_text)
    L_jensen_text, n1_guess, n2_guess = jensen_split(n_text, n1=n1_text, n2=n2_text)
    param_sections = re.findall(r'def\s+\w+\s*\(([^)]*)\)', text)
    params = set()
    for p in param_sections:
        for name in re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', p):
            params.add(name)
    n_params = len(params)
    n_star2 = n_params * 2
    return {
        'path': path,
        'total_tokens': total_tokens,
        'vocab_size': vocab_size,
        'unique_tokens_sample': unique_tokens[:200],
        'n1_text': n1_text,
        'n2_text': n2_text,
        'n_text': n_text,
        'L_by_formula_0.9nlog2n': L_formula_0_9,
        'D_by_formula': D_formula,
        'L_by_Jensen': L_jensen_text,
        'n_params_in_defs': n_params,
        'n_star2': n_star2
    }

def save_results_json(rows, json_path):
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    out = {'meta': {'generated_at_utc': timestamp}, 'table': rows}
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

def main():
    ns = [16, 32, 64, 128]
    trials = 3000
    seed = 42
    rows = []
    for n in ns:
        results = run_trials(n, trials=trials, seed=seed)
        emp_mean = mean(results)
        emp_var_pop = pvariance(results)
        emp_std = math.sqrt(emp_var_pop)
        emp_rel_err = emp_std / emp_mean if emp_mean != 0 else float('inf')
        M_th = M_theoretical(n)
        D_th = D_theoretical(n)
        std_th = math.sqrt(D_th)
        rel_err_th = std_th / M_th if M_th != 0 else float('inf')
        approx_rel = approx_rel_err(n)
        L_jensen_val, n1_guess, n2_guess = jensen_split(n)
        row = {
            'n': n,
            'trials': trials,
            'emp_mean': emp_mean,
            'emp_var_pop': emp_var_pop,
            'emp_std': emp_std,
            'emp_rel_err_empirical': emp_rel_err,
            'M_theor_0.9nlog2n': M_th,
            'D_theor_pi2n2_over_6': D_th,
            'std_theor': std_th,
            'rel_err_theor': rel_err_th,
            'approx_rel_err_1_over_2log2n': approx_rel,
            'L_jensen_equal_split': L_jensen_val,
            'L_jensen_n1': n1_guess,
            'L_jensen_n2': n2_guess
        }
        rows.append(row)
        print(f"n={n}: emp_mean={emp_mean:.6f}, emp_std={emp_std:.6f}, emp_rel_err={emp_rel_err:.6f}")
    out_dir = os.path.abspath(os.path.dirname(__file__)) if '__file__' in globals() else os.getcwd()
    json_path = os.path.join(out_dir, 'simulation_results.json')
    save_results_json(rows, json_path)
    print("Results saved to", json_path)
    try:
        source_path = os.path.abspath(__file__)
    except NameError:
        source_path = os.path.join(out_dir, 'simulator_json_only.py')
    try:
        text_analysis = analyze_source_text(source_path)
        print("--- Source analysis ---")
        print("vocab_size:", text_analysis['vocab_size'], "total_tokens:", text_analysis['total_tokens'])
    except Exception as e:
        text_analysis = {'error': str(e)}
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['text_analysis'] = text_analysis
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("JSON updated with text analysis.")

if __name__ == '__main__':
    main()
