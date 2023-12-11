import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Paramètres du jeu
width, height = 800, 600
player_size = 50
bullet_size = 10
enemy_size = 50
enemy_speed = 5

# Initialisation de l'écran
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# Fonction pour dessiner le vaisseau spatial du joueur
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_size, player_size))

# Fonction pour dessiner un projectile
def draw_bullet(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, bullet_size, bullet_size))

# Fonction pour dessiner un ennemi
def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_size, enemy_size))

def main():
    clock = pygame.time.Clock()

    # Position initiale du joueur
    player_x = (width - player_size) // 2
    player_y = height - player_size - 10

    # Initialisation des listes pour les projectiles et les ennemis
    bullets = []
    enemies = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Gestion des touches pour déplacer le joueur et tirer
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= 10
                elif event.key == pygame.K_RIGHT and player_x < width - player_size:
                    player_x += 10
                elif event.key == pygame.K_SPACE:
                    bullets.append([player_x + player_size // 2 - bullet_size // 2, player_y])

        # Déplacer les projectiles vers le haut
        bullets = [[bx, by - 10] for bx, by in bullets if by > 0]

        # Générer un nouvel ennemi de manière aléatoire
        if random.randint(0, 100) < 5:
            enemies.append([random.randint(0, width - enemy_size), 0])

        # Déplacer les ennemis vers le bas
        enemies = [[ex, ey + enemy_speed] for ex, ey in enemies if ey < height]

        # Vérifier les collisions entre les projectiles et les ennemis
        for bullet in bullets:
            for enemy in enemies:
                if (enemy[0] < bullet[0] < enemy[0] + enemy_size and
                        enemy[1] < bullet[1] < enemy[1] + enemy_size):
                    enemies.remove(enemy)
                    bullets.remove(bullet)

        # Vérifier les collisions entre le joueur et les ennemis
        for enemy in enemies:
            if (player_x < enemy[0] + enemy_size and
                    player_x + player_size > enemy[0] and
                    player_y < enemy[1] + enemy_size and
                    player_y + player_size > enemy[1]):
                pygame.quit()
                sys.exit()

        # Effacer l'écran
        screen.fill(BLACK)

        # Dessiner le joueur
        draw_player(player_x, player_y)

        # Dessiner les projectiles
        for bullet in bullets:
            draw_bullet(bullet[0], bullet[1])

        # Dessiner les ennemis
        for enemy in enemies:
            draw_enemy(enemy[0], enemy[1])

        # Mettre à jour l'écran
        pygame.display.flip()

        # Contrôler la fréquence d'images par seconde
        clock.tick(30)

if __name__ == '__main__':
    main()
