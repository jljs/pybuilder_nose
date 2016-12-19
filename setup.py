from setuptools import setup, find_packages

setup(
    name="pybuilder_nose",
    packages=['pybuilder_nose'],
    version="0.0.5",
    description="A call stack profiler for Python. Inspired by Apple's Instruments.app",
    author='Alex Dow',
    url='https://github.com/jljs/pybuilder_nose',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Testing',
    ]
)
