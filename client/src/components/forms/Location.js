import axios from 'axios';
import React, { Fragment, useState, useEffect } from 'react';

const Location = () => {

  const [user, setLocation] = useState({ 'location': '' });
  const [locationsList, setLocationList] = useState([]);

  useEffect(() => {
    const loadLocations = async () => {
      try {
        const res = await axios.get('/api/interface/locations');
        return res.data;
      } catch(err) {
        console.error(err.message);  // Temporary for handling error in dev
      }
    }
    loadLocations().then(res => {
      const locations = res.split(';');
      setLocationList(locations);
    });
  }, [locationsList.length]);

  const handleChange = event => {
    setLocation({
    ...user,
    [event.target.id]: event.target.value
    });
    dispatch({
      type: 'LOCATION',
      data: user.location
    });
  }

  return (
    <Fragment>
      <div className="location-form">
        <div className="form-group">
          <h5>Where do you want to eat?</h5>
          <select className="form-control" id="location" onChange={event=>handleChange(event)} value={user.location}>
            {
              locationsList.map((location, i) => <option key={i} value={`${location}`}>{location}</option>)
            }
          </select>
        </div>
      </div>
    </Fragment>
  )
}

export default Location;
