# setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

AUTHOR_USERNAME = "shreeharsh-ms"
SRC_REPO = f"TextSummarization-AWS-DOCKER-GITHUBACTIONS"

setuptools.setup(
    name="TextSummarization-AWS-DOCKER-GITHUBACTIONS",
    version="0.0.1",
    author="Shreeharsh manoj shivpuje",
    author_email="info.shreeharshshivpuje@gmail.com",
    description="Text Summarization using AWS, Docker, and GitHub Actions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(where="src"),
)