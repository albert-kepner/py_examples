def val_plus(p1,p2,p3,p4):
    try:
        r = p1 + p2 + p3 + p4
        if r == 24:
            return f'{p1}+{p2}+{p3}+{p4}'
    except ZeroDivisionError:
        return None
    return None

def val_0_plus_plus(p1,p2,p3,p4):
        try:
            r = p1 + ( p2 + p3 + p4 )
            if r == 24:
                return f'{p1}+({p2}+{p3}+{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_plus_plus(p1,p2,p3,p4):
        try:
            r = ( p1 +p2 + p3 ) + p4
            if r == 24:
                return f'({p1}+{p2}+{p3})+{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_plus_plus_plus(p1,p2,p3,p4):
            try:
                r = (p1 + p2) + (p3 + p4)
                if r == 24:
                    return f'({p1}+{p2})+({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_plus_plus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 + (p3 + p4))
                    if r == 24:
                        return f'{p1}+({p2}+({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_plus_plus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 + (p3 + p4))
                    if r == 24:
                        return f'{p1}+({p2}+({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_plus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 + p3 ) + p4)
                        if r == 24:
                            return f'{p1}+(({p2}+{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_plus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 + p3 ) + p4)
                        if r == 24:
                            return f'{p1}+(({p2}+{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_plus_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) + p3 ) + p4
                    if r == 24:
                        return f'(({p1}+{p2})+{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_plus_plus_minus(p1,p2,p3,p4):
            try:
                r = (p1 + p2) + (p3 - p4)
                if r == 24:
                    return f'({p1}+{p2})+({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_plus_minus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 + (p3 - p4))
                    if r == 24:
                        return f'{p1}+({p2}+({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_plus_minus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 + (p3 - p4))
                    if r == 24:
                        return f'{p1}+({p2}+({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_plus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 + p3 ) - p4)
                        if r == 24:
                            return f'{p1}+(({p2}+{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_plus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 + p3 ) - p4)
                        if r == 24:
                            return f'{p1}+(({p2}+{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_plus_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) + p3 ) - p4
                    if r == 24:
                        return f'(({p1}+{p2})+{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_plus_plus_mult(p1,p2,p3,p4):
            try:
                r = (p1 + p2) + (p3 * p4)
                if r == 24:
                    return f'({p1}+{p2})+({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_plus_mult(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 + (p3 * p4))
                    if r == 24:
                        return f'{p1}+({p2}+({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_plus_mult(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 + (p3 * p4))
                    if r == 24:
                        return f'{p1}+({p2}+({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_plus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 + p3 ) * p4)
                        if r == 24:
                            return f'{p1}+(({p2}+{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_plus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 + p3 ) * p4)
                        if r == 24:
                            return f'{p1}+(({p2}+{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_plus_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) + p3 ) * p4
                    if r == 24:
                        return f'(({p1}+{p2})+{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_plus_plus_div(p1,p2,p3,p4):
            try:
                r = (p1 + p2) + (p3 / p4)
                if r == 24:
                    return f'({p1}+{p2})+({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_plus_div(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 + (p3 / p4))
                    if r == 24:
                        return f'{p1}+({p2}+({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_plus_div(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 + (p3 / p4))
                    if r == 24:
                        return f'{p1}+({p2}+({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_plus_div(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 + p3 ) / p4)
                        if r == 24:
                            return f'{p1}+(({p2}+{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_plus_div(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 + p3 ) / p4)
                        if r == 24:
                            return f'{p1}+(({p2}+{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_plus_div(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) + p3 ) / p4
                    if r == 24:
                        return f'(({p1}+{p2})+{p3})/{p4}'
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

def val_0_plus_minus_plus(p1,p2,p3,p4):
            try:
                r = (p1 + p2) - (p3 + p4)
                if r == 24:
                    return f'({p1}+{p2})-({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_minus_plus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 - (p3 + p4))
                    if r == 24:
                        return f'{p1}+({p2}-({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_minus_plus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 - (p3 + p4))
                    if r == 24:
                        return f'{p1}+({p2}-({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_minus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 - p3 ) + p4)
                        if r == 24:
                            return f'{p1}+(({p2}-{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_minus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 - p3 ) + p4)
                        if r == 24:
                            return f'{p1}+(({p2}-{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_minus_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) - p3 ) + p4
                    if r == 24:
                        return f'(({p1}+{p2})-{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_plus_minus_minus(p1,p2,p3,p4):
            try:
                r = (p1 + p2) - (p3 - p4)
                if r == 24:
                    return f'({p1}+{p2})-({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_minus_minus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 - (p3 - p4))
                    if r == 24:
                        return f'{p1}+({p2}-({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_minus_minus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 - (p3 - p4))
                    if r == 24:
                        return f'{p1}+({p2}-({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_minus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 - p3 ) - p4)
                        if r == 24:
                            return f'{p1}+(({p2}-{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_minus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 - p3 ) - p4)
                        if r == 24:
                            return f'{p1}+(({p2}-{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_minus_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) - p3 ) - p4
                    if r == 24:
                        return f'(({p1}+{p2})-{p3})-{p4}'
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

def val_2_plus_minus_mult(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 - (p3 * p4))
                    if r == 24:
                        return f'{p1}+({p2}-({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_minus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 - p3 ) * p4)
                        if r == 24:
                            return f'{p1}+(({p2}-{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_minus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 - p3 ) * p4)
                        if r == 24:
                            return f'{p1}+(({p2}-{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_minus_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) - p3 ) * p4
                    if r == 24:
                        return f'(({p1}+{p2})-{p3})*{p4}'
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

