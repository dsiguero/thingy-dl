import os
import tempfile
import zipfile
import logging

logger = logging.getLogger(__name__)


def zipdir(src, dst):
    zipf = zipfile.ZipFile('%s.zip' % (dst), 'w', zipfile.ZIP_DEFLATED)

    abs_src = os.path.abspath(src)
    for root, dirs, files in os.walk(src):
        for file in files:
            absname = os.path.abspath(os.path.join(root, file))
            arcname = absname[len(abs_src) + 1:]
            print('zipping %s as %s' % (os.path.join(root, file), arcname))
            zipf.write(absname, arcname)
    zipf.close()