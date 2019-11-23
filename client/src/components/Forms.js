import React, { Fragment } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { removeContext, clear } from '../actions/inputs';
import { getRecommendations } from '../actions/recommendations';
import Contexts from './Contexts';
import Location from './Location';

const Forms = ({ locations, contexts, removeContext, clear, getRecommendations }) => {

  const handleSubmit = async event => {
    event.preventDefault();
    const obj = {
      locations: locations,
      contexts: contexts,
    }
    getRecommendations(obj).then(() => ( <Redirect to='/' /> ));
  }

  const handleContextRemove = context => {
    console.log(context)
    removeContext(context);
  }

  return (
    <Fragment>
      <form onSubmit={event=>handleSubmit(event)} className="form">
        <div className="container-fluid">
          <div className="row">
            <div className="col-lg-6">
              <Contexts />
            </div>
            <div className="col-lg-6">
              <Location />
            </div>
          </div>
        </div>
        
      </form>
      <div className="container-spacing">
        { contexts.length > 0 ?
          <div className="card">
            <ul className="list-group list-group-flush">
              {contexts.map((context, i) => {
                return (
                  <li className="list-group-item" key={`context-${i}`} onClick={context => handleContextRemove(context)}>
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
      <div className="container-spacing">
        <button type="button" className="btn btn-success btn-block" onClick={event => handleSubmit(event)}>Find Me Some Restaurants</button>
      </div>
      
      {
        locations.length > 0 || contexts.length > 0 ?
        <div className="container-spacing">
          <button type="button" className="btn btn-danger btn-block" onClick={() => clear()}>
            Clear
          </button>
        </div>
        :
        null
      }
    </Fragment>

  )
}

Forms.propTypes = {
  location: PropTypes.array,
  contexts: PropTypes.array,
  removeContext: PropTypes.func.isRequired,
  clear: PropTypes.func.isRequired,
  getRecommendations: PropTypes.func.isRequired,
}

const mapStateToProps = state => ({
  locations: state.locations,
  contexts: state.contexts
});

export default connect(
  mapStateToProps,
  {
    removeContext,
    clear,
    getRecommendations
  }
)(Forms);
