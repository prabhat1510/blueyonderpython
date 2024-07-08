import {useState,useEffect} from 'react';
import axios from 'axios';
import {useLocation} from "react-router-dom";
function EmployeeDetails(){
    const [employee,setEmployee] = useState([]);
    const location = useLocation();
    const {from} =location.state;

    const id =1
     
     useEffect(() => {
        axios.get(`http://localhost:5000/employees/${from}`)
              .then(function (response) {
                setEmployee(response.data)
                   })
              .catch(error => {
                      console.log(error);                        
              })
       }, []);

    return(
        <>
        <p>EmployeeDetails Component</p>
       <p>{employee.id} {employee.ename}</p> 
       </>
    );
}

export default EmployeeDetails;