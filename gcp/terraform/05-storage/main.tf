resource "google_storage_bucket" "testnr-terraform-state" {
  name          = "testnr-terraform-state"
  location      = "${var.location}"
  force_destroy = true
}