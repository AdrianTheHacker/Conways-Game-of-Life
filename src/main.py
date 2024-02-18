import pygame
from Block import Block


def createBlocksGrid(screenWidth, screenHeight, rowsAmount, columnsAmount):
    blocksGrid = pygame.sprite.Group()
    
    offset = 10
    blockWidth = (screenWidth - (2 * offset)) / rowsAmount
    blockHeight = (screenHeight - (2 * offset)) / columnsAmount

    for row in range(rowsAmount):
        blockXCordinate = offset + (row * blockWidth)

        for cell in range(columnsAmount):
            blockYCordinate = offset + (cell * blockHeight)

            blocksGrid.add(Block('white', blockWidth, blockHeight, blockXCordinate, blockYCordinate))

    return blocksGrid


def main():
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    blocksGrid: pygame.sprite.Group = createBlocksGrid(SCREEN_WIDTH, SCREEN_HEIGHT, 10, 10)
    # testBlock = Block('grey', 50, 50, 50, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")
        blocksGrid.draw(screen)
        # testBlock.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()