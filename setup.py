import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="noise_img_generator",
    version="1.0.5",
    author="Benjamin Slater",
    author_email="benjamin.ed.slater@gmail.com",
    description="CLI to generate noise images for use in game design",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slaterb1/noise_img_generator",
    project_urls={
        "Bug Tracker": "https://github.com/slaterb1/noise_img_generator/issues",
        "Source": "https://github.com/slaterb1/noise_img_generator"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "numpy",
        "pypng"
    ],
    python_requires=">=3.6",
    entry_points='''
            [console_scripts]
            noise_img_generator=noise_img_generator.__main__:cli
        '''
)
