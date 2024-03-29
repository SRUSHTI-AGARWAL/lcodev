// entire listing of products will go here 

import React , {useState, useEffect} from 'react' ;
import { getProducts } from './helper/coreapicalls';
import Base from './Base';
import '../style.css'
import Card from './Card';

export default function Home() {
// what we will call the box: products, how we will put data inside

    const [products, setProducts] = useState([])   // initially it will be managed by userState and products will be empty array. 
    const [error,setError]= useState(false) //initially as there is no error so setting value as False. 

    const LoadAllProducts = ()  => {
            getProducts()
            .then((data) => { // using callback

            if (data.error) {

                setError(data.error);
                console.log(error);
            }
            else{
                setProducts(data);
            }
            });
        };
    

    useEffect(() => {       // using callback fn
        LoadAllProducts();

    }, []);
    
// --------------------------------
    
     return(

<Base title='Home Page' description='Welcome to My T shirt Store'> 
    <h1> Hello ! This is Home Component</h1>

    {/* looping thru array to access any data */}
    
    <div className='row'>    { /*   this is bootstrap row */}
    { products.map((product,index) => {   {/*callback function */}
        return(

            <div key= {index} className='col-4 mb-4'>
                <Card product={product}/>
            </div>
        );
        })}
        </div>

</Base>

    );
} 



