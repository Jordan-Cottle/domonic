from domonic.html import *
from domonic.CDN import CDN_CSS

MARGIN = 3

# set some data
keyboard = [
    ['q','w','e','r','t','y','u','i','o','p'],
    ['a','s','d','f','g','h','j','k','l'],
    ['shift','z','x','c','v','b','n','m','backspace'],
    ['numerals','comma','space','period','enter']
]

# create a template
key_tmpl = lambda key: div( _style=f"display:inline;margin:{MARGIN}px;").html(
    button(key, _style="background-color:white;color:black;")
)

# generate keyboard
kb = []
for row in keyboard:
    kr = div(_style=f"margin:{MARGIN*2}px;")
    for key in row:
        kr.appendChild(key_tmpl(key))
    kb.append(str(kr))

# render webpage
css = link(_rel="stylesheet", _href=CDN_CSS.MARX)
render( html(
        head(css),
        body( ''.join( kb ), _style="background-color:#d1d5db;" ) ),
    "keyboard.html" )
