# Pixel Hunter: The Woodland Beast
 

Esse repositório guarda o meu projeto acadêmico! Esse jogo foi desenvolvido como uma *demo* para um trabalho da faculdade **Uninter**. A ideia principal aqui era colocar a em prática o aprendizado de Python e ver o que era possível criar usando a biblioteca Pygame. 

---

## Como Jogar (Tutorial e Controles)

O jogo é bem direto ao ponto, mas tem que ter reflexo! Você precisa sobreviver à floresta e abater 15 feras para conseguir passar da fase em segurança. Deixei aqui os controles:

- **Movimentação:** Setas do teclado (⬅️ Esquerda / ➡️ Direita)
- **Pulo:** Seta pra Cima (⬆️)
- **Atirar / Atacar:** Barra de Espaço (Space)


*Dica de ouro:* Fique de olho no seu tempo, desvie dos ataques inimigos e capriche na mira!

---

## O Background: Como o Projeto Nasceu?

Então, como aconteceu por trás dos panos? 

Tudo começou com a missão de criar algo interativo para a faculdade. A junção dinâmica **Python** + **Pygame** foi fundamental para aprender os fundamentos clássicos de *game dev*: criar um *game loop*, tratar ticks e FPS, e renderizar sprites na tela de forma otimizada.

O que rolou na codificação:
- **Tudo Orientado a Objetos (POO):** O código foi montado em classes. Temos nossa classe base `Entity` que derivou `Player` e `Enemy`. Além de separar as lógicas da fase (`Level`), do Menu, Tela de Vitória (`Victory`) e Tela de Derrota (`GameOver`).
- **Animações Fluidas:** Pra deixar o boneco vivo, montei um sistema que recorta os sprites e entende os estados do personagem (Parado, Correndo, Pulando, Atirando e, infelizmente, Morto). Tem até uns milissegundos de tempo de morte pra você ver seu herói caindo antes da tela de *Game Over*.
- **Desafios:** Achar a mecânica perfeita de física do pulo (com gravidade puxando o boneco pro chão sem ele atravessar a fase) e configurar o cérebro das colisões (`EntityMediator`) foram os maiores e mais divertidos quebra-cabeças do projeto.

É isso! Espero que a gameplay divirta quem for testar e que o código ajude a galera entender sobre programação de jogos.
