import numpy as np

@np.vectorize
def mass2_from_mchirp_mass1(mchirp: float, mass1: float):
    r"""Returns the secondary mass from the chirp mass and primary mass.
    As this is a cubic equation this requires finding the roots and returning
    the one that is real. Basically it can be shown that:
    .. math::
        m_2^3 - a(m_2 + m_1) = 0,
    where
    .. math::
        a = \frac{\mathcal{M}^5}{m_1^3}.
    This has 3 solutions but only one will be real.
    """
    a = mchirp**5 / mass1**3
    roots = numpy.roots([1,0,-a,-a*mass1])
    # Find the real one
    real_root = roots[(abs(roots - roots.real)).argmin()]
    return real_root.real
