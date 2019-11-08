import { combineReducers } from 'redux';
import inputs from './inputs';
import recommendations from './recommendations';

export default combineReducers({
  inputs,
  recommendations
});
