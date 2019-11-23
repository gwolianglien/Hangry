import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { Redirect, withRouter } from 'react-router-dom';

const Recommendation = ({ recommendations }) => {

  if (!recommendations) {
    return <Redirect to='/' />
  }

  return (
    <div>
      Recommendations
      {
        recommendations.map(restaurant => {
          return (
            <div>
              {restaurant}
            </div>
          )
        })
      }
    </div>
  )
}

Recommendation.propTypes = {
  recommendations: PropTypes.array
}

const mapStateToProps = state => ({
  recommendations: state.recommendations
})

export default withRouter(connect(mapStateToProps)(Recommendation));
