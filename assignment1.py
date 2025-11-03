import math

def find_period(L0, L1):
    g = 9.81  # gravitational acceleration (m/s^2)
    
    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / g)
        print(f"When L = {L:.1f} m, T = {T:.1f} s")
    
    # Return the periods for L0 and L1
    T0 = 2 * math.pi * math.sqrt(L0 / g)
    T1 = 2 * math.pi * math.sqrt(L1 / g)
    return T0, T1