.PHONY: install clean

PYTHON = python3

install:
	pipenv install
	pipenv run pyinstaller --onefile converter.py
	pipenv run python3 setup.py
	cp -r Convert_Toolpath.workflow ~/Library/Services/
	cp -r Save_Convert_Toolpath.workflow ~/Library/Services/
	mkdir ~/Toolpaths

clean:
	rm -rf dist
	rm -rf build
	rm -f converter.spec
	rm -rf ~/Library/Services/Convert_Toolpath.workflow
	rm -rf ~/Library/Services/Save_Convert_Toolpath.workflow
	rm -rf Toolpaths