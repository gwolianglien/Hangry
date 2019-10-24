import { combineReducers } from 'redux';
import userInputs from './userInputs';
import recommendations from './recommendations';

export default combineReducers({
  userInputs,
  recommendations
});
