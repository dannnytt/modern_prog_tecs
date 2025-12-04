from math import log2
import re
import pandas as pd
from collections import Counter, defaultdict

S = 18.0  

py_funcs = {
    "min_1d": """def min_1d(arr):
    if not arr:
        return None, -1
    min_val = arr[0]
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    return min_val, min_idx
""",
    "bubble_sort": """def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a
""",
    "binary_search": """def binary_search(a, target):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""",
    "min_2d": """def min_2d(mat):
    if not mat or not mat[0]:
        return None, -1, -1
    min_val = mat[0][0]
    min_i = 0
    min_j = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] < min_val:
                min_val = mat[i][j]
                min_i, min_j = i, j
    return min_val, min_i, min_j
""",
    "reverse_arr": """def reverse_arr(a):
    i = 0
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return a
""",
    "cyclic_shift_left": """def cyclic_shift_left(a, k):
    n = len(a)
    if n == 0:
        return a
    k = k % n
    if k == 0:
        return a
    return a[k:] + a[:k]
""",
    "replace_all": """def replace_all(a, old, new):
    for i in range(len(a)):
        if a[i] == old:
            a[i] = new
    return a
"""
}

cpp_funcs = {
    "min_1d": r"""#include <vector>
#include <utility>
using namespace std;
pair<int,int> min_1d(const vector<int>& a){
    if(a.empty()) return make_pair(0,-1);
    int min_val = a[0];
    int min_idx = 0;
    for(size_t i=1;i<a.size();++i){
        if(a[i] < min_val){
            min_val = a[i];
            min_idx = i;
        }
    }
    return make_pair(min_val, min_idx);
}
""",
    "bubble_sort": r"""#include <vector>
using namespace std;
vector<int> bubble_sort(vector<int> a){
    int n = a.size();
    for(int i=0;i<n;i++){
        bool swapped = false;
        for(int j=0;j<n-i-1;j++){
            if(a[j] > a[j+1]){
                int t = a[j]; a[j]=a[j+1]; a[j+1]=t;
                swapped = true;
            }
        }
        if(!swapped) break;
    }
    return a;
}
""",
    "binary_search": r"""#include <vector>
using namespace std;
int binary_search(const vector<int>& a, int target){
    int lo = 0, hi = (int)a.size()-1;
    while(lo <= hi){
        int mid = (lo + hi)/2;
        if(a[mid] == target) return mid;
        else if(a[mid] < target) lo = mid+1;
        else hi = mid-1;
    }
    return -1;
}
""",
    "min_2d": r"""#include <vector>
#include <tuple>
using namespace std;
tuple<int,int,int> min_2d(const vector<vector<int>>& m){
    if(m.empty() || m[0].empty()) return make_tuple(0,-1,-1);
    int min_val = m[0][0];
    int min_i = 0, min_j = 0;
    for(int i=0;i<(int)m.size();++i){
        for(int j=0;j<(int)m[i].size();++j){
            if(m[i][j] < min_val){
                min_val = m[i][j];
                min_i = i; min_j = j;
            }
        }
    }
    return make_tuple(min_val, min_i, min_j);
}
""",
    "reverse_arr": r"""#include <vector>
using namespace std;
vector<int> reverse_arr(vector<int> a){
    int i = 0, j = a.size()-1;
    while(i < j){
        int t = a[i]; a[i]=a[j]; a[j]=t;
        i++; j--;
    }
    return a;
}
""",
    "cyclic_shift_left": r"""#include <vector>
using namespace std;
vector<int> cyclic_shift_left(const vector<int>& a, int k){
    int n = a.size();
    if(n==0) return a;
    k = k % n;
    if(k==0) return a;
    vector<int> res;
    for(int i=0;i<n;i++) res.push_back(a[(i+k)%n]);
    return res;
}
""",
    "replace_all": r"""#include <vector>
using namespace std;
vector<int> replace_all(vector<int> a, int oldv, int newv){
    for(int i=0;i<(int)a.size();++i){
        if(a[i] == oldv) a[i] = newv;
    }
    return a;
}
"""
}

# множества операторов
py_keywords = set("""def return if else for while in range break continue True False None and or not is import from as with pass yield try except finally class
""".split())
cpp_keywords = set("""int void bool return if else for while switch case default break continue namespace using include template typename class struct vector pair tuple make_pair make_tuple const
""".split())

# набор операторных символов
op_symbols = ['==','!=','<=','>=','+=','-=','*=','/=','//','**','->','::','&&','||','<<','>>','%','+','-','*','/','=','<','>',',',':',';','(',')','[',']','{','}','&','|','!','~']

