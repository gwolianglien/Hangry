import React from 'react';
import axios from 'axios';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { getRecommendations } from '../../actions/recommendations';
import Contexts from '../forms/Contexts';
import Location from '../forms/Location';

const Forms = ({ location, contexts, getRecommendations }) => {

  const handleSubmit = async event => {
    event.preventDefault();
    const obj = {
      location: location,
      contexts: contexts,
    }
    getRecommendations().then(() => <Redirect to='/' />)
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
  location: PropTypes.string,
  contexts: PropTypes.array,
  getRecommendations: PropTypes.func.isRequired,
}

const mapStateToProps = state => ({
  location: state.inputs.location,
  contexts: state.inputs.contexts
});

export default connect(
  mapStateToProps,
  {
    getRecommendations
  }
)(Forms);
