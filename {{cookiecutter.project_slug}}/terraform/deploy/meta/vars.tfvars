tfc_org_name           = "{{ cookiecutter.tfc_org_name }}"
project_slug           = "{{ cookiecutter.project_slug }}"
ssh_key_name           = "{{ cookiecutter.project_slug }}"
docker_compose_version = "{{ cookiecutter.docker_compose_version }}"
gh_repo_name           = "{{ cookiecutter.project_slug }}"
droplet_user           = "{{ cookiecutter.droplet_user }}"
droplet_prefix         = "{{ cookiecutter.project_slug }}"
droplet_image          = "{{ cookiecutter.droplet_image }}"
droplet_region         = "{{ cookiecutter.droplet_region }}"
droplet_size_stage     = "{{ cookiecutter.droplet_size_stage }}"
droplet_size_prod      = "{{ cookiecutter.droplet_size_prod }}"
do_project_name        = "{{ cookiecutter.project_slug }}"
do_project_description = "{{ cookiecutter.description | escape}}"

# tokens
do_token     = ""
gh_token     = ""
tf_api_token = ""
