n, m = map(int, input().split())    # 아이들의 수, 색상의 수
color = list(int(input()) for _ in range(m))

color.sort(reverse=True)


