terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "~> 1.0"
    }
  }
}

provider "render" {
  api_key = var.render_api_key
}

variable "render_api_key" {
  type      = string
  sensitive = true
}

resource "render_web_service" "flask_api" {
  name   = "api-python-flask"
  region = "frankfurt"

  # Image Docker depuis GHCR
  image = {
    url = "ghcr.io/quentindubos80270/api-python-flask:latest"
  }

  plan = "free"

  env_vars = [
    {
      key   = "ENV"
      value = "production"
    }
  ]

  health_check_path = "/health"

  start_command = "python app.py"
}