from ascii_magic import AsciiArt

print('''






















autorun





































































autorun
''')

print("Welcome to cosmosinity's ASCII Art Generator!")
print("Make sure that you have a file named 'image.png', or else it will not work! only .png files are supported...")
input("Press enter to continue.")

img = AsciiArt.from_image('image.png')

img.to_terminal(columns=200)
print("Enjoy the art!")
input("Press enter to exit...")
