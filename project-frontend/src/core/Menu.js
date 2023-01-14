// top heading bar will go-up here and we will have the sign-up sign-in and all that rendering here. 

import React, {Fragment} from "react";
import { Link, useLocation,useNavigate } from "react-router-dom";
import { isAuthenticated, signout } from "../auth/helper";



const Menu = ({path}) => {
    
    const navigate = useNavigate()
    let location = useLocation();

    const currentTab= (path) => {
        if(location.pathname === path){
            return {color: "#2ecc72"};
        }
        else{
            return {color:"#FFFFFF"};
        }
    };

return(
    <div>
       <ul className="nav nav-tabs bg-dark text-white">

       <li className="nav-item">
        <Link 
        className="nav-link" style={currentTab("/")} to="/" > HOME
        </Link>
        </li>
       
        <li className="nav-item">
        <Link 
        className="nav-link" style={currentTab("/signin")} to="/cart" > Cart</Link>
        </li>
{/* {true && true } */}

       {isAuthenticated() && ( <li className="nav-item">
        <Link 
        className="nav-link" style={currentTab("/user/dashboard")} to="/user/dashboard" > DashBoard</Link>
        </li>)}
{/* for the users where it is not authenticated , they won't be able to see the sign-in and signup  */}
        
        {!isAuthenticated() && (
        <Fragment>

<li className="nav-item">
        <Link 
        className="nav-link" style={currentTab("/Signup")} to="/Signup" > Sign Up</Link>
        </li>

        <li className="nav-item">
        <Link 
        className="nav-link" style={currentTab("/signin")} to="/signin" > Sign In</Link>
        </li>
        </Fragment>)}

       {isAuthenticated() && ( 
       <li className="nav-item">
        <Link 
        onClick={ () => {
            signout(() => {
               navigate('/');

            }) 
        }}

        className="nav-link text-warning" style={currentTab("/signin")} to="/" > Sign Out</Link>
        </li>
)}

       </ul>
    </div>
);
};

export default Menu;