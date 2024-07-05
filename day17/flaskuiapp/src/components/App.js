//export default function App(){
import EmployeeDetails from './EmployeeDetails'
 function App(){
    const fullName="Prabhat Chandra";
    return(
        <>
        <p>Hello All Good Morning From {fullName}!!!</p>
        <EmployeeDetails completeName={fullName}/>
        </>
    );
 }
export default App;