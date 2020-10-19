"""
Model classes and functions for CLICnet.
"""
# Imports --------------------------------------------------------------------------------------------------------------
from rbm import RBM
from cancer_data import MSK, MSKTMB, TCGA, LIU, RIAZ, load_presets
import numpy as np
import pandas as pd
from lifelines import CoxPHFitter
from lifelines import KaplanMeierFitter
from pkg_resources import resource_filename
import warnings
import seaborn as sns
import matplotlib as plt
from matplotlib.pyplot import subplots
from matplotlib.pyplot import savefig

# Constants ------------------------------------------------------------------------------------------------------------
MAX_EPOCHS = 1000

TCGA_DATA = TCGA(resource_filename(__name__, "cdata/tcga.pickle"))
MSK_DATA = MSK(resource_filename(__name__, "cdata/msk.pickle"))
MSK_PD1_DATA = MSKTMB(resource_filename(__name__, "cdata/msktmb.pickle"))
LIU_DATA = LIU(resource_filename(__name__, "cdata/liu.pickle"))
RIAZ_DATA = RIAZ(resource_filename(__name__, "cdata/riaz.pickle"))

PRESETS = load_presets(resource_filename(__name__, "cdata/mut_profiles.pickle"))
CANCER_TYPES = {
    'Head&neck':'HNSC',
    'Colorectal':'COAD',
    'Stomach':'STAD',
    'Esophagus':'ESCA',
    'Thyroid':'THCA',
    'Prostate':'PRAD',
    'Kidney':'KIRC',
    'Melanoma':'SKCM',
    'Breast':'BRCA',
    'Mesothelioma':'MESO',
    'Glioma':'LGG',
    'Endometrial':'UCEC',
    'Lung':'LUAD',
    'Bladder':'BLCA',
    'Pancreatic':'PAAD'
}
ANTI_PD1_CANCERS = ['Colorectal','Esophagus','Kidney','Melanoma','Glioma','Lung','Bladder']
plt.rcParams['figure.figsize'] = 12, 8

# Functions ------------------------------------------------------------------------------------------------------------
def log_rank_rbm(cancer_type, genes, cancer_data, max_epochs=MAX_EPOCHS, trained_rbm=None):
    """
    Get log-rank of survival. An RBM is trained based on the data, unless the trained_rbm parameter is provided,
    in which case the pre-trained RBM provided is used.
    """
    cancer_name = cancer_type
    assert cancer_type in set(CANCER_TYPES.keys()), \
        "Cancer type must be one of: {}".format(", ".join(CANCER_TYPES.keys()))
    cancer_type = CANCER_TYPES[cancer_type]

    assert cancer_data.assert_cancer_in_data(cancer_type), "Cancer type {} not in data".format(cancer_name)
    assert cancer_data.assert_genes_in_data(genes), "All genes [ {} ] not present in data".format(
        ", ".join(genes)
    )

    cancer_mutations_table, cancer_clinical_table = cancer_data.extract_cancer(cancer_type, genes)
    assert not cancer_mutations_table.empty, "No mutations selected, perhaps try different genes?"
    final_gene_set = set(cancer_mutations_table.keys())

    if trained_rbm is None:
        # train a new RBM, with visible units for the number of genes and with two hidden units, for survival and
        # death, trained on the cancer mutation data
        rbm_model = RBM(num_visible=cancer_mutations_table.shape[1], num_hidden=1)
        rbm_model.train(cancer_mutations_table.to_numpy(), max_epochs=max_epochs)
    else:
        # use a pre-trained RBM model provided as a parameter
        rbm_model = trained_rbm

    survival = np.array(cancer_clinical_table['survival'])  # survival rates
    death = np.array([i == 'Dead' for i in cancer_clinical_table['vital_status']])  # deaths, where True denotes dead

    # Run the RBM on the mutations data
    # This provides a list of 0s and 1s, denoting whether the hidden unit was activated per each sample
    samples_clusters = rbm_model.run_visible(cancer_mutations_table.to_numpy()).reshape(-1).astype(int)
    if len(set(samples_clusters)) == 1:
        # All samples clustered identically
        return 1, 1, rbm_model, None, final_gene_set

    # Calculate the p-value that the survival rates of the two populations, divided by the RBM clustering,
    # are generated from different data-generating processes that are statistically significantly different
    cox_df = pd.DataFrame(np.array([survival, death, samples_clusters]).transpose(),
                          columns=['survival', 'death', 'clusters'])
    if cancer_type == "PANCANC":
        # Pan cancer analysis, adding the type as a covariate
        strata_idxs = sorted(cancer_data.clinical_table.loc[:, "type"].tolist())
        cox_df.loc[:, "cancer_type"] = [
            strata_idxs.index(x) for x in cancer_data.clinical_table.loc[:, "type"].tolist()
        ]

    # Setup Cox regression
    cph = CoxPHFitter()
    with warnings.catch_warnings(record=True) as w:
        try:
            if cancer_type == "PANCANC":
                cph.fit(cox_df, duration_col='survival', event_col='death', strata=["cancer_type"])
            else:
                cph.fit(cox_df, duration_col='survival', event_col='death')

            coef = cph.hazard_ratios_[0]
            p_value = float(cph.summary.p)
        except warnings.Warning:
            coef = 1
            p_value = 1

    cox_df['sample'] = list(cancer_mutations_table.index)
    return p_value, coef, rbm_model, cox_df, final_gene_set

