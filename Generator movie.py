# Y0uKa_Dev



from pystyle import Anime, Colors, Colorate, System, Center, Write
from pydorks import GoogleSearch


# intext:XXX movie site:drive.google.com
# XXX -inurl:(htm|html|php|pls|txt) intitle:index.of “last modified” (mp4|wma|aac|avi)


def search(movie_name: str) -> str:
    movie = GoogleSearch.search(results_len=1, intext=movie_name + " movie", site='drive.google.com')
    return "".join(movie[0].split('&')[0]) if len(movie) == 1 else False




banner = r"""
 @: :!$$$$@@@@&&##&$$$$$$$$$%:             
#@@@&////§§§§§§§§§§§§§§§§§§§/&@$%$$%**!:: 
 :::     :::!!!*!!$§§//$$#§§&$&/§§§§§§§§$ 
                 !/§§*::::&§@  :!%@#§§§§! 
               !@§§/*     :##:      :*@@  
               @§/@:                      """.replace('M', '&')


ascii_art = r"""

$$\     $$\  $$$$$$\            $$\   $$\  $$$$$$\          $$$$$$$\                       
\$$\   $$  |$$$ __$$\           $$ | $$  |$$  __$$\         $$  __$$\                      
 \$$\ $$  / $$$$\ $$ |$$\   $$\ $$ |$$  / $$ /  $$ |        $$ |  $$ | $$$$$$\  $$\    $$\ 
  \$$$$  /  $$\$$\$$ |$$ |  $$ |$$$$$  /  $$$$$$$$ |        $$ |  $$ |$$  __$$\ \$$\  $$  |
   \$$  /   $$ \$$$$ |$$ |  $$ |$$  $$<   $$  __$$ |        $$ |  $$ |$$$$$$$$ | \$$\$$  / 
    $$ |    $$ |\$$$ |$$ |  $$ |$$ |\$$\  $$ |  $$ |        $$ |  $$ |$$   ____|  \$$$  /  
    $$ |    \$$$$$$  /\$$$$$$  |$$ | \$$\ $$ |  $$ |        $$$$$$$  |\$$$$$$$\    \$  /   
    \__|     \______/  \______/ \__|  \__|\__|  \__|$$$$$$\ \_______/  \_______|    \_/    
                                                    \______|                               
                                                                                           
                                                                                           
"""[1:]



def init():
    System.Clear()
    System.Size(160, 50)
    System.Title("Phobos")
    Anime.Fade(text=Center.Center(banner), color=Colors.red_to_yellow, mode=Colorate.Vertical, enter=True)




def main():
    System.Clear()
    print('\n'*2)
    print(Colorate.Diagonal(color=Colors.red_to_yellow, text=Center.XCenter(ascii_art)))
    print('\n'*3)
    movie_name = Write.Input(text="Enter the name of the movie you want to download -> ", color=Colors.red_to_yellow, interval=0.005)
    print()
    movie_link = search(movie_name=movie_name)

    if movie_link:
        Write.Print(text="Here you go: ", color=Colors.red_to_yellow, interval=0.005)
        Write.Input(text=movie_link, color=Colors.white, interval=0.005)
        return exit()
    else:
        Write.Input(text=f"Sorry mate, I didn't find anything!", color=Colors.red_to_yellow, interval=0.005)
        return


if __name__ == '__main__':
    init()
    while True:
        main()
