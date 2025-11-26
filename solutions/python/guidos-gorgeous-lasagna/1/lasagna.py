EXPECTED_BAKE_TIME = 40
""":param EXPECTED_BAKE_TIME: int - expected bake time."""

def bake_time_remaining(elapsed_bake_time):

        """Calculate the bake time remaining.

        :param elapsed_bake_time: int - elapsed cooking time.
        :param EXPECTED_BAKE_TIME: int - expected bake time.

        This function subtracts the time already spent in the oven from the 
        expected total bake time for the lasagna.
        """
        return (EXPECTED_BAKE_TIME - elapsed_bake_time) 

        

def preparation_time_in_minutes(number_of_layers):

        """Calculate the preparation time.

        :param number_of_layers: int - the number of layers in the lasagna.

        Each layer takes 2 minutes to prepare. This function multiplies the 
        number of layers by the preparation time per layer.
        
        """
        return number_of_layers*2

        

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):

        """Calculate the elapsed cooking time.
    
        :param number_of_layers: int - the number of layers in the lasagna.
        :param elapsed_bake_time: int - elapsed cooking time.
        :return: int - total time elapsed (in minutes) preparing and cooking.
    
        This function takes two integers representing the number of lasagna layers and the
        time already spent baking and calculates the total elapsed minutes spent cooking the
        lasagna.
        """
        return (number_of_layers*2 + elapsed_bake_time)

        

bake_time_remaining(25)
preparation_time_in_minutes(3)
elapsed_time_in_minutes(3,EXPECTED_BAKE_TIME)

        


        
