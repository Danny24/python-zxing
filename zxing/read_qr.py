import zxing

testimage = "sample.png"

zx = zxing.BarCodeReader("/home/pi/zxing")
barcode = zx.decode(testimage)
print(barcode.data)
