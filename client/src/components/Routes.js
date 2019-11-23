import React from 'react';
import { Switch, Route } from 'react-router-dom'
import Home from './Home';
import Recommendation from './Recommendation';
import NotFound from './NotFound';

const Routes = () => {
  return (
    <Switch>
      <Route exact path='/' component={Home} />
      <Route exact path='/recommendations' component={Recommendation} />
      <Route component={NotFound} />
    </Switch>
  )
}
export default Routes;