def val_2_plus_minus_div(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 - (p3 / p4))
                    if r == 24:
                        return f'{p1}+({p2}-({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_minus_div(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 - p3 ) / p4)
                        if r == 24:
                            return f'{p1}+(({p2}-{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_minus_div(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 - p3 ) / p4)
                        if r == 24:
                            return f'{p1}+(({p2}-{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_minus_div(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) - p3 ) / p4
                    if r == 24:
                        return f'(({p1}+{p2})-{p3})/{p4}'
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

def val_0_plus_mult_plus(p1,p2,p3,p4):
            try:
                r = (p1 + p2) * (p3 + p4)
                if r == 24:
                    return f'({p1}+{p2})*({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_mult_plus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 * (p3 + p4))
                    if r == 24:
                        return f'{p1}+({p2}*({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_mult_plus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 * (p3 + p4))
                    if r == 24:
                        return f'{p1}+({p2}*({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_mult_plus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 * p3 ) + p4)
                        if r == 24:
                            return f'{p1}+(({p2}*{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_mult_plus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 * p3 ) + p4)
                        if r == 24:
                            return f'{p1}+(({p2}*{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_mult_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) * p3 ) + p4
                    if r == 24:
                        return f'(({p1}+{p2})*{p3})+{p4}'
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

def val_2_plus_mult_minus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 * (p3 - p4))
                    if r == 24:
                        return f'{p1}+({p2}*({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_mult_minus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 * p3 ) - p4)
                        if r == 24:
                            return f'{p1}+(({p2}*{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_mult_minus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 * p3 ) - p4)
                        if r == 24:
                            return f'{p1}+(({p2}*{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_mult_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) * p3 ) - p4
                    if r == 24:
                        return f'(({p1}+{p2})*{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_plus_mult_mult(p1,p2,p3,p4):
            try:
                r = (p1 + p2) * (p3 * p4)
                if r == 24:
                    return f'({p1}+{p2})*({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_mult_mult(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 * (p3 * p4))
                    if r == 24:
                        return f'{p1}+({p2}*({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_mult_mult(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 * (p3 * p4))
                    if r == 24:
                        return f'{p1}+({p2}*({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_mult_mult(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 * p3 ) * p4)
                        if r == 24:
                            return f'{p1}+(({p2}*{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_mult_mult(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 * p3 ) * p4)
                        if r == 24:
                            return f'{p1}+(({p2}*{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_mult_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) * p3 ) * p4
                    if r == 24:
                        return f'(({p1}+{p2})*{p3})*{p4}'
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

def val_2_plus_mult_div(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 * (p3 / p4))
                    if r == 24:
                        return f'{p1}+({p2}*({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_mult_div(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 * p3 ) / p4)
                        if r == 24:
                            return f'{p1}+(({p2}*{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_mult_div(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 * p3 ) / p4)
                        if r == 24:
                            return f'{p1}+(({p2}*{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_mult_div(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) * p3 ) / p4
                    if r == 24:
                        return f'(({p1}+{p2})*{p3})/{p4}'
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

def val_0_plus_div_plus(p1,p2,p3,p4):
            try:
                r = (p1 + p2) / (p3 + p4)
                if r == 24:
                    return f'({p1}+{p2})/({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_div_plus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 / (p3 + p4))
                    if r == 24:
                        return f'{p1}+({p2}/({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_div_plus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 / (p3 + p4))
                    if r == 24:
                        return f'{p1}+({p2}/({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_div_plus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 / p3 ) + p4)
                        if r == 24:
                            return f'{p1}+(({p2}/{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_div_plus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 / p3 ) + p4)
                        if r == 24:
                            return f'{p1}+(({p2}/{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_div_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) / p3 ) + p4
                    if r == 24:
                        return f'(({p1}+{p2})/{p3})+{p4}'
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

def val_2_plus_div_minus(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 / (p3 - p4))
                    if r == 24:
                        return f'{p1}+({p2}/({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_div_minus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 / p3 ) - p4)
                        if r == 24:
                            return f'{p1}+(({p2}/{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_div_minus(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 / p3 ) - p4)
                        if r == 24:
                            return f'{p1}+(({p2}/{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_div_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) / p3 ) - p4
                    if r == 24:
                        return f'(({p1}+{p2})/{p3})-{p4}'
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

def val_2_plus_div_mult(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 / (p3 * p4))
                    if r == 24:
                        return f'{p1}+({p2}/({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_div_mult(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 / p3 ) * p4)
                        if r == 24:
                            return f'{p1}+(({p2}/{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_div_mult(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 / p3 ) * p4)
                        if r == 24:
                            return f'{p1}+(({p2}/{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_div_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) / p3 ) * p4
                    if r == 24:
                        return f'(({p1}+{p2})/{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_plus_div_div(p1,p2,p3,p4):
            try:
                r = (p1 + p2) / (p3 / p4)
                if r == 24:
                    return f'({p1}+{p2})/({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_plus_div_div(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 / (p3 / p4))
                    if r == 24:
                        return f'{p1}+({p2}/({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_plus_div_div(p1,p2,p3,p4):
                try:
                    r = p1 + ( p2 / (p3 / p4))
                    if r == 24:
                        return f'{p1}+({p2}/({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_plus_div_div(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 / p3 ) / p4)
                        if r == 24:
                            return f'{p1}+(({p2}/{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_plus_div_div(p1,p2,p3,p4):
                    try:
                        r = p1 + (( p2 / p3 ) / p4)
                        if r == 24:
                            return f'{p1}+(({p2}/{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_plus_div_div(p1,p2,p3,p4):
                try:
                    r = ((p1 +  p2 ) / p3 ) / p4
                    if r == 24:
                        return f'(({p1}+{p2})/{p3})/{p4}'
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

