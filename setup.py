import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpletweetlib", # Replace with your own username
    version="0.0.1",
    author="Ryota Miyoshi",
    author_email="m1yosh1.ry0t4@gmail.com",
    install_requires=["requests_oauthlib"],
    description="A quite simple and easy to use tweet library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miyoshi-Ryota/simpletweetlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
