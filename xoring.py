#If you came here, then conratulations on your web skills, but if you couldn't solve this problem by yourself then its alright
#It was a good problem though
key = "😂😉😭"
string = "🙦🙨🙀🙬😨😍🙶🙡🙌🙶😮🙞😢🙪🙟🙣🙳🙔😢🙠🙋😢🙰🙂🙷😩🙚🙰🙦🙙🙧😩🙙🙪🙬😍🙡🙦🙉🙧😩🙔🙭🙼🙟🙱🙬🙁🙤"

out = ""
for i in range(len(string)):
    out+= chr(ord(string[i]) ^ ord(key[i%len(key)]))

print(out)
