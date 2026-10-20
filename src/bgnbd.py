import numpy as np
from scipy.special import gammaln, betaln


def log_verosimilitud(params, x, t_x, T):
    """Log-verosimilitud total del BG/NBD. params = (r, alpha, a, b)."""
    r, alpha, a, b = params

    comun = gammaln(r + x) + r * np.log(alpha) - gammaln(r)

    log_A = betaln(a, b + x) - betaln(a, b) - (r + x) * np.log(alpha + T)

    x_seguro = np.maximum(x, 1)
    log_B = np.where(
        x > 0,
        betaln(a + 1, b + x_seguro - 1) - betaln(a, b) - (r + x) * np.log(alpha + t_x),
        -np.inf,
    )

    return np.sum(comun + np.logaddexp(log_A, log_B))