"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline
from si_image_processing.pipelines.image_processing import pipeline as img_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    image_processing_pipeline = img_pipeline.create_pipeline()

    return {
        "__default__": image_processing_pipeline,
        "image_processing": image_processing_pipeline
    }