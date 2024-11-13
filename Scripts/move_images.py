import os
import shutil

# Define the source and destination directories
source_directory = r'C:\Users\Usuario\Documents\DANIEL\UNIVERSIDAD_COOPERATIVA\DANIEL 10MO SEMESTRE\EntrenamientoElectiva3\dataset-ajustado\DataSet remove background'  # Cambia esto por la ruta a la carpeta original
destination_directory = r'C:\Users\Usuario\Documents\DANIEL\UNIVERSIDAD_COOPERATIVA\DANIEL 10MO SEMESTRE\EntrenamientoElectiva3\dataset-ajustado-150\DataSet remove background'  # Cambia esto por la ruta de la nueva carpeta

# Recorrer la carpeta principal
def copy_images(source_dir, dest_dir, max_images=150):
    # Si la carpeta de destino no existe, crearla
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Recorrer todas las subcarpetas dentro de la carpeta fuente
    for root, dirs, files in os.walk(source_dir):
        # Obtener la ruta relativa de la carpeta actual
        relative_path = os.path.relpath(root, source_dir)
        # Crear la carpeta correspondiente en el destino
        current_dest_dir = os.path.join(dest_dir, relative_path)
        if not os.path.exists(current_dest_dir):
            current_dest_dir = current_dest_dir.replace('resized no_background', '')
            current_dest_dir = current_dest_dir.rstrip()
            os.makedirs(current_dest_dir)

        # Filtrar los archivos para incluir solo las imágenes
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'))]
        
        # Seleccionar las primeras 'max_images' imágenes
        selected_images = image_files[:max_images]

        # Copiar las imágenes seleccionadas a la carpeta correspondiente en el destino
        for image in selected_images:
            source_image_path = os.path.join(root, image)
            destination_image_path = os.path.join(current_dest_dir, image)
            try:
                shutil.copy2(source_image_path, destination_image_path)
                print(f"Copiado: {source_image_path} a {destination_image_path}")
            except FileNotFoundError as e:
                print(f"Error: No se pudo encontrar el archivo {source_image_path}. {e}")
            except Exception as e:
                print(f"Error desconocido al copiar {source_image_path}. {e}")

# Ejecutar la función
if os.path.exists(source_directory) and os.path.isdir(source_directory):
    copy_images(source_directory, destination_directory)
else:
    print(f"Error: La ruta de origen '{source_directory}' no existe o no es un directorio válido.")
