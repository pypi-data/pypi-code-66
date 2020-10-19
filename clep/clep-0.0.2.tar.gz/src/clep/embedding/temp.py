#!/usr/bin/env python
"""
Annotate a group of y-tick labels as such.
"""

import matplotlib.pyplot as plt
from matplotlib.transforms import TransformedBbox


def annotate_yranges(groups, fig, ax):
    """
    Annotate a group of consecutive yticklabels with a group name.

    Arguments:
    ----------
    groups : dict
        Mapping from group label to an ordered list of group members.
    fig: matplotlib.figure object
        The figure instance to get the bbox.
    ax : matplotlib.axes object
        The axis instance to annotate.
    """

    label2obj = {ticklabel.get_text(): ticklabel for ticklabel in ax.get_xticklabels()}

    _get_text_object_bbox(label2obj['a'], fig, ax)

    for ii, (group, members) in enumerate(groups.items()):
        first = members[0]
        last = members[-1]

        bbox0 = _get_text_object_bbox(label2obj[first], fig, ax)
        bbox1 = _get_text_object_bbox(label2obj[last], fig, ax)

        set_yrange_label(group, ax, bbox0.x0 + bbox0.width/2,
                         bbox1.x0 + bbox1.width/2,
                         min(bbox0.y0, bbox1.y0),
                         -2)


def set_yrange_label(label, ax, xmin, xmax, y, dy=-0.5, *args, **kwargs):
    """
    Annotate a y-range.

    Arguments:
    ----------
    label : string
        The label.
    ymin, ymax : float, float
        The y-range in data coordinates.
    x : float
        The x position of the annotation arrow endpoints in data coordinates.
    dx : float (default -0.5)
        The offset from x at which the label is placed.
    ax : matplotlib.axes object (default None)
        The axis instance to annotate.
    """

    dx = xmax - xmin
    props = dict(connectionstyle='angle, angleA=180, angleB=90, rad=0',
                 arrowstyle='-',
                 shrinkA=10,
                 shrinkB=10,
                 lw=1)
    ax.annotate(label,
                xy=(xmin, y - dy/5),
                xytext=(xmin + dx/3, y - dy),
                annotation_clip=False,
                arrowprops=props,
                *args, **kwargs,
    )
    ax.annotate(label,
                xy=(xmax, y - dy/5),
                xytext=(xmin + dx/3, y - dy),
                annotation_clip=False,
                arrowprops=props,
                *args, **kwargs,
    )


def _get_text_object_bbox(text_obj, fig, ax):
    # https://stackoverflow.com/a/35419796/2912349
    transform = ax.transData.inverted()
    # the figure needs to have been drawn once, otherwise there is no renderer?
    fig.canvas.draw()
    bb = text_obj.get_window_extent(renderer=ax.get_figure().canvas.renderer)
    # handle canvas resizing
    return TransformedBbox(bb, transform)


if __name__ == '__main__':

    import numpy as np

    fig, ax = plt.subplots(1, 1)

    # so we have some extra space for the annotations
    fig.subplots_adjust(bottom=0.1)

    data = np.random.rand(10, 10)
    ax.imshow(data)

    ticklabels = 'abcdefghij'
    ax.set_xticks(np.arange(len(ticklabels)))
    ax.set_xticklabels(ticklabels)

    groups = {
        'abc' : ('a', 'b', 'c'),
        'def' : ('d', 'e', 'f'),
        'ghij' : ('g', 'h', 'i', 'j')
    }

    annotate_yranges(groups, fig, ax)

    plt.show()