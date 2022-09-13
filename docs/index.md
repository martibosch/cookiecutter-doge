# Welcome to cookiecutter-doge documentation

Powered by [cookiecutter](https://github.com/cookiecutter/cookiecutter), cookiecutter-doge provides a template to generate Doge projects. Doge (DOcker, Github, tErraform) is a GitOps workflow to continuously deploy multi-environment docker-compose applications using Github and Terraform. At present, the workflow only works on DigitalOcean, but it is easy to adapt it to other cloud providers.

## Project generation options

This page describes all the template options that will be prompted by the cookiecutter CLI prior to generating your project.

- **project_name**:
  Your project's human-readable name, capitals and spaces allowed.

- **project_slug**:
  Your project's slug without underscores or spaces. Used to name your repo and DigitalOcean resources.

- **author_name**:
  Your name. The value goes into places like `LICENSE` and such.

- **description**:
  Describes your project and gets used in places like `README.md` and such.

- **open_source_license**:
  A software license for the project. The choices are:

  - GPLv3
  - Apache Software License 2.0
  - BSD
  - MIT
  - Not open source

- **tfc_org_name**:
  Name of the Terraform Cloud organization.

- **droplet_image**:
  The droplet image slug (e.g., Linux distribution). The list of image slugs is available on the [DigitalOcean API documentation](https://docs.digitalocean.com/reference/api/api-reference/#tag/Images).

- **droplet_user**:
  The name of the (sudo) user created for the droplet which can access it via ssh.

- **droplet_region**:
  The slug that indentifies the data center region of droplet. The list of region slugs is available on the [DigitalOcean API documentation](https://docs.digitalocean.com/reference/api/api-reference/#tag/Regions).

- **droplet_size_stage**, **droplet_size_prod**:
  The slug that indentifies the size (amount of RAM, the number of virtual CPUs, disk space, and transfer) of the staging and production droplet respectively. The list of size slugs is available on the [DigitalOcean API documentation](https://docs.digitalocean.com/reference/api/api-reference/#tag/Sizes).

## User guide

Before starting, make sure that you have [cookiecutter installed in your system](https://cookiecutter.readthedocs.io/en/stable/installation.html). Then, use it to generate your project:

```bash
cookiecutter gh:martibosch/cookiecutter-doge
```

Then, go to the generated directory:

```bash
cd <what you have entered as the project_slug at setup stage>
```

and follow the steps outlined in the `README.MD` to get up and running following the Doge workflow.
