SHELL := /bin/bash

install: install_conf
	@echo "[-] Installing system76-backlight-manager"
	sudo python3 setup.py install
	@echo "[-] Installing system76-backlight-manager.service Service"
	sudo install -m644 service/system76-backlight-manager.service /etc/systemd/system/
	sudo systemctl daemon-reload

install_conf:
	if [[ ! -f /etc/system76-backlight-manager.conf ]]; \
	then \
		sudo cp configs/system76-backlight-manager.conf /etc/; \
	fi

update_config:
	sudo cp configs/battery-backlight.conf /etc/

install_ci:
	pip install -r requirements.dev.txt

install_dev: venv 
	.venv/bin/pip install -r requirements.dev.txt
	make install_hook

venv:
	if [[ ! -d .venv/ ]]; \
	then \
		python3 -m venv .venv; \
	fi

install_hook:
	pre-commit install

unit_test:
	py.test --cov=system76_backlight_manager system76_backlight_manager/tests/unit
