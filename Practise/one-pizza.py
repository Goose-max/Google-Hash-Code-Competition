# One Pizza
# Hash Google 2021 Practise

global IN_FILES, OUT_FILES

IN_FILES = [
    r"C:\Users\[user]\a_an_example.in.txt",
    r"C:\Users\[user]\b_basic.in.txt",
    r"C:\Users\[user]\c_coarse.in.txt",
    r"C:\Users\[user]\d_difficult.in.txt",
    r"C:\Users\[user]\e_elaborate.in.txt",
]

OUT_FILES = [
    r"C:\Users\[user]\a_an_example.in.txt",
    r"C:\Users\[user]\b_basic.in.txt",
    r"C:\Users\[user]\c_coarse.in.txt",
    r"C:\Users\[user]\d_difficult.in.txt",
    r"C:\Users\[user]\e_elaborate.in.txt",
]


def remove_number(l):
    # List comprehension + list slicing
    return [sub[2:] for sub in l]


def remove_duplicates(l):
    # Remove duplicates
    return list(dict.fromkeys(l))


def flatten(l):
    # Split flatten string list
    # List comprehension + split() + extend()
    res = []
    [res.extend(idx.split(" ")) for idx in l]
    return res


def pizza_topping(L, D):
    # Remove numbers & duplicates & flatten
    L, D = remove_number(L), remove_number(D)
    L, D = flatten(L), flatten(D)
    L, D = remove_duplicates(L), remove_duplicates(D)
    # %%%%% LIST COMPREHENSION %%%%%%
    return [i for i in L if i not in D]


def main():
    # %%%%%%% Text File Input %%%%%%%
    for i in range(len(IN_FILES)):
        L, D = [], []  # Non mutable list
        # Input from txt file
        with open(IN_FILES[i], "r") as f_in:
            C = f_in.readline()  # Read first line
            for _ in range(int(C)):
                L.append(f_in.readline().rstrip("\n"))  # Read next line
                D.append(f_in.readline().rstrip("\n"))  # Read next line
        # Output on to txt file
        with open(OUT_FILES[i], "w+") as f_out:
            f_out.write(
                f"{len(pizza_topping(L,D))}" + " " + " ".join(pizza_topping(L, D))
            )  # write onto txt file
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


main()
