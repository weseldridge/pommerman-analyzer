import sys
import setuptools

CURRENT_PYTHON = sys.version_info[:2]
MIN_PYTHON = (3, 6)

if CURRENT_PYTHON < MIN_PYTHON:
    sys.stderr.write("""
        ============================
        Unsupported Python Version
        ============================
        
        Python {}.{} is unsupported. Please use a version newer than Python {}.{}.
    """.format(*CURRENT_PYTHON, *MIN_PYTHON))
    sys.exit(1)

with open('requirements.txt', 'r') as f:
    install_requires = f.readlines()

with open('VERSION') as f:
    VERSION = f.read().strip()

setuptools.setup(name='pommerman-analyzer',
      version=VERSION,
      description="A set of tools to help analyze pommerman game data.",
      author='Rebellious Labs',
      author_email='wes@rebelliouslabs.com',
      license='Apache 2.0',
      classifiers=[
          'Programming Language :: Python :: 3.6',
      ],
      packages=setuptools.find_packages(),
      install_requires=install_requires,
       entry_points={
        'console_scripts': [
        ],
      },
      zip_safe=False)