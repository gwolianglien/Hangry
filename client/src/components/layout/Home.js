import React, { Fragment } from 'react';
import Location from '../forms/Location';

const Banner = () => {
  return (
    <div className="banner">
      <h1>Hangry</h1>
      <h3>
        Stop hangry strikes. Get food recs faster than ever.
      </h3>
    </div>
  )
}

const Home = () => {
  return (
    <Fragment>
      <Banner />
      <Location />
    </Fragment>
  )
}
export default Home;
