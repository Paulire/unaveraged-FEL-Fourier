
# -*- coding: utf-8 -*-

"""
Created on Thu Nov 16 11:32 2021

Setup file for installation via pip

@author: paul.ireland.2017@uni.strath.ac.uk
"""

from setuptools import setup

setup(
      name='ufel_ft',
      version='0.1.0',    
      description='1D un-avaraged free electron laser model using Fourier analysis.',
      url='https://github.com/Paulire/unaveraged-FEL-Fourier/',
      author='Paul Ireland',
      author_email='paul.ireland.2017@uni.strath.ac.uk',
      license='N/A',
      packages=['ufel_ft'],
      install_requires=['scipy',
                        'numpy',                     
                        'matplotlib',
                        'tqdm'
                        ],

      classifiers=[
          'Development Status :: Work In Progress',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: N/A',  
          'Operating System :: POSIX :: Linux',        
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
    ],
)
