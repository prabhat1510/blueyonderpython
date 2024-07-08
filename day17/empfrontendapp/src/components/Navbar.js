import {Link} from 'react-router-dom';
function Navbar(){
    return(
        <>
        <p>Navbar Component</p>
        <div className="row">
            <Link className="nav-link" to="/addEmployee">Creat new Employee</Link>
            <Link className="nav-link" to="/employeedetails">Employee Details</Link>
            <Link className="nav-link" to="/employees">List of Employees</Link>
         </div>
        </>
    );
}

export default Navbar;