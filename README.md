##Game Nave Espacial com PythonGame Nave Espacial com Python

Utilizando a biblioteca Pygame, foi desenvolvido um jogo simples, onde um nave tem por objetivo desvia dos asteróides, que com o decorrer do tempo começam a vir cada vez mais rápido.

Iniciamos o jogo chamado a biblioteca e definindo o tamanho padrão da tela.

    pygame.init()
    
    screen = pygame.display.set_mode((900, 400), 0, 32)
    
    background_filename = 'imagens/fundo.jpg'
    background = pygame.image.load(background_filename).convert()

##### Screenshots do Jogo:

[![](https://i.imgur.com/RsuOsEO.jpg)](https://i.imgur.com/RsuOsEO.jpg)

[![](https://i.imgur.com/O1b7fzt.jpg)](https://i.imgur.com/O1b7fzt.jpg)
