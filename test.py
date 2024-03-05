space = " "
escape = "/"
slash = "\\"
under = "_"
line = "|"
brac_r = ")"
brac_l = "("

first_line = (space * 2) + (under * 4) + space + (under * 4) + space + (under * 3) + space + (under * 4) + (space * 2) + (under * 5) + space + under + (space * 3) + under + space + under + (space * 3) + under + space + under + space
second_line = space + escape + space + (under * 3) + escape + space + (under * 3) + line + under + space + under + escape + space + (under * 3) + (line * 2) + (space * 2) + (under * 3) + (4 * (line + space)) + slash + (3 * (space + line))
third_line = (2 * (line + space)) + (2 * space) + slash + (3 * under) + space + slash + line + space + line + slash + (3 * under) + space + slash + line + space + line + under + (2 * space) + (4 * (line + space)) + space + slash + (2 * (line + space)) + line
fourth_line = line + space + line + (3 * under) + space + (3 * under) + brac_r + (2 * (space + line)) + space + (3 * under) + brac_r + space + line + (2 * space) + under + (2 * (line + space)) + line + under + (2 * (line + space)) + line + slash + (2 * space) + line + under + line
fifth_line = space + slash + (4 * under) + line + (4 * under) + escape + (3 * under) + line + (4 * under) + escape + line + under + line + (4 * space) + slash + (3 * under) + escape + line + under + line + space + slash + under + brac_l + under + brac_r

print(first_line)
print(second_line)
print(third_line)
print(fourth_line)
print(fifth_line)