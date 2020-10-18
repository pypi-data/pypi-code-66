"""Tests polepade module."""
import numpy as np

from .context import gftool as gt


def test_opt_sv_coeff_sigma():
    """Compare `gt.polepade._opt_sv_coeff_sigma` with values provided in paper."""
    beta = np.linspace(0.05, 1.0, num=20)
    cmp_res = np.array([
        1.5066, 1.5816, 1.6466, 1.7048, 1.7580, 1.8074, 1.8537, 1.8974, 1.9389, 1.9786,
        2.0167, 2.0533, 2.0887, 2.1229, 2.1561, 2.1883, 2.2197, 2.2503, 2.2802, 2.3094,
    ])
    assert np.allclose(gt.polepade._opt_sv_coeff_sigma(beta), cmp_res, atol=1e-4)


def test_median_marcenko_pastur():
    """Compare `gt.polepade._median_marcenko_pastur` with values provided in paper.

    See Table IV.
    """
    beta = np.linspace(0.05, 1.0, num=20)
    tau = gt.polepade._opt_sv_coeff_sigma(beta)
    mu = np.array([gt.polepade._median_marcenko_pastur(bb) for bb in beta])
    omega = tau/np.sqrt(mu)
    cmp_res = np.array([
        1.519, 1.6087, 1.6896, 1.7650, 1.837,
        1.906, 1.974, 2.040, 2.106, 2.171,
        2.236, 2.302, 2.368, 2.434, 2.501,
        2.570, 2.640, 2.710, 2.783, 2.858,
    ])
    assert np.allclose(omega, cmp_res, atol=1e-3)
