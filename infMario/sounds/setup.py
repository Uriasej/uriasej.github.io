import wget
for i in range(50):
    url = input("\nurl " + str(i+1) + ": ")
    filename = wget.download(str("https://github.com/OpenHTML5Games/games-mirror/raw/gh-pages/dist/mariohtml5/sounds/") + str(url) + str('.mp3'))
    filename = wget.download(str("https://github.com/OpenHTML5Games/games-mirror/raw/gh-pages/dist/mariohtml5/sounds/") + str(url) + str('.wav'))