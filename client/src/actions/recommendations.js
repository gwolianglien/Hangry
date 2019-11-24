import axios from 'axios';
import {
  SET_RECOMMENDATIONS,
} from './constants';

export const getRecommendations = obj => async dispatch => {
    const config = {
        header: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    try {
        const recommendations = await axios.post('/api/recommendations/restaurant', obj, config);
        dispatch({
            type: SET_RECOMMENDATIONS,
            payload: recommendations,
        });
    } catch(err) {
        const errors = err.response.data.errors;
        console.error(errors);
    }
}
