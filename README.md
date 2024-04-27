# Summit Read Me

This is a simple Python app that uses Tessreact from Google for optical character recognition (OCR) to read and summarize a set of images.

## Mac Instructions

First, clone the Summit git repo:
```
git clone https://github.com/scidsg/summit.git && cd summit
```

Then, run the script:
```
chmod +x summit.sh && ./summit.sh
```

You should see an output similar to this:
```
glennsorrentino@m1 summit % chmod +x summit.sh && ./summit.sh
 ______     __  __     __    __     __    __     __     ______
/\  ___\   /\ \/\ \   /\ "-./  \   /\ "-./  \   /\ \   /\__  _\
\ \___  \  \ \ \_\ \  \ \ \-./\ \  \ \ \-./\ \  \ \ \  \/_/\ \/
 \/\_____\  \ \_____\  \ \_\ \ \_\  \ \_\ \ \_\  \ \_\    \ \_\
  \/_____/   \/_____/   \/_/  \/_/   \/_/  \/_/   \/_/     \/_/

🏔️ Summit is an OCR application to extract and summarize text from a set of images.

A free and open-source tool by Science & Design, Inc. - https://scidsg.org
🧑‍💻 Creating a virtual environment...
🎬 Activating the virtual environment...
📋 Installing required packages from requirements.txt...
Requirement already satisfied: pillow in /Users/glennsorrentino/Nextcloud/Git/read/venv/lib/python3.12/site-packages (from -r requirements.txt (line 1)) (10.3.0)
Requirement already satisfied: pytesseract in /Users/glennsorrentino/Nextcloud/Git/read/venv/lib/python3.12/site-packages (from -r requirements.txt (line 2)) (0.3.10)
Requirement already satisfied: packaging>=21.3 in /Users/glennsorrentino/Nextcloud/Git/read/venv/lib/python3.12/site-packages (from pytesseract->-r requirements.txt (line 2)) (24.0)
🚀 Summiting...
✅ Text from IMG_9673.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_9673.jpeg.txt
✅ Text from IMG_0405.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_0405.jpeg.txt
✅ Text from tesla.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/tesla.jpeg.txt
✅ Text from IMG_0265.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_0265.jpeg.txt
✅ Text from IMG_0227.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_0227.jpeg.txt
✅ Text from IMG_9666.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_9666.jpeg.txt
✅ Text from IMG_0368.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_0368.jpeg.txt
✅ Text from image.jpg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/image.jpg.txt
👍 Summary written to /Users/glennsorrentino/Nextcloud/Git/summit/text/📝 Summary.txt.
🏁 Script completed successfully.
glennsorrentino@m1 summit %
```
