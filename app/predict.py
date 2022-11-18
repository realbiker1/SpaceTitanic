import numpy as np
import pandas as pd
import joblib

model = joblib.load(r'models\spaceship_survivor_predictor.joblib')

def preprocess(data):

    feature_values = {
        'HomePlanet_Earth': 0,
        'HomePlanet_Europa': 0,
        'HomePlanet_Mars': 0,
        'cryosleep_false': 0,
        'cryosleep_true': 0,
        'Destination_55 Cancri e': 0,
        'Destination_PSO J318.5-22': 0, 
        'Destination_TRAPPIST-1e': 0, 
        'VIP_false': 1,
        'VIP_true': 0,
        'Deck_A': 0, 
        'Deck_B': 0,  
        'Deck_C': 0,
        'Deck_D': 0,   
        'Deck_E': 0,
        'Deck_F': 0,
        'Deck_G': 0,
        'Deck_T': 0,
        'Side_P': 0,
        'Side_S': 0,
        'Age': 30,
        'RoomService': 0,
        'FoodCourt': 0,
        'ShoppingMall': 0, 
        'Spa': 0,
        'VRDeck': 0,
        'TotalSpent': 0,
        'Group': 3,
        'ID': 1,
        'GroupSize': 0,
        'Cabins0-199': 0,
        'Cabins200-399': 0, 
        'Cabins400-599': 0, 
        'Cabins600-799': 0, 
        'Cabins800-999': 0,
        'Cabins1000-1199': 0,
        'Cabins1200-1399': 0, 
        'Cabins1400-1599': 0,
        'Cabins1600-1799': 0,
        'Cabins1800-2000': 1,
    }

    for key, value in data.items():
        if key in feature_values:
            if key == 'GroupSize':
                feature_values[key] = value+1
                if (value == 0) :
                    feature_values['Group'] = 9277
            elif key == 'Age':
                feature_values[key] = value
            else :            
                feature_values[key] = int(value)
                feature_values['TotalSpent'] += int(value)
        else:
            # Handle cryosleep
            if (value == True):
                feature_values['cryosleep_true'] = 1

            # Handle homeplanet
            elif (key == 'HomePlanet') :
                if (value == 'Earth'):
                    feature_values['HomePlanet_Earth'] = 1
                    feature_values['Deck_G'] = 1
                elif (value == 'Europa'):
                    feature_values['HomePlanet_Europa'] = 1
                    feature_values['Deck_B'] = 1
                elif (value == 'Mars'):
                    feature_values['HomePlanet_Mars'] = 1
                    feature_values['Deck_F'] = 1
            # Handle destination
            else :
                if (value == '55 Cancri e'):
                    feature_values['Destination_55 Cancri e'] = 1
                elif (value == 'PSO J318.5-22'):
                    feature_values['Destination_PSO J318.5-22'] = 1
                elif (value == 'TRAPPIST-1e'):
                    feature_values['Destination_TRAPPIST-1e'] = 1
     
    return feature_values


def predict(data):
 
    # Store the data in an array in the correct order:

    column_order = ['HomePlanet_Earth',
        'HomePlanet_Europa',
        'HomePlanet_Mars',
        'cryosleep_false',
        'cryosleep_true',
        'Destination_55 Cancri e',
        'Destination_PSO J318.5-22', 
        'Destination_TRAPPIST-1e',
        'VIP_false',
        'VIP_true',
        'Deck_A', 
        'Deck_B',  
        'Deck_C',
        'Deck_D',   
        'Deck_E',
        'Deck_F',
        'Deck_G',
        'Deck_T',
        'Side_P',
        'Side_S',
        'Age',
        'RoomService',
        'FoodCourt',
        'ShoppingMall', 
        'Spa',
        'VRDeck',
        'TotalSpent',
        'Group',
        'ID',
        'GroupSize',
        'Cabins0-199',
        'Cabins200-399', 
        'Cabins400-599', 
        'Cabins600-799', 
        'Cabins800-999',
        'Cabins1000-1199',
        'Cabins1200-1399', 
        'Cabins1400-1599',
        'Cabins1600-1799',
        'Cabins1800-2000',]

    data = np.array([data[feature] for feature in column_order], dtype=object)
    
    pred = model.predict(data.reshape(1,-1))

    uncertainty = model.predict_proba(data.reshape(1,-1))

    return pred, uncertainty


def postprocess(prediction):

    pred = prediction
   
    pred = str(pred[0])

    return_dict = {'pred': pred}

    return return_dict