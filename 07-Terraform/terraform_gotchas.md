# Terraform Gotchas

This document covers common pitfalls and gotchas when using Terraform.

## State Management
- Always back up your state files.
- Use remote state storage for collaboration.

## Resource Naming
- Be consistent with resource naming conventions.
- Avoid using dynamic names that can change frequently.

## Plan and Apply
- Always run `terraform plan` before `terraform apply`.
- Review the plan output carefully to understand the changes.
