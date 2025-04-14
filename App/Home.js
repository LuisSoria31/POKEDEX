import React from "react";
import { View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

const typeColor = {
    Fuego: 'red',
    Volador: 'gray',
    Electrico: 'gold',
    Agua: 'dodgerblue',
    Planta: 'green',
    Hielo: 'skyblue',
    Lucha: 'orange',
    Veneno: 'purple',
    Tierra: 'sienna',
    Roca: 'darkgray',
    Bicho: 'limegreen',
    Fantasma: 'indigo',
    Acero: 'lightgray',
    Hada: 'pink',
    Dragón: 'darkblue',
    Psíquico: 'hotpink',
    Normal: 'lightgray',
};

const pokemons = [
    {
        name: 'Charizard',
        id: '#6',
        types: ['Fuego', 'Volador'],
    },
]

export const Home = () => {
    return(
        <View>Vista del listado de pokemones</View>
    )
}