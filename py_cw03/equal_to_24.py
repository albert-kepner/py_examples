from itertools import permutations
from string import Template

def val_plus(p1,p2,p3,p4):
    try:
        r = p1 + p2 + p3 + p4
        if r == 24:
            return f'{p1}+{p2}+{p3}+{p4}'
    except ZeroDivisionError:
        return None
    return None

def val_0_plus_minus(p1,p2,p3,p4):
        try:
            r = p1 + ( p2 - p3 - p4 )
            if r == 24:
                return f'{p1}+({p2}-{p3}-{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_plus_minus(p1,p2,p3,p4):
        try:
            r = ( p1 +p2 + p3 ) - p4
            if r == 24:
                return f'({p1}+{p2}+{p3})-{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_plus_minus_mult(p1,p2,p3,p4):
            try:
                r = (p1 + p2) - (p3 * p4)
                if r == 24:
                    return f'({p1}+{p2})-({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_minus_mult(p1,p2,p3,p4):
            try:
                r = p1 + ( p2 - (p3 * p4))
                if r == 24:
                    return f'{p1}+({p2}-({p3}*{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_plus_minus_div(p1,p2,p3,p4):
            try:
                r = (p1 + p2) - (p3 / p4)
                if r == 24:
                    return f'({p1}+{p2})-({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_minus_div(p1,p2,p3,p4):
            try:
                r = p1 + ( p2 - (p3 / p4))
                if r == 24:
                    return f'{p1}+({p2}-({p3}/{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_plus_mult(p1,p2,p3,p4):
        try:
            r = p1 + ( p2 * p3 * p4 )
            if r == 24:
                return f'{p1}+({p2}*{p3}*{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_plus_mult(p1,p2,p3,p4):
        try:
            r = ( p1 +p2 + p3 ) * p4
            if r == 24:
                return f'({p1}+{p2}+{p3})*{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_plus_mult_minus(p1,p2,p3,p4):
            try:
                r = (p1 + p2) * (p3 - p4)
                if r == 24:
                    return f'({p1}+{p2})*({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_mult_minus(p1,p2,p3,p4):
            try:
                r = p1 + ( p2 * (p3 - p4))
                if r == 24:
                    return f'{p1}+({p2}*({p3}-{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_plus_mult_div(p1,p2,p3,p4):
            try:
                r = (p1 + p2) * (p3 / p4)
                if r == 24:
                    return f'({p1}+{p2})*({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_mult_div(p1,p2,p3,p4):
            try:
                r = p1 + ( p2 * (p3 / p4))
                if r == 24:
                    return f'{p1}+({p2}*({p3}/{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_plus_div(p1,p2,p3,p4):
        try:
            r = p1 + ( p2 / p3 / p4 )
            if r == 24:
                return f'{p1}+({p2}/{p3}/{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_plus_div(p1,p2,p3,p4):
        try:
            r = ( p1 +p2 + p3 ) / p4
            if r == 24:
                return f'({p1}+{p2}+{p3})/{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_plus_div_minus(p1,p2,p3,p4):
            try:
                r = (p1 + p2) / (p3 - p4)
                if r == 24:
                    return f'({p1}+{p2})/({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_div_minus(p1,p2,p3,p4):
            try:
                r = p1 + ( p2 / (p3 - p4))
                if r == 24:
                    return f'{p1}+({p2}/({p3}-{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_plus_div_mult(p1,p2,p3,p4):
            try:
                r = (p1 + p2) / (p3 * p4)
                if r == 24:
                    return f'({p1}+{p2})/({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_div_mult(p1,p2,p3,p4):
            try:
                r = p1 + ( p2 / (p3 * p4))
                if r == 24:
                    return f'{p1}+({p2}/({p3}*{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_minus(p1,p2,p3,p4):
    try:
        r = p1 - p2 - p3 - p4
        if r == 24:
            return f'{p1}-{p2}-{p3}-{p4}'
    except ZeroDivisionError:
        return None
    return None

