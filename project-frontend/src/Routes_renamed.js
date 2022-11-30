import React from "react";
import ReactDom from "react-dom";

import {BrowserRouter as Router,Routes,Route} from 'react-router-dom';
// import Home from "./core/Home";
import App from './App';

// import reportWebVitals from './reportWebVitals';
// Browser router is responsible for handling multiple URL Visits.
// using ES6 syntax to create routes
 
export default function Routes_renamed()
{
    
ReactDom.render(

<Router> 

   <Routes> <Route path='/' exact element={<Home/>} /> 
         
   </Routes>

</Router> ,document.getElementById("root"));

}




