import os
from package.main import main
from package.utils import is_frozen, frozen_temp_path

if is_frozen:
    basedir = frozen_temp_path
else:
    basedir = os.path.dirname(os.path.abspath(__file__))
resource_dir=os.path.join(basedir, 'resources')


main(resource_dir)