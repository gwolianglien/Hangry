import React, { useState, useEffect } from 'react';

const Contexts = () => {

  // Load and set all location data
  // useEffect(() => {
  //   loadLocations(locations => location.allLocations = locations);
  // })

  const [contextsForm, setContexts] = useState({
    'contexts': [],
    'allContexts': [],
  });

  const handleChange = event => setContexts({
    ...locationForm,

    [event.target.id]: event.target.value
  })


  const handleSubmit = async event => {
    event.preventDefault();
  }

  return (
    <form onSubmit={event=>handleSubmit(event)}>
      <div className="form-group">
        <label htmlFor="location">Location</label>
        <select className="form-control" id="location">
          {
            // location.allLocations.map(loc => {
            //   return (
            //     <option>{loc}</option>
            //   )
            // })
          }
          <option>1</option>
          <option>2</option>
          <option>3</option>
        </select>
      </div>
    </form>
  )
}

export default Contexts;
