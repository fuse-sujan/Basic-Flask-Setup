from setuptools import setup, find_packages

setup(name='basicflasksetup',
      version='1.0.0',
      description='Basic setup files for a flask app',
      author='Sujan Shrestha',
      author_email='sujan.shrestha@fusemachines.com',
      include_package_data=True,
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'flask',
          'flask-restplus'
      ]
      )
