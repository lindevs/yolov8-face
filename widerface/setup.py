from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

package = Extension(
    'bbox',
    ['box_overlaps.pyx'],
    include_dirs=[numpy.get_include()],
    define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
)
setup(ext_modules=cythonize([package], language_level='3str'))
