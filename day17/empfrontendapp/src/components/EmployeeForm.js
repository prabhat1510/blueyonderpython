import React,{useState} from 'react';
import sendDetailsToServer from '../service/sendDetailsToServer';

function EmployeeForm(){
    const [empData,setEmpData] =useState({
        id:"",
        ename:""
    });




const {id,ename}=empData;//destructuring

const changeHandler = e=>{
        setEmpData(
            {
                ...empData,[e.target.name]: [e.target.value]
            }
        );
    }
    const submitHandler = e=>{
        e.preventDefault();
       sendDetailsToServer(empData);
        console.log(empData);
    }

    
  return(
    <div className="row mb-3">
    <div>
        <form onSubmit={submitHandler} >
        <div className="form-group row">
            <label className="col-sm-2 col-form-label">Employee Name</label><br />
            <div class="col-sm-5">
            <input type="text" className="form-control form-control-sm" placeholder="Enter Employee Name" name="ename" value={ename} onChange={changeHandler}/> <br />
            </div>
        </div>
                    {/** <input type="submit" name="submit"/>*/}
            <button type="submit" className="btn btn-primary">Submit</button>
        </form>
    </div>
    </div>
    );
    }
export default EmployeeForm;