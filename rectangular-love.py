def find_overlap(point1, width1, point2, width2):
    highest = max(point1, point2)
    lowest = min(point1 + width1, point2 + width2)
    
    if highest >= lowest: 
      return [None, None]
      
    diff = lowest - highest
    
    return [highest, diff]
    

def find_rectangular_overlap(rect1, rect2):

    xpoint, overlapx = find_overlap(rect1["left_x"], rect1["width"], rect2["left_x"], rect2["width"])
    ypoint, overlapy = find_overlap(rect1["bottom_y"], rect1["height"], rect2["bottom_y"], rect2["height"])
    
    if not overlapx or not overlapy:
        return {"left_x": None, "bottom_y": None, "width": None, "height": None}
        
    return {"left_x": xpoint, "bottom_y": ypoint, "width": overlapx, "height": overlapy}
