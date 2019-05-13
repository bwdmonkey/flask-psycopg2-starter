SHELL=./make-venv

all: ls

# List all commands
.PHONY: ls
ls:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs


### install: installs dependencies under
.PHONY: install
install:
	python3 -m venv venv
	pip install --upgrade pip
	make post-install

.PHONY: post-install
post-install:
	pip3 install -r requirements.txt

.PHONY: clean
clean:
	rm -rf venv
