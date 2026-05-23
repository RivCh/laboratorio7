import os
from PIL import Image, ImageFilter, ImageDraw


def process_image(
        input_path: str,
        output_path: str,
        rotation_angle: int,
        filter_name: str,
        watermark_text: str
) -> str:
    # 1. Abrir la imagen original
    image = Image.open(input_path)

    # 2. Rotación dinámica
    rotated = image.rotate(int(rotation_angle))

    # 3. Aplicación del filtro dinámico
    if filter_name == "EMBOSS":
        filtered = rotated.filter(ImageFilter.EMBOSS)
    elif filter_name == "FIND_EDGES":
        filtered = rotated.filter(ImageFilter.FIND_EDGES)
    else:
        filtered = rotated

    # 4. Dibujar la marca de agua
    draw = ImageDraw.Draw(filtered)
    draw.text((20, 20), str(watermark_text), fill="white")

    # 5. Asegurar que la carpeta de destino exista y guardar
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    filtered.save(output_path)

    return output_path