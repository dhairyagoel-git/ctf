import struct
import zlib

f = open("Artifact-BC34.png", "rb").read()

print("File size:", len(f))
print("PNG signature:", f[:8].hex())

pos = 8
idat = b""

while pos + 12 <= len(f):
    length = struct.unpack(">I", f[pos:pos+4])[0]
    kind = f[pos+4:pos+8]
    data = f[pos+8:pos+8+length]
    crc = struct.unpack(">I", f[pos+8+length:pos+12+length])[0]

    calc = zlib.crc32(kind + data) & 0xffffffff

    print(
        kind.decode("ascii", errors="replace"),
        "offset:", pos,
        "length:", length,
        "stored CRC:", f"{crc:08x}",
        "calculated CRC:", f"{calc:08x}"
    )

    if kind == b"IHDR":
        print("IHDR bytes:", data.hex())

    if kind == b"IDAT":
        idat += data

    pos += 12 + length

    if kind == b"IEND":
        print("End of PNG at:", pos)
        break

print("Bytes after IEND:", len(f) - pos)

try:
    raw = zlib.decompress(idat)
    print("Decompressed image data:", len(raw), "bytes")
except zlib.error as e:
    print("IDAT decompression error:", e)