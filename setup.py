from pathlib import Path

from setuptools import setup

# loading packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

style_packages = ["black==23.1.0", "flake8==6.0.0", "isort==5.12.0"]

test_packages = ["pytest==7.2.2", "pytest-cov==4.0.0", "great-expectations==0.16.1"]

setup(
    name="gpt_summarizer",
    version=0.1,
    description="summarizing documents using OPEN AI GPT model",
    author="Bohdan Ivaniuk-Skulskyi",
    author_email="ivanyuk.bogdan1999@gmail.com",
    url="",
    python_requires=">=3.8",
    install_requires=[required_packages],
    extras_require={
        "dev": style_packages + test_packages + ["pre-commit==3.2.0"],
        "test": test_packages,
    },
)
