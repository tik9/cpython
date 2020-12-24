## Convert images

This repo serves for **batch processing all images of a folder to text**
&nbsp;

### Contents

- [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) with **[Tesseract](https://github.com/tesseract-ocr/tesseract)**
- [make the **text formatted**](image.py#L56) including [] for correct answers (**[x]**)
- [add answers **to questions**](image.py#L109) which are stored in a [python array](settings.py#L9)

&nbsp;

### Getting started
1. Fork the repo
2. Prepare the [settings](settings.py)
3. [Choose the function](image.py#L149)
    - Recommendation: Start with **image()**
    - Convert [images to text](image.py#L22) in image()
4. See the [helper functions](helper.py) with Unittests
&nbsp;

### What is the repo used for
- [Skill tests in general](https://github.com/tik9/further-skill-tests)
- **Pluralsight** [Skill tests](https://github.com/tik9/pluralsight-skill-test)
- For many more if you can contribute, PR welcome