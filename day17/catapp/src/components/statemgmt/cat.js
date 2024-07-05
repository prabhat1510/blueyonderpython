import {useState} from "react";
function Cat(props){
    //Here we are using useState(true) to initialize the isHungry variable
    const [isHungry,setIsHungry] = useState(true);//useState is a React hooks function
    /**
    function changeIsHungry(){
        setIsHungry(false);
    } */
   const changeIsHungry = ()=>{
        setIsHungry(false);
    }
    return(
        <h1>
        <p>
                I am {props.name}, and I am {isHungry ? "hungry" : "full"} !
        </p>
        <button type="button" 
                onClick={changeIsHungry} 
                disabled={!isHungry} 
                title={isHungry ? "POur me some milk, please !" :"Thank you !" }
                >Check Hungry
        </button>
        
        </h1>

    );
}
export default Cat;