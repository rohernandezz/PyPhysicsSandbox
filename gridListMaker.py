rw = 2000
rh = 1000

def divide_in(num, canvasSize, box, margin):
    box_w = box[0]
    box_h = box[1]
    
    if len(num)==2:
        columns = num[0]
        print(f"💕 columns:{columns}")
        rows = num[1]
        print(f"✅ rows:{rows}")
    else:
        print(f"🤯 too many dimensions?!")
        
    if columns == 1:
        print(f"Start from 2 columns sweetie 👈🏼")
    if columns == 1:
        print(f"Start from 2 rows sweetie 👈🏼")        
        
    margin_w = margin[0]
    margin_h = margin[1]
    
    rw = canvasSize[0]
    rh = canvasSize[1]
    
    full_rw = rw
    full_rh = rh
    
    rw = rw - margin_w - margin_w
    rh = rh - margin_h - margin_h
    
    column_w = rw / (columns-1)
    row_h    = rh / (rows-1)    
    
    start_column = margin_w
    start_row    = margin_h
    boxes = []
    
    for column in range(columns):
        for row in range(rows):
            boxes.append((start_column, full_rh-start_row, column_w, row_h))        
            start_row    = start_row + row_h
        start_row    = margin_h        
        start_column = start_column + column_w       
        
    return boxes
    
    
print(divide_in((6,3),(rw, rh),(250,250),(100,100)))
    