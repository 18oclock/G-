#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'基础类型的加工代码'

__author__ = 'WZH'


class Centerdrill(object):
    def __init__(self, x, y):
        Centerdrill.深度 = 2
        Centerdrill.x = x
        Centerdrill.y = y
        Centerdrill.S = 1000
        Centerdrill.刀位 = 1
        Centerdrill.起始位置 = 100
        Centerdrill.安全距离 = 50
        Centerdrill.其余点 = ""
        Centerdrill.R = 5
        Centerdrill.F = 100

    def print_G(self):
        return ('T%dM6(ZXZ)\n'
                'G90G40G0G54X%.3fY%.3fS%dM3\n'
                'G43H%dZ%.3fM8\n'
                'Z%d\n'
                'G83Z%.3fR%dF%dM8\n'
                'G90G0G80Z%dM9\n'
                '%s'
                'M5\n'
                'G0G91G28Z0Y0\n' % (Centerdrill.刀位,
                                    Centerdrill.x,
                                    Centerdrill.y,
                                    Centerdrill.S,
                                    Centerdrill.刀位,
                                    Centerdrill.起始位置,
                                    Centerdrill.安全距离,
                                    Centerdrill.深度,
                                    Centerdrill.R,
                                    Centerdrill.F,
                                    Centerdrill.起始位置,
                                    Centerdrill.其余点
                                    ))


class 钻头(object):
    def __init__(self, x, y, 深度, 孔径):
        钻头.x = x
        钻头.y = y
        钻头.深度 = 深度
        钻头.刀位 = 1
        钻头.孔径 = 孔径
        钻头.S = 1000
        钻头.安全距离 = 100
        钻头.起始位置 = 50
        钻头.R = 5
        钻头.Q = 2
        钻头.F = 100
        钻头.其余点 = ""

    def Print_G(self):
        return ('T%dM6(ZT%d)\n'
                'G90G40G0G54X%.3fY%.3fS%dM3\n'
                'G43H%dZ%dM8\n'
                'Z%d\n'
                'G83Z%.3fR%dQ%.3fF%dM8\n'
                '%s'
                'G90G0G80Z%dM5\n'
                'M9\n'
                'G0G91G28Z0Y0)\n' % (钻头.刀位,
                                     钻头.孔径,
                                     钻头.x,
                                     钻头.y,
                                     钻头.S,
                                     钻头.刀位,
                                     钻头.起始位置,
                                     钻头.安全距离,
                                     钻头.深度,
                                     钻头.R,
                                     钻头.Q,
                                     钻头.F,
                                     钻头.其余点,
                                     钻头.起始位置
                                     ))


class 倒角(object):
    def __init__(self, x, y, 深度, 直径):
        倒角.刀位 = 1
        倒角.角度 = 90
        倒角.x = x
        倒角.y = y
        倒角.S = 1000
        倒角.起始位置 = 100
        倒角.安全距离 = 50
        倒角.深度 = 深度
        倒角.R = 2
        倒角.F = 100
        倒角.F_fast = 300
        倒角.其余点 = ""
        倒角.半径 = 直径 / 2
        倒角.直径 = 直径

    def print_g1(self):
        return ('T%dM6(DJD%d)\n'
                'G90G40G0G54X%.3fY%.3fS%dM3\n'
                'G43H%dZ%dM8\n'
                'Z%d\n'
                'G81Z%.3fR%dF%dM8\n'
                '%s'
                'G90G0G80Z%dM5\n'
                'M9\n'
                'G0G91G28Z0Y0)\n' % (倒角.刀位,
                                     倒角.角度,
                                     倒角.x,
                                     倒角.y,
                                     倒角.S,
                                     倒角.刀位,
                                     倒角.起始位置,
                                     倒角.安全距离,
                                     倒角.深度,
                                     倒角.R,
                                     倒角.F,
                                     倒角.其余点,
                                     倒角.起始位置
                                     ))

    def print_g2(self):
        return ('T%dM6(DJD%d)\n'
                'G90G40G0G54X%.3fY%.3fS%dM3\n'
                'G43H%dZ%dM8\n'
                'Z%d\n'
                'G01Z%.3fF%d\n'
                'F91G01G41X%.3fD%.3fF%d\n'
                'G03I%.3fJ0\n'
                '%s'
                'G90G0G80Z%dM5\n'
                'M9\n'
                'G0G91G28Z0Y0)\n' % (倒角.刀位,
                                     倒角.角度,
                                     倒角.x,
                                     倒角.y,
                                     倒角.S,
                                     倒角.刀位,
                                     倒角.起始位置,
                                     倒角.安全距离,
                                     倒角.深度,
                                     倒角.F_fast,
                                     倒角.半径,
                                     倒角.刀位,
                                     倒角.F,
                                     倒角.半径,
                                     倒角.其余点,
                                     倒角.起始位置))

    def print_g(self):
        if 倒角.直径 <= 10:
            return self.print_g1()
        else:
            return self.print_g2()


