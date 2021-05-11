import image_slicer
import argparse

def main():
  parser = argparse.ArgumentParser()

  parser.add_argument(
            "--image",
            type=str,
            default='', 
            required=True,
            help="Your Image path",
        )

  parser.add_argument(
            "--slicer",
            type=int,
            default='', 
            required=True,
            help="Your slicer value (es. 8x8 = value --> 64)",
        )

  if len(sys.argv[1:]) == 0:
       parser.print_help()
       parser.exit()

  args = parser.parse_args()
  image_slicer.slice(image,slicer)

if __name__ == '__main__':
   
    main()
