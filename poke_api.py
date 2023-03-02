import requests

POKE_API_URL = 'https://pokeapi.co/'


def main():
    pokemon = search_pokemon_info('pikachu')
    print(pokemon)
    
def search_pokemon_info(search_term):

    search_poke_URL = f'https://pokeapi.co/api/v2/pokemon/{search_term}'
    
    search_term.lower()
    search_term.strip()

    #Setup the header parameters
    header_params = {
        'Accept' : 'application/json',
        'entity': 'pokemon',
    }
    #Send a GET request for pokemon that contain search term
    print(f'Getting information for {search_term}...', end='')
    resp_msg = requests.get(search_poke_URL, headers=header_params)

    #Check if paste was created successfully
    if resp_msg.ok:
        print('success.')
        body_dict = resp_msg.json()
        pokemon = [ability['ability']['name']for ability in body_dict['abilities']]
        return pokemon
    else:
        print("failure.")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")
    return None



if __name__ == '__main__':
    main()

    