import React, { Fragment } from 'react';
import { Switch, Route } from 'react-router-dom'

import Home from './layout/Home';
import Recommendation from './layout/Recommendation';
import NotFound from './layout/NotFound';

const Routes = () => {
  return (
    <Switch>
      <Route exact path='/' component={Home} />
      <Route exact path='/recommendation' component={Recommendation}/>
      <Route component={NotFound} />
    </Switch>
  )
}
export default Routes;