def val_0_minus_plus_plus(p1,p2,p3,p4):
            try:
                r = (p1 - p2) + (p3 + p4)
                if r == 24:
                    return f'({p1}-{p2})+({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_plus_plus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 + (p3 + p4))
                    if r == 24:
                        return f'{p1}-({p2}+({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_plus_plus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 + (p3 + p4))
                    if r == 24:
                        return f'{p1}-({p2}+({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_plus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 + p3 ) + p4)
                        if r == 24:
                            return f'{p1}-(({p2}+{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_plus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 + p3 ) + p4)
                        if r == 24:
                            return f'{p1}-(({p2}+{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_plus_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) + p3 ) + p4
                    if r == 24:
                        return f'(({p1}-{p2})+{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_plus_minus(p1,p2,p3,p4):
            try:
                r = (p1 - p2) + (p3 - p4)
                if r == 24:
                    return f'({p1}-{p2})+({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_plus_minus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 + (p3 - p4))
                    if r == 24:
                        return f'{p1}-({p2}+({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_plus_minus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 + (p3 - p4))
                    if r == 24:
                        return f'{p1}-({p2}+({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_plus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 + p3 ) - p4)
                        if r == 24:
                            return f'{p1}-(({p2}+{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_plus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 + p3 ) - p4)
                        if r == 24:
                            return f'{p1}-(({p2}+{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_plus_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) + p3 ) - p4
                    if r == 24:
                        return f'(({p1}-{p2})+{p3})-{p4}'
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

def val_2_minus_plus_mult(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 + (p3 * p4))
                    if r == 24:
                        return f'{p1}-({p2}+({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_plus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 + p3 ) * p4)
                        if r == 24:
                            return f'{p1}-(({p2}+{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_plus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 + p3 ) * p4)
                        if r == 24:
                            return f'{p1}-(({p2}+{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_plus_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) + p3 ) * p4
                    if r == 24:
                        return f'(({p1}-{p2})+{p3})*{p4}'
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

def val_2_minus_plus_div(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 + (p3 / p4))
                    if r == 24:
                        return f'{p1}-({p2}+({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_plus_div(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 + p3 ) / p4)
                        if r == 24:
                            return f'{p1}-(({p2}+{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_plus_div(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 + p3 ) / p4)
                        if r == 24:
                            return f'{p1}-(({p2}+{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_plus_div(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) + p3 ) / p4
                    if r == 24:
                        return f'(({p1}-{p2})+{p3})/{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_minus(p1,p2,p3,p4):
        try:
            r = p1 - ( p2 - p3 - p4 )
            if r == 24:
                return f'{p1}-({p2}-{p3}-{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_minus_minus(p1,p2,p3,p4):
        try:
            r = ( p1 -p2 - p3 ) - p4
            if r == 24:
                return f'({p1}-{p2}-{p3})-{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_minus_minus_plus(p1,p2,p3,p4):
            try:
                r = (p1 - p2) - (p3 + p4)
                if r == 24:
                    return f'({p1}-{p2})-({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_minus_plus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 - (p3 + p4))
                    if r == 24:
                        return f'{p1}-({p2}-({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_minus_plus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 - (p3 + p4))
                    if r == 24:
                        return f'{p1}-({p2}-({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_minus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 - p3 ) + p4)
                        if r == 24:
                            return f'{p1}-(({p2}-{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_minus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 - p3 ) + p4)
                        if r == 24:
                            return f'{p1}-(({p2}-{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_minus_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) - p3 ) + p4
                    if r == 24:
                        return f'(({p1}-{p2})-{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_minus_minus(p1,p2,p3,p4):
            try:
                r = (p1 - p2) - (p3 - p4)
                if r == 24:
                    return f'({p1}-{p2})-({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_minus_minus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 - (p3 - p4))
                    if r == 24:
                        return f'{p1}-({p2}-({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_minus_minus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 - (p3 - p4))
                    if r == 24:
                        return f'{p1}-({p2}-({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_minus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 - p3 ) - p4)
                        if r == 24:
                            return f'{p1}-(({p2}-{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_minus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 - p3 ) - p4)
                        if r == 24:
                            return f'{p1}-(({p2}-{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_minus_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) - p3 ) - p4
                    if r == 24:
                        return f'(({p1}-{p2})-{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_minus_mult(p1,p2,p3,p4):
            try:
                r = (p1 - p2) - (p3 * p4)
                if r == 24:
                    return f'({p1}-{p2})-({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_minus_mult(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 - (p3 * p4))
                    if r == 24:
                        return f'{p1}-({p2}-({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_minus_mult(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 - (p3 * p4))
                    if r == 24:
                        return f'{p1}-({p2}-({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_minus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 - p3 ) * p4)
                        if r == 24:
                            return f'{p1}-(({p2}-{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_minus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 - p3 ) * p4)
                        if r == 24:
                            return f'{p1}-(({p2}-{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_minus_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) - p3 ) * p4
                    if r == 24:
                        return f'(({p1}-{p2})-{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_minus_div(p1,p2,p3,p4):
            try:
                r = (p1 - p2) - (p3 / p4)
                if r == 24:
                    return f'({p1}-{p2})-({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_minus_div(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 - (p3 / p4))
                    if r == 24:
                        return f'{p1}-({p2}-({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_minus_div(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 - (p3 / p4))
                    if r == 24:
                        return f'{p1}-({p2}-({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_minus_div(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 - p3 ) / p4)
                        if r == 24:
                            return f'{p1}-(({p2}-{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_minus_div(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 - p3 ) / p4)
                        if r == 24:
                            return f'{p1}-(({p2}-{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_minus_div(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) - p3 ) / p4
                    if r == 24:
                        return f'(({p1}-{p2})-{p3})/{p4}'
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

