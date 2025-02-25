from setuptools import setup,find_packages

setup(name= "pixellib",
      version='0.7.0',
      description='PixelLib is a library used for easy implementation of semantic and instance segmentation of objects in images and videos with few lines of code.PixelLib makes it possible to train a custom segmentation model using few lines of code.PixelLib supports background editing of images and videos using few lines of code. ',
      url="https://github.com/ayoolaolafenwa/PixelLib",
      author='Ayoola Olafenwa',
      license='MIT',
      packages= find_packages(),
      install_requires=['pillow','scikit-image','opencv-python','matplotlib','imgaug', 'labelme2coco', 'imantics', 'Cython',
      'pyQt5', 'fvcore', 'iopath', 'omegaconf', 'cloudpickle', 'termcolor', 'yacs', 'tabulate', 'tqdm', 'future','pydot', 'dataclasses',
      'hydra-core', 'black'],
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={'': ['pkg/*.yaml']},
   
      )
