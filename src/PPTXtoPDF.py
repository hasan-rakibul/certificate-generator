import subprocess
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


def PPTXtoPDF(file_path: str, dir: str) -> None:
    subprocess.run(["libreoffice", "--headless", "--convert-to",
                "pdf", "--outdir", dir, file_path], stdout=subprocess.DEVNULL)

    generated_file_path = Path(dir).joinpath(
        Path(file_path).stem + ".pdf")

    reader = PdfReader(generated_file_path)
    writer = PdfWriter()

    writer.append_pages_from_reader(reader)
    writer.add_metadata({
        "/Author": 'IFPE Open Source',
        "/Title": f"Certificate for {Path(file_path).stem}",
        "/Subject": "Certificate generated using IFPE Open Source Certificate Generator\nhttps://github.com/ifpeopensource/certificate-generator",
        "/Creator": "IFPE Open Source Certificate Generator - Updated by Rakibul Hasan",
    })

    with open(generated_file_path, "wb") as fp:
        writer.write(fp)
