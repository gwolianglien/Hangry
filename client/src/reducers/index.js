import { combineReducers } from 'redux';
import alerts from './alerts';
import contexts from './contexts';
import locations from './locations';
import cuisines from './cuisines';
import recommendations from './recommendations';

export default combineReducers({
  alerts,
  contexts,
  locations,
  cuisines,
  recommendations,
});
