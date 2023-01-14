import React from "react";
import { API } from "../../backend";
import { createOrder } from "./orderhelper";

export const getMeToken = (userId,token) => {
    return fetch(`${API}payment/gettoken/${userId}/{token}/`,{
        method: "GET",      
        // as there is not Header, formData or JSOn data so we are using just GET method and not POST method. 
    })
.then ((response) => {
    return response.json()
})
.catch((err) => console.log(err))
}

export const processPayment = (userId, token, paymentInfo)=> {
    const formData= new FormData()
    
    for(const name in paymentInfo){
        formData.append(name, paymentInfo[name])

    }

    return fetch(`${API}payment/process/${userId}/${token}/`,{
        method: "POST",
        body: formData
    })

    .then((response) => {
        return response.json();
    })
    .catch((err) => console.log(err))
}