token_re = re.compile(r"""
    (\".*?\"|\'.*?\')|        # строки
    ([A-Za-z_]\w*)|           # идентификаторы
    (\d+\.\d+|\d+)|           # числа
    (==|!=|<=|>=|\+=|-=|\*=|/=|//|\*\*|->|::|&&|\|\||<<|>>)| # многосимвольные операции
    ([\+\-\*\/%=<>&\|\!\~\:\;\,\(\)\[\]\{\}]) # одиночные символы
""", re.VERBOSE | re.DOTALL)

def tokenize(code):
    tokens = []
    for m in token_re.finditer(code):
        tok = m.group(0)
        tokens.append(tok)
    return tokens

def classify_tokens(tokens, lang='py'):
    operators = []
    operands = []
    for t in tokens:
        if lang=='py' and t in py_keywords:
            operators.append(t)
        elif lang=='cpp' and t in cpp_keywords:
            operators.append(t)
        elif t in op_symbols:
            operators.append(t)
        elif re.match(r'^[A-Za-z_]\w*$', t): 
            operands.append(t)
        elif re.match(r'^\d+(\.\d+)?$', t):  
            operands.append(t)
        elif (t.startswith('"') or t.startswith("'")):
            operands.append(t)
        else:
            if re.match(r'^[\:\;\,\(\)\[\]\{\}]$', t):
                operators.append(t)
            else:
                operands.append(t)
    return operators, operands

def compute_metrics(code, lang='py', n2_star=None):
    tokens = tokenize(code)
    ops, oprs = classify_tokens(tokens, lang)

    op_counter = Counter(ops)
    opr_counter = Counter(oprs)
    n1 = len(op_counter)  
    n2 = len(opr_counter) 
    N1 = sum(op_counter.values())
    N2 = sum(opr_counter.values())
    n = n1 + n2
    N = N1 + N2
    # length by Halstead
    def safe_log2(x):
        return log2(x) if x>0 else 0.0
    N_hat = n1*safe_log2(n1) + n2*safe_log2(n2)
    # V*
    if n2_star is None:
        n2_star = 1
    V_star = (2 + n2_star) * safe_log2(2 + n2_star)
    # V
    V = N * safe_log2(n) if n>0 else 0.0
    L = V_star / V if V>0 else 0.0
    L_hat = (2.0 / n1) * (n2 / N2) if n1>0 and N2>0 else 0.0
    I = (2.0 / n1) * (n2 / N2) * N * safe_log2(n) if n1>0 and N2>0 else 0.0
    T1_hat = (N_hat**2) / (S * V_star) if S>0 and V_star>0 else 0.0
    # T2^
    T2_hat = 0.0
    if n1>0 and n2>0 and S>0 and n>0:
        T2_hat = (n1 * N2 * (n1*safe_log2(n1) + n2*safe_log2(n2)) * safe_log2(n)) / (2.0 * S * n2)
    T3_hat = (n1 * N2 * N * safe_log2(n)) / (2.0 * S * n2) if n1>0 and n2>0 and S>0 and n>0 else 0.0
    # lambda metrics
    lambda1 = (L_hat**2) * V if V>0 else 0.0
    lambda2 = (V_star**2) / V if V>0 else 0.0
    return {
        'n2*': n2_star,
        'n1': n1,
        'n2': n2,
        'n': n,
        'N1': N1,
        'N2': N2,
        'N': N,
        'N^': N_hat,
        'V*': V_star,
        'V': V,
        'L': L,
        "L^": L_hat,
        'I': I,
        'T1^': T1_hat,
        'T2^': T2_hat,
        'T3^': T3_hat,
        'lambda1': lambda1,
        'lambda2': lambda2,
        'ops_counter': op_counter,
        'oprs_counter': opr_counter,
        'tokens': tokens
    }

# n2* для каждой функции
n2star_map = {
    'min_1d': 3,         
    'bubble_sort': 2,    
    'binary_search': 3,  
    'min_2d': 4,         
    'reverse_arr': 2,    
    'cyclic_shift_left': 3, 
    'replace_all': 4
}

rows = []

for name, code in py_funcs.items():
    mets = compute_metrics(code, lang='py', n2_star=n2star_map[name])
    row = {'language':'Python', 'function':name, 'code': code}
    row.update(mets)
    rows.append(row)

for name, code in cpp_funcs.items():
    mets = compute_metrics(code, lang='cpp', n2_star=n2star_map[name])
    row = {'language':'C++', 'function':name, 'code': code}
    row.update(mets)
    rows.append(row)

df = pd.DataFrame(rows)

display_cols = ['language','function','n2*','n1','n2','n','N1','N2','N','N^','V*','V','L','L^','I','T1^','T2^','T3^','lambda1','lambda2']

pd.options.display.float_format = '{:0.4f}'.format
df_display = df[display_cols].copy()
df_display = df_display.set_index(['language','function'])
print(df_display)