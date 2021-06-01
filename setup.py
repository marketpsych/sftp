from distutils.core import setup
setup(
  name = 'marketpsych',
  packages = ['marketpsych'],
  version = '0.0.1',
  license='MIT',
  description = 'MarketPsych libraries',
  url = 'https://github.com/marketpsych/marketpsych',
  keywords = ['sentiment'],
  install_requires=[
          'paramiko',
      ],
  classifiers=[ 
    'Development Status :: 4 - Alpha',
    'Intended Audience :: Developers',
    'License :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)