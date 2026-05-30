# Prometheus Basics

This document covers the basics of Prometheus.

## Introduction
Prometheus is an open-source systems monitoring and alerting toolkit.

## Installation
- Follow the official Prometheus installation guide for your operating system.

## Basic Concepts
- **Metrics**: Data points collected by Prometheus.
- **Targets**: Endpoints that Prometheus scrapes metrics from.
- **Alerts**: Notifications based on metric conditions.
- **Exporters**: Tools that expose metrics to Prometheus.

## Basic Commands
- `prometheus --config.file=prometheus.yml`: Start Prometheus with a specific configuration file.
- `promtool check config prometheus.yml`: Check the syntax of a Prometheus configuration file.