def val_2_minus_mult_plus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 * (p3 + p4))
                    if r == 24:
                        return f'{p1}-({p2}*({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_mult_plus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 * p3 ) + p4)
                        if r == 24:
                            return f'{p1}-(({p2}*{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_mult_plus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 * p3 ) + p4)
                        if r == 24:
                            return f'{p1}-(({p2}*{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_mult_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) * p3 ) + p4
                    if r == 24:
                        return f'(({p1}-{p2})*{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_mult_minus(p1,p2,p3,p4):
            try:
                r = (p1 - p2) * (p3 - p4)
                if r == 24:
                    return f'({p1}-{p2})*({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_mult_minus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 * (p3 - p4))
                    if r == 24:
                        return f'{p1}-({p2}*({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_mult_minus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 * (p3 - p4))
                    if r == 24:
                        return f'{p1}-({p2}*({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_mult_minus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 * p3 ) - p4)
                        if r == 24:
                            return f'{p1}-(({p2}*{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_mult_minus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 * p3 ) - p4)
                        if r == 24:
                            return f'{p1}-(({p2}*{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_mult_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) * p3 ) - p4
                    if r == 24:
                        return f'(({p1}-{p2})*{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_mult_mult(p1,p2,p3,p4):
            try:
                r = (p1 - p2) * (p3 * p4)
                if r == 24:
                    return f'({p1}-{p2})*({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_mult_mult(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 * (p3 * p4))
                    if r == 24:
                        return f'{p1}-({p2}*({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_mult_mult(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 * (p3 * p4))
                    if r == 24:
                        return f'{p1}-({p2}*({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_mult_mult(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 * p3 ) * p4)
                        if r == 24:
                            return f'{p1}-(({p2}*{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_mult_mult(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 * p3 ) * p4)
                        if r == 24:
                            return f'{p1}-(({p2}*{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_mult_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) * p3 ) * p4
                    if r == 24:
                        return f'(({p1}-{p2})*{p3})*{p4}'
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

def val_2_minus_mult_div(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 * (p3 / p4))
                    if r == 24:
                        return f'{p1}-({p2}*({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_mult_div(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 * p3 ) / p4)
                        if r == 24:
                            return f'{p1}-(({p2}*{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_mult_div(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 * p3 ) / p4)
                        if r == 24:
                            return f'{p1}-(({p2}*{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_mult_div(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) * p3 ) / p4
                    if r == 24:
                        return f'(({p1}-{p2})*{p3})/{p4}'
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

def val_2_minus_div_plus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 / (p3 + p4))
                    if r == 24:
                        return f'{p1}-({p2}/({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_div_plus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 / p3 ) + p4)
                        if r == 24:
                            return f'{p1}-(({p2}/{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_div_plus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 / p3 ) + p4)
                        if r == 24:
                            return f'{p1}-(({p2}/{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_div_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) / p3 ) + p4
                    if r == 24:
                        return f'(({p1}-{p2})/{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_div_minus(p1,p2,p3,p4):
            try:
                r = (p1 - p2) / (p3 - p4)
                if r == 24:
                    return f'({p1}-{p2})/({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_div_minus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 / (p3 - p4))
                    if r == 24:
                        return f'{p1}-({p2}/({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_div_minus(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 / (p3 - p4))
                    if r == 24:
                        return f'{p1}-({p2}/({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_div_minus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 / p3 ) - p4)
                        if r == 24:
                            return f'{p1}-(({p2}/{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_div_minus(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 / p3 ) - p4)
                        if r == 24:
                            return f'{p1}-(({p2}/{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_div_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) / p3 ) - p4
                    if r == 24:
                        return f'(({p1}-{p2})/{p3})-{p4}'
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

def val_2_minus_div_mult(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 / (p3 * p4))
                    if r == 24:
                        return f'{p1}-({p2}/({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_div_mult(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 / p3 ) * p4)
                        if r == 24:
                            return f'{p1}-(({p2}/{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_div_mult(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 / p3 ) * p4)
                        if r == 24:
                            return f'{p1}-(({p2}/{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_div_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) / p3 ) * p4
                    if r == 24:
                        return f'(({p1}-{p2})/{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_minus_div_div(p1,p2,p3,p4):
            try:
                r = (p1 - p2) / (p3 / p4)
                if r == 24:
                    return f'({p1}-{p2})/({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_minus_div_div(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 / (p3 / p4))
                    if r == 24:
                        return f'{p1}-({p2}/({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_minus_div_div(p1,p2,p3,p4):
                try:
                    r = p1 - ( p2 / (p3 / p4))
                    if r == 24:
                        return f'{p1}-({p2}/({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_minus_div_div(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 / p3 ) / p4)
                        if r == 24:
                            return f'{p1}-(({p2}/{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_minus_div_div(p1,p2,p3,p4):
                    try:
                        r = p1 - (( p2 / p3 ) / p4)
                        if r == 24:
                            return f'{p1}-(({p2}/{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_minus_div_div(p1,p2,p3,p4):
                try:
                    r = ((p1 -  p2 ) / p3 ) / p4
                    if r == 24:
                        return f'(({p1}-{p2})/{p3})/{p4}'
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

