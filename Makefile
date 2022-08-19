PY_ENV = venv
PY_BIN = $(PY_ENV)/bin

all: build


$(PY_BIN)/python:
	python -m venv $(PY_ENV)
	chmod +x $(PY_BIN)/activate
	./$(PY_BIN)/activate


$(PY_BIN)/html2image: $(PY_BIN)/python
	$(PY_BIN)/pip3 install html2image


build: $(PY_BIN)/html2image
	$(VBIN)/python build.py

clean:
	rm -rf */__pycache__
	rm -rf index.html
	rm -rf img


fclean: clean
	rm -rf $(PY_ENV)


.PHONY: build clean fclean
