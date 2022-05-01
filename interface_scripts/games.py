from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from interface_scripts.quit_window import quit_window
from interface_scripts.message_box import message_box

from random import randrange, randint

class Snake(QFrame):
    def __init__(self):
        super(Snake, self).__init__()
        self.initUI()
    highscore = 0
    def initUI(self):
        
        self.newGame()
        self.setStyleSheet("QFrame { background: rgb(230,230,230) }")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setFixedSize(500, 500)
        self.setObjectName("Snake")
        self.setWindowTitle('Snake')
        self.setWindowIcon(QIcon(":icons/icon_snake.png"))
        self.setCursor(QCursor(Qt.OpenHandCursor))
        self.oldPos = QPoint(self.width(), self.height())

        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))


        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.scoreBoard(qp)
        self.placeFood(qp)
        self.drawSnake(qp)
        self.scoreText(event, qp)
        if self.isOver:
            self.gameOver(event)
        qp.end()

    def keyPressEvent(self, e):
        if not self.isPaused:
            #print "inflection point: ", self.xpos, " ", self.ypos
            if e.key() == Qt.Key_Up and self.lastKeyPress != 'UP' and self.lastKeyPress != 'DOWN':
                self.direction("UP")
                self.lastKeyPress = 'UP'
            elif e.key() == Qt.Key_Down and self.lastKeyPress != 'DOWN' and self.lastKeyPress != 'UP':
                self.direction("DOWN")
                self.lastKeyPress = 'DOWN'
            elif e.key() == Qt.Key_Left and self.lastKeyPress != 'LEFT' and self.lastKeyPress != 'RIGHT':
                self.direction("LEFT")
                self.lastKeyPress = 'LEFT'
            elif e.key() == Qt.Key_Right and self.lastKeyPress != 'RIGHT' and self.lastKeyPress != 'LEFT':
                self.direction("RIGHT")
                self.lastKeyPress = 'RIGHT'
            elif e.key() == Qt.Key_P:
                self.pause()
                
            elif e.key() == Qt.Key_Escape:
                self.pause()
                self.w = quit_window(text= "Are you sure you want\nto quit Snake ?", icon = ":icons/icon_snake.png", what_to_kill = "Snake")

        elif e.key() == Qt.Key_P:
            self.start()
        elif e.key() == Qt.Key_Space:
            self.newGame()
        elif e.key() == Qt.Key_Escape:
            self.pause()
            self.w = quit_window(text= "Are you sure you want\nto quit Snake ?", icon = ":icons/icon_snake.png", what_to_kill = "Snake")
        else :
            self.start()

    def newGame(self):
        self.score = 0
        self.xpos = 12
        self.ypos = 36
        self.lastKeyPress = 'RIGHT'
        self.timer = QBasicTimer()
        self.snakeArray = [[self.xpos, self.ypos], [self.xpos-12, self.ypos], [self.xpos-24, self.ypos]]
        self.foodx = 0
        self.foody = 0
        self.isPaused = False
        self.isOver = False
        self.FoodPlaced = False
        self.speed = 100
        self.pause()
        
    def pause(self):
        self.isPaused = True
        self.timer.stop()
        self.update()

    def start(self):
        self.isPaused = False
        self.timer.start(self.speed, self)
        self.update()

    def direction(self, dir):
        if (dir == "DOWN" and self.checkStatus(self.xpos, self.ypos+12)):
            self.ypos += 12
            self.repaint()
            self.snakeArray.insert(0 ,[self.xpos, self.ypos])
        elif (dir == "UP" and self.checkStatus(self.xpos, self.ypos-12)):
            self.ypos -= 12
            self.repaint()
            self.snakeArray.insert(0 ,[self.xpos, self.ypos])
        elif (dir == "RIGHT" and self.checkStatus(self.xpos+12, self.ypos)):
            self.xpos += 12
            self.repaint()
            self.snakeArray.insert(0 ,[self.xpos, self.ypos])
        elif (dir == "LEFT" and self.checkStatus(self.xpos-12, self.ypos)):
            self.xpos -= 12
            self.repaint()
            self.snakeArray.insert(0 ,[self.xpos, self.ypos])

    def scoreBoard(self, qp):
        qp.setPen(Qt.NoPen)
        qp.setBrush(QColor(25, 80, 0, 160))
        qp.drawRect(0, 0, 500, 24)
        qp.setBrush(QColor(0, 0, 0))
        qp.drawRect(0, 478, 500, 6)

    def scoreText(self, event, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Segoe UI', 8))
       
        if self.isPaused:
            
            qp.drawText(4, 495, "Paused")            
        else :
            qp.drawText(4, 495, "SCORE : " + str(self.score))  
        
        qp.setPen(QColor(255, 255, 255))
        qp.setFont(QFont('Segoe UI', 10))
        qp.drawText(8, 17, "HIGHSCORE: " + str(Snake.highscore))  
        qp.drawText(260, 17, "P = pause/resume, ESC = quit")

    def gameOver(self, event):
        Snake.highscore = max(Snake.highscore, self.score)
        self.end_message_snake = message_box("Score Snake",f"Game Over !\nYour score : {self.score}\nHighest Score : {Snake.highscore}", icon = ":icons/icon_snake.png")
        self.newGame()   

    def checkStatus(self, x, y):
        if y > 471 or x > 492 or x < -5 or y < 13:
            self.pause()
            self.isPaused = True
            self.isOver = True
            return False
        elif self.snakeArray[0] in self.snakeArray[1:len(self.snakeArray)]:
            self.pause()
            self.isPaused = True
            self.isOver = True
            return False
        elif self.ypos == self.foody and self.xpos == self.foodx:
            self.FoodPlaced = False
            self.score += 1
            return True
        elif self.score >= 573:
            pass


        self.snakeArray.pop()

        return True

    #places the food when theres none on the board 
    def placeFood(self, qp):
        if self.FoodPlaced == False:
            self.foodx = randrange(24)*12
            self.foody = randrange(2, 24)*12
            if not [self.foodx, self.foody] in self.snakeArray:
                self.FoodPlaced = True
        qp.setBrush(QColor(80, 180, 0, 160))
        qp.drawRect(self.foodx, self.foody, 12, 12)

    #draws each component of the snake
    def drawSnake(self, qp):
        qp.setPen(Qt.NoPen)
        qp.setBrush(QColor(255, 80, 0, 255))
        for i in self.snakeArray:
            qp.drawRect(i[0], i[1], 12, 12)

    #game thread
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.direction(self.lastKeyPress)
            self.repaint()
        else:
            QFrame.timerEvent(self, event)
            
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.setCursor(QCursor(Qt.ClosedHandCursor))
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        
    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.OpenHandCursor))


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    highscore = 0
    def initUI(self):
        """initiates application UI"""
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setCursor(QCursor(Qt.OpenHandCursor))
        self.setObjectName("Tetris")
        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        self.tboard.start()
        self.tboard.pause()
        self.setFixedSize(230, 500)
        
        self.center()
        self.setWindowTitle('Tetris')
        self.setWindowIcon(QIcon(":icons/icon_tetris.png"))

        self.oldPos = QPoint(self.width(), self.height())


        self.main_frame = QFrame(self)
        self.main_frame.setObjectName("Tetris")
        self.main_frame.setGeometry(0,0,230, 500)

        self.hor_lane = QFrame(self.main_frame)
        self.hor_lane.setObjectName(u"hor_lane")
        #self.hor_lane.setMinimumSize(QSize(1, 0))
        
        #self.hor_lane.move(0, 470)
        self.hor_lane.setGeometry(0, 474, 500, 6)
        self.hor_lane.setFrameShape(QFrame.HLine)
        self.hor_lane.setFrameShadow(QFrame.Sunken)
        self.hor_lane.setStyleSheet('background : black;')

        self.frame = QFrame(self.main_frame)
        self.frame.setGeometry(0,0, 500, 31)
        self.frame.setStyleSheet("background : rgba(25, 80, 0, 160);")
        
        self.txt = QLabel("  P = pause/resume, ESC = quit", self.frame)
        self.txt.setGeometry(0, 2, 300, 30)
        self.txt.setStyleSheet("font : 9pt 'Segoe UI'; color : white; background: transparent")

        self.show()
        
    def center(self):
        """centers the window on the screen"""

        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))

    def keyPressEvent(self, event):
        if event.key()== Qt.Key_Escape:
            if not self.tboard.isPaused:
                self.tboard.pause()
            self.w = quit_window(text= "Are you sure you want\nto quit Tetris ?", icon = ":icons/icon_tetris.png", what_to_kill = "Tetris")
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.setCursor(QCursor(Qt.ClosedHandCursor))
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.OpenHandCursor))

