key = "😂😉😭"
string = "damn! that's crazy if you wrote the code yourself"
# string = """🙦🙨🙀🙬😩🙙🙪🙨🙙😥🙺😍🙡🙻🙌🙸🙰😍🙫🙯😍🙻🙦🙘😢🙾🙟🙭🙽🙈😢🙽🙅🙧😩🙎🙭🙭🙈😢🙰🙂🙷🙻🙞🙧🙥🙋😮😩🙏🙷🙽😍🙫🙯😍🙻🙦🙘😢🙽🙂🙭🙢😍🙯🙰😍🙪🙬🙁🙲😥😍�
# 🙬🙁🙮😩🙅🙧🙡🙈🙪🙬�"""
# string = """🙦🙨🙀🙬😩🙙🙪🙨🙙😥🙺😍🙡🙻🙌🙸🙰😍🙫🙯😍🙻🙦🙘😢🙾🙟🙭🙽🙈😢🙽🙅🙧😩🙎🙭🙭🙈😢🙰🙂🙷🙻🙞🙧🙥🙋😮😩🙏🙷🙽😍🙫🙯😍🙻🙦🙘😢🙽🙂🙭🙢😍🙯🙰😍🙪🙬🙁🙲😧😍�
# 🙽🙄🙮🙥😍🙲🙻🙈🙶🙽🙔😢🙮🙂🙭🙭�"""
string = "🙦🙨🙀🙬😨😍🙶🙡🙌🙶😮🙞😢🙪🙟🙣🙳🙔😢🙠🙋😢🙰🙂🙷😩🙚🙰🙦🙙🙧😩🙙🙪🙬😍🙡🙦🙉🙧😩🙔🙭🙼🙟🙱🙬🙁🙤"

out = ""
for i in range(len(string)):
    out+= chr(ord(string[i]) ^ ord(key[i%len(key)]))

print(out)