terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "1.7.5"
    }
  }
}

variable "api_key" {
  type = string
}

variable "owner_id" {
  type = string
}

variable "environment" {
  type = string
}

provider "render" {
  api_key = var.api_key
  owner_id = var.owner_id
}

resource "render_project" "api-python-flask" {
  name = "api-python-flask"
  environments = {
    "production" = {
      name = "production"
      protected_status = "unprotected"
    },
    "development" = {
      name = "development"
      protected_status = "unprotected"
    }
  }
}

resource "render_web_service" "api-python-flask-app" {
  name = "api-iscod"
  plan = "starter"
  region = "frankfurt"
  environment_id = render_project.api-python-flask.environments[var.environment].id
  runtime_source = {
    image = {
      image_url = "ghcr.io/quentindubos80270/api-python-flask/api-iscod"
      tag = "latest"
    }
  }
}