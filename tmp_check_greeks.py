import sys
import os
sys.path.append(os.path.abspath("src"))

from pricing.greeks import call_delta, gamma, vega

print(call_delta(100, 100, 1, 0.2, 0.05))
print(gamma(100, 100, 1, 0.2, 0.05))
print(vega(100, 100, 1, 0.2, 0.05))
