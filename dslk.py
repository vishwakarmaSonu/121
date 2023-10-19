def fun(t):
    def fun1():
        print(t)

    return fun1()

if __name__ == '__main__':

   (fun("sdfa"))
