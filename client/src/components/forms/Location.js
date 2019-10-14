import React, { useState, useEffect } from 'react';
import { loadLocations } from '../../actions/interface';

const Location = () => {

  // Load and set all location data
  // useEffect(() => {
  //   loadLocations(locations => location.allLocations = locations);
  // })

  const [locationForm, setLocation] = useState({
    'location': '',
    'allLocations': [],
  });

  const handleChange = event => setLocation({
    ...locationForm,
    [event.target.id]: event.target.value
  })


  const handleSubmit = async event => {
    event.preventDefault();
  }

  return (
    <form onSubmit={event=>handleSubmit(event)}>
      <div className="form-group">
        <h5>Where are you?</h5>
        <select class="form-control" id="location">
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

export default Location;