def val_0_minus_plus(p1,p2,p3,p4):
        try:
            r = p1 - ( p2 + p3 + p4 )
            if r == 24:
                return f'{p1}-({p2}+{p3}+{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_minus_plus(p1,p2,p3,p4):
        try:
            r = ( p1 -p2 - p3 ) + p4
            if r == 24:
                return f'({p1}-{p2}-{p3})+{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_minus_plus_mult(p1,p2,p3,p4):
            try:
                r = (p1 - p2) + (p3 * p4)
                if r == 24:
                    return f'({p1}-{p2})+({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_plus_mult(p1,p2,p3,p4):
            try:
                r = p1 - ( p2 + (p3 * p4))
                if r == 24:
                    return f'{p1}-({p2}+({p3}*{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_minus_plus_div(p1,p2,p3,p4):
            try:
                r = (p1 - p2) + (p3 / p4)
                if r == 24:
                    return f'({p1}-{p2})+({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_plus_div(p1,p2,p3,p4):
            try:
                r = p1 - ( p2 + (p3 / p4))
                if r == 24:
                    return f'{p1}-({p2}+({p3}/{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_minus_mult(p1,p2,p3,p4):
        try:
            r = p1 - ( p2 * p3 * p4 )
            if r == 24:
                return f'{p1}-({p2}*{p3}*{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_minus_mult(p1,p2,p3,p4):
        try:
            r = ( p1 -p2 - p3 ) * p4
            if r == 24:
                return f'({p1}-{p2}-{p3})*{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_minus_mult_plus(p1,p2,p3,p4):
            try:
                r = (p1 - p2) * (p3 + p4)
                if r == 24:
                    return f'({p1}-{p2})*({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_mult_plus(p1,p2,p3,p4):
            try:
                r = p1 - ( p2 * (p3 + p4))
                if r == 24:
                    return f'{p1}-({p2}*({p3}+{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_minus_mult_div(p1,p2,p3,p4):
            try:
                r = (p1 - p2) * (p3 / p4)
                if r == 24:
                    return f'({p1}-{p2})*({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_mult_div(p1,p2,p3,p4):
            try:
                r = p1 - ( p2 * (p3 / p4))
                if r == 24:
                    return f'{p1}-({p2}*({p3}/{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_minus_div(p1,p2,p3,p4):
        try:
            r = p1 - ( p2 / p3 / p4 )
            if r == 24:
                return f'{p1}-({p2}/{p3}/{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_minus_div(p1,p2,p3,p4):
        try:
            r = ( p1 -p2 - p3 ) / p4
            if r == 24:
                return f'({p1}-{p2}-{p3})/{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_minus_div_plus(p1,p2,p3,p4):
            try:
                r = (p1 - p2) / (p3 + p4)
                if r == 24:
                    return f'({p1}-{p2})/({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_div_plus(p1,p2,p3,p4):
            try:
                r = p1 - ( p2 / (p3 + p4))
                if r == 24:
                    return f'{p1}-({p2}/({p3}+{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_minus_div_mult(p1,p2,p3,p4):
            try:
                r = (p1 - p2) / (p3 * p4)
                if r == 24:
                    return f'({p1}-{p2})/({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_div_mult(p1,p2,p3,p4):
            try:
                r = p1 - ( p2 / (p3 * p4))
                if r == 24:
                    return f'{p1}-({p2}/({p3}*{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_mult(p1,p2,p3,p4):
    try:
        r = p1 * p2 * p3 * p4
        if r == 24:
            return f'{p1}*{p2}*{p3}*{p4}'
    except ZeroDivisionError:
        return None
    return None

def val_0_mult_plus(p1,p2,p3,p4):
        try:
            r = p1 * ( p2 + p3 + p4 )
            if r == 24:
                return f'{p1}*({p2}+{p3}+{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_mult_plus(p1,p2,p3,p4):
        try:
            r = ( p1 *p2 * p3 ) + p4
            if r == 24:
                return f'({p1}*{p2}*{p3})+{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_mult_plus_minus(p1,p2,p3,p4):
            try:
                r = (p1 * p2) + (p3 - p4)
                if r == 24:
                    return f'({p1}*{p2})+({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_plus_minus(p1,p2,p3,p4):
            try:
                r = p1 * ( p2 + (p3 - p4))
                if r == 24:
                    return f'{p1}*({p2}+({p3}-{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_mult_plus_div(p1,p2,p3,p4):
            try:
                r = (p1 * p2) + (p3 / p4)
                if r == 24:
                    return f'({p1}*{p2})+({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_plus_div(p1,p2,p3,p4):
            try:
                r = p1 * ( p2 + (p3 / p4))
                if r == 24:
                    return f'{p1}*({p2}+({p3}/{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_mult_minus(p1,p2,p3,p4):
        try:
            r = p1 * ( p2 - p3 - p4 )
            if r == 24:
                return f'{p1}*({p2}-{p3}-{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_mult_minus(p1,p2,p3,p4):
        try:
            r = ( p1 *p2 * p3 ) - p4
            if r == 24:
                return f'({p1}*{p2}*{p3})-{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_mult_minus_plus(p1,p2,p3,p4):
            try:
                r = (p1 * p2) - (p3 + p4)
                if r == 24:
                    return f'({p1}*{p2})-({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_minus_plus(p1,p2,p3,p4):
            try:
                r = p1 * ( p2 - (p3 + p4))
                if r == 24:
                    return f'{p1}*({p2}-({p3}+{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_mult_minus_div(p1,p2,p3,p4):
            try:
                r = (p1 * p2) - (p3 / p4)
                if r == 24:
                    return f'({p1}*{p2})-({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_minus_div(p1,p2,p3,p4):
            try:
                r = p1 * ( p2 - (p3 / p4))
                if r == 24:
                    return f'{p1}*({p2}-({p3}/{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_mult_div(p1,p2,p3,p4):
        try:
            r = p1 * ( p2 / p3 / p4 )
            if r == 24:
                return f'{p1}*({p2}/{p3}/{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_mult_div(p1,p2,p3,p4):
        try:
            r = ( p1 *p2 * p3 ) / p4
            if r == 24:
                return f'({p1}*{p2}*{p3})/{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_mult_div_plus(p1,p2,p3,p4):
            try:
                r = (p1 * p2) / (p3 + p4)
                if r == 24:
                    return f'({p1}*{p2})/({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_div_plus(p1,p2,p3,p4):
            try:
                r = p1 * ( p2 / (p3 + p4))
                if r == 24:
                    return f'{p1}*({p2}/({p3}+{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_mult_div_minus(p1,p2,p3,p4):
            try:
                r = (p1 * p2) / (p3 - p4)
                if r == 24:
                    return f'({p1}*{p2})/({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_div_minus(p1,p2,p3,p4):
            try:
                r = p1 * ( p2 / (p3 - p4))
                if r == 24:
                    return f'{p1}*({p2}/({p3}-{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_div(p1,p2,p3,p4):
    try:
        r = p1 / p2 / p3 / p4
        if r == 24:
            return f'{p1}/{p2}/{p3}/{p4}'
    except ZeroDivisionError:
        return None
    return None

