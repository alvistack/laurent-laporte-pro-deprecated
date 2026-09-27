from setuptools import setup

setup(
    name='deprecated',
    version='3.0.0',
    description='Python @deprecated decorator to deprecate old python classes, functions or methods.',
    author_email='Laurent LAPORTE <laurent.laporte.pro@gmail.com>',
    maintainer_email='Laurent LAPORTE <laurent.laporte.pro@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    install_requires=[
        'wrapt<3,>=1.16',
    ],
    packages=[
        'deprecated',
    ],
    package_dir={'': 'src'},
)
