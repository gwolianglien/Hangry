import React from 'react';
import axios from 'axios';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'react-redux';
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
      <Location />
      <Contexts />
      <button type="button" className="btn btn-primary" onClick={event=>handleSubmit(event)}>Primary</button>
    </form>
  )
}

const mapStateToProps = state => ({
  location: state.forms.location,
  contexts: state.forms.contexts
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
