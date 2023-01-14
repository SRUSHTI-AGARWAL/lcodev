import React from 'react';
import Menu from './Menu';

const Base = ({
    title = 'My Title',
    description = "My description",
    className = "bg-dark text-white",
    children     // this children is responsible for injecting any component inside the base template. we can inject 1 or any. 

}) => {
 
    return (

        <div>
            <Menu />
            <div className='container-fluid'>
                
                <div className='jumbotron bg-dark text-white text-center'>
                    <h2 className='display-2'>{title}</h2>    {/* to inject any variable we use curly braces */}
                    
                    <p className='lead'>{description}</p>
                </div>

{/* ============================================================================== */}
            <div className={className} >{children}</div>  { /*children is responsible for adding any component we pass using this Base */}
  {/* =================================================================================== */}
           
            </div>


<footer className='footer bg-dark mt-20vh py-2'>
    <div className='container-fluid bg-success text-white text-center py-3'>
        <h4>    for any ques reach me at insta.</h4>
        <button className='btn btn-warning btn-lg'> Contact Us</button>
        <div className='container'> 
        <span className='text-warning' > An amazing django-react full stack course </span>
        </div>
    </div>
</footer>
        </div>   



    );
}



export default Base;