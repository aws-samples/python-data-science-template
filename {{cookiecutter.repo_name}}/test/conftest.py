from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def root_dir(request):
    return Path(request.config.rootdir)


class Helpers:
    @staticmethod
    def import_from_file(name, fname):
        import importlib.util

        spec = importlib.util.spec_from_file_location(name, fname)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod


@pytest.fixture
def helpers():
    return Helpers
