import os
import re

import folium
import matplotlib.pyplot as plt
import mlflow
import pytest

import geospin.utilities.mlflow as utils_mlflow


@pytest.fixture
def tracking_uri(tmpdir):
    data_dir = tmpdir.mkdir('data')
    path = data_dir.join('mlruns')
    return str(path)


def plot_line():
    plt.plot(range(5))
    return plt.gcf()


def simple_map():
    return folium.Map()


@pytest.mark.parametrize(
    'visualization_function, name_pattern',
    [
        (plot_line, r'plot_line.*\.png'),
        (simple_map, r'simple_map.*\.html')
    ]
)
def test_save_visualization_to_mlflow(visualization_function,
                                      name_pattern, tracking_uri):
    # ---- Arrange ----
    mlflow.set_tracking_uri(tracking_uri)

    # ---- Act ----
    with mlflow.start_run():
        utils_mlflow.save_visualization_to_mlflow(visualization_function)
        artifact_uri = mlflow.get_artifact_uri()

    # ---- Assert ----
    file_names = os.listdir(artifact_uri)
    # Does a file with the desired name pattern occur in the artifacts?
    assert any(re.search(name_pattern, fn) for fn in file_names)
