import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riden-NSC",  # Replace with your own username
    version="0.0.1",
    author="Nate Costello",
    author_email="natecostello@gmail.com",
    description="A package that collects information from a RD60XX power supply",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/natecostello/riden_status",
    project_urls={
        "Bug Tracker": "https://github.com/natecostello/riden_status/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['riden-status'],
    python_requires=">=3.6",
    install_requires=["pyserial>=3.0", "minimalmodbus", "rd6006 @ git+https://github.com/natecostello/rd6006.git"]
)

# For specifying the rd6006 libray,
# Using this: https://stackoverflow.com/questions/32688688/how-to-write-setup-py-to-include-a-git-repository-as-a-dependency/54794506#54794506
