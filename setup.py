from setuptools import setup, find_packages

setup(
    name="pomodoro_timer",
    version="0.1.0",
    author="Duke Lester",
    author_email="dukelester4@gmail.com",
    description="A simple Pomodoro Timer built with Tkinter.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dukelester/pomodoro_timer",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tk"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Scheduling",
    ],
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "pomodoro_timer=pomodoro_timer.main:window.mainloop"
        ]
    },
    package_data={
        "pomodoro_timer": ["assets/*.png"],
    },
    keywords="pomodoro timer productivity tkinter desktop app",
)
