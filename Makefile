.PHONY: install clean

PYTHON = python3

install:
	pipenv install
	pipenv run pyinstaller --onefile converter.py
	pipenv run python3 setup.py
	mv Convert_Toolpath.workflow ~/Library/Services/

clean:
	rm -rf dist
	rm -rf build
	rm -f converter.spec
	rm -rf ~/Library/Services/Convert_Toolpath.workflow