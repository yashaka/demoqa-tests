from pathlib import Path

import resources


def to_resource(relative_path):
    return str(Path(resources.__file__).parent.joinpath(relative_path).absolute())
