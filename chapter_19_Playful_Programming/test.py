from ConfigParser import ConfigParser

config = ConfigParser()
config.read(
    'D:/FALSE/workspace/Python_Workspace/Beginning Python From Novice to Professional/chapter_19_Playful_Programming/config.txt')

print config.get('messages', 'greeting')

radius = input(config.get('messages', 'question') + '')

print config.get('messages', 'result_message'),

print config.getfloat('numbers', 'pi') * radius ** 2
