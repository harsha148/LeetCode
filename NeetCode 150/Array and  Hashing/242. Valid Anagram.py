class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        array=[]
        for token in tokens:
            if(token=='+'):
                x=array.pop()
                y=array.pop()
                array.append(int(x)+int(y))
            elif token=='-':
                x=array.pop()
                y=array.pop()
                array.append(int(y)-int(x))
            elif token=='/':
                x=array.pop()
                y=array.pop()
                array.append(int(y)/int(x))
            elif token=='*':
                x=array.pop()
                y=array.pop()
                array.append(int(y)*int(x))
            else:
                array.append(token)
        return int(array.pop())
