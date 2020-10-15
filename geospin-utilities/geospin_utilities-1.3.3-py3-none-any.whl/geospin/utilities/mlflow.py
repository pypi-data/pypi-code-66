import tempfile

import folium
import matplotlib
import mlflow


def save_visualization_to_mlflow(visualization_function, prefix=''):
    """
    Save visualization to artifacts URI in mlflow run.

    This function:

    - Automatically creates and removes intermittent data that is required to
    store mlflow artifacts.
    - Ensures unique naming of artifacts using the name of the
    `visualzation_function` and adding a random string to the file name. This
    avoids overwriting visualizations that have the same name by
    accident.
    - Supports matplotlib figures and folium maps. It automatically adds the
    appropriate file extension (PNG or HTML). Other formats are easy to
    add.

    :param function visualization_function:
        Function that returns any of [matplotlib.figure.Figure, folium.Map]
    :param str prefix:
        Optional, prefix for the final file name in the artifact store.
    """
    visualization = visualization_function()

    if isinstance(visualization, matplotlib.figure.Figure):
        extension = '.png'
        save_method = 'savefig'
    elif isinstance(visualization, folium.Map):
        extension = '.html'
        save_method = 'save'
    else:
        raise ValueError('`plot_function` must be a Figure or a Map.')

    full_prefix = f'{visualization_function.__name__}_' + f'{prefix}_'

    temporary_file = tempfile.NamedTemporaryFile(
        prefix=full_prefix, suffix=extension)

    path_to_temporary_file = temporary_file.name

    # Save figure or map to temporary path
    getattr(visualization, save_method)(path_to_temporary_file)

    mlflow.log_artifact(path_to_temporary_file)
    temporary_file.close()
