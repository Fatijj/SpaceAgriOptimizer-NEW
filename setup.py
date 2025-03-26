from setuptools import setup, find_packages

setup(
    name="space-agriculture-rl",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.31.0",
        "pandas>=2.1.1",
        "numpy>=1.26.1",
        "matplotlib>=3.8.1",
        "tensorflow>=2.15.0",
        "kaggle>=1.5.16",
        "Pillow>=10.1.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Space Agriculture Reinforcement Learning System",
    keywords="space, agriculture, reinforcement learning, AI",
    url="https://github.com/yourusername/space-agriculture-rl",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)