import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

requires = [i.strip() for i in open('requirements.txt').readlines()]

setuptools.setup(
    name='zoopy',
    version='1.0.0',
    description='Python Library to ZOOP.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andersonqueiroz/zoopy',
    author='Anderson Queiroz, Franklin Dias',
    author_email='anderson@emai.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)