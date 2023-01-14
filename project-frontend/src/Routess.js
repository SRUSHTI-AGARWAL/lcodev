import React from "react";

import {BrowserRouter,Routes,Route} from 'react-router-dom';
import Home from "./core/Home";
import Signup from "./user/Signup";
import UserDashboard from "./user/UserDashboard";
import PrivateRoutes from './auth/helper/PrivateRoutes';
import Signin from "./user/Signin";
import Cart from "./core/Cart";

// Browser router is responsible for handling multiple URL Visits.
// using ES6 syntax to create routes
 
const Routess= () => {
    return(


<BrowserRouter> 

   <Routes> 
      
      <Route path='/' exact element={<Home/>} /> 
      <Route path='/Signup' exact element={<Signup/>} /> 
      <Route element= {<PrivateRoutes/>} >

            <Route path="/user/dashboard"  exact element={<UserDashboard />} />
     </Route>
     <Route path='/Signin' exact element={<Signin/>}  />    
     <Route path='/Cart' exact element={<Cart/>}  /> 

   
   </Routes>

</BrowserRouter>
    );
}

export default Routess;