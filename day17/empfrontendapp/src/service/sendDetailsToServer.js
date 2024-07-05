const sendDetailsToServer=(props)=>{
    let payload= {
        "ename":props.ename.toString(),
        "id":props.id.toString()
        
        }
    console.log(payload);
}

export default sendDetailsToServer;