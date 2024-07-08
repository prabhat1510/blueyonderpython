import {useState,useEffect} from 'react';
//import {employees} from '../service/sendDetailsToServer';
import axios from 'axios';
import {Link} from 'react-router-dom';
function EmployeeList(){
     const [empList,setEmpList] = useState([]);
     //const [employee, setEmployee] = useState([]);
     //const [isLoading, setIsLoading] = useState(false);
     //const [error, setError] = useState(null);
     useEffect(() => {
        axios.get("http://localhost:5000/employees")
              .then(function (response) {
                      setEmpList(response.data)
                   })
              .catch(error => {
                      console.log(error);                        
              })
       }, []);

    return(
        <>
        <p>EmployeeList Component</p>
        <div className="mt-5">
        
        <table className="table table-striped">
          <thead>
            <tr>
              <th>S.No.</th>
              <th>ID</th>
              <th>Name</th>
              <th>Actions</th>
              
            </tr>
          </thead>
          <tbody>
            {empList.map((item, i) => {
              return (
                <tr key={i + 1}>
                  <td>{i + 1}</td>
                  <td>{item.id}</td>
                  <td>{item.ename}</td>
                  <td>
                    <Link className="nav-link" to="/employeedetails" state={{from: `${item.id}`}}>
                      <i className="fa fa-pencil" aria-hidden="true">View</i>
                    </Link>
                    <Link className="nav-link" to="/editemployeedetails" state={{from: `${item.id}`}}>
                      <i className="fa fa-eye" aria-hidden="true">Edit</i>
                    </Link>
                    <Link className="nav-link" to="/deleteEmployee" state={{from: `${item.id}`}}>
                    <i
                      className="fa fa-trash-o"
                      aria-hidden="true"
                     
                    >Delete</i>
                    </Link>
                  </td>

                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
        </>
    );

}

export default EmployeeList;