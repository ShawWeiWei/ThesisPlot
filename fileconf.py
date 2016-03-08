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


# class fileconf(Interface):
#     """define file pattern"""
#     self.CoupleType = ""
#     self.Conn = ""
#     self.Compos = ""
#     self.Spec = ""
#
#     def updateCoupleType():
#
#     def updateConn():
#
#     def updateCompos():
#
#     def updateSpec():


# @implementer(fileconf)
class ExcitoryCouple:
    def __init__(self, p_ml1, gc_exc, v_exc, threshold, con, p=0):
        self.coupleType = "ExcitatoryCouple"
        self.conn = ""
        self.compos = ""
        self.spec = ""
        self.plot_title = ""

        self.p_ml1 = p_ml1

        self.con = con
        self.p = p

        self.gc_exc = gc_exc
        self.v_exc = v_exc
        self.threshold = threshold

        self.update()

    def set_p_ml1(self, p_ml1):
        self.p_ml1 = p_ml1
        self.update()

    def set_con(self, con):
        self.con = con
        self.update()

    def set_p(self, p):
        self.p = p
        self.update()

    def set_gc_exc(self, gc_exc):
        self.gc_exc = gc_exc
        self.update()

    def set_v_exc(self, v_exc):
        self.v_exc = v_exc
        self.update()

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.update()

    def update(self):
        self.compos = u'pML1=%d%%' % self.p_ml1
        self.conn = isConn(self.con, self.p)
        self.spec = u'gc_exc=%.5f_v_exc=%.5f_threshold=%.5f' % (self.gc_exc, self.v_exc, self.threshold)
        self.plot_title = '''pML1=%d%%_%s_gc_exc=%.5f''' % \
                          (self.p_ml1, self.conn, self.gc_exc)


# @implementer(fileconf)
class InhibitoryCouple:
    def __init__(self, p_ml1, p_inh, gc_exc, gc_inh, v_exc, v_inh, threshold, con, p=0):
        self.coupleType = "CoupleWithInhibition"
        self.conn = ""
        self.compos = ""
        self.spec = ""
        self.plot_title = ""

        self.con = con
        self.p = p

        self.p_ml1 = p_ml1
        self.p_inh = p_inh
        self.p_ml2 = 100 - p_ml1 - p_inh

        self.gc_exc = gc_exc
        self.gc_inh = gc_inh
        self.v_exc = v_exc
        self.v_inh = v_inh
        self.threshold = threshold

        self.update()

    def set_p_ml1(self, p_ml1):
        self.p_ml1 = p_ml1
        self.p_ml2 = 100 - p_ml1 - self.p_inh
        self.update()

    def set_p_inh(self, p_inh):
        self.p_inh = p_inh
        self.p_ml2 = 100 - p_inh - self.p_ml1
        self.update()

    def set_con(self, con):
        self.con = con
        self.update()

    def set_p(self, p):
        self.p = p
        self.update()

    def set_gc_exc(self, gc_exc):
        self.gc_exc = gc_exc
        self.update()

    def set_gc_inh(self, gc_inh):
        self.gc_inh = gc_inh
        self.update()

    def set_v_exc(self, v_exc):
        self.v_exc = v_exc
        self.update()

    def set_v_inh(self, v_inh):
        self.v_inh = v_inh
        self.update()

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.update()

    def update(self):
        self.spec = u'gc_exc=%.5f_v_exc=%.5f_gc_inh=%.5f_v_inh=%.5f_threshold=%.5f' % \
                    (self.gc_exc, self.v_exc, self.gc_inh, self.v_inh, self.threshold)
        self.compos = u'pML1=%d%%_pML2=%d%%' % (self.p_ml1, self.p_ml2)
        self.conn = isConn(self.con, self.p)
        self.plot_title = '''pML1=%d%%_pML2=%d%%_%s
                            gc_exc=%.5f_gc_inh=%.5f''' % \
                          (self.p_ml1, self.p_ml2, self.conn, self.gc_exc, self.gc_inh)
