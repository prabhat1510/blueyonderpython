import React,{useState,useEffect} from 'react';
import axios from 'axios';
import {useLocation,useNavigate} from "react-router-dom";

function EditEmployeeDetails(){
    const[employee,setEmployee]=useState([]);
    const location = useLocation();
    const {from} =location.state;
    const navigate = useNavigate();
    useEffect(
        ()=>{
            axios
            .get("http://localhost:5000/employees/"+from)
            .then(
                (res)=>{
                    console.log(res.data);
                    setEmployee(res.data);
                }
            )
            .catch(
                (err)=>{
                    console.log(err);
                }
            );
        }
        
        
        ,[]);

        const handleInput=(e)=>{
            e.preventDefault();
            console.log("Handle Input"+e.target);
            //e.preventDefault();
            const {name,value}=e.target;
            console.log(name,value);
            setEmployee({
                ...employee,[name]:value
            });
        };
        const handelSubmit=(e)=>{
            e.preventDefault();
            console.log(from + " ---  "+JSON.stringify(employee));
            axios.patch("http://localhost:5000/employees/"+from,JSON.stringify(employee),{
                headers: {
                    "Content-Type": "application/json",
                  }
            })
            .then(
                (res)=>{
                    setEmployee(res.data);
                    navigate("/employees");
                }
            )
            .catch(
                (err)=>{
                    console.log(err);
                }
            );
        }
    return (<>
    <p>Edit Employee</p>
    <div className="user-form">
      <div className="heading">
      
        <p>Edit Form</p>
      </div>
      <form onSubmit={handelSubmit}>
        <div className="mb-3">
          <label for="name" className="form-label">
           Employee Name
          </label>
          <input
            type="text"
            className="form-control"
            id="ename"
            name="ename"
            value={employee.ename}
            onChange={handleInput}
          />
        </div>
        <button type="submit" className="btn btn-primary submit-btn">
          EDIT
        </button>
      </form>
    </div>

    </>);
}

export default EditEmployeeDetails;