from setuptools import setup


def get_requirements():
    with open("requirements.txt", "r") as f:
        return f.read().split("\n")


setup(
    name="system76-backlight-manager",
    version="0.1",
    description="Control the backlight of your System76 laptop",
    url="https://github.com/JeffLabonte/System76-Backlight-Manager-cli",
    author="Jean-François Labonté",
    author_email="grimsleepless@protonmail.com",
    include_package_data=True,
    install_requires=get_requirements(),
    license="GPLv3",
    packages=["system76_backlight_manager", "system76_backlight_manager.schema"],
    entry_points={"console_scripts": ["system76-backlight-manager=system76_backlight_manager.__main__:main"]},
)
