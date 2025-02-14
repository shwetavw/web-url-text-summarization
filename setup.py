from setuptools import setup, find_packages

setup(
    name="web-url-text-summarization",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        "validators"
    ],
    entry_points={
        "console_scripts": [
            # Add command line scripts here
        ],
    },
    author="shweta",
    author_email="your.email@example.com",
    description="A project for summarizing content from web page",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shwetavw/web-url-text-summarization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)