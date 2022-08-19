VENV = venv
VBIN = $(VENV)/bin

all: build


$(VBIN)/python:
	python -m venv $(VENV)
	chmod +x $(VBIN)/activate
	./$(VBIN)/activate


$(VBIN)/html2image: $(VBIN)/python
	$(VBIN)/pip3 install html2image


build: $(VBIN)/html2image
	$(VBIN)/python build.py

clean:
	rm -rf */__pycache__
	rm -rf index.html
	rm -rf img


fclean: clean
	rm -rf $(VENV)


.PHONY: build clean fclean
