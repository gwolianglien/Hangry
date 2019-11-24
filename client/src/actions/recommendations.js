import axios from 'axios';
import {
  SET_RECOMMENDATIONS,
} from './constants';

export const getRecommendations = inputs => async dispatch => {
    const config = {
        header: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    try {
        const res = await axios.post('/api/recommendations/restaurant', inputs, config);
        const obj = res.data;
        let recommendations = [];
        for (var key in obj) {
            recommendations.push(obj[key])
        }
        dispatch({
            type: SET_RECOMMENDATIONS,
            payload: recommendations,
        });
    } catch(err) {
        const errors = err.response.data.errors;
        console.error(errors);
    }
}
