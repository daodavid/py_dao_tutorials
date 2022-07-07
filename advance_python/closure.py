def print_name(name):
    def bind():
        print(name)

    return bind;




n_d = print_name("David")

n_k = print_name("Fuck")


n_d()
n_k()