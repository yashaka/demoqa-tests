def resource(relative_path):
    import demoqa_tests
    from pathlib import Path
    return (
        Path(demoqa_tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
