from datetime import datetime


def base_model(path):
    return {
        "name": path.rsplit('/', 1)[-1],
        "path": path,
        "writable": True,
        "last_modified": None,
        "created": None,
        "content": None,
        "format": None,
        "mimetype": None,
    }


def base_directory_model(path):
    m = base_model(path)
    m.update(
        type='directory',
        last_modified=datetime.fromtimestamp(0),
        created=datetime.fromtimestamp(0),
    )
    return m