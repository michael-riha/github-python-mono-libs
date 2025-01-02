
def main():
    print("Testing remote package from GitHub...")
    import lib1  # Replace 'lib1' with the actual name of the package
    lib1.some_function()  # Assuming 'lib1' has a function called 'some_function'

    from pkg_lib2.pkg1 import some_function
    # Now you can call the function directly
    some_function()

    import pkg_lib2.pkg1
    # Call the function using dot notation
    pkg_lib2.pkg1.some_function()
    remove_modules("pkg_lib2")
    # Import the module with an alias
    import pkg_lib2.pkg1 as pkg
    # Now you can use the alias to call the function
    pkg.some_function()
    remove_modules("pkg_lib2")

    import pkg_lib2.pkg1
    # Call the function using dot notation
    pkg_lib2.pkg1.some_function()

    import mynamespace.subpackage_a as sub_a
    print(sub_a.name)

    import mynamespace.subpackage_b as sub_b
    print(sub_b.name)


"""
Removes all modules with the given name prefix from the Python module cache.

This function is useful when you need to reload a module after making changes to it,
or when you want to ensure that a module is not cached in memory.

Args:
    module_name (str): The prefix of the module names to remove.

Returns:
    None
"""
def remove_modules(module_name: str):
    import sys
    # Store the names of modules to be deleted
    modules_to_delete = [name for name in sys.modules if name.startswith(module_name)]

    # Delete the modules
    for module_name in modules_to_delete:
        del sys.modules[module_name]
    
    # # reload after changes
    # import importlib
    # # After making changes to your_module
    # importlib.reload(module_name)

if __name__ == "__main__":
    import debugpy
    debugpy.listen(("0.0.0.0", 5678))  # Set up remote debugger on port 5678
    print("Waiting for debugger to attach...")
    debugpy.wait_for_client()  # Pause execution until debugger is attached
    print("Debugger attached!")
    main()
