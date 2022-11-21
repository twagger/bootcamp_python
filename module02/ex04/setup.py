"""Setup script"""


from setuptools import setup

setup(
    name = 'my_minipack',
    version = '1.0.0',
    summary = 'How to create a package in python.',
    home_page = None,
    author = 'twagner',
    author_email = 'twagner@student.42.fr',
    license = 'GPLv3',
    location = '~/goinfre/miniconda3/envs/test_env/lib/python3.7/site-packages',
    metadata_version = '2.1',
    installer = 'pip',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: HowTo',
        'Topic :: Package',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
