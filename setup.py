from setuptools import setup, find_packages

install_requires = [
    "torch==1.12.0",
    "tqdm==4.62.3",
    "sklearn==0.0",
    "transformers==4.21.0",
    "bidict==0.21.4",
    "tree-sitter-parsers==0.0.7",
    "tensorflow==2.9.0",
    "keras-radam==0.15.0",
    "pickle5==0.0.11",
    "nltk==3.7",
]

setup(
    name='curs',
    version="0.2.0",
    py_modules=['curs'],
    description='classify unsafe Rust code',
    author='Yijun Yu and Dimitris Gkoumas and Nghi D. Q. Bui',
    author_email='yijun.yu@huawei.com',
    license="MIT",
    url='https://github.com/yijunyu/curs',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
    ],
    package_dir={"curs": "curs"},
    packages=find_packages("."),
    package_data={'curs': ['*.txt', 'tbcnn/*', 'codeBERT/*']},
    scripts=['./scripts/curs'],
    install_requires=install_requires,
    include_package_data=True,
)
