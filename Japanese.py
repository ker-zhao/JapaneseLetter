
import random

jt1 = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやいゆえよらりるれろわいうえを"
jt2 = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤイユエヨラリルレロワイウエヲ"

pronounce = "a i u e o ka ki ku ke ko sa shi su se so ta chi tsu te to \
na ni nu ne no ha hi fu he ho ma mi mu me mo ya i yu e yo ra ri ru re ro wa i u e o".split(" ")

chinese_char = """\
安阿あアa   以伊いイi   宇宇うえu   衣江えエe   於於おオo \
加加かカka  幾機きキki  久久くクku  計介けケke  己己こコko \
左散さサsa  之之しシshi 寸須すスsu  世世せセse  曾曾そソso \
太多たタta  知千ちチchi 川川つツtsu 天天てテte  止止とトto \
奈奈なナna  仁仁にニni  奴奴ぬヌnu  袮袮ねネne  乃乃のノno \
波八はハha  比比ひヒhi  不不ふフfu  部部へヘhe  保保ほホho \
末末まマma  美三みミmi  武牟むムmu  女女めメme  毛毛もモmo \
也也やヤya  以伊いイi   由由ゆユyu  衣衣えエe   与與よヨyo \
良良らラra  利利りリri  留流るルru  礼礼れレre  吕呂ろロro \
和和わワwa  以伊いイi   宇宇うウu   衣江えエe   遠遠をヲo""".split()

# order_list = list(range(50))
# The follow two lines control the letter range.
start = 0
end = 5

# THe follow line control use hiragana or katakana.
source = jt1

order_list = list(range(start, end))
random.shuffle(order_list)

for i in order_list:

    current_char = source[i]
    input_data = input(" " + current_char + " : ").strip()
    try:
        input_index = pronounce.index(input_data)
    except:
        print("Wrong!!!!!!!!!!!!!!!!!!!!   -----   Right answer is: " + chinese_char[i])
        continue
    # if source[input_index] == current_char:
    if chinese_char[i][4:] == input_data:
        print("Right")
    else:
        print("Wrong!!!!!!!!!!!!!!!!!!!!   -----   Right answer is: " + chinese_char[i])
