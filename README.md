## Convert images

This repo serves for **batch processing all images of a folder to text**
&nbsp;

### Contents

- [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) with [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [Make the text formatted](image.py#L56) including [] for correct answers ([x])
- Add answers to questions stored in a [python array](settings.py#L9)

&nbsp;

### Getting started

1. Prepare the [settings](settings.py)
2. [Choose the function](image.py#L149)
    - Start with **image()**
    - Convert [images to text](image.py#L22) in image()
3. See the [helper functions](helper.py) with **Unittests**
&nbsp;

### What is the repo used for
- Pluralsight [Skill tests](https://github.com/tik9/pluralsight-skill-test)
- [Skill tests in general](https://github.com/tik9/further-skill-tests)