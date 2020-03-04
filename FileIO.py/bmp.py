"""Module for dealing with BMP bitmap image files."""

def write_grayscale(filename, pixels):
    """ create and write a grayscale BMP file
    
    args:
        filename : The name of the BMP file to be created
        pixels : A crectangular image stored as sequence of rows.
                each row must be an iterable series for integer between 0-255
                
    Raises:
        valueError : If any of the interger values are out of range
        OSError : is the file couldn't be written
    """

    