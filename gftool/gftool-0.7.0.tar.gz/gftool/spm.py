"""Sparse Modelling approach for analytical continuation.

This module is based on [otsuki2017]_.

The basic idea is the following.
The analytic continuation can be expressed as an integral equation

.. math:: G(x) = ∫dω K(x, ω)ρ(ω)

where :math:`G(x)` is the (known) Green's function on a specific axis,
:math:`ρ(ω)` is the desired spectral function on the real-frequency axis,
and :math:`K(x, ω)` is the integration kernel.

This integral equation can be discretized (Riemann sum)

.. math:: G_j = ∑_i K_{ji} ρ_i

where :math:`G_j` are the known data points for the Green's function,
:math:`ρ_i` is the desired spectral function on a different grid.

The solution is obtained by solving the matrix equation. To reduce noise,
a truncated SVD of :math:`K_{ji}` is used and L1 regularization is employed via
Lasso.


References
----------
.. [otsuki2017] Otsuki, J., Ohzeki, M., Shinaoka, H., Yoshimi, K., 2017.
   Sparse modeling approach to analytical continuation of imaginary-time
   quantum Monte Carlo data.
   Phys. Rev. E 95, 061302.
   https://doi.org/10.1103/PhysRevE.95.061302

"""
import numpy as np
from sklearn import linear_model

import gftool as gt


def kernel_tau_ww(tau, ww, beta):
    """Kernel transforming from real energies `ww` to imaginary time `tau`."""
    # TODO: avoid overflows ww<0: np.exp((beta-tau)*ww)*gt.fermi_fct(ww, beta=beta)
    return np.exp(-tau*ww)*gt.fermi_fct(-ww, beta=beta)


def kernel_z_ww(z, ww):
    return 1./(z - ww)


#
# testing
#

# test data
from gftool import fourier
import matplotlib.pyplot as plt

BETA = 100
tau = np.linspace(0, BETA, num=2049)
iws = gt.matsubara_frequencies(range(1024), beta=BETA)
gf_iw = gt.square_gf_z(iws, half_bandwidth=1)
gf_tau = gt.fourier.iw2tau(gf_iw, beta=BETA, n_fit=5)

ww, dw = np.linspace(-2, 2, num=1000, retstep=True)
gf_ww = gt.square_gf_z(ww+1e-16j, half_bandwidth=1)

K = -kernel_tau_ww(tau[:, np.newaxis], ww, beta=BETA) * dw
# check kernel
gf_tau_k = K @ (-gf_ww.imag/np.pi)
plt.plot(gf_tau)
plt.plot(gf_tau_k, '--')
plt.show()

U, s, Vh = np.linalg.svd(K)
plt.plot(s)
plt.show()

truncation = 50  # chosen by hand from plot

gf_tau_mod = U.transpose().conj()[:truncation, :] @ gf_tau

reg = linear_model.LassoLarsCV(verbose=True, n_jobs=-1).fit(np.diagflat(s[:truncation]), gf_tau_mod)
print(reg.score(np.diagflat(s[:truncation]), gf_tau_mod))
rho_mod = reg.coef_
rho = Vh.conj().transpose()[:, :truncation] @ rho_mod
plt.plot(-gf_ww.imag/np.pi)
plt.plot(rho)

plt.plot(gf_tau)
plt.plot(K@rho, '--')

#
# test iws -> ww
#
K = kernel_z_ww(iws[:, np.newaxis], ww) * dw
# check kernel
gf_iw_k = K @ (-gf_ww.imag/np.pi)
plt.plot(gf_iw.imag)
plt.plot(gf_iw_k.imag, '--')
plt.show()

U, s, Vh = np.linalg.svd(K)
plt.plot(s)
plt.show()

truncation = 50  # chosen by hand from plot

gf_iw_mod = U.transpose().conj()[:truncation, :] @ gf_iw
xcon = np.diagflat(np.concatenate((s[:truncation], s[:truncation])))

reg = linear_model.LassoLarsCV(verbose=True, n_jobs=-1).fit(xcon, np.concatenate([gf_iw_mod.real, gf_iw_mod.imag]))
print(reg.score(xcon, np.concatenate([gf_iw_mod.real, gf_iw_mod.imag])))
rho_mod = reg.coef_[:truncation] + 1j*reg.coef_[truncation:]
rho = Vh.conj().transpose()[:, :truncation] @ rho_mod
plt.plot(-gf_ww.imag/np.pi)
plt.plot(rho)

plt.plot(gf_tau)
plt.plot(K@rho, '--')

