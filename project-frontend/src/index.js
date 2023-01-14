import React from 'react';
import ReactDOM from 'react-dom/client';
import './style.css';
import Routess from './Routess';
import { Route } from 'react-router-dom';
import reportWebVitals from './reportWebVitals';

// ReactDom.render(<Routes/>, document.getElementById("root"));


// as routing functionality does not come by default in react.js 


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Routess />
  </React.StrictMode>
);