from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='spotify-refresh-token-generator',
    version='0.0.8',
    author='Aaron Mamparo',
    author_email='aaronmamparo@gmail.com',
    description='A command-line utility to generate a long-term refresh token for the Spotify API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/amamparo/spotify-refresh-token-generator',
    package_dir={
        '': 'src'
    },
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'generate-spotify-refresh-token = spotify_refresh_token_generator.__main__:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>= 3.7'
)
