# SubstancePNGtoQuixelPNG
Script converting 16bit Greyscale and 32bit RGBA to 24bit RGB PNGs to be imported as custom surface in Quixel Mixer

### Requirements:
- Python 3.8
- Pillow Image Library (pip install Pillow in cmd)
### Usage:
- Run the script via cmd (i.e. C:\SubstancePNGtoQuixelPNG>mk24png.py)
- Provide Source Directory containing the map directories (i.e. C:\Maps, containing directories 00,01,...)

Keep in mind that the script converts only PNGs within the first level directories of the source directoy. Source\Dir01 Source\Dir02 etc.
Nested directories aren't supported. If you only want to convert the contents of one directory, either adapt the script, or put it in an envelope directory.

The script is provided as is and I don't take any responsibility for possible file corruption.

Based on file size and amount of files, the script can take a considerably long time to execute.

