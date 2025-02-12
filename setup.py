from setuptools import setup, find_namespace_packages


setup(
    name="Python_HW4",
    version="1.0.0",
    author="Filip Povidernyi",
    author_email="p.poviderniy@gmail.com",
    description="Home work of course Python in Neoversity",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Filip-Povidernyi/Python_HW4",
    packages=find_namespace_packages(),
    python_requires=">=3.6",
    install_requires=[],
    entry_points={'console_scripts': [
        'task_4 = home_work.birthday:main',
        'task_3 = home_work.diff_days:main',
        'task_2 = home_work.get_numbers:main',
        'task_1 = home_work.normalize_numbers:main']}
)
