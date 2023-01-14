import React , {useState,useEffect} from "react";
import { Navigate } from "react-router-dom";
import { isAuthenticated , signout} from "../auth/helper";
import { cartEmpty } from "./helper/carthelper";
import { createOrder } from "./helper/orderhelper";
import { getMeToken, processPayment } from "./helper/paymenthelper";

import DropIn from "braintree-web-drop-in-react";
import Signin from "../user/Signin";

// Braintree payment gateway 
const PaymentB = ({
    products,
    reload= undefined,
    setReload = (f) => f,
}) => {

    const [info,setInfo] = useState({
        loading: false,
        success: false,
        clientToken: null, 
        error:"",
        instance : {}
    })

    const userId = isAuthenticated && isAuthenticated().user.id;
    const token = isAuthenticated && isAuthenticated().token;

    const getToken = (userId, token) => {   // used for contacting the server and getting a token 
        getMeToken(userId, token)
        .then(info => {

            if(info.error){
                setInfo({
                    ...info,
                    error:info.error,
                })
                signout(() =>{
                    return <Navigate to='/' />;
                });
            }
            else{
                const clientToken = info.clientToken;
                setInfo({clientToken});
            }
        })

        .catch(err => console.log(err))
    };

useEffect(() => {
    getToken(userId,token);
},[]);

const getAmount = () => {
    let amount = 0;
    products.map( p => {
        amount= amount + parseInt(p.price)
    }) ;
    return amount;
};

const onPurchase= () => {
 setInfo({loading:true})
 let nonce;
 let getNonce= info.instance.requestPaymentMethod()
 .then( data => {
    nonce = data.nonce;
    const paymentData={
        paymentMethodNonce : nonce,
        amount: getAmount(),
    };
    processPayment(userId, token, paymentData)
    .then(response => {
        if (response.error){
            if(response.code == '1'){
                console.log("Payment Failed")
                signout(()=> {
                    return <Navigate to='/' />
                })
            }
        }
        else{
                setInfo({...info,
                success: response.success, loading:false})
                console.log("Payment Success")
                let product_names = ""
                 products.forEach(function(item){
                    product_names += item.name + ", "
                });
                const orderData ={
                    products: product_names,
                    transaction_id : response.transaction.id,
                    amount: response.transaction.amount
                }
                createOrder(userId,token,orderData)
                .then(response => {
                    if(response.error){
                        if(response.code =="1"){
                            console.log("Order failed")
                        }
                        signout(() => {
                            return <Navigate to = "/" />
                        })
                    }
                    else{
                        if(response.success == true){
                            console.log("Order Placed")
                        }
                    }
                })
                .catch(error => {
                    setInfo({loading:false,success:false})
                    console.log("Order Failed", error)
                });
                cartEmpty(()=>{
                    console.log("cart is empptied Out")
                })
                setReload(!reload)
            }
        })
    .catch(e => console.log(e))

 })
 .catch(e => console.log("NONCE",e))
}

const showbtnDropIn = () => 
{

    // products.length > 0 
    // info.clientToken !== null && 
    return(
        <div> 
        {
            
            info.clientToken !== null && products.length > 0 ? 
            (
                <div> 
                    <h5> Hello</h5>
                    
                    <DropIn 
                    options= {{authorization: info.clientToken}}
                    onInstance = {(instance) => (info.instance = instance) }
                    >
                    </DropIn>
                   
                 <button className="btn btn-block btn-success"> Buy Now </button> 
                    </div>
            ) : 
            (
            <h4> Please Login  or add something in Cart </h4>
            )   
        }
    </div> 
    )
}


return (
    <div> 
<h3>  Your Bill is {getAmount()} </h3>
{showbtnDropIn()}
    </div>
);
};


export default PaymentB;

