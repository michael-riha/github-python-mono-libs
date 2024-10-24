import lib1  # Replace 'lib1' with the actual name of the package

def main():
    print("Testing remote package from GitHub...")
    lib1.some_function()  # Assuming 'lib1' has a function called 'some_function'

if __name__ == "__main__":
    import debugpy
    debugpy.listen(("0.0.0.0", 5678))  # Set up remote debugger on port 5678
    print("Waiting for debugger to attach...")
    debugpy.wait_for_client()  # Pause execution until debugger is attached
    print("Debugger attached!")
    main()
