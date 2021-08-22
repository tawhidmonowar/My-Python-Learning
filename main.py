data = "mail tawhidmonowar@gmail.com number: 01796938534"
at = data.find("@")
enDom = data.find(" ", at)
doName = data[at:enDom]
em = data.find(" ")
emAd = data[em:at]
print(emAd+doName)
