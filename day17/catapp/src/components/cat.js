

function Cat(props){
    
    return (
        <div>
        <p>I am also a cat and my name is {props.name} </p>
        <p>I look like <img src={props.img}  height="200px" width="100px" alt="massi"/></p>
        </div>
    );
}

export default Cat;