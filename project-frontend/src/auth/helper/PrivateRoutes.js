// configuration for routes which are not accessible without authentication, will be done here 

import React from "react";
import { Navigate,Outlet } from "react-router-dom";

import { isAuthenticated} from ".";
import Signin from "../../user/Signin";


const PrivateRoutes = ({component: Component, ...rest }) => {


return isAuthenticated() ? <Outlet /> : <Navigate to="/Signin" />;

   };

export default PrivateRoutes;



// we are getting redirected to signin here with no data initialyy as we need to get jwt for authorization. 

   