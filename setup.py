from setuptools import setup

setup(name='pyparak',
      version='0.0.1',
      description='A library which provides drivers for connecting to SHAPARAK gateways through single interface.',
      url='https://github.com/mrdaliri/pyparak',
      author='Mohammad-Reza Daliri',
      author_email='rmdaliri@gmail.com',
      license='MIT',
      packages=['pyparak'],
      install_requires=[
          'pay-ir',
      ],
      zip_safe=False)
