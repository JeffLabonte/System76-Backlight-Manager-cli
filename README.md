# System76-Backlight-Manager-cli

[![codecov](https://codecov.io/gh/JeffLabonte/System76-Backlight-Manager-cli/branch/main/graph/badge.svg?token=O2RPF973FR)](https://codecov.io/gh/JeffLabonte/System76-Backlight-Manager-cli)

[![CI](https://github.com/JeffLabonte/System76-Backlight-Manager-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/JeffLabonte/System76-Backlight-Manager-cli/actions/workflows/ci.yml)

A python script to manage your keyboard backlight on your S76 laptop.

## To setup the development environment and run the software

make install-dev
source .venv/bin/activate
python system76_backlight_manager

## To install the software

make install
sudo systemctl start system76-backlight-manager.service
