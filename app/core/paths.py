import os

local_path = os.path.dirname(os.path.dirname(__file__))
base_path = os.path.dirname(local_path)


def setup_path(file_path: str, root: bool = False) -> str:
    if root:
        return os.path.join(base_path, file_path)
    return os.path.join(local_path, file_path)


__all__ = ["setup_path"]
