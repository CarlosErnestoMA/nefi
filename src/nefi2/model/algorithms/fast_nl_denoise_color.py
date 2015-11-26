# -*- coding: utf-8 -*-

__algorithm__ = 'Fast nl Means Denoising Colored'
__belongs2__ = 'Preprocessing'


def apply(image, settings):
    """Replace this stub with actual implementation."""
    print '> Algorithm: %s processing "%s" with "%s"' % (__algorithm__, image, settings)
    sign(image, settings)
    return 'NUMPY.NDARRAY'


def belongs():
    """Define method membership."""
    return __belongs2__


def get_name():
    """Return algorithm name that will be displayed in UI."""
    return __algorithm__


def sign(image, settings):
    """Save the name of the current algorithm and settings used to process the
    image in the Image class."""
    image.sign(__algorithm__, settings)


if __name__ == '__main__':
    pass