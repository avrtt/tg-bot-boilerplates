#!/usr/bin/env bash

set -e

poetry run alembic upgrade head
exec poetry run python -O -m template2
