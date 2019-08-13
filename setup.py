import setuptools
import importlib

# Avoid native import statements as we don't want to depend on the package being created yet.
def load_module(module_name, full_path):
    spec = importlib.util.spec_from_file_location(module_name, full_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

version = load_module("autoleagueplay.version", "autoleagueplay/version.py")
paths = load_module("autoleagueplay.paths", "autoleagueplay/paths.py")

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setuptools.setup(
    name='autoleagueplay',
    packages=setuptools.find_packages(),
    install_requires=[
        'dataclasses',
        'rlbot',
        'rlbottraining>=0.3.0',
        'docopt',
        'requests',
        'watchdog',
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
    ],
    python_requires='>=3.7.0',
    version=version.__version__,
    description='An automatic runner for RLBot league play.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Eastvillage, DomNomNom, and the RLBot Community',
    author_email='rlbotofficial@gmail.com',
    url='https://github.com/NicEastvillage/AutoLeague',
    keywords=['rocket-league', 'league-play'],
    license='MIT License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        # Allow people to run `autoleagueplay` instead of `python -m autoleagueplay`
        'console_scripts': ['autoleagueplay = autoleagueplay.__main__:main']
    },
    package_data={
        'autoleagueplay': [
            'autoleagueplay/default_match_config.cfg',
            'autoleagueplay/psyonix_allstar.cfg',
            'autoleagueplay/psyonix_pro.cfg',
            'autoleagueplay/psyonix_rookie.cfg'
        ]
    },
    include_package_data=True
)
