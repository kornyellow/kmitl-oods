def main():
    print("*** Rabbit & Turtle ***")
    print("Enter Input : ", end="")
    d, vr, vt, vf = list(map(int, input().split(" ")))
    print("%.2f" % (d/(vt-vr)*vf))

if __name__ == "__main__":
    main()
