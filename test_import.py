def calculate_tip(pcent,bill):
        if 1 >= pcent >= 0:
            return round((pcent*bill),2)