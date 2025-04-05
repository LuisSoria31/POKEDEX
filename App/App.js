import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, TextInput, Pressable, Systrace } from 'react-native';

  export default function App() {
  return (
    <View style={styles.container}>
      <View>
        <Image source={{ uri: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png" }}
          width={200}
          height={200} />
      </View>
      <View>
        <Text style={styles.title}>Iniciar Sesion</Text>
        <Text style={styles.label}>Correo:</Text>
        <TextInput style={styles.input}placeholder='Ingrese su Correo'></TextInput>
        <Text style={styles.label}>Contraseña:</Text>
        <TextInput style={styles.input}placeholder='Ingrese su Contraseña'></TextInput>
        <Pressable style={styles.send}>
          <Text style={styles.send.textButton}>Enviar</Text>
        </Pressable>
      </View>
      <View style={styles.containerFooter}>
        <Text style={styles.containerFooter.texts}>Olvidaste tu Contraseña</Text>
        <Text style={styles.containerFooter.texts}>Registrate</Text>
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

  title:{
    fontSize: 30,
    fontWeight: 'bold'
  },
  label:{
    fontSize: 20,
    fontWeight: 'bold'
  },
  input:{
    borderRadius: 10,
    borderWidth: 2,
    borderColor: 'black',
    fontSize: 15,
    width: 'auto',
  },
  send:{
    backgroundColor: 'red',
    width: 'auto',
    height: 'auto',
    fontWeight: 'bold',
    fontSize: 30,
    borderRadius: 10,
    marginTop: 15,
    alignItems: 'center',
    textButton:{
      color:"white",
      fontSize: 25,
      fontWeight: 'bold'
    }
  },
  containerFooter:{
    justifyContent:'space-between',
    alignItems: 'center',
    texts:{
      fontSize: 20,
      margin:5
    }
  }
});
