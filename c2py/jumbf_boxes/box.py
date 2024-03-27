# Base jumbf box class

class Box():

    l_box = 0   # Length of box in bytess
    t_box = ''  # Box type

    def __init__(self, box_type):
        self.t_box = box_type
        self.l_box = len(bytes.fromhex(self.t_box)) + 4    # Size of box_type (4 bytes) + self size (4 bytes)

    def get_length(self):
        return self.l_box
    

