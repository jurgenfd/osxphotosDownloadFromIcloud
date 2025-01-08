import time
import osxphotos
MAX_PHOTOS = 10000  # Maximum number of photos to download

def my_function():
    photosdb = osxphotos.PhotosDB()     # Load the Photos library
    photos = photosdb.photos()     # Get all photos
    print(f"Downloading up to {MAX_PHOTOS} photos")
    photo_count = 0
    
    for photo in photos:
        if photo_count >= MAX_PHOTOS:
            print("Downloaded enough photos, stopping...")
            break
        if photo.ismissing:
            print(f"Photo {photo.original_filename} is missing locally, triggering download...")
            # Attempt to export the photo, which might trigger a download
            photo.export("/Users/jd/Downloads/iCloudPhotoDump",
                         raw_photo=True, use_photos_export=True)
            photo_count += 1
            time.sleep(1) # sleep for a second to avoid hammering the API
    print(f"Downloaded {photo_count} photos")
# end def

if __name__ == "__main__":
    my_function()
