from setuptools import setup

setup(name='pybank',
      version='0.33',
      
      description='Core Banking Simulator',
      long_description=open('README.rst').read(),
      
      classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: OS Independent',
        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        
        'Topic :: Communications',
        'Intended Audience :: Developers',
      ],
      
      keywords='Core banking financial',
      
      url='https://github.com/timgabets/pybank',
      author='Tim Gabets',
      author_email='tim@gabets.ru',
      
      license='LGPLv2',
      packages=['pybank'],
      install_requires=['tracetools', 'pynblock', 'bpc8583'],
      zip_safe=True)