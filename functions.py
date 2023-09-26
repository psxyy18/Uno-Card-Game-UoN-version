import random



def handle_card_24(uno, n):
    for _ in range(n):
        try:
            uno.player_list[uno.position].append(uno.deck1.pop())
        except:
            uno.deck1, uno.deck2 = uno.deck2, uno.deck1
            random.shuffle(uno.deck1)
            uno.player_list[uno.position].append(uno.deck1.pop())
    uno.message = "%s Draws %d cards" % (uno.bot_map[uno.position], n)
    uno.special_check = 1


def handle_function_card(uno, item):
    uno.special_check = 0
    uno.deck2.append(item)
    if not uno.easy:  
        d = dict()
        d['Blue'] = 0
        d['Green'] = 0
        d['Yellow'] = 0
        d['Red'] = 0
        d['Black'] = 0
        for _item in uno.player_list[uno.position]:
            d[_item[1]] += 1
        d = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))
        new_color = d[-1][0] 
        if new_color == 'Black':
            new_color = d[-2][0]
    else:
        new_color = random.choice(uno.color)  
    uno.message = "%s plays %s %s, new color is %s" % (uno.bot_map[uno.position], item[0], item[1], new_color)
    uno.current = (uno.current[0], new_color)
