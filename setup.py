from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    
setup(
    name = 'cgpt',
    version = '0.0.3',
    author = 'Aina Yves',
    author_email = 'randrianaina.yves@gmail.com',
    license = 'MIT',
    description = 'Use openai chat-gpt on your cli',
    long_description=long_desc,
    url = 'https://github.com/Aina15-DT/cli-gpt>',
    py_modules = ['cli_gpt', 'app'],
    packages = find_packages(),
    install_requires = ['aiohttp==3.8.4',
                        'aiosignal==1.3.1',
                        'async-timeout==4.0.2',
                        'attrs==22.2.0','bleach==6.0.0',
                        'certifi==2022.12.7',
                        'cffi==1.15.1',
                        'charset-normalizer==3.1.0',
                        'click==8.1.3',
                        'cryptography==39.0.2',
                        'docutils==0.19',
                        'frozenlist==1.3.3',
                        'idna==3.4',
                        'importlib-metadata==6.0.0',
                        'importlib-resources==5.12.0',
                        'jaraco.classes==3.2.3',
                        'jeepney==0.8.0',
                        'keyring==23.13.1',
                        'markdown-it-py==2.2.0',
                        'mdurl==0.1.2',
                        'more-itertools==9.1.0',
                        'multidict==6.0.4',
                        'openai==0.27.2',
                        'pkginfo==1.9.6',
                        'pycparser==2.21',
                        'Pygments==2.14.0',
                        'python-dotenv==1.0.0',
                        'readme-renderer==37.3',
                        'requests==2.28.2',
                        'requests-toolbelt==0.10.1',
                        'rfc3986==2.0.0',
                        'rich==13.3.2',
                        'SecretStorage==3.3.3',
                        'six==1.16.0',
                        'tqdm==4.65.0',
                        'twine==4.0.2',
                        'typing_extensions==4.5.0',
                        'urllib3==1.26.15',
                        'webencodings==0.5.1',
                        'yarl==1.8.2',
                        'zipp==3.15.0',],
                        
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cgpt=cgpt:cli
    '''
)