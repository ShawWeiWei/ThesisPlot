from zope.interface import Interface
from zope.interface import implements

def 
if self.con=='Square':
    self.connection='Square'
        elif self.con=='SmallWorld':
            self.connection=u'SmallWorld_%.5f'%(self.p)
        elif self.con=='Sparser':
            self.connection=u'Sparser_%.5f'%(self.p)
        else:
            raise ValueError


class fileconf(Interface):
    """define file pattern"""
    self.CoupleType=""
    self.Conn=""
    self.Compos=""
    self.Spec=""

    def updateCoupleType():

    def updateConn():

    def updateCompos():

    def updateSpec():

class ExcitoryCouple(Object):
    def __init__(self,pML1,gc_exc,Vsyn,threshold,con,p=0):
        self.pML1=pML1
        self.gc_exc=gc_exc
        self.Vsyn=Vsyn
        self.threshold=threshold
        self.couple=ExcitatoryCouple
        self.con=con
        self.p=p
        self.update()

    def setGc(self,gc_exc):
        self.gc_exc=gc_exc
        self.update()
    
    def setProp(self,pML1):
        self.pML1=pML1
        self.update()

    def setCon(self,con):
        self.con=con
        self.update()

    def setP(self,p):
        self.p=p
        self.update()

    def update(self):
      
        self.coupleAndNoise=u'gc=%.5f_Vsyn=%.5f_threshold=%.5f'%(self.gc_exc,self.Vsyn,self.threshold)
        self.composition=u'pML1=%d%%'%(self.pML1)
        self.plot_title=u'pML=%d%%_gc=%.5f'%(self.pML1,self.gc_exc)


class InhibitoryCouple(Object):