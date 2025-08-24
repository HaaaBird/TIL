# boj_2448.py
# 별 찍기 11


def print_star(n):
    if n == 1:
        return ["*"]
    else:
        if n == 3:
            stars = print_star(n // 3)
            result_list = []
            for star in stars:
                result_list.append((" "*(n-1)) + star + (" "*(n-1)))
            for star in stars:
                result_list.append((" "*(n-2)) + star + (" "*(n-2)) + star + (" "*(n-2)))
            for star in stars:
                result_list.append(star * (n * 2 - 1))
            return result_list
        else:
            stars = print_star(n // 2)
            result_list = []
            for i in range(n):
                if i == 0:
                    result_list.append((" " * (n//2)) + stars[i] + (" " * (n//2)))
                elif i == 1:
                    result_list.append((" " * (n // 2)) + stars[i] + (" " * (n // 2)))
                elif i == 2:
                    result_list.append((" " * (n // 2)) + stars[i] + (" " * (n // 2)))
                else:
                    result_list.append(stars[i % 3])

if __name__ == "__main__":
    N = int(input())
    result = print_star(N)

    for star in result:
        print(star)