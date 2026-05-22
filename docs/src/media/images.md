# Images with Pillow

`Pillow` is the maintained fork of the Python Imaging Library.

```python
from PIL import Image

mac = Image.open('example.jpg')
type(mac)  # PIL.JpegImagePlugin.JpegImageFile
```

```python
# mac.show()   # opens in the system image viewer
mac            # in a Jupyter notebook, displays inline
```

```python
print(mac.size)
print(mac.format_description)
print(mac.filename)
```

## Cropping

Coordinates are measured from the **top-left** corner `(0, 0)` — i.e. the 4th quadrant.

```python
mac.crop((0, 0, 100, 100))     # (left, upper, right, lower)
```

```python
pencils = Image.open('pencils.jpg')
width, height = pencils.size

pencils.crop((0, 0, width / 3, height / 10))     # top-left slice
pencils.crop((0, 1100, width / 3, height))       # bottom-left slice
```

## Paste, resize, rotate

```python
width_mac, height_mac = mac.size
computer = mac.crop((
    width_mac / 10 * 4 + 40,
    height_mac / 10 * 6.5,
    width_mac / 10 * 6 - 10,
    height_mac,
))

mac.paste(im=computer, box=(0, 0))

mac.resize((3000, 500))
mac.rotate(90)
```

## Transparency & blending

```python
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

red.putalpha(0)
blue.paste(im=red, box=(0, 0), mask=red)
# blue.save("out.png")   # save (overwrite if path already exists)
```

> **JPEG has no alpha channel**
>
> If you call `.putalpha()` on a JPEG-loaded image, convert it first:
>
> ```python
> img = Image.open('blue_color.png').convert('RGB')
> img.save('blue_new.jpg')
> ```

