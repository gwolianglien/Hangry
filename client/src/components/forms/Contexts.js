import React, { Fragment, useState, useEffect } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import axios from 'axios';
import { addContext, removeContext } from '../../actions/state';

const Contexts = ({ contexts, addContext, removeContext }) => {

  const [user, setContexts] = useState({ context: '' });
  const [count, setCount] = useState(0);
  const [contextsList, setContextsList] = useState([]);

  useEffect(() => {
    const loadContexts = async () => {
      try {
        const res = await axios.get('/api/interface/contexts');
        return res.data;
      } catch(err) {
        console.error(err.message);  // Temporary for handling error in dev
      }
    }
    loadContexts().then(res => {
      const contexts = res.split(';');
      setContextsList(contexts)
    });
  }, [contextsList.length]);

  const handleChange = event => setContexts({
    ...user,
    [event.target.id]: event.target.value
  });

  const handleAddState = () => {
    var idx = contexts.indexOf(user.context);  // try to find vibe in contexts state
    if (user.context && idx === -1 && contexts.length < 5) {
      addContext(user.context);
      setContexts({ context: '' });
    } else {
      setContexts({ context: '' });
    }
  }

  const handleRemoveState = context => {
    console.log(context)
    removeContext(context);
    console.log(contexts)
  }

  return (
    <Fragment>
      <div className="form-group">
        <h5 htmlFor="context">What are you feeling for?</h5>
        <select className="form-control" id="context" onChange={event=>handleChange(event)} value={user.context}>
          { contextsList.map((context, i) => <option key={`option-${i}`} value={`${context}`}>{context}</option> )}
        </select>
        <button className="btn btn-primary btn-block" onClick={() => handleAddState()}>Add Vibe</button>
      </div>
      { contexts.length > 0 ?
        <div className="card">
          <ul className="list-group list-group-flush">
            {contexts.map((context, i) => {
              return (
                <li className="list-group-item context-card" key={`context-${i}`} onClick={() => handleRemoveState(context)}>
                  {context}
                </li>
              )
            })}
          </ul>
        </div>
        :
        null
      }
    </Fragment>
  )
}

Contexts.propTypes = {
  conexts: PropTypes.array,
  addContext: PropTypes.func.isRequired,
  removeContext: PropTypes.func.isRequired,
}

const mapStateToProps = state => ({
  contexts: state.inputs.contexts
});


export default connect(
  mapStateToProps,
  {
    addContext,
    removeContext
  }
)(Contexts);
