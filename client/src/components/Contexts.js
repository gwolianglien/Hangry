import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import axios from 'axios';
import { addContext, removeContext } from '../actions/inputs';
import { createAlert } from '../actions/alerts';

const Contexts = ({ contexts, addContext, removeContext, createAlert }) => {

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
    if (contexts.length > 5) {
      setUser({ context: '' });
      createAlert('You can only add 5 contexts!', 'danger');
      return null;
    }
    addContext(user.context);
    setUser({ context: '' });
  }

  const handleContextRemove = context => {
    removeContext(context);
  }

  return (
    <div className="contexts-container">
      <div className="form-group">
        <h5 htmlFor="context">What are you feeling for?</h5>
        <select className="form-control" id="context" onChange={event => handleChange(event)} value={user.context}>
          <option value=''>Surprise Me!</option>
          { contextsList.map((context, i) => <option key={`option-${i}`} value={`${context}`}>{context}</option> )}
        </select>
        <button className="btn btn-primary btn-block" onClick={event => handleContextAdd(event)}>Add Vibe</button>
      </div>
      { contexts.length > 0 ?
        <div className="card">
          <ul className="list-group list-group-flush">
            {contexts.map((context, i) => {
              return (
                <li className="list-group-item context-card" key={`context-${i}`} onClick={() => handleContextRemove(context)}>
                  {context}
                </li>
              )
            })}
          </ul>
        </div>
        :
        null
      }
    </div>
  )
}

Contexts.propTypes = {
  contexts: PropTypes.array,
  addContext: PropTypes.func.isRequired,
  removeContext: PropTypes.func.isRequired,
  createAlert: PropTypes.func.isRequired,
}

const mapStateToProps = state => ({
  contexts: state.contexts
});

export default connect(
  mapStateToProps,
  {
    addContext,
    removeContext,
    createAlert
  }
)(Contexts);
