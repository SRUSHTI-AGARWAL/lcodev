import React from 'react';


 const ImageHelper = ({product}) => 
{   const imageurl = product ? product.image :
    'https://images.pexels.com/photos/7775641/pexels-photo-7775641.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
      
    return(


        <div className='rounded border border-success p-2 '> 
            <img 
            src= {imageurl}
            style = {{ height:'50vh', maxWidth: "100%", objectFit:'cover'}} 
            
             /*viewport height(VH) and viewport width(VW) */

            className='mb-3 rounded'
            alt= ''
            />
            
            <h1> This is image helper file </h1>
        </div>
    )
}


export default ImageHelper;