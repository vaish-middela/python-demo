import yaml
import os
import sys
from pathlib import Path


# --------------------------------------------------------------------------
# --- Core Function to Load Configuration ---
# --------------------------------------------------------------------------
def load_config(file_path):
    """Load a YAML config file safely into a Python dictionary."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"ERROR: Configuration file not found at: {file_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"ERROR: Invalid YAML in config file: {e}")
        sys.exit(1)


# --------------------------------------------------------------------------
# --- Main Logic of the Script ---
# --------------------------------------------------------------------------
def main():
    # 1. Determine the path to the config file
    # __file__ is inside src/, so go up one level to project root
    # Project root is always the parent of src/
    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "configs" / "settings.yaml"

    print(f"DEBUG: Config path = {config_path}")

    # 2. Load the configuration
    settings = load_config(config_path)

    print("\n--- Application Settings Loaded ---")

    # 3. Access values using dictionary keys
    app_name = settings["app"]["name"]
    app_version = settings["app"]["version"]
    log_level = settings["app"]["log_level"]
    db_host = settings["database"]["host"]
    db_port = settings["database"]["port"]
    output_dir = settings["paths"]["output_directory"]

    # 4. Display loaded settings
    print(f"App Name:        {app_name} (Version {app_version})")
    print(f"Database Target: {db_host}:{db_port}")
    print(f"Log Level:       {log_level}")
    print(f"Output Path:     {output_dir}")
    print("-----------------------------------")

    # 5. Example logical check
    if log_level.upper() == "DEBUG":
        print("\nNote: DEBUG mode is active. Be careful with YAML indentation!")


# --------------------------------------------------------------------------
# --- Entry Point ---
# --------------------------------------------------------------------------
if __name__ == "__main__":
    main()
