import React from 'react';
import axios from 'axios';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { getRecommendations } from '../../actions/recommendations';
// import Contexts from '../forms/Contexts';
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
    {
      // <Contexts />
    }
      <Location />
      <button type="button" className="btn btn-primary" onClick={event=>handleSubmit(event)}>Primary</button>
    </form>
  )
}

const mapStateToProps = state => ({
  location: state.userInputs.location,
  contexts: state.userInputs.contexts
});

Forms.propTypes = {
  location: PropTypes.string,
  contexts: PropTypes.array,
  getRecommendations: PropTypes.func.isRequired,
}

export default connect(
  mapStateToProps,
  {
    getRecommendations
  }
)(Forms);
