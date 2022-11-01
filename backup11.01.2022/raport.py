array = []
array1 = []
array21 = []
array22 = []
array31 = []
array32 = []
with open("wejscie.txt") as file:
    for line in file:
        array.append(line)
file.close()
with open("wyjscie.txt") as file1:
    for line1 in file1:
       array1.append(line1)
file1.close()
with open("wejscie1.txt") as file21:
    for line21 in file21:
        array21.append(line21)
file21.close()
with open("wyjscie1.txt") as file22:
    for line22 in file22:
        array22.append(line22)
file22.close()
with open("wejscie2.txt") as file31:
    for line31 in file31:
        array31.append(line31)
file31.close()
with open("wyjscie2.txt") as file32:
    for line32 in file32:
        array32.append(line32)
file32.close()
web = open("raport.html", "w+")
web.writelines(
    f'<html>\n'
    f' <head> \n '
    f'<title>Zawody sportowe </title> \n'
    f' <link rel="stylesheet" href="styl.css" type="text/css" /> \n'
    '</head> \n '
    '<body> \n '
    '<div class ="box1">\n'
    '<h1>Zawody sportowe</h1> \n'
    ' <h2> XXIV OI, etap II, dzień próbny</h2> \n '
    '</div>'
    '<section><h2> Testy dla poszczególnych danych: </h2></section> \n '
    '<div> \n '
    '<div class="box"> \n '
    '<h3> Wejście </h3> \n '
    '<ul>')
for a in array:
    web.write(
        f'<p>{a}</p>')
web.writelines(
    '</ul> \n'
    '<ul> \n')
for a21 in array21:
    web.write(
        f'<p>{a21}</p>')
web.writelines(
    '</ul> \n'
    '<ul> \n')
for a31 in array31:
    web.write(
        f'<p>{a31}</p>')
web.writelines(
    '</ul> \n'
    '</div> \n '
    '<div class="box"> \n '
    '<h3> Wyjście  </h3> \n '
    '<ul> \n')
for a1 in array1:
    web.write(
        f'<p>{a1}</p>')
web.writelines(
    '</ul> \n'
    '<ul> \n')
for a22 in array22:
     web.write(
         f'<p>{a22}</p>')
web.writelines(
    '</ul> \n'
    '<ul> \n')
for a32 in array32:
     web.write(
         f'<p>{a32}</p>')
web.writelines(
    '</ul> \n'
    '</div> \n'
    '</div> \n')
web.writelines(
    '</body> \n '
    '</html>')

