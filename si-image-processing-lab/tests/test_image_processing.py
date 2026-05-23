import os
from PIL import Image
from src.si_image_processing.pipelines.image_processing.nodes import process_image


def test_process_image_reto():
    input_path = "data/01_raw/marte.jpg"
    output_path = "data/03_primary/test_output_reto.jpg"

    rotation_angle = 90
    filter_name = "FIND_EDGES"
    watermark_text = "Prueba Unitaria UNI"

    if os.path.exists(output_path):
        os.remove(output_path)

    result = process_image(
        input_path=input_path,
        output_path=output_path,
        rotation_angle=rotation_angle,
        filter_name=filter_name,
        watermark_text=watermark_text
    )

    assert result == output_path
    assert os.path.exists(output_path) is True

    with Image.open(output_path) as img:
        assert img.format == "JPEG"