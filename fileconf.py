from zope.interface import Interface
from zope.interface import implementer
from zope.interface import implements


def isConn(con, p):
    if con == 'Square':
        connection = 'Square'
    elif con == 'SmallWorld':
        connection = u'SmallWorld_%.5f' % p
    elif con == 'Sparser':
        connection = u'Sparser_%.5f' % p
    else:
        raise ValueError
    return connection


class fileconf(Interface):
    """define file pattern"""
    self.CoupleType = ""
    self.Conn = ""
    self.Compos = ""
    self.Spec = ""

    def updateCoupleType():

    def updateConn():

    def updateCompos():

    def updateSpec():


@implementer(fileconf)
class ExcitoryCouple:
    def __init__(self, pML1, gc_exc, Vsyn, threshold, con, p=0):
        self.coupleType = "ExcitatoryCouple"
        self.conn = ""
        self.compos = ""
        self.spec = ""

        self.pML1 = pML1
        self.con = con
        self.p = p

        self.gc_exc = gc_exc
        self.Vsyn = Vsyn
        self.threshold = threshold

        self.update()

    def set_gc(self, gc_exc):
        self.gc_exc = gc_exc
        self.update()

    def set_prop(self, pML1):
        self.pML1 = pML1
        self.update()

    def set_con(self, con, p):
        self.con = con
        self.p = p
        self.update()

    def update(self):
        self.spec = u'gc=%.5f_Vsyn=%.5f_threshold=%.5f' % (self.gc_exc, self.Vsyn, self.threshold)
        self.compos = u'pML1=%d%%' % (self.pML1)
        self.conn = isConn(self.con, self.p)
        # self.plot_title = u'pML=%d%%_gc=%.5f' % (self.pML1, self.gc_exc)


@implementer(fileconf)
class InhibitoryCouple:
    def __init__(self, pML1, pML2, gc_exc, gc_inh, V_exc, V_inh, threshold, con, p=0):
        self.coupleType = "CoupleWithInhibition"
        self.conn = ""
        self.compos = ""
        self.spec = ""
        self.con = con
        self.p = p

        self.pML1 = pML1
        self.pML2 = pML2

        self.gc_exc = gc_exc
        self.gc_inh = gc_inh
        self.V_exc = V_exc
        self.V_inh = V_inh
        self.threshold = threshold

        self.update()

    def set_gc(self, gc_exc, gc_inh):
        self.gc_exc = gc_exc
        self.gc_inh = gc_inh
        self.update()

    def set_prop(self, pML1, pML2):
        self.pML1 = pML1
        self.pML2 = pML2
        self.update()

    def set_con(self, con, p):
        self.con = con
        self.p = p
        self.update()

    def update(self):
        self.spec = u'gc_exc=%.5f_V_exc=%.5f_gc_inh=%.5f_V_inh=%.5f_threshold=%.5f' % \
                    (self.gc_exc, self.V_exc, self.gc_inh, self.V_inh, self.threshold)
        self.compos = u'pML1=%d%%_pML2=%d%%' % (self.pML1, self.pML2)
        self.conn = isConn(self.con, self.p)
        # self.plot_title = 'pML1=%d%%_pML2=%d%%_gc_exc=%.5f_gc_inh=%.5f' % \
        #                   (self.pML1, self.pML2, self.gc_exc, self.gc_inh)
