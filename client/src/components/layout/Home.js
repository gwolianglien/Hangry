import React, { Fragment } from 'react';
import Form from './Form';

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
      <Form />
    </Fragment>
  )
}

export default Home;
