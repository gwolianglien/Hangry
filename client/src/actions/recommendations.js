import axios from 'axios';

export const getRecommendations = (body) => async dispatch => {
    const config = {
        header: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    try {
        const recommendations = await axios.get('/api/restaurant/recommend', body, config);
        dispatch({
            type: 'RECOMMENDATION',
            data: recommendations,
        });
    } catch(err) {
        const errors = err.response.data.errors;
        console.error(errors);
        // if (errors) {
        //     errors.forEach(error => dispatch(createAlert(error.msg, 'danger')));
        // }
    }
}
