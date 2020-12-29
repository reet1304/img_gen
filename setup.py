from setuptools import setup, find_packages

setup(
    name='img_gen',
    version='0.0.10',
    install_requires=[
          'pillow',
    ],
    packages=find_packages(),
    scripts=[
        'img_gen_preshow'
    ],
    package_data={'img_gen': ['arial.ttf']},

)