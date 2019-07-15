import os
import shutil
import tempfile
from flask import current_app


def savefile(file, filename):
    try:
        _, tmpfolder = os.path.split(tempfile.mkdtemp())
        tmpfolder = current_app.config['IMAGE_FILE_MOUNTPOINT'] + tmpfolder
        os.mkdir(tmpfolder)
        tmpfile = tmpfolder + "/" + filename
        file.save(tmpfile)
    except Exception as ex:
        raise
    return tmpfile


def deletefile(tmpfile):
    try:
        tmpfolder, _ = os.path.split(tmpfile)
        shutil.rmtree(tmpfolder)
    except Exception as ex:
        pass
