import os
import pickle

CACHE_DIR = "cache"


def get_cache_path(repo_name):

    safe_name = repo_name.replace("/", "_")

    return os.path.join(
        CACHE_DIR,
        f"{safe_name}.pkl"
    )


def save_cache(repo_name, data):

    os.makedirs(
        CACHE_DIR,
        exist_ok=True
    )

    path = get_cache_path(repo_name)

    with open(path, "wb") as f:
        pickle.dump(data, f)


def load_cache(repo_name):

    path = get_cache_path(repo_name)

    if not os.path.exists(path):
        return None

    with open(path, "rb") as f:
        return pickle.load(f)