def val_0_div_plus(p1,p2,p3,p4):
        try:
            r = p1 / ( p2 + p3 + p4 )
            if r == 24:
                return f'{p1}/({p2}+{p3}+{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_div_plus(p1,p2,p3,p4):
        try:
            r = ( p1 /p2 / p3 ) + p4
            if r == 24:
                return f'({p1}/{p2}/{p3})+{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_div_plus_minus(p1,p2,p3,p4):
            try:
                r = (p1 / p2) + (p3 - p4)
                if r == 24:
                    return f'({p1}/{p2})+({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_plus_minus(p1,p2,p3,p4):
            try:
                r = p1 / ( p2 + (p3 - p4))
                if r == 24:
                    return f'{p1}/({p2}+({p3}-{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_div_plus_mult(p1,p2,p3,p4):
            try:
                r = (p1 / p2) + (p3 * p4)
                if r == 24:
                    return f'({p1}/{p2})+({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_plus_mult(p1,p2,p3,p4):
            try:
                r = p1 / ( p2 + (p3 * p4))
                if r == 24:
                    return f'{p1}/({p2}+({p3}*{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_div_minus(p1,p2,p3,p4):
        try:
            r = p1 / ( p2 - p3 - p4 )
            if r == 24:
                return f'{p1}/({p2}-{p3}-{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_div_minus(p1,p2,p3,p4):
        try:
            r = ( p1 /p2 / p3 ) - p4
            if r == 24:
                return f'({p1}/{p2}/{p3})-{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_div_minus_plus(p1,p2,p3,p4):
            try:
                r = (p1 / p2) - (p3 + p4)
                if r == 24:
                    return f'({p1}/{p2})-({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_minus_plus(p1,p2,p3,p4):
            try:
                r = p1 / ( p2 - (p3 + p4))
                if r == 24:
                    return f'{p1}/({p2}-({p3}+{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_div_minus_mult(p1,p2,p3,p4):
            try:
                r = (p1 / p2) - (p3 * p4)
                if r == 24:
                    return f'({p1}/{p2})-({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_minus_mult(p1,p2,p3,p4):
            try:
                r = p1 / ( p2 - (p3 * p4))
                if r == 24:
                    return f'{p1}/({p2}-({p3}*{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_div_mult(p1,p2,p3,p4):
        try:
            r = p1 / ( p2 * p3 * p4 )
            if r == 24:
                return f'{p1}/({p2}*{p3}*{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_div_mult(p1,p2,p3,p4):
        try:
            r = ( p1 /p2 / p3 ) * p4
            if r == 24:
                return f'({p1}/{p2}/{p3})*{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_div_mult_plus(p1,p2,p3,p4):
            try:
                r = (p1 / p2) * (p3 + p4)
                if r == 24:
                    return f'({p1}/{p2})*({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_mult_plus(p1,p2,p3,p4):
            try:
                r = p1 / ( p2 * (p3 + p4))
                if r == 24:
                    return f'{p1}/({p2}*({p3}+{p4}))'
            except ZeroDivisionError:
                return None
            return None

def val_0_div_mult_minus(p1,p2,p3,p4):
            try:
                r = (p1 / p2) * (p3 - p4)
                if r == 24:
                    return f'({p1}/{p2})*({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_mult_minus(p1,p2,p3,p4):
            try:
                r = p1 / ( p2 * (p3 - p4))
                if r == 24:
                    return f'{p1}/({p2}*({p3}-{p4}))'
            except ZeroDivisionError:
                return None
            return None

