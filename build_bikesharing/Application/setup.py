from setuptools import setup, find_packages

setup(
    name="BikeSharingRentals",
    version="0.1.18",
    description="Bike Sharing app prediction",
    author="Srikrishnan Shankar",
    author_email="srikrishnan.shankar@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "pytest",
        "scikit-learn",
        "joblib",
        "pyyaml"        
    ],
    include_package_data=True,
)
