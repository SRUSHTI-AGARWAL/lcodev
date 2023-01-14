import React, {useState} from "react";
import ImageHelper from "./helper/ImageHelper";
import {Navigate, redirect,useNavigate,setRedirect} from 'react-router-dom';
import { addItemToCart, removeItemFromCart } from "./helper/carthelper";
import { isAuthenticated } from "../auth/helper";


const Card = ({
  
  
  product,
  addtoCart=true,
  removeFromCart = false,
  reload = undefined,
  setReload = f => f,
  //function(f) {return f}
  }) => {

const navigate = useNavigate()
const [redirect,setRedirect] = useState(false)
const cartTitle =  product? product.name: "A photo from pexels"
const cartDescription = product? product.description:" Default Description"
const cartPrice = product? product.price:" Default Price"


const addToCart = () => {
    
  if(isAuthenticated())     
  {
     addItemToCart(product, () =>  setRedirect(true))
    console.log(" Added to Cart") ;
    // console.log(redirect)
    navigate('/Cart') 
  }
    else{
      console.log("Login Please!");
      navigate('/Signin')
    }
  };



const getARedirect =  (redirect) => {

  if (redirect){
  
    navigate('/Cart')
}
};

// todo : const getToSignUp=   write later 

const showAddToCart = (addToCart) => 
   { return (
      addtoCart && (
        <button
                onClick={addToCart}   
                // {/*  here we don't pass it as method directly but as a ref. so it does not run directly.*/}

                className="btn btn-block btn-outline-success mt-2 mb-2">
                Add to Cart
              </button>
      ));
    };

    const showRemoveFromCart = removeFromCart => {

      return (
        removeFromCart &&(
          <button
                      onClick={() => {
                        //todo: handle this too 
                        removeItemFromCart(product.id);
                        setReload(!reload)
                        console.log("Product removed from cart")
                      }}
                      className="btn btn-block btn-outline-danger mt-2 mb-2">
                      Remove from cart
                    </button>
        ));
          };


  return (
    <div className="card text-white bg-dark border border-info ">
      <div className="card-header lead"> {cartTitle}</div>
      <div className="card-body">
        <ImageHelper product={product} />
        <p className="lead bg-success font-weight-normal text-wrap">
         {cartDescription}
        </p>
        <p className="btn btn-success rounded  btn-sm px-4">{cartPrice}</p>


        <div className="row">
          <div className="col-12">
            {showAddToCart(addToCart)}
          </div>

          <div className="col-12">
            {showRemoveFromCart(removeFromCart)}
          </div>
        </div>
      </div>
    </div>
  );
};


export default Card;
