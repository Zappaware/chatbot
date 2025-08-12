import os

def get_files_info(working_directory, directory="."):
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
    
    
    

   

    
    