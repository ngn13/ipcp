from setuptools import setup, find_packages

VERSION = "0.0.2" 
DESCRIPTION = "Simple CLI that lets you copy a specified interface's IP address"

setup(
        name="ipcp", 
        version=VERSION,
        author="ngn13",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=["pyperclip"], 
        entry_points={'console_scripts': ['ipcp=ipcp.__init__:main']}
)
