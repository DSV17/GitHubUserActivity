from setuptools import setup

setup(
    name='github-activity',
    version='0.1',
    py_modules=['gitHub_user_activity'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'github-activity=gitHub_user_activity:main',
        ],
    },
)