def val_0_mult_plus_plus(p1,p2,p3,p4):
            try:
                r = (p1 * p2) + (p3 + p4)
                if r == 24:
                    return f'({p1}*{p2})+({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_plus_plus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 + (p3 + p4))
                    if r == 24:
                        return f'{p1}*({p2}+({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_plus_plus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 + (p3 + p4))
                    if r == 24:
                        return f'{p1}*({p2}+({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_plus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 + p3 ) + p4)
                        if r == 24:
                            return f'{p1}*(({p2}+{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_plus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 + p3 ) + p4)
                        if r == 24:
                            return f'{p1}*(({p2}+{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_plus_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) + p3 ) + p4
                    if r == 24:
                        return f'(({p1}*{p2})+{p3})+{p4}'
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

def val_2_mult_plus_minus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 + (p3 - p4))
                    if r == 24:
                        return f'{p1}*({p2}+({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_plus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 + p3 ) - p4)
                        if r == 24:
                            return f'{p1}*(({p2}+{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_plus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 + p3 ) - p4)
                        if r == 24:
                            return f'{p1}*(({p2}+{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_plus_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) + p3 ) - p4
                    if r == 24:
                        return f'(({p1}*{p2})+{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_plus_mult(p1,p2,p3,p4):
            try:
                r = (p1 * p2) + (p3 * p4)
                if r == 24:
                    return f'({p1}*{p2})+({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_plus_mult(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 + (p3 * p4))
                    if r == 24:
                        return f'{p1}*({p2}+({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_plus_mult(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 + (p3 * p4))
                    if r == 24:
                        return f'{p1}*({p2}+({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_plus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 + p3 ) * p4)
                        if r == 24:
                            return f'{p1}*(({p2}+{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_plus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 + p3 ) * p4)
                        if r == 24:
                            return f'{p1}*(({p2}+{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_plus_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) + p3 ) * p4
                    if r == 24:
                        return f'(({p1}*{p2})+{p3})*{p4}'
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

def val_2_mult_plus_div(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 + (p3 / p4))
                    if r == 24:
                        return f'{p1}*({p2}+({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_plus_div(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 + p3 ) / p4)
                        if r == 24:
                            return f'{p1}*(({p2}+{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_plus_div(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 + p3 ) / p4)
                        if r == 24:
                            return f'{p1}*(({p2}+{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_plus_div(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) + p3 ) / p4
                    if r == 24:
                        return f'(({p1}*{p2})+{p3})/{p4}'
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

def val_2_mult_minus_plus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 - (p3 + p4))
                    if r == 24:
                        return f'{p1}*({p2}-({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_minus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 - p3 ) + p4)
                        if r == 24:
                            return f'{p1}*(({p2}-{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_minus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 - p3 ) + p4)
                        if r == 24:
                            return f'{p1}*(({p2}-{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_minus_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) - p3 ) + p4
                    if r == 24:
                        return f'(({p1}*{p2})-{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_minus_minus(p1,p2,p3,p4):
            try:
                r = (p1 * p2) - (p3 - p4)
                if r == 24:
                    return f'({p1}*{p2})-({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_minus_minus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 - (p3 - p4))
                    if r == 24:
                        return f'{p1}*({p2}-({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_minus_minus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 - (p3 - p4))
                    if r == 24:
                        return f'{p1}*({p2}-({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_minus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 - p3 ) - p4)
                        if r == 24:
                            return f'{p1}*(({p2}-{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_minus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 - p3 ) - p4)
                        if r == 24:
                            return f'{p1}*(({p2}-{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_minus_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) - p3 ) - p4
                    if r == 24:
                        return f'(({p1}*{p2})-{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_minus_mult(p1,p2,p3,p4):
            try:
                r = (p1 * p2) - (p3 * p4)
                if r == 24:
                    return f'({p1}*{p2})-({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_minus_mult(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 - (p3 * p4))
                    if r == 24:
                        return f'{p1}*({p2}-({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_minus_mult(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 - (p3 * p4))
                    if r == 24:
                        return f'{p1}*({p2}-({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_minus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 - p3 ) * p4)
                        if r == 24:
                            return f'{p1}*(({p2}-{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_minus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 - p3 ) * p4)
                        if r == 24:
                            return f'{p1}*(({p2}-{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_minus_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) - p3 ) * p4
                    if r == 24:
                        return f'(({p1}*{p2})-{p3})*{p4}'
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

