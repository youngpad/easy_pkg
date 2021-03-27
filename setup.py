from setuptools import setup

package_name = 'easy_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='martin',
    maintainer_email='martinmaeland@outlook.com',
    description='easy publisher and subscriber.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'easy_publisher = easy_pkg.easy_publisher:main',
                'easy_subscriber = easy_pkg.easy_subscriber:main'
        ],
    },
)
