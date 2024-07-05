import Cat from './cat';
import imageTom from '../assets/images/tom.jfif';
function Cafe(){

    return(
        <Cat name='Tom' img={imageTom} />
    );
}

export default Cafe;