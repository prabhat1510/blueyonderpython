export default function EmployeeDetails(props){
    let employee={
        fName :"Blue",
        lName :"Yonder",
        city : "BLR"
    }
    return(
        <>
        <p>I am EmployeeDetails Component</p>
        <p>{employee.fName } {employee.lName} {employee.city}</p>
        <p>{props.completeName}</p>
        </>
    )
}