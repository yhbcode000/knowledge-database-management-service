from setuptools import setup, find_packages

setup(
    name='knowledge_database_management_service',  # The name of your project
    version='0.1.0',  # Initial version of your project
    author='Your Name or Team',  # Replace with your name or your team's name
    author_email='your-email@example.com',  # Replace with your email
    description='A service for managing AI knowledge with enhanced human control, versioning, and management convenience.',
    long_description=open('README.md').read(),  # Use README.md for the long description
    long_description_content_type='text/markdown',  # Specify the content type of the long description
    url='https://github.com/your-repo/knowledge-database-management-service',  # Replace with the URL to your project
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include additional files specified in MANIFEST.in
    install_requires=[
        'flask>=2.2.3',  # Flask for building the web service
        'sqlalchemy>=1.4.39',  # SQLAlchemy for database management
        'alembic>=1.7.7',  # Alembic for database migrations/version control
        'requests>=2.26.0',  # Requests for handling HTTP requests
        'PyYAML>=6.0',  # PyYAML for handling YAML configurations
        'gunicorn>=20.1.0',  # Gunicorn for deploying the service
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',  # For running tests
            'flake8>=4.0.0',  # For code style checking
            'black>=22.3.0',  # For code formatting
        ],
        'test': [
            'pytest>=7.0.0',
            'coverage>=6.0',  # For measuring code coverage
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.10',  # Minimum version requirement of Python
    entry_points={
        'console_scripts': [
            'start-knowledge-db=knowledge_db_service.main:main',  # Replace with the actual entry point of your service
        ],
    },
)