def make_trees():
    ## The possible tree configurations with 4 leaf nodes are:
    ## 1) one root with two children, each having two leaf nodes
    ## 2) one root with one child having three leaf nodes, and the other child being a leaf node
    ## 3) one root with one child being a leaf node, and the other child having three leaf nodes
    ## 4) one root with one child having two leaf nodes, and the other child having two leaf nodes
    ## 5) Three total nodes in a straight line with the last node having two leaf nodes, each node has degree 2 except the leaves
    trees_1op = []
    trees_2op = []
    trees_3op = []

    op1 = op2 = op3 = '+'
    nm1 = nm2 = nm3 = 'plus'

    # Configuration 1 (single op choice)
    tree1 = Template('''def val_${nm1}(p1,p2,p3,p4):
    try: 
        r = p1 ${op1} p2 ${op1} p3 ${op1} p4
        if r == 24:
            return f'{p1}${op1}{p2}${op1}{p3}${op1}{p4}'
    except ZeroDivisionError:
        return None
    return None
''')
    trees_1op.append(tree1)

    # Configuration 2 and 3 (2 op choices)
    tree2 = Template('''def val_${ix}_${nm1}_${nm2}(p1,p2,p3,p4):
        try: 
            r = p1 ${op1} ( p2 ${op2} p3 ${op2} p4 )
            if r == 24:
                return f'{p1}${op1}({p2}${op2}{p3}${op2}{p4})'
        except ZeroDivisionError:
            return None
        return None
''')
    trees_2op.append(tree2)
    tree2 = Template('''def val_${ix}_${nm1}_${nm2}(p1,p2,p3,p4):
        try: 
            r = ( p1 ${op1}p2 ${op1} p3 ) ${op2} p4
            if r == 24:
                return f'({p1}${op1}{p2}${op1}{p3})${op2}{p4}'
        except ZeroDivisionError:
            return None
        return None
''')
    trees_2op.append(tree2)

    # Configuration 4 and 5 (3 op choices)
    tree3 = Template('''def val_${ix}_${nm1}_${nm2}_${nm3}(p1,p2,p3,p4):
            try: 
                r = (p1 ${op1} p2) ${op2} (p3 ${op3} p4)
                if r == 24:
                    return f'({p1}${op1}{p2})${op2}({p3}${op3}{p4})'
            except ZeroDivisionError:
                return None
            return None
    ''')
    trees_3op.append(tree3)
    tree3 = Template('''def val_${ix}_${nm1}_${nm2}_${nm3}(p1,p2,p3,p4):
            try: 
                r = p1 ${op1} ( p2 ${op2} (p3 ${op3} p4))
                if r == 24:
                    return f'{p1}${op1}({p2}${op2}({p3}${op3}{p4}))'
            except ZeroDivisionError:
                return None
            return None
    ''')
    trees_3op.append(tree3)

    operators = ['+', '-', '*', '/']
    op_names = {'+': 'plus', '-': 'minus', '*': 'mult', '/': 'div'}

    for op1 in operators:
        nm1 = op_names[op1]
        other_ops1 = list(operators)
        other_ops1.remove(op1)

        fn = tree1.substitute(nm1=nm1, op1=op1)
        print(fn)
        for op2 in other_ops1:
            nm2 = op_names[op2]
            other_ops2 = list(other_ops1)
            other_ops2.remove(op2)

            for ix, tree2 in enumerate(trees_2op):
                fn = tree2.substitute(ix=ix, nm1=nm1, op1=op1, nm2=nm2, op2=op2)
                print(fn)

            for op3 in other_ops2:
                nm3 = op_names[op3]
                for ix, tree3 in enumerate(trees_3op):
                    fn = tree3.substitute(ix=ix, nm1=nm1, op1=op1, nm2=nm2, op2=op2, nm3=nm3, op3=op3)
                    print(fn)


def try_symbols():
    val_symbols = {k: v for k, v in globals().items() if k.startswith("val_")}
    print(val_symbols.keys())
    for k, v in val_symbols.items():
        p1 = 6
        print(k)
        print(v(6, 6, 6, 6))
        print(f'{k=} {v(6,6,6,6)=}')

def equal_to_24(p1,p2,p3,p4):
    val_symbols = {k: v for k, v in globals().items() if k.startswith("val_")}
    for k, v in val_symbols.items():
        for p in permutations([p1,p2,p3,p4]):
            a,b,c,d = p
        val = v(a,b,c,d)
        if val:
            return val
    return "It's not possible!"


def main1():
    make_trees()


def main2():
    try_symbols()


if __name__ == "__main__":
    main2()
