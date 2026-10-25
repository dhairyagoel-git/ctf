import zipfile

with zipfile.ZipFile("test2.zip", "w") as zf:
    zf.write("manifest.json")  # the normal root manifest, same as before
    zf.writestr("LABEL_GOES_HERE", "CONTENT_GOES_HERE")  # the sneaky second entry