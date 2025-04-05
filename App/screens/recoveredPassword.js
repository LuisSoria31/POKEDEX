import { StyleSheet, Text, View, TextInput, } from "react-native";

export default function recoveredPassword() {
    return (
        <View style={styles.container}>
            <View>
                <Text style={styles.title}>Recuperar Contraseña</Text>
                <Text style={styles.label}>Correo:</Text>
                <TextInput style={styles.input}></TextInput>
                <Pressable style={styles.send}>
                    <Text style={styles.send.textButton}>Enviar para Recuperar</Text>
                </Pressable>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: '#fff',
        padding: 10,
        alignItems: 'center',
        justifyContent: 'center'
    },

    title: {
        fontSize: 30,
        fontWeight: 'bold'
    },
    label: {
        fontSize: 20,
        fontWeight: 'bold'
    },
    input: {
        borderRadius: 10,
        borderWidth: 2,
        borderColor: 'black',
        fontSize: 15,
        width: 'auto',
    },
    send: {
        backgroundColor: 'red',
        width: 'auto',
        height: 'auto',
        fontWeight: 'bold',
        fontSize: 30,
        borderRadius: 10,
        marginTop: 15,
        alignItems: 'center',
        textButton: {
            color: "white",
            fontSize: 25,
            fontWeight: 'bold'
        }
    },
    containerFooter: {
        justifyContent: 'space-between',
        alignItems: 'center',
        texts: {
            fontSize: 20,
            margin: 5
        }
    }
});