from mystix.targets.visualization.graphs import GraphManager
from threading import Thread
import time
from math import sin, pi
import numpy as np  # type: ignore

MOCK_DATA_RESOLUTION = 50


# MOCK_DATA_X = [t for t in np.linspace(0, 2*pi, MOCK_DATA_RESOLUTION)]
# MOCK_DATA_Y = [sin(t) for t in MOCK_DATA_X]
# mock_ptr = 0
# def get_mock_data(count: int):
#     x_data = []
#     y_data = []
#     global mock_ptr
#     for i in range(count):
#         x_data.append(
#             MOCK_DATA_X[
#                 (mock_ptr + i) % len(MOCK_DATA_X)] + moc)
#         y_data.append(
#             MOCK_DATA_Y[
#                 (mock_ptr + i) % len(MOCK_DATA_Y)])
#     mock_ptr = mock_ptr + count
#     return x_data, y_data

t = 0.0


def get_mock_data(count: int):
    x_data = []
    y_data = []
    global t
    for i in range(count):
        x_data.append(t)
        y_data.append(sin(t))
        t = t + (2*pi/MOCK_DATA_RESOLUTION)
    return x_data, y_data


def run():
    gm = GraphManager()
    gm.add_plot("example_plot", line_plot=True)
    def run_mock_logic():
        for i in range(30): # 3 seconds of playback
            t,y = get_mock_data(5)
            gm.add_plot_data("example_plot", t, y)
            time.sleep(0.1)

    logic = Thread(target=run_mock_logic)
    logic.start()

    gm.graphics.display(ttl=3000)

    logic.join()
    gm.clean()
