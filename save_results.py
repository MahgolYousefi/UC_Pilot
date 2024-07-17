import os
import datetime


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def save_results(data, file_prefix):
    folder_path = 'C:/HAT_Results'
    # Ensure the folder exists
    folder_path = ensure_folder_exists(folder_path)

    # Get current datetime to use as a filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{file_prefix}_{current_time}.txt"
    file_path = os.path.join(folder_path, filename)

    # Write data to the file
    with open(file_path, 'w') as file:
        file.write(data)

    return f"Results sent successfully."
