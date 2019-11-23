import uuid from 'uuid';
import { ADD_ALERT, REMOVE_ALERT } from './constants';

export const createAlert = (msg, type, timeout = 5000) => dispatch => {
    const id = uuid.v4();
    dispatch({
        type: ADD_ALERT,
        payload: { msg, type, id }
    });
    setTimeout(() => dispatch({ 
        type: REMOVE_ALERT, 
        payload: id 
    }), timeout);
}