def val_2_mult_minus_div(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 - (p3 / p4))
                    if r == 24:
                        return f'{p1}*({p2}-({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_minus_div(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 - p3 ) / p4)
                        if r == 24:
                            return f'{p1}*(({p2}-{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_minus_div(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 - p3 ) / p4)
                        if r == 24:
                            return f'{p1}*(({p2}-{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_minus_div(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) - p3 ) / p4
                    if r == 24:
                        return f'(({p1}*{p2})-{p3})/{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_mult(p1,p2,p3,p4):
        try:
            r = p1 * ( p2 * p3 * p4 )
            if r == 24:
                return f'{p1}*({p2}*{p3}*{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_mult_mult(p1,p2,p3,p4):
        try:
            r = ( p1 *p2 * p3 ) * p4
            if r == 24:
                return f'({p1}*{p2}*{p3})*{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_mult_mult_plus(p1,p2,p3,p4):
            try:
                r = (p1 * p2) * (p3 + p4)
                if r == 24:
                    return f'({p1}*{p2})*({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_mult_plus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 * (p3 + p4))
                    if r == 24:
                        return f'{p1}*({p2}*({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_mult_plus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 * (p3 + p4))
                    if r == 24:
                        return f'{p1}*({p2}*({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_mult_plus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 * p3 ) + p4)
                        if r == 24:
                            return f'{p1}*(({p2}*{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_mult_plus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 * p3 ) + p4)
                        if r == 24:
                            return f'{p1}*(({p2}*{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_mult_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) * p3 ) + p4
                    if r == 24:
                        return f'(({p1}*{p2})*{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_mult_minus(p1,p2,p3,p4):
            try:
                r = (p1 * p2) * (p3 - p4)
                if r == 24:
                    return f'({p1}*{p2})*({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_mult_minus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 * (p3 - p4))
                    if r == 24:
                        return f'{p1}*({p2}*({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_mult_minus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 * (p3 - p4))
                    if r == 24:
                        return f'{p1}*({p2}*({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_mult_minus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 * p3 ) - p4)
                        if r == 24:
                            return f'{p1}*(({p2}*{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_mult_minus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 * p3 ) - p4)
                        if r == 24:
                            return f'{p1}*(({p2}*{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_mult_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) * p3 ) - p4
                    if r == 24:
                        return f'(({p1}*{p2})*{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_mult_mult(p1,p2,p3,p4):
            try:
                r = (p1 * p2) * (p3 * p4)
                if r == 24:
                    return f'({p1}*{p2})*({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_mult_mult(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 * (p3 * p4))
                    if r == 24:
                        return f'{p1}*({p2}*({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_mult_mult(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 * (p3 * p4))
                    if r == 24:
                        return f'{p1}*({p2}*({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_mult_mult(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 * p3 ) * p4)
                        if r == 24:
                            return f'{p1}*(({p2}*{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_mult_mult(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 * p3 ) * p4)
                        if r == 24:
                            return f'{p1}*(({p2}*{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_mult_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) * p3 ) * p4
                    if r == 24:
                        return f'(({p1}*{p2})*{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_mult_div(p1,p2,p3,p4):
            try:
                r = (p1 * p2) * (p3 / p4)
                if r == 24:
                    return f'({p1}*{p2})*({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_mult_div(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 * (p3 / p4))
                    if r == 24:
                        return f'{p1}*({p2}*({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_mult_div(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 * (p3 / p4))
                    if r == 24:
                        return f'{p1}*({p2}*({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_mult_div(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 * p3 ) / p4)
                        if r == 24:
                            return f'{p1}*(({p2}*{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_mult_div(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 * p3 ) / p4)
                        if r == 24:
                            return f'{p1}*(({p2}*{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_mult_div(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) * p3 ) / p4
                    if r == 24:
                        return f'(({p1}*{p2})*{p3})/{p4}'
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

def val_2_mult_div_plus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 / (p3 + p4))
                    if r == 24:
                        return f'{p1}*({p2}/({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_div_plus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 / p3 ) + p4)
                        if r == 24:
                            return f'{p1}*(({p2}/{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_div_plus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 / p3 ) + p4)
                        if r == 24:
                            return f'{p1}*(({p2}/{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_div_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) / p3 ) + p4
                    if r == 24:
                        return f'(({p1}*{p2})/{p3})+{p4}'
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

def val_2_mult_div_minus(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 / (p3 - p4))
                    if r == 24:
                        return f'{p1}*({p2}/({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_div_minus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 / p3 ) - p4)
                        if r == 24:
                            return f'{p1}*(({p2}/{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_div_minus(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 / p3 ) - p4)
                        if r == 24:
                            return f'{p1}*(({p2}/{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_div_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) / p3 ) - p4
                    if r == 24:
                        return f'(({p1}*{p2})/{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_div_mult(p1,p2,p3,p4):
            try:
                r = (p1 * p2) / (p3 * p4)
                if r == 24:
                    return f'({p1}*{p2})/({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_div_mult(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 / (p3 * p4))
                    if r == 24:
                        return f'{p1}*({p2}/({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_div_mult(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 / (p3 * p4))
                    if r == 24:
                        return f'{p1}*({p2}/({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_div_mult(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 / p3 ) * p4)
                        if r == 24:
                            return f'{p1}*(({p2}/{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_div_mult(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 / p3 ) * p4)
                        if r == 24:
                            return f'{p1}*(({p2}/{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_div_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) / p3 ) * p4
                    if r == 24:
                        return f'(({p1}*{p2})/{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_mult_div_div(p1,p2,p3,p4):
            try:
                r = (p1 * p2) / (p3 / p4)
                if r == 24:
                    return f'({p1}*{p2})/({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_mult_div_div(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 / (p3 / p4))
                    if r == 24:
                        return f'{p1}*({p2}/({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_mult_div_div(p1,p2,p3,p4):
                try:
                    r = p1 * ( p2 / (p3 / p4))
                    if r == 24:
                        return f'{p1}*({p2}/({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_mult_div_div(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 / p3 ) / p4)
                        if r == 24:
                            return f'{p1}*(({p2}/{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_mult_div_div(p1,p2,p3,p4):
                    try:
                        r = p1 * (( p2 / p3 ) / p4)
                        if r == 24:
                            return f'{p1}*(({p2}/{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_mult_div_div(p1,p2,p3,p4):
                try:
                    r = ((p1 *  p2 ) / p3 ) / p4
                    if r == 24:
                        return f'(({p1}*{p2})/{p3})/{p4}'
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

def val_0_div_plus_plus(p1,p2,p3,p4):
            try:
                r = (p1 / p2) + (p3 + p4)
                if r == 24:
                    return f'({p1}/{p2})+({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_plus_plus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 + (p3 + p4))
                    if r == 24:
                        return f'{p1}/({p2}+({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_plus_plus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 + (p3 + p4))
                    if r == 24:
                        return f'{p1}/({p2}+({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_plus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 + p3 ) + p4)
                        if r == 24:
                            return f'{p1}/(({p2}+{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_plus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 + p3 ) + p4)
                        if r == 24:
                            return f'{p1}/(({p2}+{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_plus_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) + p3 ) + p4
                    if r == 24:
                        return f'(({p1}/{p2})+{p3})+{p4}'
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

