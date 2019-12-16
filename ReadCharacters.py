with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(4))
    # print(song.read())
    print(song.readline())

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip()) # делит текстовый файл по строкам

print(camelot_lines)