class 螺纹铣刀(object,):
    def __init__(self, x, y, 深度, 大径, 螺距):
        螺纹铣刀.刀位 = 1
        螺纹铣刀.x = x
        螺纹铣刀.y = y
        螺纹铣刀.S = 3000
        螺纹铣刀.起始位置 = 100
        螺纹铣刀.安全距离 = 50
        螺纹铣刀.深度 = 深度
        螺纹铣刀.F_fast = 200
        螺纹铣刀.大径半径 = 大径/2
        螺纹铣刀.螺距 = 螺距
        螺纹铣刀.F = 100

    def print_g(self):
        return ('T%dM6(螺纹铣刀)\n'
                'G90G40G0G54X%.3fY%.3fS%dM3\n'
                'G43H%dZ%dM8\n'
                'Z%d\n'
                'G91G01Z%.3fF%d\n'
                'G91G01G41X%.3fD%.3fF%d\n'
                'G03I%.3fJ0Z%.3f\n'
                'G91G01G40X%.3f\n'
                'G91G01Z%.3fF%d\n'
                'G90G01G41X%.3fD%.3fF%d\n'
                'G03I%.3fJ0Z%.3f\n'
                'G91G01G41X%.3f\n'
                'G90G0Z%dM9\n'
                'M5\n'
                'G0G91G28Z0Y0)\n' % (螺纹铣刀.刀位,
                                     螺纹铣刀.x,
                                     螺纹铣刀.y,
                                     螺纹铣刀.S,
                                     螺纹铣刀.刀位,
                                     螺纹铣刀.起始位置,
                                     螺纹铣刀.安全距离,
                                     螺纹铣刀.深度,
                                     螺纹铣刀.F_fast,
                                     螺纹铣刀.大径半径,
                                     螺纹铣刀.刀位,
                                     螺纹铣刀.F,
                                     螺纹铣刀.大径半径*-1,
                                     螺纹铣刀.螺距,
                                     螺纹铣刀.大径半径*-1,
                                     螺纹铣刀.深度,
                                     螺纹铣刀.F_fast,
                                     螺纹铣刀.大径半径,
                                     螺纹铣刀.刀位,
                                     螺纹铣刀.F,
                                     螺纹铣刀.大径半径*-1,
                                     螺纹铣刀.螺距,
                                     螺纹铣刀.大径半径*-1,
                                     螺纹铣刀.起始位置))


class 攻丝(object):
    def __init__(self, x, y, 深度, 螺距):
        攻丝.刀位 = 1
        攻丝.x = x
        攻丝.y = y
        攻丝.S = 100
        攻丝.起始位置 = 100
        攻丝.安全距离 = 50
        攻丝.R = 5
        攻丝.深度 = 深度
        攻丝.其余点 = ""
        攻丝.螺距 = 螺距

    def F(self):
        return 攻丝.螺距 * 攻丝.S

    def print_g(self):
        return ('T%dM6(攻丝)\n'
                'G90G40G0G54X%.3fY%.3fS%dM3\n'
                'G43H%dZ%dfM8\n'
                'Z%d\n'
                'G84Z%.3fR%dF%.3f(F = S * P)'
                '%s'
                'G90G0G80Z%dM5\n'
                'M9\n'
                'G0G91G28Z0Y0)\n' % (攻丝.刀位,
                                     攻丝.x,
                                     攻丝.y,
                                     攻丝.S,
                                     攻丝.刀位,
                                     攻丝.起始位置,
                                     攻丝.安全距离,
                                     攻丝.深度,
                                     攻丝.R,
                                     攻丝.F,
                                     攻丝.其余点,
                                     攻丝.起始位置))

class 镗刀(object):
    def __init__(self, x, y, 深度):
        镗刀.刀位 = 1
        镗刀.x = x
        镗刀.y = y
        镗刀.S = 1000
        镗刀.起始位置 = 100
        镗刀.安全距离 = 50
        镗刀.深度 = 深度
        镗刀.R = 60
        镗刀.Q = 0.1
        镗刀.F = 30
        镗刀.其余点 = ""
    def print_g(self):
        return ('T%dM6(攻丝)\n'
                'G90G40G0G54X%dY%dS%dM3\n'
                'G43H%dZ%dM8\n'
                'Z%d\n'
                'G98G76Z%dR%d0Q%.2fF%d\n'
                '%s'
                'G90G0G80Z%dM5\n'
                'M9\n'
                'G0G91G28Z0Y0)\n' % (镗刀.刀位,
                                     镗刀.x,
                                     镗刀.y,
                                     镗刀.S,
                                     镗刀.刀位,
                                     镗刀.起始位置,
                                     镗刀.安全距离,
                                     镗刀.深度,
                                     镗刀.R,
                                     镗刀.Q,
                                     镗刀.F,
                                     镗刀.其余点,
                                     镗刀.起始位置))

# class 螺旋铣刀(object):
#     def __init__(self):
