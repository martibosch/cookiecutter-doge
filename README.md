# Cookiecutter Doge

[![ci](https://github.com/martibosch/cookiecutter-doge/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/martibosch/cookiecutter-doge/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-doge/badge/?version=latest)](https://cookiecutter-doge.readthedocs.io/en/latest/?badge=latest)
[![GitHub license](https://img.shields.io/github/license/martibosch/cookiecutter-doge.svg)](https://github.com/martibosch/cookiecutter-doge/blob/main/LICENSE)

Powered by [cookiecutter](https://github.com/cookiecutter/cookiecutter), cookiecutter-doge provides a template to generate Doge :dog2: projects. Doge (DOcker, Github, tErraform) is a GitOps workflow to ensure multi-environment continuous integration/deployment (CI/CD) for docker-compose applications using Github and Terraform. It has been mainly developed to deploy Django applications based on the [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) framework, but it can be extended to other docker-compose setups that require remote infrastructure. At present, the workflow only works on DigitalOcean, but it is easy to adapt it to other cloud providers.

See the [documentation](https://cookiecutter-doge.readthedocs.io), [example project](https://github.com/martibosch/doge-hello-world) with a "Hello, World!" app (using [FastAPI](https://fastapi.tiangolo.com/)) and [its corresponding user guide](https://github.com/martibosch/doge-hello-world/blob/main/README.md).

![such workflow](https://raw.githubusercontent.com/martibosch/cookiecutter-doge/main/doge.png "such workflow")

## Acknowledgments

- With the support of the École Polytechnique Fédérale de Lausanne (EPFL)
