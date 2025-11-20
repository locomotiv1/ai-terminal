from setuptools import setup, find_packages

setup(
    name='ai-terminal',
    version='0.1.0',
    description='A CLI tool to translate natural language into Linux commands.',
    url="https://github.com/locomotiv1/ai-terminal",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "pyperclip",
        "genai",
   ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'ai=ai_terminal.main:aiInit',
        ],
    },
)
