from typing import List

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.post("/file/")
async def create_file(file: bytes = File(...)):
    # works with small files because the bytes are stored in memory during the opration
    return {"file_size": len(file)}


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """A file stored in memory up to a maximum size limit,
    and after passing this limit it will be stored in disk.

    It will work well for large files like images, videos, large binaries, etc. without consuming all the memory.
    """
    return {"filename": file.filename}


@router.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    """Upload multiple files at once."""
    return {"filenames": [file.filename for file in files]}


@router.get("/")
async def main():
    content = """
<body>
<form action="/files/file/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/files/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
