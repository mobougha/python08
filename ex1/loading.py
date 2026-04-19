import sys
import importlib.util


def check_dependency(module_name: str, display_name: str, task: str) -> bool:
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        return False

    try:
        mod = importlib.import_module(module_name)
        version = getattr(mod, "__version__", "unknown")
        print(f"[OK] {display_name} ({version}) - {task}")
        return True
    except Exception:
        return False


def perform_data_analysis() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    deps_status = []
    deps_status.append(
        check_dependency("pandas", "pandas", "Data manipulation ready")
    )
    deps_status.append(
        check_dependency("numpy", "numpy", "Numerical computation ready")
    )
    deps_status.append(
        check_dependency("requests", "requests", "Network access ready")
    )
    deps_status.append(
        check_dependency("matplotlib", "matplotlib", "Visualization ready")
    )

    if not all(deps_status):
        print("\n[ERROR] Missing dependencies detected!")
        print("\n--- Dependency Management Differences ---")
        print("Pip uses a flat requirements.txt file and installs packages "
              "into your current active Python environment.")
        print("Poetry uses pyproject.toml, automatically manages its own "
              "isolated virtual environments, and cleanly resolves "
              "dependency trees.")
        print("\nInstallation instructions:")
        print("For pip:")
        print("  pip install -r requirements.txt")
        print("For Poetry:")
        print("  poetry install")
        sys.exit(1)

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import requests

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    try:
        req = requests.get("https://api.github.com", timeout=3)
        _ = req.status_code
    except Exception:
        pass

    data = np.random.randn(1000, 2)
    df = pd.DataFrame(data, columns=["Signal", "Noise"])
    df["Matrix_Score"] = df["Signal"] * df["Noise"]

    x = np.arange(1000)
    y = df["Matrix_Score"]
    plt.plot(x, y)

    print("Generating visualization...\n")

    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    perform_data_analysis()


if __name__ == "__main__":
    main()
