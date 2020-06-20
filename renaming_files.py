import os


def main():
    path = "/home/howard/Homework/Algorithm/Final_Project/handwrite__detect"
    count = 1

    for root, dirs, files in os.walk(path):
        for i in files:
            os.rename(os.path.join(root, i), os.path.join(root, str(count) + ".bmp"))
            count += 1


if __name__ == '__main__':
    main()