from setuptools import setup, find_packages

packages = find_packages()

setup(
    name='PyscesToolbox',
    version='0.8.0',
    packages=packages,
    url='https://github.com/PySCeS/PyscesToolbox',
    license='',
    author='Carl Christensen',
    author_email='carldc@sun.ac.za',
    description='A set of metabolic model analysis tools for PySCeS.',
    install_requires=['IPython>=3.0.0,<4.0.0',
                      'numpy',
                      'sympy',
                      'pysces',
                      'matplotlib',
                      'd3networkx_psctb',
                      'numpydoc'],
     dependency_links=['git+ssh://github.com/exe0cdc/ipython-d3networkx.git#egg=d3networkx_psctb-0.1'],
)
