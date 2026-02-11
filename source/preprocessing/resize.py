from pathlib import Path
from PIL import Image

def preprocess_artworks(src_root, dest_root, min_images=99, target_size=(224, 224)):
    # Convert strings to Path objects
    src_path = Path(src_root)
    dest_path = Path(dest_root)
    
    # Create destination root if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)

    # Iterate through artist subfolders
    for artist_dir in src_path.iterdir():
        if artist_dir.is_dir():
            # Get list of all image files
            images = [f for f in artist_dir.iterdir() if f.suffix.lower() in ['.jpg']]
            
            # Filter by your count requirement
            if len(images) >= min_images:
                print(f"Processing {artist_dir.name}: {len(images)} images found.")
                
                # Create corresponding folder in processed directory
                artist_dest = dest_path / artist_dir.name
                artist_dest.mkdir(exist_ok=True)
                
                for img_path in images:
                    try:
                        with Image.open(img_path) as img:
                            # Convert to RGB (handles RGBA or grayscale cases)
                            img = img.convert('RGB')
                            # Resize using high-quality Lanczos resampling
                            img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                            # Save to new location
                            img_resized.save(artist_dest / img_path.name)
                    except Exception as e:
                        print(f"Could not process {img_path.name}: {e}")
            else:
                print(f"Skipping {artist_dir.name}: Only {len(images)} images.")

if __name__ == "__main__":
    SOURCE = "data/raw/images"
    DESTINATION = "data/processed/resized224"
    
    preprocess_artworks(SOURCE, DESTINATION)
    print("Done! Check data/processed/resized224 for your images.")