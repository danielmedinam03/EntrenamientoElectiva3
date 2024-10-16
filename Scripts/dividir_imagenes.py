import os
import shutil
import re
from sklearn.model_selection import train_test_split

# Ruta del dataset original que contiene las imágenes ya preprocesadas
original_dataset_dir = r'C:\Users\Usuario\Documents\DANIEL\UNIVERSIDAD_COOPERATIVA\DANIEL 10MO SEMESTRE\EntrenamientoElectiva3\DataSet Ajustado\DataSet fill background'

# Directorios para los conjuntos de entrenamiento, validación y prueba
base_dir = r'C:\Users\Usuario\Documents\DANIEL\UNIVERSIDAD_COOPERATIVA\DANIEL 10MO SEMESTRE\EntrenamientoElectiva3\DataSet Ajustado'
train_dir = os.path.join(base_dir, 'train')
valid_dir = os.path.join(base_dir, 'valid')
test_dir = os.path.join(base_dir, 'test')

# Crear directorios si no existen
os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Función para obtener todas las imágenes de un directorio y sus subdirectorios
def get_all_images(directory):
    all_images = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                all_images.append(os.path.join(root, file))
    return all_images

# Obtener todas las imágenes
all_images = get_all_images(original_dataset_dir)

# Imprimir información de depuración
print(f"Directorio de imágenes: {original_dataset_dir}")
print(f"¿El directorio existe? {os.path.exists(original_dataset_dir)}")
print(f"Número de imágenes encontradas: {len(all_images)}")
if all_images:
    print(f"Primeras 5 imágenes: {all_images[:5]}")
else:
    print("No se encontraron imágenes en el directorio especificado.")

# Dividir el dataset en entrenamiento (70%), validación (20%) y prueba (10%)
train_images, temp_images = train_test_split(all_images, test_size=0.3, random_state=42)
valid_images, test_images = train_test_split(temp_images, test_size=(1/3), random_state=42)

# Función para copiar imágenes manteniendo la estructura de directorios, pero eliminando el fragmento especificado
def copy_images(image_list, destination_dir):
    for img_path in image_list:
        relative_path = os.path.relpath(img_path, original_dataset_dir)
        
        # Dividir la ruta en partes
        path_parts = relative_path.split(os.sep)
        
        # Eliminar el fragmento "resized no_background fillbg" de cada parte de la ruta
        cleaned_parts = [re.sub(r'resized no_background fillbg', '', part).strip() for part in path_parts]
        
        # Reconstruir la ruta relativa
        cleaned_relative_path = os.path.join(*cleaned_parts)
        
        dest_path = os.path.join(destination_dir, cleaned_relative_path)
        
        # Asegurarse de que el directorio de destino exista
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Copiar la imagen
        shutil.copy(img_path, dest_path)

# Copiar las imágenes a los directorios correspondientes
copy_images(train_images, train_dir)
copy_images(valid_images, valid_dir)
copy_images(test_images, test_dir)

# Confirmar la cantidad de imágenes en cada conjunto
print(f'Cantidad de imágenes en entrenamiento: {len(train_images)}')
print(f'Cantidad de imágenes en validación: {len(valid_images)}')
print(f'Cantidad de imágenes en prueba: {len(test_images)}')
