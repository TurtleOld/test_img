import os

from PIL import Image


def create_tiff(folders, output_filename):
    images = []

    for folder in folders:
        for filename in os.listdir(folder):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                filepath = os.path.join(folder, filename)
                try:
                    image = Image.open(filepath)
                    images.append(image)
                except IOError:
                    print("Не смог открыть картинку!")

    images[0].save(
        output_filename,
        save_all=True,
        append_images=images[1:],
        optimize=True,
        compression="tiff_deflate",
        duration=500,
        loop=0,
    )


create_tiff(
    [
        "1369_12_Наклейки 3-D_3",
        "1388_2_Наклейки 3-D_1",
        "1388_6_Наклейки 3-D_2",
        "1388_12_Наклейки 3-D_3",
    ],
    "test_img.tif",
)
