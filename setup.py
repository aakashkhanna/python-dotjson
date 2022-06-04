from setuptools import setup


def read_files(files):
    data = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            data.append(f.read())
    return "\n".join(data)


long_description = read_files(['README.md', 'CHANGELOG.md'])

setup(
    name="python-dotjson",
    description="Read key-value pairs from a settings.json file and set them as environment variables, dictionary or Pydantic models",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Aakash Khanna",
    author_email="me+aakashkh13@gmail.com",
    url="https://github.com/aakashkhanna/python-dotjson",
    keywords=['environment variables', 'deployments', 'settings', 'json', 'dotjson',
              'configurations', 'python', 'settings', 'pydantic', 'appsettings', 'settings.json'],
    packages=['dotjson'],
    package_dir={'': 'src'},
    python_requires=">=3.8",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'Environment :: Web Environment',
    ]
)