class Board(QFrame):
    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22
    Speed = 400
    

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        """initiates board"""

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.score = 0
        
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

    def shapeAt(self, x, y):
        """determines shape at the board position"""

        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        """sets a shape at the board"""

        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self):
        """returns the width of one square"""

        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        """returns the height of one square"""

        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        """starts game"""

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.score = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.score))

        self.newPiece()
        self.timer.start(Board.Speed, self)

    def pause(self):
        """pauses game"""

        if not self.isStarted:
            return

        self.isPaused = True

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("Paused")

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.score))

        self.update()

    def paintEvent(self, event):
        """paints all shapes of the game"""

        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())

    def keyPressEvent(self, event):
        """processes key press events"""

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()
        test=True


        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            if key == Qt.Key_Left:
                test=True
                self.tryMove(self.curPiece, self.curX - 1, self.curY)

            elif key == Qt.Key_Right:
                test=True
                self.tryMove(self.curPiece, self.curX + 1, self.curY)

            elif key == Qt.Key_Down:
                test=True
                self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

            elif key == Qt.Key_Up:
                test=True
                self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

            elif key == Qt.Key_Space:
                test=True
                self.dropDown()

            elif key == Qt.Key_D:
                test=True
                self.oneLineDown()
            
            elif key == Qt.Key_Escape:
                test=False
                self.w = quit_window(text= "Are you sure you want\nto quit Tetris ?", icon = ":icons/icon_tetris.png", what_to_kill = "Tetris")

            else :
                test = True

            if test: 
                self.isPaused = False
                self.isStarted = True
                self.timer.start(Board.Speed, self)
                self.msg2Statusbar.emit(str(self.score))


        else:
            if key == Qt.Key_Left:
                self.tryMove(self.curPiece, self.curX - 1, self.curY)

            elif key == Qt.Key_Right:
                self.tryMove(self.curPiece, self.curX + 1, self.curY)

            elif key == Qt.Key_Down:
                self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

            elif key == Qt.Key_Up:
                self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

            elif key == Qt.Key_Space:
                self.dropDown()

            elif key == Qt.Key_D:
                self.oneLineDown()
            
            elif key == Qt.Key_Escape:
                self.pause()
                self.w = quit_window(text= "Are you sure you want\nto quit Tetris ?", icon = ":icons/icon_tetris.png", what_to_kill = "Tetris")
            else :
                super(Board, self).keyPressEvent(event)

    def timerEvent(self, event):
        """handles timer event"""

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)

    def clearBoard(self):
        """clears shapes from the board"""

        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def dropDown(self):
        """drops down a shape"""

        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()

    def oneLineDown(self):
        """goes one line down with a shape"""

        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):
        """after dropping shape, remove full lines and create new shape"""

        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self):
        """removes all full lines from the board"""

        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.score = self.score + numFullLines
            self.msg2Statusbar.emit(str(self.score))

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()

    def newPiece(self):
        """creates a new shape"""

        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")
            Tetris.highscore = max(Tetris.highscore, self.score)
            self.end_message_tetris = message_box("Score Tetris",f"Game Over !\nYour score : {self.score}\nHighest score : {Tetris.highscore}", icon = ":icons/icon_tetris.png")
            self.initBoard()
            self.start()
            self.pause()



    def tryMove(self, newPiece, newX, newY):
        """tries to move a shape"""

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True

    def drawSquare(self, painter, x, y, shape):
        """draws a square of a shape"""

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

    def __init__(self):

        self.coords = [[0, 0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)

    def shape(self):
        """returns shape"""

        return self.pieceShape

    def setShape(self, shape):
        """sets a shape"""

        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape

    def setRandomShape(self):
        """chooses a random shape"""

        self.setShape(randint(1, 7))

    def x(self, index):
        """returns x coordinate"""

        return self.coords[index][0]

    def y(self, index):
        """returns y coordinate"""

        return self.coords[index][1]

    def setX(self, index, x):
        """sets x coordinate"""

        self.coords[index][0] = x

    def setY(self, index, y):
        """sets y coordinate"""

        self.coords[index][1] = y

    def minX(self):
        """returns min x value"""

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

    def maxX(self):
        """returns max x value"""

        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def minY(self):
        """returns min y value"""

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def maxY(self):
        """returns max y value"""

        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    def rotateLeft(self):
        """rotates shape to the left"""

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

    def rotateRight(self):
        """rotates shape to the right"""

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result