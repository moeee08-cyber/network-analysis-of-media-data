import pandas as pd
import requests
import os
import zipfile
from urllib.parse import urlparse

def download_and_unzip_files(excel_path, target_dir):
    """
    Download zip files from links in Excel and extract them directly to target directory.
    
    :param excel_path: Path to the Excel file with download links
    :param target_dir: Directory to extract files
    """
    # Create directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Read the Excel file
    df = pd.read_excel(excel_path, header=None)
    
    # Get the first column (assuming links are in the first column)
    links = df.iloc[:, 0]

    
    # Download and extract each link
    for index, link in enumerate(links):
        try:
            # Validate link
            if not isinstance(link, str):
                print(f"Skipping invalid link at row {index}")
                continue
            
            # Send GET request
            response = requests.get(link, stream=True)
            response.raise_for_status()
            
            # Create temporary zip file
            temp_zip = os.path.join(target_dir, f'temp_{index}.zip')
            
            # Save the zip file
            with open(temp_zip, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            
            # Extract the zip file directly to target directory
            with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
                zip_ref.extractall(target_dir)
            
            # Remove temporary zip file
            os.remove(temp_zip)
            
            print(f"Successfully downloaded and extracted file from link {index + 1}")
            
        except requests.RequestException as e:
            print(f"Error downloading link {link}: {e}")
        except zipfile.BadZipFile:
            print(f"Error: Invalid zip file from link {link}")
            # Clean up temp file if it exists
            if os.path.exists(temp_zip):
                os.remove(temp_zip)

# Example usage
if __name__ == '__main__':
    excel_file_path = '/Users/wumengmeng/Desktop/project-MediaAgenda/two-mode/step1testcode/testlink.xlsx'
    target_directory = '/Users/wumengmeng/Desktop/project-MediaAgenda/two-mode/step1testcode'
    
    download_and_unzip_files(excel_file_path, target_directory)
