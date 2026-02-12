import zipfile
import os

def zip_files(output_filename, source_files):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in source_files:
            if os.path.isfile(item):
                print(f"Zipping file: {item}")
                zipf.write(item)
            elif os.path.isdir(item):
                print(f"Zipping directory: {item}")
                for root, dirs, files in os.walk(item):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start='.')
                        zipf.write(file_path, arcname)

if __name__ == "__main__":
    files_to_zip = ['app.py', 'utils.py', 'assets']
    output_zip = 'projeto_base.zip'
    
    # Remove existing if any
    if os.path.exists(output_zip):
        os.remove(output_zip)
        
    zip_files(output_zip, files_to_zip)
    print(f"Backup created successfully: {os.path.abspath(output_zip)}")
