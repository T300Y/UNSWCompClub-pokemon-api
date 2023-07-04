import requests
from pkmn import Pokemon

# Insert the URLs to be used for your Pokemon Battle
MY_API = 'http://tedzn9.pythonanywhere.com/pokemon'
FRIEND_API = 'http://mkngds.pythonanywhere.com/pokemon'


def extract_pkmn(api_url) -> Pokemon:
    # Get the online published pokemon
    # ----Your code here---- #
    response = requests.get(api_url)
    # Check whether everythings all good with our data packet
    # 200 is good, 404 is bad, 500 is internal code issue
    # ----Your code here---- #
    assert(response.status_code == 200)
    # Make Pokemon object
    # ----Your code here---- #
    pkmn = Pokemon(response.json())
    # return (pokemon object)
    return pkmn