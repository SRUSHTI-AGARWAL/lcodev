import React , { useState } from "react";
import Base from "../core/Base";
import { Link } from "react-router-dom";
import {signup} from '../auth/helper'


const Signup = () => {
  const [values, setValues] = useState({
  
  name: "",
  email: "",
  password: "",
  error: "",
  success: false,

  
   } );

   const{ name, email, password, error, success}= values;

   const handleChange = name => event => {
    setValues({...values, error:false, [name]: event.target.value });

   };


   const onSubmit= (event) =>{
    event.preventDefault();
    setValues({...values,error:false})
    signup({name,email,password})
    .then((data) =>
    {
        console.log("DATA",data)
    if(data.email === email){

        setValues({
            ...values,
        name:"",
        email:"",
       password:"",
        error:"",
    success:true
    }) }
else{
    setValues({
        ...values,
        error:true,
        success:false
    })
}

    })

    .catch(e => console.log(e))

   }

   const successMessage=() => {

    return(
        <div className="row">
            <div className="col-md-6 offset-sm-3 text-left">
                <div className="alert alert-success"
                style={{display : success ? "": "none"}}>
                    New account is successfully created! Please <Link to={"/signin"}> login now! </Link>

                </div>
            </div>
        </div>
    )
   }

   const errorMessage=() => {

    return(
        <div className="row">
            <div className="col-md-6 offset-sm-3 text-left">
                <div className="alert alert-warning"
                style={{display : error ? "": "none"}}>
                    Invalid details! Try Again

                </div>
            </div>
        </div>
    )
   }

   const signUpForm =() => {
    return(
        <div className="row">
            <div className= "col-md-6 offset-sm-3 text-left">
                
                <form className="container">
                <div className="form-group">
                        <label className="text-light">Name</label>
                        <input
                        className="form-control"
                        value={name}
                        onChange= {handleChange("name")}
                        type="text" 
                        />

                    </div>
                    <div className="form-group">
                        <label className="text-light">Email</label>
                        <input
                        className="form-control"
                        value={email}
                        onChange= {handleChange("email")}
                        type="text" />

                    </div>
                    <div className="form-group">
                        <label className="text-light">password</label>
                        <input
                        className="form-control"
                        value={password}
                        onChange= {handleChange("password")}
                        type="password" />

                    </div>

                    <button 
                    onClick={onSubmit} 
                    //  if onSubmit() is used , then method will run directly. but we are running here it as event handler hence () not used.*/ */}
                    className="btn btn-success btn-block container-fluid"> Submit</button>

                </form>
            </div>
        </div>
    )
   }
    return (
        <Base title="Sign-up Page" description="A Sign-up for Srisht's Store Page">
           
                {errorMessage()}
                {successMessage()}           
                {signUpForm()}

        
        <p className="text-white text-center"> 
        {JSON.stringify(values)}
        </p>

        </Base>
    );
}

export default Signup;


