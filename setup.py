from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='google_spell_checker',
    version='0.1.0',
    description='Google Spell Checker',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/cahya-wirawan/google-spell-checker',
    author='Cahya Wirawan',
    author_email='cahya.wirawan@gmail.com',
    license='MIT',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
    ],
)
