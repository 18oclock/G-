import basic


class drill(object):
    def __init__(self, l, d, x, y):
        drill.x = x
        drill.y = y
        drill.深度 = l
        drill.直径 = d

    def print_g(self):
        return ('%s\n'
                '%s' % (basic.Centerdrill(drill.x, drill.y).print_G(),
                        basic.钻头(drill.x, drill.y, drill.深度, drill.直径).Print_G()))



f = open('test.txt', 'w')
f.write(drill(1, 2, 3, 4).print_g())
f.close()
