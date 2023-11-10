import os
import shutil
import re


def copy_images_with_exact_numbers_in_title(
    source_folder, destination_folder, exact_numbers_in_title, prefix="snap_"
):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    updated_numbers = [number - 1 for number in exact_numbers_in_title]

    # The regex pattern now includes the prefix before the number
    pattern = re.compile(
        r"\b" + re.escape(prefix) + "(" + "|".join(map(str, updated_numbers)) + r")\b"
    )

    image_files = [
        img
        for img in os.listdir(source_folder)
        if img.endswith((".png", ".tiff", ".jpeg", ".gif", ".bmp"))
    ]

    selected_images = [
        img for img in image_files if pattern.search(os.path.splitext(img)[0])
    ]

    for image_name in selected_images:
        shutil.copy(os.path.join(source_folder, image_name), destination_folder)

    return f"Copied images with titles containing exact numbers {updated_numbers} with prefix '{prefix}' to {destination_folder}"


source_folder = r"C:\Users\Aashman Sharma\Documents\Paraview\cmos"  # Replace with your source folder path
destination_folder = r"C:\Users\Aashman Sharma\Documents\Paraview\Test10_[1,1]_box"  # Replace with your destination folder path
exact_numbers_in_title = [
    10,
    25,
    40,
    65,
    82,
    95,
    121,
    136,
    149,
    177,
    192,
    208,
    230,
    247,
    263,
    288,
    303,
    320,
]  # Exact numbers to match in the image titles

# If all your files start with "snap_", you do not need to change the prefix parameter
copy_images_with_exact_numbers_in_title(
    source_folder, destination_folder, exact_numbers_in_title
)
