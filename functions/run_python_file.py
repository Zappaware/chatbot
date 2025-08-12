import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        # Normalize working directory and target directory
        working_directory = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target is within working_directory
        if not target_path.startswith(working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Ensure target exists and is a file
        if not os.path.isfile(target_path):
            return f'Error: File "{file_path}" not found or is not a regular file.'

        # Ensure file ends in .py extension
        if not target_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        
        cmd = ['python3', target_path]
        if args:
            cmd.extend(args)
        try:
            completed = subprocess.run(
                cmd,
                cwd=working_directory,
                capture_output=True,
                text=True,
                timeout=30
            )
            output = []
            if completed.stdout:
                output.append(f"STDOUT:\n{completed.stdout}")
            if completed.stderr:
                output.append(f"STDERR:\n{completed.stderr}")
            if completed.returncode != 0:
                output.append(f"Process exited with code {completed.returncode}")
            if not output:
                return "No output produced."
            return "\n".join(output)
        except Exception as e:
            return f"Error: executing Python file: {e}"
    except Exception as e:
        return f"Error: executing Python file: {e}"

        