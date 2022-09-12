import os
import re

import checksumdir
import pytest
from binaryornot.check import is_binary

try:
    import sh
except (ImportError, ModuleNotFoundError):
    sh = None  # sh doesn't support Windows

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
        "project_name": "Doge Hello World",
        "project_slug": "doge-hello-world",
        "author_name": "Martí Bosch",
        "gh_username": "martibosch",
        "description": "Example 'Hello, World!' app using the Doge workflow",
        "tfc_org_name": "exaf-epfl",
        "droplet_image": "ubuntu-22-04-x64",
        "droplet_user": "ubuntu",
        "droplet_region": "fra1",
        "droplet_size_stage": "s-1vcpu-1gb",
        "droplet_size_prod": "s-2vcpu-4gb",
        "docker_compose_version": "2.10.2",
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path):
            match = RE_OBJ.search(line)
            assert match is None, f"cookiecutter var not replaced in {path}"


def test_project_generation(cookies, context):
    """Test that project is generated and fully rendered."""

    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_slug"]
    assert result.project_path.is_dir()

    project_path = str(result.project_path)
    paths = build_files_list(project_path)
    assert paths
    check_paths(paths)

    try:
        sh.git("init", _cwd=project_path)
        sh.pre_commit("install", _cwd=project_path)
        # test that pre-commit does not change any file
        hash = checksumdir.dirhash(project_path)
        sh.pre_commit("run", "--all-files", _cwd=project_path)
        assert hash == checksumdir.dirhash(project_path)
    except sh.ErrorReturnCode as e:
        pytest.fail(e.stdout.decode())
