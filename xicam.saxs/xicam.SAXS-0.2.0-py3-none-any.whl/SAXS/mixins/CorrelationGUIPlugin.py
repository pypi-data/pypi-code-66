from qtpy.QtWidgets import QWidget

from xicam.core import msg
from xicam.plugins import GUILayout
from xicam.gui.models import IntentsModel
from xicam.gui.widgets.linearworkfloweditor import WorkflowEditor
from xicam.gui.widgets.views import StackedCanvasView, DataSelectorView

from xicam.SAXS.widgets.XPCSToolbar import XPCSToolBar
from xicam.SAXS.workflows.roi import ROIWorkflow
from xicam.SAXS.workflows.xpcs import OneTime, TwoTime


# FIXME: the old way used TabWidget.currentWidget with XPCSToolBar...
# - previous: view was a tab view with the SAXSReductionViewer mixin as its widget
# - how can we adapt this to StackedCanvasView / CanvasView?


# # SAXS GUI Plugin mixin can use shared components
# class SAXSGUIPlugin(CorrelationGUIPlugin, SAXSReductionGUIPlugin)


class CorrelationStage(QWidget):
    def __init__(self, model, parent=None, **layout_kwargs):

        if layout_kwargs.pop("center", None) is not None:
            msg.notifyMessage("CorrelationStage already provides a \"center\" widget.", msg.WARNING)

        if layout_kwargs.pop("righttop", None) is not None:
            msg.notifyMessage("CorerlationStage already provides a \"righttop\" widget.", msg.WARNING)

        self.model = model
        self.intents_model = IntentsModel()
        self.intents_model.setSourceModel(self.model)

        self.data_selector_view = DataSelectorView()
        self.data_selector_view.setModel(model)

        self.canvases_view = StackedCanvasView()
        self.canvases_view.setModel(self.intents_model)

        self.roi_workflow = ROIWorkflow()
        # THIS PROBABLY WONT WORK WITH THIS CANVAS VIEW
        self.toolbar = XPCSToolBar(view=self.canvases_view.view, workflow=self.roi_workflow, index=0)
        # Tool bar mixin can be a view kwarg

        # view_kwargs -> sequence of "str" (can't be types... needs to be serializable), need another registry?
        # ImageCanvas.__init__(..., **view_kwargs)
        # ImageCanvas.__new__(..., **view_kwargs):
            # Build new view type with view_kwargs
        # meta-programmable canvas

        self.gui_layout = GUILayout(center=self.canvases_view,
                                    righttop=self.data_selector_view,
                                    top=self.toolbar,
                                    **layout_kwargs)

        super(CorrelationStage, self).__init__(parent=parent)

    def do_thing(self):
        msg.notifyMessage("WORKFLOW RUNNING...")
        # Grab the "current" image?
        # How do we know what the current image is?
        images = None
        # Execute roi workflow
        # Can we embed the roi-workflow in core / gui operations eventually?
        # Execute the workflow editor workflow
        roi_result = None
        with msg.busyContext():
            roi_future = self.roi_workflow.execute(data=None, image=None)
            roi_result = roi_future
        roi_result = roi_future.result()
        label = roi_result[-1]["roi"]


# if processor:
#     roiFuture = self.roiworkflow.execute(data=self.correlationView.currentWidget().image[0],
#                                          image=self.correlationView.currentWidget().imageItem)  # Pass in single frame for data shape
#     roiResult = roiFuture.result()
#     label = roiResult[-1]["roi"]
#     if label is None:
#         msg.notifyMessage("Please define an ROI using the toolbar before running correlation.")
#         return
#
#     workflow = processor.workflow
#     # FIXME -- don't grab first match
#     technique = \
#         [technique for technique in self.schema()['techniques'] if technique['technique'] == 'scattering'][0]
#     stream, field = technique['data_mapping']['data_image']
#     # TODO: the compute() takes a long time..., do we need to do this here? If so, show a progress bar...
#     # Trim the data frames
#     catalog = self.currentCatalog()
#     data = [getattr(catalog, stream).to_dask()[field][0].where(
#         DataArray(label, dims=["dim_1", "dim_2"]), drop=True).compute()]
#     # Trim the dark images
#     msg.notifyMessage("Skipping dark correction...")
#     darks = [None] * len(data)
#     dark_stream, dark_field = technique['data_mapping']['dark_image']
#     if stream in catalog:
#         darks = [getattr(catalog, dark_stream).to_dask()[dark_field][0].where(
#             DataArray(label, dims=["dim_1", "dim_2"]), drop=True).compute()]
#     else:
#         msg.notifyMessage(f"No dark stream named \"{dark_stream}\" for current catalog. No dark correction.")
#     label = label.compress(np.any(label, axis=0), axis=1).compress(np.any(label, axis=1), axis=0)
#     labels = [label] * len(data)  # TODO: update for multiple ROIs
#     numLevels = [1] * len(data)
#
#     numBufs = []
#     for i in range(len(data)):
#         shape = data[i].shape[0]
#         # multi_tau_corr requires num_bufs to be even
#         if shape % 2:
#             shape += 1
#         numBufs.append(shape)
#
#     if kwargs.get('finished_slot'):
#         finishedSlot = kwargs['finished_slot']
#     else:
#         finishedSlot = self.updateDerivedDataModel
#
#     # workflow_pickle = pickle.dumps(workflow)
#     workflow.execute_all(None,
#                          # data=data,
#                          images=data,
#                          darks=darks,
#                          labels=labels,
#                          finished_slot=partial(finishedSlot,
#                                                workflow=workflow))
#                                                # workflow_pickle=workflow_pickle))


class OneTimeCorrelationStage(CorrelationStage):
    def __init__(self, model, parent=None):
        onetime_workflow = OneTime()
        onetime_editor = WorkflowEditor(onetime_workflow)
        onetime_editor.sigRunWorkflow.connect(self.do_thing)
        onetime_editor.sigRunWorkflow.disconnect(onetime_editor.run_workflow)
        super(OneTimeCorrelationStage, self).__init__(model, parent=parent, rightbottom=onetime_editor)


class TwoTimeCorrelationStage(CorrelationStage):
    def __init__(self, model, parent=None):
        twotime_workflow = TwoTime()
        twotime_editor = WorkflowEditor(twotime_workflow)
        twotime_editor.sigRunWorkflow.connect(self.do_thing)
        twotime_editor.sigRunWorkflow.disconnect(twotime_editor.run_workflow)
        super(TwoTimeCorrelationStage, self).__init__(model, parent=parent, rightbottom=twotime_editor)
