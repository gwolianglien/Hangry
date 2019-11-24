import React, { Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

const Recommendations = ({ recommendations }) => {
  return (
    <Fragment>
      {
        recommendations.length > 0 ?
        <div className="rec-container">
          <div className="rec-banner">
            <h1>Let's Eat!</h1>
          </div>
          <div className="container-fluid">
            <div className="row">
              {
                recommendations.map(restaurant => {
                  return (
                    <div className="col-lg-4">
                      {RestaurantCard(restaurant)}
                    </div>
                  )
                })
            }
            </div>
          </div>
        </div>
        :
        null
      }
    </Fragment>
  )
}

const RestaurantCard = restaurant => {
  return (
    <div className="card">
      <div className="card-body">
        <h5 className="card-title">{restaurant.name}</h5>
        <h6 className="card-subtitle mb-2 text-muted">Rating: {restaurant.rating}</h6>
        <h6 className="card-subtitle mb-2 text-muted">Price: {restaurant.price}</h6>
        {/* <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a className="" class="card-link">Card link</a>
        <a className="" class="card-link">Another link</a> */}
      </div>
    </div>
  )
}

Recommendations.propTypes = {
  recommendations: PropTypes.object
}

const mapStateToProps = state => ({
  recommendations: state.recommendations
})

export default connect(mapStateToProps)(Recommendations);
