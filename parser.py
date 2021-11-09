#!/usr/bin/env python

import click
import os
import plistlib
from pathlib import Path


def read(path):
    """return webloc url"""
    if hasattr(plistlib, "load"):
        return plistlib.load(open(path, 'rb')).get("URL")
    return plistlib.readPlist(path).get("URL")

@click.command()
@click.option("--path", default=".", help="Folder path to iterate.")
                
def _cli(path):
    target_md = os.path.join(path, "result.md")
    md = open(target_md, 'w')
    
    pathlist = Path(path).glob('**/*.webloc')
    for filepath in pathlist:
        webloc_filepath = str(filepath)
        
        url = read(webloc_filepath)
        line = "[%s](%s)\n" % (filepath.name.replace(".webloc", ""), url)
        md.write(line)        
        continue
    md.close()
    
if __name__ == '__main__':
    _cli()