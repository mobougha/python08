import sys
import os
import sysconfig


def check_virtual_environment() -> None:
    """
    Checks if the python script is running inside a virtual environment.
    Prints different instructions based on Matrix theme.
    """
    is_venv = (sys.prefix != sys.base_prefix or
               os.environ.get("VIRTUAL_ENV") is not None)

    if is_venv:
        venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
        venv_name = os.path.basename(venv_path)

        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()

        pkg_path = sysconfig.get_path('purelib')
        print("Package installation path:")
        print(pkg_path)
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


def main() -> None:
    try:
        check_virtual_environment()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
