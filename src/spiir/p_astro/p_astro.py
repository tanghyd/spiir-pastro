import numpy as np

# from ligo.p_astro_computation import p_astro_update

from .mass_contour import predict_pastro


def compute_pastro(
    p_astro_labels: list[str] = ["BNS", "NSBH", "BBH", "Terrestrial"]
) -> dict[str, float]:
    p_astro_values = np.abs(np.random.randn(4))
    p_astro_values /= p_astro_values.sum()  # normalise
    p_astro = {}
    for label, value in zip(p_astro_labels, p_astro_values.tolist()):
        p_astro[label] = value
    return p_astro


def update_posteriors():
    pass


# def evaluate_p_astro_from_bayesfac(
#     astro_bayesfac: float,
#     mean_values_dict: dict[str, float],
#     coefficients: dict[str, float],
#     mchirp: float,
#     snr: float,
#     eff_distance: float,
#     m_bounds: tuple[float, float],
#     mgap_bounds: tuple[float, float],
#     group_mgap: bool = True,
#     lal_cosmology: bool = True,
#     truncate_lower_dist: float | None = 0.003,
#     num_bins: int | None = None,
#     activation_counts: float | None = None
# ):
#     """
#     Evaluates `p_astro` for a new event using Bayes factor, masses, and number
#     of astrophysical categories. Invoked with every new GraceDB entry.

#     Parameters
#     ----------
#     astro_bayesfac : float
#         astrophysical Bayes factor
#     mean_values_dict: dictionary
#         mean values of Poisson counts
#     coefficients: float
#         The estimated model coefficients of fitted mass/distance models.
#     mchirp: float
#         The source frame chirp mass.
#     snr: float
#         The coincident signal-to-noise ratio (SNR)
#     eff_distance: float
#         The estimated effective distance, usually taken as the minimum across all coincident detectors.
#     m_bounds: tuple[float, float]
#         The upper and lower bounds for both component masses (m1 >= m2).
#     mgap_bounds: tuple[float, float]
#         The boundaries that define the mass gap between BH and NS.
#     group_mgap: bool
#         If True, aggregates Mass Gap from BH+Gap, Gap+NS, and Gap+Gap.
#     lal_cosmology: bool
#         If True, it uses the Planck15 cosmology model as defined in lalsuite instead of the astropy default.

#     Returns
#     -------
#     p_astro : dictionary
#         p_astro for all source categories
#     """

#     probs = predict_pastro(
#         coefficients,
#         mchirp,
#         snr,
#         eff_distance,
#         m_bounds,
#         mgap_bounds,
#         group_mgap,
#         lal_cosmology,
#         truncate_lower_dist=0.003,
#     )

#     a_hat_bns = probs["BNS"]
#     a_hat_bbh = probs["BBH"]
#     a_hat_nsbh = probs["NSBH"]

#     # Compute category-wise Bayes factors
#     # from astrophysical Bayes factor
#     rescaled_fb = len(probs) * astro_bayesfac
#     bns_bayesfac = a_hat_bns * rescaled_fb
#     nsbh_bayesfac = a_hat_nsbh * rescaled_fb
#     bbh_bayesfac = a_hat_bbh * rescaled_fb

#     # Construct category-wise Bayes factor dictionary
#     event_bayesfac_dict = {
#         "counts_BNS": bns_bayesfac,
#         "counts_NSBH": nsbh_bayesfac,
#         "counts_BBH": bbh_bayesfac
#     }

#     # Compute the p-astro values for each source category
#     # using the mean values
#     p_astro_values = {}
#     for category in mean_values_dict:
#         p_astro_values[category.split("_")[1]] = p_astro_update(
#             category=category,
#             event_bayesfac_dict=event_bayesfac_dict,
#             mean_values_dict=mean_values_dict
#         )

#     return p_astro_values
