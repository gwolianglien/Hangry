import React, { Fragment } from 'react';
import Forms from './Forms';

const Banner = () => {
  return (
    <div className="banner">
      <h1>Hangry</h1>
      <h3>
        Stop hangry strikes. Get food recs fast.
      </h3>
    </div>
  )
}

const Home = () => {
  return (
    <Fragment>
      <Banner />
      <Forms />
    </Fragment>
  )
}

export default Home;
