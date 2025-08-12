import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        # Normalize working directory and target directory
        working_directory = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, directory))

        # Ensure target is within working_directory
        if not target_path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Ensure target is actually a directory
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'
        
    
        # Build output lines
        output_lines = [f'Result for {directory or "current directory"}:']
        for entry in os.scandir(target_path):
            file_size = entry.stat().st_size
            is_dir = entry.is_dir()
            output_lines.append(
                f' - {entry.name}: file_size={file_size} bytes, is_dir={is_dir}'
            )

        return "\n".join(output_lines)

    except Exception as e:
        # Catch any error and return it as a string with "Error:" prefix
        return f"Error: {str(e)}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

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

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)
