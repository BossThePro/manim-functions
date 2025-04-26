from manim import *

class TestScene(Scene):
    def construct(self):
        coin = Coin(scale=2)
        self.add(coin)
        self.wait(1)
        #self.play(coin.moveCoin(position=4*LEFT+2.5*UP, scale=0.65))
        #self.wait()
        self.play(coin.moveSplitCoinHorizontal(position=4*LEFT+2.5*UP, scale=0.65))
        self.wait(1)
# To do for coin: 
# Add movement for coin1 and coin2 if coin has been split
# Make coin flippable

class Coin(VGroup):
    def __init__(self, radius=1, color=YELLOW, labelFront="H", labelBack="T", scale=1, position=0, *vmobjects, **kwargs):
        """ Creates a coin mobject with labels on both sides, that has the ability to be flipped

        Args:
            radius (float): Defines the radius of the coin 
            color (ManimColor): Defines the color of the coin
            labelFront (str): Defines the frontfacing label of the coin
            labelBack (str): Defines the backfacing label of the coin
            scale (float): Defines the scale of the coin in accordance with manim
            position (np.array): Sets the position of the coin 
        """        
        super().__init__(*vmobjects, **kwargs)
        #Defining all necessary properties of circle
        self.labelFront = labelFront
        self.labelBack = labelBack
        self.color = color
        self.radius = radius
        self.coinScale = scale
        self.circle = Circle(radius=radius, color=color).set_fill(color).scale(scale).move_to(position)
        self.scaleLabel = scale*1.55
        self.label = Text(labelFront).move_to(self.circle.get_center()).scale(self.scaleLabel)  
        self.add(self.circle, self.label) 
    def moveCoin(self, scale=None, position=0):
        """Moves the coin into a certain position with a moving animation based on parameters and alters the scale if necessary. Warning: DO not call the other move functions if this has been called

        Args:
            position (np.array): Sets the position that the coin shall be moved to
            scale (float): Sets the scale of the coin (defaults to current scale if no parameter is given)
        """
        if scale == None:
            scale = self.coinScale
        self.generate_target()
        self.target.move_to(position).scale(scale/self.coinScale)
        return MoveToTarget(self)
    def moveSplitCoinVertical(self, scale=None, position = 0):
        """Moves the coin into a certain position and displays both sides of the coin by splitting vertically with a moving animation and alters the scale if specified. Warning: DO not call the other move functions if this has been called

        Args:
            scale (float): Scales the coins. Defaults to current scale.
            position (np.array): Moves the coin to position x,y. Defaults to center.
        """        
        if scale == None:
            scale = self.coinScale
        self.secondCircle = None
        self.secondLabel = None
        self.generate_target()
        self.secondCircle = Circle(radius=self.radius, color=self.color).set_fill(self.color).scale(scale).move_to(self.circle.get_center())
        self.secondLabel = Text(self.labelBack).move_to(self.secondCircle.get_center())
        positionSecond = position.copy()
        positionSecond[1] = -positionSecond[1]
        self.target.move_to(position).scale(scale/self.coinScale).add(self.secondCircle.move_to(positionSecond), self.secondLabel.move_to(self.secondCircle.get_center()))
        return MoveToTarget(self)
    def moveSplitCoinHorizontal(self, scale=None, position = 0):
        """Moves the coin into a certain position and displays both sides of the coin by splitting horizontally with a moving animation and alters the scale if specified. Warning: DO not call the other move functions if this has been called

        Args:
            scale (float): Scales the coins. Defaults to current scale.
            position (np.array): Moves the coin to position x,y. Defaults to center.
        """        
        if scale == None:
            scale = self.coinScale
        self.secondCircle = None
        self.secondLabel = None
        self.generate_target()
        self.secondCircle = Circle(radius=self.radius, color=self.color).set_fill(self.color).scale(scale).move_to(self.circle.get_center())
        self.secondLabel = Text(self.labelBack).move_to(self.secondCircle.get_center())
        positionSecond = position.copy()
        positionSecond[0] = -positionSecond[0]
        self.target.move_to(position).scale(scale/self.coinScale).add(self.secondCircle.move_to(positionSecond), self.secondLabel.move_to(self.secondCircle.get_center()))
        return MoveToTarget(self)