def val_2_div_plus_minus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 + (p3 - p4))
                    if r == 24:
                        return f'{p1}/({p2}+({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_plus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 + p3 ) - p4)
                        if r == 24:
                            return f'{p1}/(({p2}+{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_plus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 + p3 ) - p4)
                        if r == 24:
                            return f'{p1}/(({p2}+{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_plus_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) + p3 ) - p4
                    if r == 24:
                        return f'(({p1}/{p2})+{p3})-{p4}'
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

def val_2_div_plus_mult(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 + (p3 * p4))
                    if r == 24:
                        return f'{p1}/({p2}+({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_plus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 + p3 ) * p4)
                        if r == 24:
                            return f'{p1}/(({p2}+{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_plus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 + p3 ) * p4)
                        if r == 24:
                            return f'{p1}/(({p2}+{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_plus_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) + p3 ) * p4
                    if r == 24:
                        return f'(({p1}/{p2})+{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_plus_div(p1,p2,p3,p4):
            try:
                r = (p1 / p2) + (p3 / p4)
                if r == 24:
                    return f'({p1}/{p2})+({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_plus_div(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 + (p3 / p4))
                    if r == 24:
                        return f'{p1}/({p2}+({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_plus_div(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 + (p3 / p4))
                    if r == 24:
                        return f'{p1}/({p2}+({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_plus_div(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 + p3 ) / p4)
                        if r == 24:
                            return f'{p1}/(({p2}+{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_plus_div(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 + p3 ) / p4)
                        if r == 24:
                            return f'{p1}/(({p2}+{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_plus_div(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) + p3 ) / p4
                    if r == 24:
                        return f'(({p1}/{p2})+{p3})/{p4}'
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

def val_2_div_minus_plus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 - (p3 + p4))
                    if r == 24:
                        return f'{p1}/({p2}-({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_minus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 - p3 ) + p4)
                        if r == 24:
                            return f'{p1}/(({p2}-{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_minus_plus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 - p3 ) + p4)
                        if r == 24:
                            return f'{p1}/(({p2}-{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_minus_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) - p3 ) + p4
                    if r == 24:
                        return f'(({p1}/{p2})-{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_minus_minus(p1,p2,p3,p4):
            try:
                r = (p1 / p2) - (p3 - p4)
                if r == 24:
                    return f'({p1}/{p2})-({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_minus_minus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 - (p3 - p4))
                    if r == 24:
                        return f'{p1}/({p2}-({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_minus_minus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 - (p3 - p4))
                    if r == 24:
                        return f'{p1}/({p2}-({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_minus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 - p3 ) - p4)
                        if r == 24:
                            return f'{p1}/(({p2}-{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_minus_minus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 - p3 ) - p4)
                        if r == 24:
                            return f'{p1}/(({p2}-{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_minus_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) - p3 ) - p4
                    if r == 24:
                        return f'(({p1}/{p2})-{p3})-{p4}'
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

def val_2_div_minus_mult(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 - (p3 * p4))
                    if r == 24:
                        return f'{p1}/({p2}-({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_minus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 - p3 ) * p4)
                        if r == 24:
                            return f'{p1}/(({p2}-{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_minus_mult(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 - p3 ) * p4)
                        if r == 24:
                            return f'{p1}/(({p2}-{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_minus_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) - p3 ) * p4
                    if r == 24:
                        return f'(({p1}/{p2})-{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_minus_div(p1,p2,p3,p4):
            try:
                r = (p1 / p2) - (p3 / p4)
                if r == 24:
                    return f'({p1}/{p2})-({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_minus_div(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 - (p3 / p4))
                    if r == 24:
                        return f'{p1}/({p2}-({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_minus_div(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 - (p3 / p4))
                    if r == 24:
                        return f'{p1}/({p2}-({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_minus_div(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 - p3 ) / p4)
                        if r == 24:
                            return f'{p1}/(({p2}-{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_minus_div(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 - p3 ) / p4)
                        if r == 24:
                            return f'{p1}/(({p2}-{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_minus_div(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) - p3 ) / p4
                    if r == 24:
                        return f'(({p1}/{p2})-{p3})/{p4}'
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

def val_2_div_mult_plus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 * (p3 + p4))
                    if r == 24:
                        return f'{p1}/({p2}*({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_mult_plus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 * p3 ) + p4)
                        if r == 24:
                            return f'{p1}/(({p2}*{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_mult_plus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 * p3 ) + p4)
                        if r == 24:
                            return f'{p1}/(({p2}*{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_mult_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) * p3 ) + p4
                    if r == 24:
                        return f'(({p1}/{p2})*{p3})+{p4}'
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

