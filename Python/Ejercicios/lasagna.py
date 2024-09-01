EXPECTED_BAKE_TIME = 40 #tiempo que debe estar una lasaña en el horno

def bake_time_remaining(actual): #cuanto le queda a la lasaña
    return EXPECTED_BAKE_TIME - actual

def preparation_time_in_minutes(number_of_layers):#tiempo que debe estar por capa
    return number_of_layers*2

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """ Calcula el tiempo transcurrido cocinado 
    :param number_of_layers: int - el numero de capas de la lasaña
    :param elapsed_bake_time: int - tiempo transcurrido cocinado
    :return: int - tiempo total de tiempo transcurrido (in minutos) preparando y cocinando la lasaña
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
