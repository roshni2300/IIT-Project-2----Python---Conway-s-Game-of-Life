import pygame
import random
import argparse
import os

CELL_SIZE = 20
MARGIN = 1
BOTTOM_PANEL_HEIGHT = 60  # Minimal for controls only


def parse_args():
   parser = argparse.ArgumentParser()
   parser.add_argument("--width", type=int, default=40)
   parser.add_argument("--height", type=int, default=20)
   parser.add_argument("--fps", type=int, default=6)
   return parser.parse_args()


def next_gen(live_cells, width, height):
   from collections import Counter
   neighbor_counts = Counter((x + dx, y + dy)
                             for (x, y) in live_cells
                             for dx in (-1, 0, 1)
                             for dy in (-1, 0, 1)
                             if (dx, dy) != (0, 0))
   return set(
       cell for cell, count in neighbor_counts.items()
       if count == 3 or (count == 2 and cell in live_cells)
       if 0 <= cell[0] < width and 0 <= cell[1] < height
   )


def random_fill(width, height):
   return set(
       (x, y)
       for x in range(width)
       for y in range(height)
       if random.random() < 0.2
   )


def save_pattern(cells, filename="patterns.txt"):
   with open(filename, "w") as f:
       for x, y in cells:
           f.write(f"{x},{y}\n")


def load_pattern(filename="patterns.txt"):
   if not os.path.exists(filename):
       return set()
   with open(filename, "r") as f:
       return set(tuple(map(int, line.strip().split(","))) for line in f)


def draw_board(screen, cells, width, height):
   for x in range(width):
       for y in range(height):
           rect = pygame.Rect(x * (CELL_SIZE + MARGIN), y * (CELL_SIZE + MARGIN), CELL_SIZE, CELL_SIZE)
           color = (255, 255, 0) if (x, y) in cells else (30, 30, 30)
           pygame.draw.rect(screen, color, rect)


def render_text(screen, text, pos, font):
   label = font.render(text, True, (255, 255, 255))
   screen.blit(label, pos)


def main():
   args = parse_args()
   grid_width, grid_height = args.width, args.height
   screen_width = grid_width * (CELL_SIZE + MARGIN)
   screen_height = grid_height * (CELL_SIZE + MARGIN) + BOTTOM_PANEL_HEIGHT

   pygame.init()
   screen = pygame.display.set_mode((screen_width, screen_height))
   pygame.display.set_caption("Conway's Game of Life")
   clock = pygame.time.Clock()
   font = pygame.font.SysFont("consolas", 16)

   running = True
   paused = False
   cells = random_fill(grid_width, grid_height)
   generation = 0

   while running:
       screen.fill((0, 0, 0))
       draw_board(screen, cells, grid_width, grid_height)

       # Bottom panel
       pygame.draw.rect(screen, (20, 20, 20),
                        (0, screen_height - BOTTOM_PANEL_HEIGHT, screen_width, BOTTOM_PANEL_HEIGHT))
       pygame.draw.rect(screen, (255, 255, 255),
                        (0, screen_height - BOTTOM_PANEL_HEIGHT, screen_width, BOTTOM_PANEL_HEIGHT), 2)

       render_text(screen, f"Gen: {generation}", (10, screen_height - BOTTOM_PANEL_HEIGHT + 10), font)
       render_text(screen, f"Live: {len(cells)}", (10, screen_height - BOTTOM_PANEL_HEIGHT + 30), font)
       render_text(screen, "Space:▶/⏸  N:Step  R:Random  S:Save  L:Load",
                   (200, screen_height - BOTTOM_PANEL_HEIGHT + 20), font)

       pygame.display.flip()

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   paused = not paused
               elif event.key == pygame.K_n and paused:
                   cells = next_gen(cells, grid_width, grid_height)
                   generation += 1
               elif event.key == pygame.K_c:
                   cells.clear()
                   generation = 0
               elif event.key == pygame.K_r:
                   cells = random_fill(grid_width, grid_height)
                   generation = 0
               elif event.key == pygame.K_s:
                   save_pattern(cells)
               elif event.key == pygame.K_l:
                   cells = load_pattern()
                   generation = 0

       if not paused:
           cells = next_gen(cells, grid_width, grid_height)
           generation += 1

       clock.tick(args.fps)

   pygame.quit()


if __name__ == "__main__":
   main()

