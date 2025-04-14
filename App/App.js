import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Login } from './Login';
import { navigationRef } from './navigation';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { useState } from 'react';
import { Home } from './Home';

const Stack = createNativeStackNavigator();


const Tab = createBottomTabNavigator();

function Tabs() {
  return (
    <Tab.Navigator initialRouteName='Home' screenOptions={{ headerShown: false }}>
      <Tab.Screen name="Home" component={Home} />
    </Tab.Navigator>
  );
}
  export default function App() {
    const [isLogged, setIsLogged] = useState(false)
    return (
    <NavigationContainer ref={navigationRef}>
      <Stack.Navigator initialRouteName="Login" screenOptions={{headerShown: false}}>
        {
          isLogged ? (
            <Stack.Screen name="Tabs" component={Tabs}/>
          ) : (
            <Stack.Screen name="Login">
              {(props) => <Login {...props} onLogin={() => setIsLogged(true)} />}
            </Stack.Screen> 
          )
        }
       </Stack.Navigator>
    </NavigationContainer>
  );
}