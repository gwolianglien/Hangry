import axios from 'axios';
import React, { useState, useEffect } from 'react';
// import { parseData } from '../../actions/interface';

const Location = () => {
  // Default state and form
  const [user, setLocation] = useState({ 'location': '' });
  const [locationsList, setLocationList] = useState([]);

  // Load and set all location data
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

  const handleChange = event => setLocation({
    ...user,
    [event.target.id]: event.target.value
  })

  const handleSubmit = async event => {
    event.preventDefault();
  }

  return (
    <form onSubmit={event=>handleSubmit(event)}>
      <div className="form-group">
        <h5>Where are you?</h5>
        <select className="form-control" id="location" onChange={event=>handleChange(event)} value={user.location}>
          {
            locationsList.map((location, i) => <option key={i} value={`${location}`}>{location}</option>)
          }
        </select>
      </div>
    </form>
  )
}

export default Location;
