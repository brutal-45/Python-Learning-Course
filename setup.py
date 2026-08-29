"""
Setup script for Python Learning Repository
============================================

This is a demonstration setup.py file showing how to package the repository.
For actual installation, run:
    pip install -e .

Usage:
    python setup.py sdist bdist_wheel  # Build distribution packages
    pip install .                      # Install as a package
    pip install -e .                   # Install in editable mode
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = (
    readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
)

setup(
    name="python-learning-repo",
    version="1.0.0",
    author="Python Learning Community",
    author_email="python-learning@example.com",
    description="A comprehensive guide to master Python programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-learning-repo",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/python-learning-repo/issues",
        "Documentation": "https://github.com/yourusername/python-learning-repo#readme",
        "Source Code": "https://github.com/yourusername/python-learning-repo",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords=["python", "learning", "tutorial", "education", "programming"],
    packages=find_packages(exclude=["tests*", "examples*"]),
    python_requires=">=3.9",
    install_requires=[
        # Core dependencies (minimal for learning materials)
    ],
    extras_require={
        "dev": [
            "flake8>=6.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
        "projects": [
            "requests>=2.31.0",
            "beautifulsoup4>=4.12.0",
            "pandas>=2.0.0",
            "numpy>=1.24.0",
        ],
        "all": [
            "flake8>=6.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "requests>=2.31.0",
            "beautifulsoup4>=4.12.0",
            "pandas>=2.0.0",
            "numpy>=1.24.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "python-learn=quick_start:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.py"],
    },
)
