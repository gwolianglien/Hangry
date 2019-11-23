import React from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { getRecommendations } from '../actions/recommendations';
import Contexts from './Contexts';
import Location from './Location';

const Forms = ({ locations, contexts, getRecommendations }) => {

  const handleSubmit = async event => {
    event.preventDefault();
    const obj = {
      locations: locations,
      contexts: contexts,
    }
    getRecommendations(obj).then(() => ( <Redirect to='/' /> ));
  }

  return (
    <form onSubmit={event=>handleSubmit(event)}>
      <Contexts />
      <Location />
      <button type="button" className="btn btn-primary" onClick={event=>handleSubmit(event)}>Primary</button>
    </form>
  )
}

Forms.propTypes = {
  location: PropTypes.array,
  contexts: PropTypes.array,
  getRecommendations: PropTypes.func.isRequired,
}

const mapStateToProps = state => ({
  locations: state.locations,
  contexts: state.contexts
});

export default connect(
  mapStateToProps,
  {
    getRecommendations
  }
)(Forms);
