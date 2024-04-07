from setuptools import setup, find_packages

setup(
    name="flaskfy",
    author="Álvaro Mbeia Daniel Miguel",
    author_email="alvarombeiadanielmiguel@gmail.com",
    description="This is a lib to help generate flask apps with custom components",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "pymysql",
        "flask",
    ],
    entry_points = {
        "console_scripts": [
            "createflaskapp = flaskfy:criar_projeto_flask"
        ]
    }
)