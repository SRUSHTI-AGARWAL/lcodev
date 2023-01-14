import React, {useState,useEffect} from "react";  // usestate because we will get the products from local storage and keep it in a container to checkfor any change in state. 
import Base from "./Base";
import Card from "./Card";
import { loadCart } from "./helper/carthelper";
import PaymentB from "./PaymentB";

const Cart = () => {
    const [products, setProducts] = useState([])
    const [reload, setReload] = useState(false)

// lifecycle method: we want to run loadcart before this component(useEffect)  mounts and we want somebody to invoke this loadCart method.and when we want something to happen before this component mounts then these are known as lifecycle method and here is where we can use {useEffect} 

useEffect (() => {
    setProducts(loadCart())
   }, [reload]);

    const LoadAllProducts = (products) =>{
return(
    <div>

        {/* during callback fn, if there are curly braces then either thee should be return keyword or there should be parenthesis */}

{products.map(( product, index) => (
<Card
key= {index}
product = {product}
removeFromCart = {true}
addtoCart={false}
reload = {reload}
setReload = {setReload}
/>

))}
  </div>

)
}

const LoadCheckOut = () =>{
    return(
        <div>
    
            <h1> CheckOut </h1>
        </div>
    
    )
    }

    return(
        <Base title="My Cart" description="Welcome to Checkout">
            <div className="row text-center">

        <div className="col-6 text-center"> 
        
        
        { products.length > 0 ? (LoadAllProducts(products)) :(<p className="text-center"> No Products Added</p>)
        }

         </div>

        <div className="col-6 text-center">
            
            {products.length > 0 ? (<PaymentB products={products} setReload={setReload} />) :
             
             (
             
             <p className="text-center">  Please login or add something in the Cart  </p>
             )
            
        }
        </div>
    
</div>
        </Base>
    );

};


export default Cart;