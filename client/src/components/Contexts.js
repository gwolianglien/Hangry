import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import axios from 'axios';
import { addContext } from '../actions/inputs';
import { createAlert } from '../actions/alerts';

const Contexts = ({ contexts, addContext, createAlert }) => {

  const [user, setUser] = useState({ context: '' });  // User input
  const [contextsList, setContextsList] = useState([]);  // UI

  useEffect(() => {
    const loadContexts = async () => {
      try {
        const res = await axios.get('/api/interface/contexts');
        return res.data;
      } catch(err) {
        console.error(err.message);  // Temporary for handling error in dev
      }
    }
    loadContexts().then(res => setContextsList(res.split(';')));
  }, [contextsList.length]);

  const handleChange = event => setUser({
    ...user,
    [event.target.id]: event.target.value
  });

  const handleContextAdd = event => {
    event.preventDefault();
    if (!user.context) {
      setUser({ context: '' });
      createAlert("We'll try to surprise you!", 'primary', 3000)
      return null;
    }
    if (contexts.length >= 5) {
      setUser({ context: '' });
      createAlert("Let's try to keep the vibes at 5!", 'danger', 3000);
      return null;
    }
    addContext(user.context);
    setUser({ context: '' });
  }

  return (
    <div className="contexts-container">
      <div className="form-group">
        <h5 className="text-center">What're you up for?</h5>
        <select className="form-control" id="context" onChange={event => handleChange(event)} value={user.context}>
          <option value=''>Surprise Me!</option>
          { contextsList.map((context, i) => <option key={`option-${i}`} value={`${context}`}>{context}</option> )}
        </select>
      </div>
      <button className="btn btn-primary btn-block" onClick={event => handleContextAdd(event)}>Add Vibe</button>
    </div>
  )
}

Contexts.propTypes = {
  contexts: PropTypes.array,
  addContext: PropTypes.func.isRequired,
  createAlert: PropTypes.func.isRequired,
}

const mapStateToProps = state => ({
  contexts: state.contexts
});

export default connect(
  mapStateToProps,
  {
    addContext,
    createAlert
  }
)(Contexts);
