import {useState,useEffect} from 'react';
import axios from 'axios';
import {useLocation} from "react-router-dom";

function DeleteEmployee(){
    const [employee,setEmployee] = useState([]);
    const location = useLocation();
    const {from} =location.state;
    useEffect(() => {
        axios.delete(`http://localhost:5000/employees/${from}`)
              .then(function (response) {
                setEmployee(response.data)
                   })
              .catch(error => {
                      console.log(error);                        
              })
       }, []);
    return(
        <>
        <p>Delete Employee Component</p>
        <p>Employee id {from} deleted successfully</p>
        </>
    );
}

export default DeleteEmployee;