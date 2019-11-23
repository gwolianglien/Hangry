import {
    ADD_CONTEXT,
    REMOVE_CONTEXT,
    ADD_LOCATION,
    REMOVE_LOCATION,
    CLEAR
} from './constants';

export const clear = () => async dispatch => {
    dispatch({ type: CLEAR });
}
  
export const addContext = context => async dispatch => {
    dispatch({ type: ADD_CONTEXT, payload: context });
}

export const removeContext = context => async dispatch => {
    dispatch({ type: REMOVE_CONTEXT, payload: context });
}

export const addLocation = location => async dispatch => {
    dispatch({ type: ADD_LOCATION, payload: location });
}

export const removeLocation = location => async dispatch => {
    dispatch({ type: REMOVE_LOCATION, payload: location });
}