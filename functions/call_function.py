import os

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.arguments

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    

    