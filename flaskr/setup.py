#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:26:49 2017

@author: caowenhong
"""

from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
