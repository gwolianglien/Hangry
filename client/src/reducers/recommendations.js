import {
  SET_RECOMMENDATIONS,
  CLEAR
} from '../actions/constants';

const initialState = {};

export default (state=initialState, action) => {
  switch(action.type) {
    case SET_RECOMMENDATIONS:
      return action.payload;
    case CLEAR:
      return {};
    default:
      return state;
  }
}
