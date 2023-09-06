import os
import requests
import bz2

def download_and_extract_shape_predictor():
    # URL of the shape predictor BZip2 compressed file (replace with the correct URL)
    shape_predictor_url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"

    # Define the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Path to save the downloaded shape predictor BZip2 compressed file
    shape_predictor_bz2_path = os.path.join(project_root, "shape_predictor_68_face_landmarks.dat.bz2")

    # Path to save the extracted shape predictor file
    shape_predictor_path = os.path.join(project_root, "shape_predictor_68_face_landmarks.dat")

    # Check if the shape predictor file already exists
    if not os.path.isfile(shape_predictor_path):
        try:
            # Download the shape predictor BZip2 compressed file
            print("Downloading shape predictor BZip2 compressed file...")
            response = requests.get(shape_predictor_url, stream=True)

            # Check if the request was successful
            if response.status_code == 200:
                # Save the downloaded BZip2 compressed file to the specified path
                with open(shape_predictor_bz2_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)

                print("Shape predictor BZip2 compressed file downloaded successfully.")

                # Extract the BZip2 compressed file
                with open(shape_predictor_bz2_path, "rb") as bz2_file, open(shape_predictor_path, "wb") as output_file:
                    decompressor = bz2.BZ2Decompressor()
                    for data in iter(lambda: bz2_file.read(100 * 1024), b''):
                        output_file.write(decompressor.decompress(data))

                print("Shape predictor file extracted successfully.")

                # Delete the BZip2 compressed file to save space
                os.remove(shape_predictor_bz2_path)
                print("Shape predictor BZip2 compressed file deleted.")
            else:
                print(f"Failed to download the shape predictor BZip2 compressed file. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred while downloading and extracting the shape predictor BZip2 compressed file: {str(e)}")
    else:
        print("Shape predictor file already exists. No need to download or extract.")

if __name__ == "__main__":
    download_and_extract_shape_predictor()
