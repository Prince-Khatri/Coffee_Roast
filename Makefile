fileName ?= model.py

clean:
	@echo "Checking unused code..."
	vulture $(fileName) || true

	@echo "Removing unused imports and variables..."
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports $(fileName)

	@echo "Formatting code..."
	black $(fileName)

	@echo "Generating requirements.py"
	pipreqs . --force
	@echo "Code cleaned and requirements.txt is created "
