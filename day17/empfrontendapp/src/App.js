import React from 'react';
import Home from "./components/Home";
import AboutUs from "./components/AboutUs";
import Errors from "./components/Errors";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import UserRegistration from "./components/UserRegistration";
import EmployeeForm from "./components/EmployeeForm";
import EmployeeDetails from "./components/EmployeeDetails";
import EmployeeList from "./components/EmployeeList";
import DeleteEmployee from "./components/DeleteEmployee";
import {BrowserRouter,Routes,Route} from 'react-router-dom';


function  App() {
    return(
        <BrowserRouter>
            <Routes>
                        <Route path="/" element={<Navbar />} />
                        <Route path="/home" element={<Home />} />
                        <Route path="/about" element={<AboutUs />}  />
                        <Route path="/login" element={<Login />}  />
                        <Route path="/register" element={<UserRegistration />}  />
                        <Route element={<Errors />} />
                        <Route path="/addEmployee" element={<EmployeeForm />}  />
                        <Route path="/employeedetails" element={<EmployeeDetails />}  />
                        <Route path="/employees" element={<EmployeeList />}  />
                        <Route path="/deleteEmployee" element={<DeleteEmployee />}  />
            </Routes>
            </BrowserRouter>
    );
}

export default App;