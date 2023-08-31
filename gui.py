import pygame

# Create a new deck of cards 
def create_deck():
    deck = []
    for suit in ['Clubs', 'Diamond', 'Hearts', 'Spades']:
        for value in range(1, 14):
            deck.append(f'{value}{suit}')
    return deck

# Load cards
def load_cards():
    cards = {}
    for suit in ['Clubs', 'Diamond', 'Hearts', 'Spades']:
        for value in range(1, 14):
            cards[f'{value}{suit}'] = pygame.image.load(f'images/cards/{suit} {value}.png')
    return cards

# Display selected card 
def display_card(cards, screen):
    width = 50
    for i in range(1, 14):
        screen.blit(cards[f'{i}Clubs'], (width, 50))
        width += 50


pygame.init()

# Screen size
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)

# Set up the drawing window
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('pokerKing v0.1')

# Run until the user asks to quit
running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with black 
    screen.fill((0, 0, 0))

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, white, (50, 50, screen_width - 100, screen_height - 100), 2)
    pygame.draw.circle(screen, white, (screen_width // 2, screen_height // 2), 100, 2)

    # Update cards
    cards = load_cards()
    display_card(cards, screen)

    # Flip the display
    pygame.display.flip()

    # Frame rate 60
    pygame.time.Clock().tick(60)

pygame.quit()

