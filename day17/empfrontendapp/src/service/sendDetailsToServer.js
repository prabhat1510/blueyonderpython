import axios from 'axios';
const sendDetailsToServer=(props)=>{
    const URL ="http://localhost:5000/employees"
    let payload= {
        "ename":props.ename.toString(),
        "id":props.id.toString()
        
        }
    console.log(payload);
    //addEmployee(payload,URL) 
}
export function addEmployee(empData){
    console.log("Inside Add Employee call")
    const URL ="http://localhost:5000/employees"
    let payload= {
        "ename":empData.ename.toString(),
        "id":empData.id.toString()
        
        }
    console.log(payload);
    axios.post(URL,empData)
}

export function employees(){
    console.log("Inside Employees call")
    const URL ="http://localhost:5000/employees"
    let result;
     axios.get(URL).then(
        (res)=>{
            result= res.data
        }
    )
    return result
}

export default sendDetailsToServer;