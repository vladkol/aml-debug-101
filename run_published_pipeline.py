from azureml.pipeline.core import PublishedPipeline
from azureml.core.experiment import Experiment
from azureml.core import Workspace

workspace = Workspace.from_config()

published_pipeline_id = ""
is_debug = True
debug_relay_connection_name = "test"

if published_pipeline_id is None or published_pipeline_id == "":
    raise ValueError("Initialize published_pipeline_id")

pipeline_parameters = {
    "is_debug": is_debug
}
if is_debug:
    if debug_relay_connection_name == "":
        raise ValueError("Hybrid connection name cannot be empty!")

    pipeline_parameters.update({
        "debug_relay_connection_name": debug_relay_connection_name
    })

experiment = Experiment(workspace, "Pipeline_debug_experiment")
published_pipeline = PublishedPipeline.get(
    workspace=workspace, id=published_pipeline_id)
experiment.submit(published_pipeline, pipeline_parameters=pipeline_parameters)
