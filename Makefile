SHELL := /bin/bash
UV := /Users/graphplaying/.local/bin/uv

install:
	$(UV) sync

brain-games:
	$(UV) run brain-games

build:
	$(UV) build

package-install:
	$(UV) tool install dist/hexlet_code-0.1.0-py3-none-any.whl

# было "make lint:" — это неверное имя цели
lint:
	$(UV) run ruff check brain_games

brain-even:
	$(UV) run brain-even

brain-calc:
	$(UV) run brain-calc

brain-gcd:
	$(UV) run brain-gcd

brain-progression:
	$(UV) run brain-progression