from setuptools import setup, find_packages

setup(
    name='spotify-recommender',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/JachymPutta/spotify-recs',
    license='MIT',
    author='Jachym Putta',
    author_email='jachym.putta@yale.edu',
    description='A recommendation algorithm for Spotify',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'spotipy',
        # add other dependencies
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
