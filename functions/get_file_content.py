import os

def get_file_content(working_directory, directory):
    try:
        # Normalize working directory and target directory
        working_directory = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, directory))

        # Ensure target is within working_directory
        if not target_path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Ensure target is actually a directory
        if not os.path.isfile(target_path):
            return f'Error: "{directory}" is not a directory'
        
        MAX_CHARS = 10000

        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            return file_content_string

    except Exception as e:
        # Catch any error and return it as a string with "Error:" prefix
        return f"Error: {str(e)}"
