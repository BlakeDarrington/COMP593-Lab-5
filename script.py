from pastebin_api import post_new_paste
from poke_api import search_pokemon_info
import sys

def main():
    search_term = get_search_term()
    pokemon = search_pokemon_info(search_term)

    if pokemon:                                                     
        title, body_text = get_paste_data(pokemon, search_term)      
        paste_url = post_new_paste(title, body_text, '1M')           
        print(paste_url)       
    return

def get_search_term():
    numparams = len(sys.argv) -1
    if numparams > 0:
        return sys.argv[1]
    else:
        print('Error: Missing search term.')
        sys.exit(1)

def get_paste_data(pokemon, search_term):                 
    search_term.title()                                         
    title = (f'{search_term.title()}\'s Abilities')                
    body_text = '- ' + '\n- '.join(pokemon)                                  
    return title, body_text 


if __name__ == '__main__':
    main()