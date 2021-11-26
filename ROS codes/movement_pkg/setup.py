from setuptools import setup

package_name = 'movement_pkg'

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
    maintainer='bober',
    maintainer_email='68807442+bober2496@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'user_input_node = movement_pkg.user_input_node:main',
            'motors_node = movement_pkg.motors_node:main'
        ],
    },
)
