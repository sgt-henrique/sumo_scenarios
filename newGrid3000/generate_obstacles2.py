# Adaptado para 3km x 3km com 80% de ocupação dos quarteirões

x_start = 9.75
y_start = 9.75

x_length = 80.49
y_length = 80.49

x_delta = 19.51
y_delta = 19.51

counter = 0

# 27 x 27 blocos para cobrir 3km x 3km
for i in range(27):
    for j in range(27):
        x_begin = (j * x_delta) + (j * x_length) + x_start
        x_end = x_begin + x_length
            
        y_begin = (i * y_delta) + (i * y_length) + y_start
        y_end = y_begin + y_length
            
        print("<poly id=\"building#{}\" type=\"building\" color=\"1.0,.0,.0\" fill=\"1\" shape=\"{} {} {} {} {} {} {} {} {}\" />".format(
            counter,
            x_begin, y_begin,
            x_end, y_begin,
            x_end, y_end,
            x_begin, y_end,
            x_begin, y_begin
        ))
        
        counter += 1

