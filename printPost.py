def printPost(inorder, preorder, Strt, End):
    global prIndex, temp
    if (Strt > End):
        return
    inIndex = temp[preorder[prIndex]]
    prIndex += 1
    printPost(inorder, preorder, Strt, inIndex - 1)
    printPost(inorder, preorder, inIndex + 1, End)
    print(inorder[inIndex], end = " ")
 
def printPostMain(inorder, preorder, n):
    for i in range(n):
        temp[inorder[i]] = i
    printPost(inorder, preorder, 0, n - 1)

n =int(input())
prIndex = 0
temp = {}
inOrder = input().split(' ')
preOrder = input().split(' ')
printPostMain(inOrder, preOrder, n)