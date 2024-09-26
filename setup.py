from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='image_processor_jr',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9.5',
    description='Pacote para processamento de imagens.',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jacivaldocarvalho/image-processing', 
    author='Jacivaldo Carvalho',
    author_email='jacivaldocarvalho@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
