from setuptools import setup, find_packages

setup(
    name="coding_ask",  # Paket nomi (masalan, my_generative_ai)
    version="0.1.0",
    author="Muhammad",
    author_email="muhammadrasulcoder@gmail.com",
    description="Generative AI javoblar generatsiyasi uchun funksiya",
    long_description=open("README.MD").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/muhammed7177/coding_ask",  # GitHub havolangiz
    packages=find_packages(),
    install_requires=[
        "google-generativeai"  # Kerakli kutubxonalar
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)