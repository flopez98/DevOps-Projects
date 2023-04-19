locals {
  execute_command = "chmod +x {{ .Path }}; {{ .Vars }} sudo -E '{{ .Path }}'"
}