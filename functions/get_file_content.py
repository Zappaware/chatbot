import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        # Normalize working directory and target directory
        working_directory = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target is within working_directory
        if not target_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Ensure target is actually a directory
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'


        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            return file_content_string

    except Exception as e:
        # Catch any error and return it as a string with "Error:" prefix
        return f"Error: {str(e)}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to retrieve content from, relative to the working directory.",
            ),
        },
    ),
)
