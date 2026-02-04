install:
	uv sync

VD-games:
	uv run vd-main

build:
	uv build

package-install:
	uv tool install dist/*.whl
