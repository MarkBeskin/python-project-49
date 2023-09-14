install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	poetry run python3 -m pip install dist/*.whl

# тут у меня появилась проблема с pip - при применении команды выходила ошибка
# error: externally-managed-environment
# решением стало сменить pip на pipx 
#ubuntu-package-install:
#	python3 -m pipx install dist/*.whl

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc
