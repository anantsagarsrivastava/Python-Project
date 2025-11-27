from PIL import Image
import os

input_dir = 'photos'
output_dir = 'photos_clean'
os.makedirs(output_dir, exist_ok=True)

for fname in ['ANANT.jpg', 'abhiraj.jpg', 'swaroop.jpg', 'bharat.jpg', 'vansh.jpg']:
    try:
        img = Image.open(os.path.join(input_dir, fname))
        # Convert to RGB (strips ICC profile and other metadata)
        img_rgb = img.convert('RGB')
        # Save as clean JPEG
        output_path = os.path.join(output_dir, fname)
        img_rgb.save(output_path, 'JPEG', quality=95)
        print(f"Cleaned: {fname}")
    except Exception as e:
        print(f"Error cleaning {fname}: {e}")
