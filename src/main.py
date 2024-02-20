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


def changeBlockState(block, numberOfNeighbors):
    if not block.state:
            if numberOfNeighbors == 3:
                block.state == True
            return

    if numberOfNeighbors < 2:
        block.state = False

    if numberOfNeighbors == 2 or numberOfNeighbors == 3:
        block.state = True

    if numberOfNeighbors > 3:
        block.state = False


def getNumberOfNeightbors(index, blocksGrid, rowsAmount, columnsAmount):
    numberOfNeighbors = 0
    checkTop = True
    checkBottom = True
    checkLeft = True
    checkRight = True

    if index < rowsAmount:
        checkTop = False

    if index >= (rowsAmount * columnsAmount) - columnsAmount:
        checkBottom = False

    if index % columnsAmount != 0:
        checkLeft = False

    if (index + 1) % columnsAmount == 0:
        checkRight = False

    print(f'{index}: {(index + 1) % columnsAmount}: {checkBottom}')


    if checkTop:
        if checkLeft and blocksGrid[index - (columnsAmount + 1)].state:
            numberOfNeighbors += 1

        if blocksGrid[index - columnsAmount].state:
            numberOfNeighbors += 1

        if blocksGrid[index - (columnsAmount - 1)].state:
            numberOfNeighbors += 1

    if checkLeft and blocksGrid[index - 1].state:
        numberOfNeighbors += 1

    if checkRight and blocksGrid[index + 1].state:
        numberOfNeighbors += 1

    if checkBottom:
        if checkLeft and blocksGrid[index + (columnsAmount - 1)].state:
            numberOfNeighbors += 1

        if blocksGrid[index + (columnsAmount)].state:
            numberOfNeighbors += 1

        if checkRight:
            if blocksGrid[index + (columnsAmount + 1)].state:
                numberOfNeighbors += 1

    return numberOfNeighbors


    # if checkTop:
    #     if checkLeft and blocksGrid[index - (rowsAmount + 1)].state:      # If block on top left is alive
    #         numberOfNeighbors += 1

    #     if blocksGrid[index - rowsAmount].state:
    #         numberOfNeighbors += 1

    #     if checkRight and blocksGrid[index - (rowsAmount - 1)].state:
    #         numberOfNeighbors += 1

    # if checkLeft and blocksGrid[index - 1].state:
    #     numberOfNeighbors += 1

    # if checkRight and blocksGrid[index + 1].state:
    #     numberOfNeighbors += 1

    # if checkBottom:
    #     if checkLeft and blocksGrid[index + (rowsAmount - 1)].state:
    #         numberOfNeighbors += 1

    #     print(index)
    #     if blocksGrid[index + rowsAmount].state:
    #         numberOfNeighbors += 1
        
    #     if checkRight and blocksGrid[index + 1].state:        # Error with check right
    #         numberOfNeighbors += 1


def updateBlocks(blocksGrid, rowsAmount, columnsAmount):
    numberOfNeighbors = 4

    for index, block in enumerate(blocksGrid.sprites()):
        numberOfNeighbors = getNumberOfNeightbors(index, blocksGrid.sprites(), rowsAmount, columnsAmount)
        changeBlockState(block, numberOfNeighbors)

        
def main():
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    blocksGrid: pygame.sprite.Group = createBlocksGrid(SCREEN_WIDTH, SCREEN_HEIGHT, 10, 10)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updateBlocks(blocksGrid, 10, 10)

        screen.fill("purple")
        blocksGrid.draw(screen)
        blocksGrid.update()
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()