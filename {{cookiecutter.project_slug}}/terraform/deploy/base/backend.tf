terraform {
  cloud {
    organization = "{{ cookiecutter.tfc_org_name }}"
    workspaces {
      name = "{{ cookiecutter.project_slug }}-base"
    }
  }
}
