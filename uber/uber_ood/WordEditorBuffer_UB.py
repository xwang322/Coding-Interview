/*
* 刚Uber ATG电面，就一道题：
* Create a basic word editor buffer data structure which maintains the state of the text buffer given the following set of callback functions,
* which will need to be implemented inside your structure:
* Assume that this will be called by the system when the user presses a physical key on the keyboard.
* Input parameter is the key that was pressed
* void onKeyPress(char c);
* Assume that this will be called by the system when the user sets the cursor to a
* specific character index in the display buffer
*void onSetCursor(int index);
* Return the current text buffer
* std::string getText();
* Keypress should be as efficient as possible, as keypress is called many more times than setCursor.
* 要求onKeyPress() constant run time，其他function无所谓，只能用array implement，可以用多个array。
**/

# First Solution is by 2 stacks
class WordEditorBuffer(object):
    def __init__(self):
        self.stack1 = []
        self.stack2  =[]

    def onKeyPress(self, char):
        self.stack1.append(char)

    def onSetCursor(self, index):
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        if len(self.stack1) < index:
            print 'Index Out Of Bounce'
            return
        while len(self.stack1) > index:
            self.stack2.append(self.stack1.pop())

    def getText(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        print self.stack1


obj = WordEditorBuffer()
obj.onKeyPress('a')
obj.onKeyPress('b')
obj.onKeyPress('c')
obj.onKeyPress('d')
print obj.stack1
obj.onSetCursor(2)
print obj.stack1, obj.stack2
obj.onKeyPress('e')
obj.onKeyPress('f')
obj.onKeyPress('g')
obj.onSetCursor(9)
obj.onSetCursor(4)
obj.onSetCursor(0)
print obj.stack1, obj.stack2
obj.getText()
