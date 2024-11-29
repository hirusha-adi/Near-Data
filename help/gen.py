import os

commands = {
    "Administration": [
        ("/move", "Move users from one voice channel to another"),
    ],
    "Crypto": [
        ("/btc", "Get the current Bitcoin Rates"),
        ("/eth", "Get the current Etherium Rates"),
        ("/xmr", "Get the current XMR Rates"),
        ("/doge", "Get the current Doge Coin Rates"),
        ("/xrp", "Get the current XRP Rates"),
        ("/rvn", "Get the current Raven Coin Rates")
    ],
    "Encoding": [
        ("/b64encode", "Encode to Base64"),
        ("/b64decode", "Decode from Base64"),
        ("/md5", "Get MD5 Hash"),
        ("/sha1", "Get SHA1 Hash"),
        ("/sha224", "Get SHA224 Hash"),
        ("/sha512", "Get SHA512 Hash"),
        ("/leet", "Convert text to L33T format")
    ],
    "Fake Information": [
        ("/fake", "List out all the fake information commands - Theres a LOT!"),
        ("/fakeprofiles", "Generate a given number of fake profiles"),
    ],
    "Fun": [
        ("/inspire", "List out all the fake information commands - Theres a LOT!"),
        ("/meme", "Get a random meme"),
        ("/dadjoke", "Get a random dad joke"),
        ("/joke", "Get a random joke"),
        ("/wyr", "Would You Rather...?"),
        ("/advice", "Get advice for your life")
    ],
    "General": [
        ("/ping", "Check the response time of the Discord Bot"),
        ("/uptime", "How long has the bot been up for?"),
        ("/clean", "Amount of messages to Delete")
    ],
    "Information Gathering": [
        ("/ipinfo", "IP Address Lookup"),
        ("/avatar", "Get the User Avatar"),
        ("/serverinfo", "Get Information about the Server"),
        ("/userinfo", "User to get the Information of. Defaults to the Author")
    ],
    "Music": [
        ("/lyrics", "Search the Lyrics of any Song"),
        ("--join", "Join a Voice Channel"),
        ("--leave", "Leave the Voice Channel"),
        ("--play", "Play the song"),
        ("--skip", "Skip the currently playing song"),
        ("--pause", "Pause the music"),
        ("--resume", "Resume the music"),
        ("--shuffle", "Shuffle the pending music list"),
        ("--volume", "Change the volume of the song")
    ],
    "Tools": [
        ("/passwordgen", "Generate a very secure and unique password"),
        ("/passwordchk", "Password Strength Check and Profiler"),
        ("/insta", "Grab the Instagram Profile Picture of a Profile"),
        ("/bin", "Create a PrivateBin from a Text")
    ]
}

for vals in commands.values():
    for val in vals:
        com_name, com_desc = val
        com_name_final = ""
        if com_name.startswith("/"):
            com_name_final = com_name[1:]
        elif com_name.startswith("--"):
            com_name_final = com_name[2:]
        print(com_name_final)
        file_name = os.path.join(os.getcwd(), f"{com_name_final}.md")
        file_contents = f"""### {com_name}

{com_desc}"""
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(file_contents)
