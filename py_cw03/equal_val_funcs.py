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