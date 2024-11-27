import os
import shutil

# Define file types and their corresponding folders
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.csv', '.xlsx', '.pptx'],
    'Media': ['.mp4', '.mp3', '.avi', '.mov', '.wav'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
}

def organize_files(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Error: The directory {directory} does not exist.")
        return

    # Get a list of files in the directory
    files = os.listdir(directory)

    # Iterate over all files in the directory
    for file in files:
        file_path = os.path.join(directory, file)

        # Skip directories, we only want to process files
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()

        # Determine the correct folder based on file type
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                folder_path = os.path.join(directory, folder)

                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file to the appropriate folder
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved {file} to {folder}/")
                moved = True
                break

        # If no match is found, move the file to "Others"
        if not moved:
            others_folder = os.path.join(directory, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, file))
            print(f"Moved {file} to Others/")

# Main function to call organize_files
def main():
    # Ask user for the directory to organize
    directory = input("Enter the directory path to organize: ")

    # Call the file organization function
    organize_files(directory)

if __name__ == '__main__':
    main()
