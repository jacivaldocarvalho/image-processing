from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
    ],
    description='Pacote para processamento básico de imagens.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jacivaldocarvalho/image-processing', 
    author='Jacivaldo Carvalho',
    author_email='jacivaldocarvalho@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
