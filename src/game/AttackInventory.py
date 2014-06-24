__author__ = 'Victoria'

#This works just fine by it's self, but I tried and failed to have this
#implemented so that when the character moves if the monster is in a certain radius
#this should pop up to the user so that user can use an attack. This brought up
#the issue of getting the button box to pop up in the canvas. Then I want also
#want it so that when the user picks the user specific kind of attack that it 
#properly appears on the screen.  So I know this needs to be broken down and
#worked on a lot but it's a start.

#from src.game.AttackSpell import*
#from src.game.AttackWeapon import*
from Tkinter import *

class AttackInventory(Tk):
    def __init__(self):
        Tk.__init__(self)
        if self.state != 'disable':

            self.defense = Label(master = self, text= "What would you like to use as a defense?",
                                 height = 10, width=40,bg= 'red')
            self.defense.pack()
            self.state = 'disable'

            spell = Button(self, text='Spell', command=self.spell)
            spell.pack(padx = 5, pady = 5, side = LEFT)

            weapon = Button(self, text='Weapon', command= self.weapon)
            weapon.pack(padx = 5, pady = 5, side = LEFT)

            physical = Button(self, text='Physical', command=self.physical)
            physical.pack(padx = 5, pady = 5, side = LEFT)


    def spell(self, extra = True):
        top = self._top = Toplevel(self)
        if extra:
            self.entry0 = Entry(top)
            self.spell = "What kind of spell would you like to use?"
            print (self.spell)

        self.fire = Button(top, text='Fireball', command= self.fireBall)
        self.fire.pack()

        self.thunder = Button(top, text='Thunderbolt', command= self.thunderBolt)
        self.thunder.pack()

        self.spirit = Button(top, text='Spirit Shield', command= self.spiritShield)
        self.spirit.pack()

    def fireBall(self):
        self.entry0.get()
        self.fireBall = "You are using a fireball attack!"
        print (self.fireBall)
        #self.top.destroy()
        self.quit()

    def thunderBolt(self):
        self.entry0.get()
        self.thunderBolt = "You are using a thunderbolt attack!"
        print (self.thunderBolt)
        #self.top.destroy()
        self.quit()

    def spiritShield(self):
        self.entry0.get()
        self.spiritShield = "You are using a Spirit Shield attack!"
        print (self.spiritShield)
        #self.top.destroy()
        self.quit()

    def weapon(self, extra=True):
        top = self.top = Toplevel(self)
        if extra:
            self.entry1 = Entry(top)
            self.weapon = "What kind of weapon would you like to use?"
            print (self.weapon)

        self.ax = Button(top, text='Ax', command= self.ax)
        self.ax.pack()

        self.bowArrow = Button(top, text='Bow and Arrow', command= self.bowArrow)
        self.bowArrow.pack()

        self.sword = Button(top, text='Sword', command= self.sword)
        self.sword.pack()

    def ax(self):
        self.entry1.get()
        self.ax = "You are using an ax as an attack!"
        print (self.ax)
        self.top.destroy()
        self.quit()

    def bowArrow(self):
        self.entry1.get()
        self.bowArrow = "You are using a bow and arrow as an attack!"
        print (self.bowArrow)
        self.top.destroy()
        self.quit()

    def sword(self):
        self.entry1.get()
        self.sword = "You are using a sword as an attack!"
        print (self.sword)
        self.top.destroy()
        self.quit()

    def physical(self, extra = True):
        top = self._top = Toplevel(self)
        if extra:
            self.entry2 = Entry(top)
            self.physical = "What kind of physical attack would you like to use?"
            print (self.physical)

        self.punch = Button(top, text='Punch', command= self.punch)
        self.punch.pack()

        self.kick = Button(top, text='Kick', command= self.kick)
        self.kick.pack()

        self.run = Button(top, text='Run', command= self.run)
        self.run.pack()

    def punch(self):
        self.entry2.get()
        self.punch = "You are using a punching the enemy!"
        print (self.punch)
        #self.top.destroy()
        self.quit()

    def kick(self):
        self.entry2.get()
        self.kick = "You are kicking the enemy!"
        print (self.kick)
        #self.top.destroy()
        self.quit()

    def run(self):
        self.entry2.get()
        self.run = "You are running away!"
        print (self.run)
        #self.top.destroy()
        self.quit()

att = AttackInventory()
att.mainloop()