def log_rank_rbm_preset(cancer_type, cancer_data, gene_set_idx, trained_rbm=None):
    """
    Run log_rank_rbm on preset gene set for cancer_type, in index gene_set_idx (between 1 and 5).
    """
    assert cancer_type in set(CANCER_TYPES.keys()), \
        "Wrong cancer type, {}. Cancer type must be one of: {}".format(cancer_type, ", ".join(CANCER_TYPES.keys()))
    assert 1 <= gene_set_idx <= 5, "gene_set_idx must be between 1 and 5"

    gene_set_idx = gene_set_idx - 1
    cancer_code = CANCER_TYPES[cancer_type]
    genes = PRESETS[cancer_code][gene_set_idx]
    return log_rank_rbm(cancer_type, genes, cancer_data, trained_rbm=trained_rbm)

def log_rank_rbm_plots(cancer_type, cancer_data_train, cancer_data_test, genes, savepath=None):
    """
    Make KM and Heatmap plot from genes in cancer data
    """
    # Plot HM:
    cancer_name = cancer_type
    cancer_type = CANCER_TYPES[cancer_type]

    train_p_value, train_coef, train_rbm_model, cox_df_train, gene_set = log_rank_rbm(
        cancer_name, genes, cancer_data_train
    )

    data_train = get_hm_data(cancer_data_train, cancer_type, cox_df_train, genes)

    test_p_value, test_coef, rbm_model, cox_df_test,gene_set = log_rank_rbm(
        cancer_name, genes, cancer_data_test,trained_rbm=train_rbm_model
    )

    data_test = get_hm_data(cancer_data_test, cancer_type, cox_df_test, genes)

    colors1 = [
        (0.9411764705882353, 0.9372549019607843, 0.8823529411764706),
        (0.12156862745098039, 0.4666666666666667, 0.7058823529411765),
        (0.9882352941176471, 0.5529411764705883, 0.3843137254901961),
        (0.0392156862745098, 0.3411764705882353, 0.20392156862745098)
    ]

    fig1, (axs1, axs2) = subplots(2, 2, sharey=False)
    sns.heatmap(data_train.transpose(), cmap=colors1, ax=axs1[0],xticklabels=False,yticklabels=1,cbar=False)
    axs1[0].set_title('Training HM ' + cancer_name)
    sns.heatmap(data_test.transpose(), cmap=colors1, ax=axs2[0],xticklabels=False,yticklabels=1,cbar=False)
    axs2[0].set_title('Test HM ' + cancer_name)


    # Plot KM:
    survival_0, survival_1, death_0, death_1 = get_km_data(cox_df_train)
    kaplan_meier = KaplanMeierFitter()

    kaplan_meier.fit(survival_0, death_0, label='cluster 0')
    kaplan_meier.plot(ax=axs1[1])

    kaplan_meier.fit(survival_1, death_1, label='cluster 1')
    kaplan_meier.plot(ax=axs1[1])

    mytext = "P=%.2e, HR=%.2f" % (train_p_value, train_coef)
    axs1[1].text(1, 0.4, mytext)
    axs1[1].set_title('Training KM ' + cancer_name)

    survival_0, survival_1, death_0, death_1 = get_km_data(cox_df_test)
    kaplan_meier = KaplanMeierFitter()

    kaplan_meier.fit(survival_0, death_0, label='cluster 0')
    kaplan_meier.plot(ax=axs2[1])

    kaplan_meier.fit(survival_1, death_1, label='cluster 1')
    kaplan_meier.plot(ax=axs2[1])

    mytext = "P=%.2e, HR=%.2f" % (test_p_value, test_coef)
    axs2[1].text(1, 0.4, mytext)
    axs2[1].set_title('Test KM ' + cancer_name)

    if savepath:
        savefig(savepath + 'clicnet' + cancer_type + ".pdf")

def log_rank_rbm_plots_preset(cancer_type, cancer_data_train, cancer_data_test, gene_set_idx, savepath=None):
    assert cancer_type in set(CANCER_TYPES.keys()), \
        "Wrong cancer type, {}. Cancer type must be one of: {}".format(cancer_type, ", ".join(CANCER_TYPES.keys()))
    assert 1 <= gene_set_idx <= 5, "gene_set_idx must be between 1 and 5"
    gene_set_idx = gene_set_idx - 1
    cancer_code = CANCER_TYPES[cancer_type]
    genes = PRESETS[cancer_code][gene_set_idx]
    return log_rank_rbm_plots(cancer_type, cancer_data_train, cancer_data_test, genes, savepath=savepath)

def get_hm_data(cancer_data, cancer_type, cox_df, genes):
    mutations, clinical = cancer_data.extract_cancer(cancer_type, genes)
    mutations = mutations[list(mutations.columns)].astype(int)
    clusters = list(cox_df['clusters'])
    clusters_idxs = list(np.argsort(clusters))
    data = mutations.iloc[clusters_idxs].copy()
    data['cluster'] = [0.3 if clusters[i] == 0 else 0.6 for i in clusters_idxs]

    return data


def get_km_data(df_cox):
    surv = list(df_cox['survival'])
    death = list(df_cox['death'])
    clst = list(df_cox['clusters'])

    survival_0 = [surv[i] for i in range(len(surv)) if clst[i] == 0]
    survival_1 = [surv[i] for i in range(len(surv)) if clst[i] == 1]
    death_0 = [death[i] for i in range(len(surv)) if clst[i] == 0]
    death_1 = [death[i] for i in range(len(surv)) if clst[i] == 1]

    return survival_0, survival_1, death_0, death_1
