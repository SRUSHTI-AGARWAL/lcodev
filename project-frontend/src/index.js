import React from 'react';
import ReactDom from 'react-dom';
import './style.css';
import Routes_renamed from './Routes_renamed';
import { Routes } from 'react-router-dom';

ReactDom.render(<Routes/>, document.getElementById("root"));


// as routing functionality does not come by default in react.js 