def val_2_div_mult_minus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 * (p3 - p4))
                    if r == 24:
                        return f'{p1}/({p2}*({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_mult_minus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 * p3 ) - p4)
                        if r == 24:
                            return f'{p1}/(({p2}*{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_mult_minus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 * p3 ) - p4)
                        if r == 24:
                            return f'{p1}/(({p2}*{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_mult_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) * p3 ) - p4
                    if r == 24:
                        return f'(({p1}/{p2})*{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_mult_mult(p1,p2,p3,p4):
            try:
                r = (p1 / p2) * (p3 * p4)
                if r == 24:
                    return f'({p1}/{p2})*({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_mult_mult(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 * (p3 * p4))
                    if r == 24:
                        return f'{p1}/({p2}*({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_mult_mult(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 * (p3 * p4))
                    if r == 24:
                        return f'{p1}/({p2}*({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_mult_mult(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 * p3 ) * p4)
                        if r == 24:
                            return f'{p1}/(({p2}*{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_mult_mult(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 * p3 ) * p4)
                        if r == 24:
                            return f'{p1}/(({p2}*{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_mult_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) * p3 ) * p4
                    if r == 24:
                        return f'(({p1}/{p2})*{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_mult_div(p1,p2,p3,p4):
            try:
                r = (p1 / p2) * (p3 / p4)
                if r == 24:
                    return f'({p1}/{p2})*({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_mult_div(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 * (p3 / p4))
                    if r == 24:
                        return f'{p1}/({p2}*({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_mult_div(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 * (p3 / p4))
                    if r == 24:
                        return f'{p1}/({p2}*({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_mult_div(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 * p3 ) / p4)
                        if r == 24:
                            return f'{p1}/(({p2}*{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_mult_div(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 * p3 ) / p4)
                        if r == 24:
                            return f'{p1}/(({p2}*{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_mult_div(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) * p3 ) / p4
                    if r == 24:
                        return f'(({p1}/{p2})*{p3})/{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_div(p1,p2,p3,p4):
        try:
            r = p1 / ( p2 / p3 / p4 )
            if r == 24:
                return f'{p1}/({p2}/{p3}/{p4})'
        except ZeroDivisionError:
            return None
        return None

def val_1_div_div(p1,p2,p3,p4):
        try:
            r = ( p1 /p2 / p3 ) / p4
            if r == 24:
                return f'({p1}/{p2}/{p3})/{p4}'
        except ZeroDivisionError:
            return None
        return None

def val_0_div_div_plus(p1,p2,p3,p4):
            try:
                r = (p1 / p2) / (p3 + p4)
                if r == 24:
                    return f'({p1}/{p2})/({p3}+{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_div_plus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 / (p3 + p4))
                    if r == 24:
                        return f'{p1}/({p2}/({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_div_plus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 / (p3 + p4))
                    if r == 24:
                        return f'{p1}/({p2}/({p3}+{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_div_plus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 / p3 ) + p4)
                        if r == 24:
                            return f'{p1}/(({p2}/{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_div_plus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 / p3 ) + p4)
                        if r == 24:
                            return f'{p1}/(({p2}/{p3})+{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_div_plus(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) / p3 ) + p4
                    if r == 24:
                        return f'(({p1}/{p2})/{p3})+{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_div_minus(p1,p2,p3,p4):
            try:
                r = (p1 / p2) / (p3 - p4)
                if r == 24:
                    return f'({p1}/{p2})/({p3}-{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_div_minus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 / (p3 - p4))
                    if r == 24:
                        return f'{p1}/({p2}/({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_div_minus(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 / (p3 - p4))
                    if r == 24:
                        return f'{p1}/({p2}/({p3}-{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_div_minus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 / p3 ) - p4)
                        if r == 24:
                            return f'{p1}/(({p2}/{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_div_minus(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 / p3 ) - p4)
                        if r == 24:
                            return f'{p1}/(({p2}/{p3})-{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_div_minus(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) / p3 ) - p4
                    if r == 24:
                        return f'(({p1}/{p2})/{p3})-{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_div_mult(p1,p2,p3,p4):
            try:
                r = (p1 / p2) / (p3 * p4)
                if r == 24:
                    return f'({p1}/{p2})/({p3}*{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_div_mult(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 / (p3 * p4))
                    if r == 24:
                        return f'{p1}/({p2}/({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_div_mult(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 / (p3 * p4))
                    if r == 24:
                        return f'{p1}/({p2}/({p3}*{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_div_mult(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 / p3 ) * p4)
                        if r == 24:
                            return f'{p1}/(({p2}/{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_div_mult(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 / p3 ) * p4)
                        if r == 24:
                            return f'{p1}/(({p2}/{p3})*{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_div_mult(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) / p3 ) * p4
                    if r == 24:
                        return f'(({p1}/{p2})/{p3})*{p4}'
                except ZeroDivisionError:
                    return None
                return None

def val_0_div_div_div(p1,p2,p3,p4):
            try:
                r = (p1 / p2) / (p3 / p4)
                if r == 24:
                    return f'({p1}/{p2})/({p3}/{p4})'
            except ZeroDivisionError:
                return None
            return None

def val_1_div_div_div(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 / (p3 / p4))
                    if r == 24:
                        return f'{p1}/({p2}/({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_2_div_div_div(p1,p2,p3,p4):
                try:
                    r = p1 / ( p2 / (p3 / p4))
                    if r == 24:
                        return f'{p1}/({p2}/({p3}/{p4}))'
                except ZeroDivisionError:
                    return None
                return None

def val_3_div_div_div(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 / p3 ) / p4)
                        if r == 24:
                            return f'{p1}/(({p2}/{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_4_div_div_div(p1,p2,p3,p4):
                    try:
                        r = p1 / (( p2 / p3 ) / p4)
                        if r == 24:
                            return f'{p1}/(({p2}/{p3})/{p4})'
                    except ZeroDivisionError:
                        return None
                    return None

def val_5_div_div_div(p1,p2,p3,p4):
                try:
                    r = ((p1 /  p2 ) / p3 ) / p4
                    if r == 24:
                        return f'(({p1}/{p2})/{p3})/{p4}'
                except ZeroDivisionError:
                    return None
                return None
