import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

const NotFound = () => {
  return (
    <Fragment>
      <h1>
        <Link to='/'>
          Sorry, We Couldn't Find Your Page!
        </Link>
      </h1>
    </Fragment>
  )
}

export default NotFound;
