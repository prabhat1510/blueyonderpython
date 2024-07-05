import {useState,useEffect} from 'react';
//import {employees} from '../service/sendDetailsToServer';
import axios from 'axios';
function EmployeeList(){
     const [empList,setEmpList] = useState([]);
     
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
              
            </tr>
          </thead>
          <tbody>
            {empList.map((item, i) => {
              return (
                <tr key={i + 1}>
                  <td>{i + 1}</td>
                  <td>{item.id}</td>
                  <td>{item.ename}</td>
                  
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