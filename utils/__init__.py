
__title__ = "easy-utils"
__version__ = "0.0.1"

from .images import ImageFile, ImageBatchFiles

IMAGE = {"SINGLE":ImageFile, "BATCH":ImageBatchFiles}

ACCEPTED_FORMATS = {
    "png":IMAGE,
    "jpg":IMAGE,
    "jpeg":IMAGE,
    "webp":IMAGE,
    "pdf":IMAGE,
}
