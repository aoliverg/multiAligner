# multiAligner
A script to create multilingual alignments from Hunalign ladder alignments.


For example, to align a file available in Spanish, French, Italian, Portuguese, Catalan and Croating, and taking as a common (source) language Spanish, we need to:

- Segment all the files
- Align Spanish with all other languages with Hunalign and obtanining the ladder files

multiAligner.py has the -h option that shows the help:

```
python3 multiAligner.py -h
usage: multiAligner.py [-h] [-l LADDERS [LADDERS ...]] [-f FILES [FILES ...]] [-o OUTPUT]

Align multiple files.

options:
  -h, --help            show this help message and exit
  -l LADDERS [LADDERS ...], --ladders LADDERS [LADDERS ...]
                        The ladder files to process
  -f FILES [FILES ...], --files FILES [FILES ...]
                        The common source and target segmented files
  -o OUTPUT, --output OUTPUT
                        The common source and target segmented files
```

Use the script in the following way:

```python3 multiAligner.py -l file-ladder-spa-fra.txt file-ladder-spa-ita.txt file-ladder-spa-por.txt file-ladder-spa-rom.txt file-ladder-spa-cat.txt file-ladder-spa-hrv.txt -f file-seg-spa.txt file-seg-fra.txt file-seg-ita.txt file-seg-por.txt file-seg-rom.txt file-seg-cat.txt file-seg-hrv.txt -o aligned-all.txt```
```
The file aligned-all is a tabbed text file with all the alignments.
