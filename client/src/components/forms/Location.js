import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import axios from 'axios';
import { addLocation } from '../../actions/inputs';

const Location = ({ addLocation }) => {

  const [user, setUser] = useState({ location: '' });  //User input
  const [locationsList, setLocationList] = useState([]);  //UI

  useEffect(() => {
    const loadLocations = async () => {
      try {
        const res = await axios.get('/api/interface/locations');
        return res.data;
      } catch(err) {
        console.error(err.message);  // Temporary for handling error in dev
      }
    }
    loadLocations().then(res => setLocationList(res.split(';')));
  }, [locationsList.length]);

  const handleChange = event => {
    setUser({
      ...user,
      [event.target.id]: event.target.value
    });
    addLocation(event.target.value);
  }

  return (
    <div className="locations-container">
      <div className="location-form">
        <div className="form-group">
          <h5 className="text-center">Where to?</h5>
          <select className="form-control" id="location" onChange={event => handleChange(event)} value={user.location}>
            <option value=''>Surprise Me!</option>
            {
              locationsList.map((location, i) => <option key={`loc-${i}`} value={`${location}`}>{location}</option>)
            }
          </select>
        </div>
      </div>
    </div>
  )
}

Location.propTypes = {
  addLocation: PropTypes.func.isRequired,
}

export default connect(
  null,
  {
    addLocation,
  }
)(Location);
