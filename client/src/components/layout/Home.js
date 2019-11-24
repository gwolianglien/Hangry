import React, { Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import Recommendations from './Recommendations';
import Forms from '../forms/Forms';

const Home = ({ recommendations }) => {
  return (
    <Fragment>
      <div className="home-banner">
        <h1><strong>Never Get Hangry Again.</strong></h1>
      </div>
      <Recommendations />
      <Forms />
    </Fragment>
  )
}

Home.propTypes = {
  recommendations: PropTypes.object
}

const mapStateToProps = state => ({
  recommendations: state.recommendations
})

export default connect(mapStateToProps)(Home);
