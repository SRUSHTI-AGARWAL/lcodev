import {API} from '../../backend';


export const getProducts = () => {


    return fetch(`${API}product`, {method: GET})    // as we are not posting any form data or JSON data so a simple GET request and not POST request.
.then( response => {return response.json()} )  // we are using .json to convert it into JSON Format.
.catch( err => console.log(err))

}

