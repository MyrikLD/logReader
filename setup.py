from setuptools import setup

setup(name='logReader',
      version='0.1',
      description='PyQt5 programm for parse and reading any log file.',
      url='https://github.com/MyrikLD/logReader',
      author='MyrikLD',
      author_email='myrik260138@tut.by',
      license='GPLv3',
      packages=['logReader'],
      install_requires=['python-dateutil'],
      entry_points={'console_scripts': ['logreader = logReader.main:main']},
      classifiers=['Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Utilities'],
      # package_data={'logReader': ['default.yaml', 'ui.ui', 'about.ui']},
      include_package_data=True,
      zip_safe=False)