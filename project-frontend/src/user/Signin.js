import React ,  { useState }from "react";
import Base from "../core/Base";
import { Link , Navigate} from "react-router-dom";
import { signin,authenticate,isAuthenticated, signout } from "../auth/helper/index";
import Home from "../core/Home";


const Signin = () => {

    const [values,setValues] = useState({
        name:"",
        email:"srish1997@gmail.com",
        password:"12345",
        error:"",
        success: false,
        loading : false,
        didRedirect : false

    })

    const{ name, email, password, error, success,loading,didRedirect}= values;

   const handleChange = name => event => {
    setValues({...values, error:false, [name]: event.target.value });

   };

const onSubmit = (event) => {
event.preventDefault();
setValues({...values,error:false,loading:true})

    // const user = {email,password}

    signin({email,password})
    // 'data' is any variable name given to the data we will receive.
    .then(data => {  
        
        if(localStorage.getItem("jwt")){
            // setValues({
            //     ...values,
            //     loading:false,
            //     success: false
            // })
            console.log(data)

        }

        else if(data.token){

                    authenticate(data,() => {

                        console.log("Data Added",data)

                        setValues({
                            ...values,
                            didRedirect:true,
                            loading:false
                        })
                    })
                }  
        else{

            console.log("it is some other error")
           
        }
    }
    )

    .catch( e => console.log(e))
   }   
 
   const performRedirect= () => {
        if(isAuthenticated()){

            return  <Navigate to="/" />
            
        }

   };

   const loadingMessage = () => {
    return (
        loading && (
            <div className="alert alert-info ">
                <h2> Loading...</h2>
            </div>
        )
    )
   }
    const successMessage=() => {

        return(
            <div className="row">
                <div className="col-md-6 offset-sm-3 text-left">
                    <div className="alert alert-success"
                    style={{display : loading ? "": "none"}}>

                        You have successfully Logged in!!

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
    
       const signInForm =() => {
        return(
            <div className="row">
                <div className= "col-md-6 offset-sm-3 text-left">
                    
                    <form className="container">
                    
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


    
    return(

        <Base title="Sign-in Page" description="This is Sign-in Page">
            {loadingMessage()}
            {signInForm()}
     

        <p className=" text-center">  {JSON.stringify(values)}  </p>
        {performRedirect()}
        {successMessage()}
      
        </Base>

    );
    
    }


    export default Signin;