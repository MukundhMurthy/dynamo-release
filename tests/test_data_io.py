import os

import numpy as np
import pandas as pd

import dynamo
import dynamo as dyn

# import utils


def test_save_rank_info(adata):
    adata.uns['rank_1'] = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    adata.uns['rank_2'] = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
    dyn.export_rank_xlsx(adata)


def test_scEU_seq():
    dynamo.sample_data.scEU_seq_rpe1()
    assert os.path.exists("./data/rpe1.h5ad")


def test_zebrafish():
    dynamo.sample_data.zebrafish()


if __name__ == "__main__":
    # test_scEU_seq()
    # test_zebrafish()
    # adata = utils.gen_or_read_zebrafish_data()
    # test_save_rank_info(adata)
    pass
