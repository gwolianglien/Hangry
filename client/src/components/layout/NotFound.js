import React from 'react';
import { withRouter, Redirect } from 'react-router-dom';

const NotFound = () => {
  return (
    <Redirect to='/' />
  )
}

export default withRouter(NotFound);
