# SubstancePNGtoQuixelPNG
Script converting 16bit Greyscale and 32bit RGBA to 24bit RGB PNGs to be imported as custom surface in Quixel Mixer

The script converts only PNGs within the first level directories of the source directoy. Source\Dir01 Source\Dir02 etc.
Nested directories aren't supported. If you only want to convert the contents of one folder, either adapt the script or put it in a envelope directory which can be used by the script.

The script is provided as is and I don't take any responsibility in possible file corruption.

Based on file size and amount of files, the script can take a considerably long time to finish.
