import warnings

from dagster import (
    Definitions,
    ExperimentalWarning,
    FilesystemIOManager,
    load_assets_from_package_module,
)

from my_pipeline import asset

# Ignore "AutoMaterialization" ExperimentalWarning from Dagster
warnings.filterwarnings("ignore", category=ExperimentalWarning)


resources = {
    "io_manager": FilesystemIOManager(base_dir="/opt/dagster/io_manager_storage"),
}

defs = Definitions(
    assets=load_assets_from_package_module(asset),
    jobs=[],
    resources=resources,
)