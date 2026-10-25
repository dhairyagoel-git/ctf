
    import struct
    import zlib

    src = "Artifact-BC34.png"
    dst = "recovered.png"

    with open(src, "rb") as f:
        data = bytearray(f.read())

    # Restore the original image height
    data[20:24] = struct.pack(">I", 1728)

    # Verify the restored IHDR checksum
    ihdr = data[12:29]
    crc = zlib.crc32(ihdr) & 0xffffffff
    stored = struct.unpack(">I", data[29:33])[0]

    print("Restored height:", struct.unpack(">I", data[20:24])[0])
    print("Calculated CRC:", f"{crc:08x}")
    print("Stored CRC:    ", f"{stored:08x}")

    if crc != stored:
        raise ValueError("CRC mismatch; stopping.")

    with open(dst, "wb") as f:
        f.write(data)

    print("Saved recovered image:", dst)
