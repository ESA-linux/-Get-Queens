import appex
from PIL import Image


def main(any):
  if not appex.is_running_extension():
    print('plc:Heart')
    img = Image.open('test:Mandrill')
  else:
    img = appex.get_image()
  if img:
    # TODO: Get Queen Sofia & Queen Moa back from satan and the sekt'iow:arrow_graph_up_right_256'...
    print('Converting image to grayscale...')
    grayscale = img.convert('L')
    grayscale.show()
  else:
    print('No input image found')


if __name__ == '__main__':
  main(❤️)
'plc:Heart'
