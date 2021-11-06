from time import sleep

from pynvim import attach


def define_function():
    nvim = attach('socket', path='/tmp/nvim')
    # buffer = nvim.current.buffer
    nvim.command('e! ~/hello.py')
    # buffer[:] = [
    # 'def hello_world():', '\treturn "Hello world!"', '',
    # 'if __name__=="__main__":', '\tprint(hello_world)'
    # ]
    nvim.input(r'i')
    nvim.input(r'def')
    sleep(0.5)
    nvim.input(r'<tab>')
    sleep(0.5)
    nvim.input(r'hello_world')
    sleep(0.5)
    nvim.input(r'<tab>')
    sleep(0.5)
    nvim.input(r'<tab>')
    sleep(0.5)
    nvim.input(r'<tab>')
    sleep(0.5)
    nvim.input(r'return "Hello world!!!"')
    sleep(0.5)
    nvim.input(r'<enter>')
    sleep(0.5)
    nvim.input(r'ifmain')
    sleep(0.5)
    nvim.input(r'<tab>')
    sleep(0.5)
    nvim.input(r'print(hello_world)')
    nvim.input(r'<escape>')
    nvim.command('w')


if __name__ == '__main__':
    define_function()
